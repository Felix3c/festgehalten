#!/usr/bin/env python3
"""Misst die von der Stadt Köln selbst veröffentlichte Wartezeit in den
Kundenzentren und hängt einen Messwert je Zentrum an messwerte.csv an.

Quelle (Open-Data-Feed, keine Anmeldung nötig):
    https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php

Felder laut Datensatzbeschreibung (offenedaten-koeln.de/dataset/
kundenzentren-koeln-wartezeiten), geprüft per echtem Abruf am 08.09.2026:
    title_anz, timestamp, link, status, sondertext, wartezeit_minuten

Nur Standardbibliothek. Kein Secret, keine Abhängigkeit.

Aufruf:
    python messen.py                   # misst nur im Messfenster, je Slot einmal
    python messen.py --erzwingen       # misst immer (Funktionstest)
    python messen.py --quelle anzeige  # zweite Quelle, eigene Datei (siehe unten)

Zweite Quelle (seit 05.10.2026 Messquelle der Wetten): Die Bürger-Seite
„Wartezeiten in unseren Kundenzentren" lädt ihre Werte aus
    https://www.stadt-koeln.de/interne-dienste/wartezeiten/wartezeiten.json
Mit --quelle anzeige wird diese Datei gemessen und nach messwerte-anzeige.csv
geschrieben, nie nach messwerte.csv. Die Wetten koeln-2026-077 bis -082 nennen
den Open-Data-Feed; solange er eingefroren ist, zählt die Anzeige (Entscheidung
des Halters vom 05.10.2026, Vermerk in jeder der sechs Wetten).

Messfenster und Slot (seit 16.09.2026, siehe fenster.py): Außerhalb der
terminfreien Zeiten (Mo 7:30–15:00, Mi 7:30–12:00 Ortszeit) oder wenn
messwerte.csv für heute im selben Slot (vormittag/nachmittag) schon einen
Abruf hat, endet das Skript mit Exit-Code 0 und schreibt nichts. So kann der
Zeitplan mehrfach starten, ohne doppelte oder wertlose Zeilen zu erzeugen.

Exit-Code 0 bei Erfolg, ungleich 0 mit Meldung auf stderr, wenn der Feed
nicht abrufbar oder nicht auswertbar ist. Ein Fehler bei der
Wayback-Archivierung führt NICHT zum Abbruch — das Feld wayback_url bleibt
dann leer.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

import fenster

# https seit 03.10.2026: http:// leitete ab 20.09. per 301 um und liefert jetzt 403.
FEED_URL = "https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php"
WAYBACK_SAVE_URL = "https://web.archive.org/save/" + FEED_URL
CSV_PATH = Path(__file__).resolve().parent / "messwerte.csv"
CSV_HEADER = [
    "abgerufen_am",
    "kundenzentrum",
    "wartezeit_minuten",
    "feed_timestamp",
    "wayback_url",
]
# Datenquelle der Bürger-Seite (Befund 05.10.2026): frisch, während der Feed seit 16.09. steht.
ANZEIGE_URL = "https://www.stadt-koeln.de/interne-dienste/wartezeiten/wartezeiten.json"
ANZEIGE_CSV_PATH = Path(__file__).resolve().parent / "messwerte-anzeige.csv"
ANZEIGE_HEADER = [
    "abgerufen_am",
    "kundenzentrum",
    "wartezeit_minuten",
    "stand_iso",
    "status",
    "quelle",
    "wayback_url",
    "beleg_sha256",
]
# Rohkopie je Abruf neben der CSV: Die Datei wird alle zehn Minuten neu geschrieben, und
# Save Page Now leitet oft auf eine ältere Aufnahme um (Befund 05.10.2026) — die Wayback-Kopie
# zeigt dann nicht den gemessenen Stand.
ANZEIGE_BELEG_ORDNER = "belege-anzeige"
ANZEIGE_QUELLE = "anzeige"
ANZEIGE_BEREICH = "meldeangelegenheiten"
USER_AGENT = "Mozilla/5.0 (wettbuch koeln-wartezeit messen.py)"
FEED_TIMEOUT_SEKUNDEN = 20
WAYBACK_TIMEOUT_SEKUNDEN = 30


def fetch_feed(url: str = FEED_URL, timeout: int = FEED_TIMEOUT_SEKUNDEN) -> bytes:
    """Ruft den Open-Data-Feed ab und gibt die rohen Bytes zurück.

    Wirft eine Exception, wenn der Feed nicht erreichbar ist — das ist
    gewollt: ohne Feed gibt es keinen Messwert, der Aufrufer soll abbrechen.
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_feed(data: bytes) -> list[dict]:
    """Extrahiert je Kundenzentrum wartezeit_minuten und timestamp.

    Der Feed enthält daneben noch die 'Kfz-Zulassungsstelle' mit einem seit
    Jahren nicht mehr aktualisierten Zeitstempel (Stand der Recherche vom
    08.09.2026: 27.03.2022) — die wird hier bewusst nicht mitgezählt, weil
    sie kein Kundenzentrum ist.
    """
    payload = json.loads(data.decode("utf-8"))
    items = payload.get("items", [])
    ergebnis = []
    for item in items:
        name = (item.get("title_anz") or "").strip()
        if not name.startswith("Kundenzentrum"):
            continue
        rohwert = item.get("wartezeit_minuten")
        try:
            wartezeit = int(str(rohwert).strip())
        except (TypeError, ValueError):
            wartezeit = rohwert
        ergebnis.append(
            {
                "kundenzentrum": name,
                "wartezeit_minuten": wartezeit,
                "feed_timestamp": (item.get("timestamp") or "").strip(),
            }
        )
    return ergebnis


def trigger_wayback(
    feed_url: str = FEED_URL, timeout: int = WAYBACK_TIMEOUT_SEKUNDEN
) -> str | None:
    """Löst eine Wayback-Archivierung des Feeds aus und liefert die Archiv-URL.

    Gibt None zurück, wenn irgendetwas schiefgeht (Netz, Timeout, Wayback
    down) — das ist bewusst kein Fehler, der das Skript stoppt.
    """
    save_url = "https://web.archive.org/save/" + feed_url
    req = urllib.request.Request(save_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            archiv_url = resp.geturl()
            if not archiv_url or archiv_url == save_url:
                archiv_url = resp.headers.get("Content-Location") or resp.headers.get(
                    "Location"
                )
            return archiv_url
    except Exception as exc:  # noqa: BLE001 - bewusst breit, siehe Docstring
        print(f"Warnung: Wayback-Archivierung fehlgeschlagen: {exc}", file=sys.stderr)
        return None


def frische_records(records: list[dict], jetzt: datetime) -> list[dict]:
    """Nur Zentren, deren feed_timestamp von heute ist und nicht in der Zukunft liegt (Ortszeit).

    Befund 03.10.2026: Der Feed stand seit Mi 16.09.2026 07:45 still (alle Zentren
    „geöffnet" mit denselben Minuten, Wayback 16.09./20.09./03.10. gleich). Solche
    Werte sind keine Messung. Unlesbare Zeitstempel zählen als veraltet.
    """
    lokal = fenster.ortszeit(jetzt).replace(tzinfo=None)
    frisch = []
    for r in records:
        try:
            stempel = datetime.strptime(r["feed_timestamp"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
        if stempel.date() == lokal.date() and stempel <= lokal + timedelta(minutes=5):
            frisch.append(r)
    return frisch


def feed_veraltet(records: list[dict], jetzt: datetime) -> str | None:
    """Neuester feed_timestamp, wenn kein Zentrum frisch ist (frische_records), sonst None."""
    if frische_records(records, jetzt):
        return None
    stempel = sorted(r["feed_timestamp"] for r in records)
    return stempel[-1] if stempel else ""


def parse_anzeige(data: bytes) -> tuple[dict, list[dict]]:
    """Liest wartezeiten.json: Kopf (stand_iso, status) und je Kundenzentrum die Wartezeit.

    Nur der Bereich 'meldeangelegenheiten' (die neun Kundenzentren); die
    Führerscheinstellen im selben Dokument sind kein Kundenzentrum. Die Datei
    nennt nur den Ortsnamen ('Ehrenfeld'), der Feed 'Kundenzentrum Ehrenfeld' —
    hier wird auf die Schreibweise des Feeds abgebildet, damit beide Dateien
    vergleichbar bleiben. Die Gruppen (unter 30 / unter 60 / über 60 Minuten)
    sind nur Sortierung und werden aufgelöst.
    """
    payload = json.loads(data.decode("utf-8-sig"))
    kopf = {
        "stand_iso": str(payload.get("stand_iso") or "").strip(),
        "status": payload.get("status", ""),
    }
    records = []
    for bereich in payload.get("bereiche", []):
        if bereich.get("id") != ANZEIGE_BEREICH:
            continue
        for gruppe in bereich.get("gruppen", []):
            for eintrag in gruppe.get("eintraege", []):
                name = (eintrag.get("name") or "").strip()
                if not name:
                    continue
                rohwert = eintrag.get("wartezeit")
                try:
                    wartezeit = int(str(rohwert).strip())
                except (TypeError, ValueError):
                    wartezeit = rohwert
                records.append(
                    {"kundenzentrum": f"Kundenzentrum {name}", "wartezeit_minuten": wartezeit}
                )
    return kopf, records


def anzeige_frisch(stand_iso: str, jetzt: datetime) -> bool:
    """True, wenn stand_iso von heute ist (Ortszeit) und nicht in der Zukunft liegt.

    Dieselbe Regel wie frische_records beim Feed. Unlesbar oder ohne Zeitzone: nicht frisch.
    """
    try:
        stand = fenster.ortszeit(datetime.fromisoformat(stand_iso))
    except (TypeError, ValueError):
        return False
    lokal = fenster.ortszeit(jetzt)
    return stand.date() == lokal.date() and stand <= lokal + timedelta(minutes=5)


def sichere_beleg(rohdaten: bytes, ordner: Path, jetzt: datetime) -> str:
    """Legt die abgerufenen Bytes unverändert ab und liefert ihren SHA-256.

    Dateiname: wartezeiten-<JJJJMMTT-HHMMSS Ortszeit>-<erste 8 Zeichen des Hashes>.json.
    Lässt sich die Datei nicht schreiben, bleibt der Hash trotzdem in der CSV — das ist
    bewusst kein Fehler, der die Messung stoppt.
    """
    sha = hashlib.sha256(rohdaten).hexdigest()
    name = f"wartezeiten-{fenster.ortszeit(jetzt):%Y%m%d-%H%M%S}-{sha[:8]}.json"
    try:
        ordner.mkdir(parents=True, exist_ok=True)
        (ordner / name).write_bytes(rohdaten)
    except OSError as exc:
        print(f"Warnung: Belegkopie nicht geschrieben ({ordner / name}): {exc}", file=sys.stderr)
    return sha


def build_rows_anzeige(
    kopf: dict,
    records: list[dict],
    abgerufen_am: str,
    wayback_url: str | None,
    beleg_sha256: str = "",
) -> list[list]:
    """Baut die Zeilen für messwerte-anzeige.csv (Spalten: ANZEIGE_HEADER)."""
    return [
        [
            abgerufen_am,
            r["kundenzentrum"],
            r["wartezeit_minuten"],
            kopf["stand_iso"],
            kopf["status"],
            ANZEIGE_QUELLE,
            wayback_url or "",
            beleg_sha256,
        ]
        for r in records
    ]


def fremde_kopfzeile(csv_path: Path, header: list[str]) -> list[str] | None:
    """Kopfzeile der Datei, wenn sie existiert, nicht leer ist und NICHT `header` trägt, sonst None.

    Sperre für die zweite Quelle: Anzeige-Zeilen dürfen nie in messwerte.csv
    oder messwerte-laptop.csv landen (andere Spalten, andere Messquelle).
    """
    if not csv_path.exists() or csv_path.stat().st_size == 0:
        return None
    with csv_path.open(newline="", encoding="utf-8") as f:
        erste = next(csv.reader(f), [])
    return None if erste == header else erste


def build_rows(records: list[dict], abgerufen_am: str, wayback_url: str | None) -> list[list]:
    """Baut die CSV-Zeilen aus den geparsten Feed-Datensätzen."""
    return [
        [
            abgerufen_am,
            r["kundenzentrum"],
            r["wartezeit_minuten"],
            r["feed_timestamp"],
            wayback_url or "",
        ]
        for r in records
    ]


def append_csv(csv_path: Path, rows: list[list], header: list[str] = CSV_HEADER) -> None:
    """Hängt Zeilen an die CSV an, schreibt bei Bedarf zuerst den Header."""
    ist_neu = not csv_path.exists() or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if ist_neu:
            writer.writerow(header)
        writer.writerows(rows)


def _jetzt() -> datetime:
    """Aktueller Zeitpunkt mit Zeitzone; eigene Funktion, damit Tests sie ersetzen können."""
    return datetime.now().astimezone()


# Ein Vormittagslauf darf nur der erste Abruf des Tages sein, ein Nachmittagslauf
# höchstens der zweite und frühestens 60 Minuten nach dem letzten. Die Zeile selbst
# trägt keinen Slot; die Zählregel kommt ohne aus und heilt auch den Fall, dass ein
# verspäteter Vormittagslauf erst nach 12:00 gemessen hat.
MAX_ABRUFE_JE_TAG = {"vormittag": 1, "nachmittag": 2}
MINDESTABSTAND = timedelta(minutes=60)


def abrufe_heute(csv_path: Path, jetzt: datetime) -> list[datetime]:
    """Alle verschiedenen Abrufzeitpunkte von heute (Ortszeit), sortiert.

    Zeilen mit unlesbarem oder zeitzonenlosem Zeitstempel werden übersprungen,
    nie zum Absturz.
    """
    if not csv_path.exists():
        return []
    heute = fenster.ortszeit(jetzt).date()
    gefunden: set[datetime] = set()
    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                zeitpunkt = fenster.ortszeit(fenster.parse_abgerufen_am(row["abgerufen_am"]))
            except (KeyError, TypeError, ValueError):
                continue
            if zeitpunkt.date() == heute:
                gefunden.add(zeitpunkt)
    return sorted(gefunden)


def schon_gemessen(csv_path: Path, jetzt: datetime, ziel_slot: str | None = None) -> str | None:
    """Liefert den letzten Abruf von heute, wenn dieser Lauf nichts mehr schreiben darf, sonst None.

    ziel_slot fehlt: Slot aus der Uhrzeit `jetzt` (Vormittag vor 12:00, sonst Nachmittag).
    """
    ziel_slot = ziel_slot or fenster.slot(jetzt) or "nachmittag"
    abrufe = abrufe_heute(csv_path, jetzt)
    if not abrufe:
        return None
    letzter = abrufe[-1]
    if len(abrufe) >= MAX_ABRUFE_JE_TAG[ziel_slot]:
        return letzter.isoformat(timespec="seconds")
    if fenster.ortszeit(jetzt) - letzter < MINDESTABSTAND:
        return letzter.isoformat(timespec="seconds")
    return None


def _fenster_sperre(csv_path: Path, jetzt: datetime, lokal: str) -> str | None:
    """Meldung, wenn dieser Lauf nicht messen darf (außerhalb des Fensters oder Slot belegt), sonst None."""
    if not fenster.im_messfenster(jetzt):
        return (
            f"Außerhalb des Messfensters ({lokal}; Mo 7:30–15:00, Mi 7:30–12:00 Ortszeit): "
            "keine Messung, keine Zeile."
        )
    # Slot nach dem GEPLANTEN Lauf (Umgebungsvariable KOELN_CRON = github.event.schedule),
    # sonst nach der Uhrzeit. Ein verspäteter Vormittagslauf frisst so nicht den Nachmittag.
    ziel_slot = fenster.slot_aus_cron(os.environ.get("KOELN_CRON", "")) or fenster.slot(jetzt)
    vorhanden = schon_gemessen(csv_path, jetzt, ziel_slot)
    if vorhanden:
        return (
            f"Heute bereits gemessen ({vorhanden}), dieser Lauf gilt als '{ziel_slot}': "
            "keine weitere Zeile."
        )
    return None


def _messen_anzeige(
    csv_path: Path, jetzt: datetime, abgerufen_am: str, lokal: str, erzwingen: bool
) -> int:
    """Misst die zweite Quelle (wartezeiten.json) und hängt an die Anzeige-Datei an."""
    try:
        rohdaten = fetch_feed(ANZEIGE_URL)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"Fehler: Anzeige-Datei nicht erreichbar ({ANZEIGE_URL}): {exc}", file=sys.stderr)
        return 1

    beleg_sha256 = sichere_beleg(rohdaten, csv_path.parent / ANZEIGE_BELEG_ORDNER, jetzt)

    try:
        kopf, records = parse_anzeige(rohdaten)
    except (ValueError, AttributeError, TypeError, RecursionError) as exc:
        print(f"Fehler: Anzeige-Datei nicht auswertbar: {exc}", file=sys.stderr)
        return 1

    if not records:
        print(
            f"Fehler: Anzeige-Datei geliefert, aber kein Eintrag im Bereich '{ANZEIGE_BEREICH}' "
            "(Aufbau der Datei vermutlich geändert).",
            file=sys.stderr,
        )
        return 1

    if not erzwingen and not anzeige_frisch(kopf["stand_iso"], jetzt):
        archiv = trigger_wayback(ANZEIGE_URL)
        print(
            f"Fehler: Anzeige-Datei veraltet (stand_iso {kopf['stand_iso']!r}, Abruf {lokal}). "
            f"Keine Zeile. Beleg: {archiv or '(Archivierung fehlgeschlagen)'}",
            file=sys.stderr,
        )
        return 1

    wayback_url = trigger_wayback(ANZEIGE_URL)
    rows = build_rows_anzeige(kopf, records, abgerufen_am, wayback_url, beleg_sha256)
    append_csv(csv_path, rows, ANZEIGE_HEADER)

    print(f"{len(rows)} Messwerte an {csv_path} angehängt (abgerufen_am={abgerufen_am}).")
    for r in rows:
        print(f"  {r[1]}: {r[2]} Min. (stand_iso={r[3]}, status={r[4]})")
    print(f"  wayback_url: {wayback_url or '(leer, Archivierung fehlgeschlagen)'}")
    print(f"  beleg_sha256: {beleg_sha256} (Rohkopie in {ANZEIGE_BELEG_ORDNER}/)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--erzwingen",
        action="store_true",
        help="auch außerhalb des Messfensters und bei schon vorhandenem Abruf messen (Funktionstest)",
    )
    parser.add_argument(
        "--csv",
        help="Zieldatei statt messwerte.csv (Rückfallebene Laptop: messwerte-laptop.csv, siehe nachtragen.py)",
    )
    parser.add_argument(
        "--quelle",
        choices=["feed", ANZEIGE_QUELLE],
        default="feed",
        help="feed = Open-Data-Feed (Standard); anzeige = wartezeiten.json der Bürger-Seite, "
        "schreibt nach messwerte-anzeige.csv",
    )
    args = parser.parse_args(argv)
    ist_anzeige = args.quelle == ANZEIGE_QUELLE
    if args.csv:
        csv_path = Path(args.csv)
    else:
        csv_path = ANZEIGE_CSV_PATH if ist_anzeige else CSV_PATH

    jetzt = _jetzt()
    abgerufen_am = jetzt.isoformat(timespec="seconds")
    lokal = fenster.ortszeit(jetzt).strftime("%a %d.%m.%Y %H:%M %Z")

    # Die beiden Quellen teilen sich nie eine Datei: Die Anzeige schreibt nur in Dateien mit
    # „anzeige" im Namen und eigener Kopfzeile, der Feed nie in eine Datei mit fremder Kopfzeile.
    if ist_anzeige:
        fremd = fremde_kopfzeile(csv_path, ANZEIGE_HEADER)
        if fremd is not None or ANZEIGE_QUELLE not in csv_path.name:
            print(
                f"Fehler: {csv_path} ist keine Anzeige-Datei (Name ohne 'anzeige' oder Kopfzeile "
                f"{fremd}). Die zweite Quelle schreibt nie in die Messwerte des Feeds. Keine Zeile.",
                file=sys.stderr,
            )
            return 1
    else:
        fremd = fremde_kopfzeile(csv_path, CSV_HEADER)
        if fremd is not None:
            print(
                f"Fehler: {csv_path} ist keine Feed-Datei (Kopfzeile {fremd}). Keine Zeile.",
                file=sys.stderr,
            )
            return 1

    if not args.erzwingen:
        sperre = _fenster_sperre(csv_path, jetzt, lokal)
        if sperre:
            print(sperre)
            return 0

    if ist_anzeige:
        return _messen_anzeige(csv_path, jetzt, abgerufen_am, lokal, args.erzwingen)

    try:
        rohdaten = fetch_feed()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"Fehler: Feed nicht erreichbar ({FEED_URL}): {exc}", file=sys.stderr)
        return 1

    try:
        records = parse_feed(rohdaten)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"Fehler: Feed-Antwort nicht auswertbar: {exc}", file=sys.stderr)
        return 1

    if not records:
        print(
            "Fehler: Feed geliefert, aber keine Kundenzentren gefunden "
            "(Feldnamen im Feed vermutlich geändert).",
            file=sys.stderr,
        )
        return 1

    veraltet = None if args.erzwingen else feed_veraltet(records, jetzt)
    if veraltet is not None:
        archiv = trigger_wayback()
        print(
            f"Fehler: Feed veraltet, kein Kundenzentrum heute aktualisiert (neuester timestamp "
            f"{veraltet!r}, Abruf {lokal}). Keine Zeile. Beleg: {archiv or '(Archivierung fehlgeschlagen)'}",
            file=sys.stderr,
        )
        return 1
    if not args.erzwingen:
        records = frische_records(records, jetzt)

    wayback_url = trigger_wayback()

    rows = build_rows(records, abgerufen_am, wayback_url)
    append_csv(csv_path, rows)

    print(f"{len(rows)} Messwerte an {csv_path} angehängt (abgerufen_am={abgerufen_am}).")
    for r in rows:
        print(f"  {r[1]}: {r[2]} Min. (feed_timestamp={r[3]})")
    print(f"  wayback_url: {wayback_url or '(leer, Archivierung fehlgeschlagen)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
