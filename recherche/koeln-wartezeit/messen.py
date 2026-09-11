#!/usr/bin/env python3
"""Misst die von der Stadt Köln selbst veröffentlichte Wartezeit in den
Kundenzentren und hängt einen Messwert je Zentrum an messwerte.csv an.

Quelle (Open-Data-Feed, keine Anmeldung nötig):
    http://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php

Felder laut Datensatzbeschreibung (offenedaten-koeln.de/dataset/
kundenzentren-koeln-wartezeiten), geprüft per echtem Abruf am 08.09.2026:
    title_anz, timestamp, link, status, sondertext, wartezeit_minuten

Nur Standardbibliothek. Kein Secret, keine Abhängigkeit.

Aufruf:
    python messen.py

Exit-Code 0 bei Erfolg, ungleich 0 mit Meldung auf stderr, wenn der Feed
nicht abrufbar oder nicht auswertbar ist. Ein Fehler bei der
Wayback-Archivierung führt NICHT zum Abbruch — das Feld wayback_url bleibt
dann leer.
"""
from __future__ import annotations

import csv
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

FEED_URL = "http://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php"
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


def main() -> int:
    abgerufen_am = datetime.now().astimezone().isoformat(timespec="seconds")

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

    wayback_url = trigger_wayback()

    rows = build_rows(records, abgerufen_am, wayback_url)
    append_csv(CSV_PATH, rows)

    print(f"{len(rows)} Messwerte an {CSV_PATH} angehängt (abgerufen_am={abgerufen_am}).")
    for r in rows:
        print(f"  {r[1]}: {r[2]} Min. (feed_timestamp={r[3]})")
    print(f"  wayback_url: {wayback_url or '(leer, Archivierung fehlgeschlagen)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
