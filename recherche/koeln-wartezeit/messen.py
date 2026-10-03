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
    python messen.py              # misst nur im Messfenster, je Slot einmal
    python messen.py --erzwingen  # misst immer (Funktionstest)

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


def append_csv(csv_path: Path, rows: list[list]) -> None:
    """Hängt Zeilen an die CSV an, schreibt bei Bedarf zuerst den Header."""
    ist_neu = not csv_path.exists() or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if ist_neu:
            writer.writerow(CSV_HEADER)
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
    args = parser.parse_args(argv)
    csv_path = Path(args.csv) if args.csv else CSV_PATH

    jetzt = _jetzt()
    abgerufen_am = jetzt.isoformat(timespec="seconds")
    lokal = fenster.ortszeit(jetzt).strftime("%a %d.%m.%Y %H:%M %Z")

    if not args.erzwingen:
        if not fenster.im_messfenster(jetzt):
            print(
                f"Außerhalb des Messfensters ({lokal}; Mo 7:30–15:00, Mi 7:30–12:00 Ortszeit): "
                "keine Messung, keine Zeile."
            )
            return 0
        # Slot nach dem GEPLANTEN Lauf (Umgebungsvariable KOELN_CRON = github.event.schedule),
        # sonst nach der Uhrzeit. Ein verspäteter Vormittagslauf frisst so nicht den Nachmittag.
        ziel_slot = fenster.slot_aus_cron(os.environ.get("KOELN_CRON", "")) or fenster.slot(jetzt)
        vorhanden = schon_gemessen(csv_path, jetzt, ziel_slot)
        if vorhanden:
            print(
                f"Heute bereits gemessen ({vorhanden}), dieser Lauf gilt als '{ziel_slot}': "
                "keine weitere Zeile."
            )
            return 0

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
