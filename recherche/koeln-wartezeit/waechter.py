#!/usr/bin/env python3
"""Wächter für den Köln-Fall: Lief die Messung heute?

Liest messwerte.csv und zählt die verschiedenen Abrufzeitpunkte (Spalte
abgerufen_am), die auf das heutige Datum fallen (Europe/Berlin, wie messen.py
sie schreibt). Ein Messlauf erzeugt genau einen Abrufzeitpunkt für alle
Kundenzentren. Weniger Abrufe als erwartet → Exit 1, damit der Workflow laut
scheitert und GitHub eine Mail schickt.

Seit der Messung an der Anzeige (05.10.2026) prüft der Workflow mit --csv die
Datei der GitHub-Messstelle (messwerte-anzeige-github.csv); der eingefrorene
Feed schreibt keine Zeilen mehr nach messwerte.csv.

Ohne --erwartet bestimmt der Wächter das Soll selbst (Frage 453, Felix 22.10.2026):
Montag 13:00–15:00 Ortszeit zwei Abrufe (Vormittag + Nachmittag), sonst einer. Ist das
Messfenster des Tages schon zu (Mo 15:00, Mi 12:00, andere Tage immer), bringt Nachstoßen
nichts mehr: Dann wird nur gemeldet (Exit 3), statt rot zu scheitern. Anlass: GitHub startet
den Montags-Nachmittagslauf oft 4–5 h zu spät, das gab jeden Montag einen Fehlalarm.

Exit:    0 Messung lief · 1 fehlt, Fenster offen → nachstoßen · 3 fehlt, Fenster zu → melden
Aufruf:  python waechter.py [--erwartet N] [--csv DATEI]   (Standard: automatisch, messwerte.csv)
Test:    WAECHTER_JETZT=2026-10-19T17:05:00+02:00 python waechter.py
         WAECHTER_DATUM=2026-09-11 python waechter.py   (Tag gilt als vorbei)
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import datetime, time
from pathlib import Path

from fenster import FENSTER, MONTAG, ZEITZONE, ortszeit

CSV_PATH = Path(__file__).resolve().parent / "messwerte.csv"
NACHMITTAG_AB = time(13, 0)
EXIT_NACHSTOSSEN = 1
EXIT_MELDEN = 3


def abrufe_am(csv_path: Path, datum: str) -> list[str]:
    """Alle verschiedenen abgerufen_am-Werte, die mit `datum` (YYYY-MM-DD) beginnen."""
    with csv_path.open(newline="", encoding="utf-8") as f:
        return sorted({r["abgerufen_am"] for r in csv.DictReader(f) if r["abgerufen_am"].startswith(datum)})


def soll_abrufe(jetzt: datetime) -> int:
    """Mindestzahl Abrufe bis `jetzt`: Montag 13:00 bis Fensterschluss zwei, sonst einer."""
    lokal = ortszeit(jetzt)
    if lokal.weekday() == MONTAG and NACHMITTAG_AB <= lokal.time() < FENSTER[MONTAG][1]:
        return 2
    return 1


def fenster_zu(jetzt: datetime) -> bool:
    """True, wenn heute nicht mehr gemessen werden kann (Fenster vorbei oder kein Messtag)."""
    lokal = ortszeit(jetzt)
    grenzen = FENSTER.get(lokal.weekday())
    return grenzen is None or lokal.time() >= grenzen[1]


def urteil(jetzt: datetime, anzahl: int) -> tuple[str, int]:
    """('ok' | 'nachstossen' | 'melden', Soll) für `anzahl` Abrufe heute."""
    soll = soll_abrufe(jetzt)
    if anzahl >= soll:
        return "ok", soll
    return ("melden" if fenster_zu(jetzt) else "nachstossen"), soll


def _jetzt() -> datetime:
    if text := os.environ.get("WAECHTER_JETZT"):
        return datetime.fromisoformat(text)
    if datum := os.environ.get("WAECHTER_DATUM"):
        return datetime.fromisoformat(datum).replace(hour=23, minute=59, tzinfo=ZEITZONE)
    return datetime.now(ZEITZONE)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--erwartet", type=int, default=None,
                        help="feste Mindestzahl Abrufe heute (leer = automatisch, siehe oben)")
    parser.add_argument(
        "--csv", type=Path, default=CSV_PATH, help="zu prüfende Datei (Standard: messwerte.csv)"
    )
    args = parser.parse_args(argv)
    csv_path = args.csv

    jetzt = _jetzt()
    datum = ortszeit(jetzt).strftime("%Y-%m-%d")
    if not csv_path.exists():
        print(f"FEHLT: {csv_path} existiert nicht.", file=sys.stderr)
        return 1

    abrufe = abrufe_am(csv_path, datum)
    if args.erwartet is None:
        ergebnis, soll = urteil(jetzt, len(abrufe))
    else:
        soll = args.erwartet
        ergebnis = "ok" if len(abrufe) >= soll else "nachstossen"
    print(f"{datum}: {len(abrufe)} Abruf(e) in {csv_path.name}, erwartet mindestens {soll}."
          + (" Zeitpunkte: " + ", ".join(abrufe) if abrufe else ""))
    if ergebnis == "ok":
        print("Messung lief.")
        return 0
    if ergebnis == "melden":
        print(f"MELDUNG: Messung für {datum} nicht (vollständig) in {csv_path.name}. "
              "Das Messfenster ist zu, Nachstoßen bringt nichts mehr; Laptop-Messung prüfen.")
        return EXIT_MELDEN
    print(f"FEHLT: Messung für {datum} nicht (vollständig) in {csv_path.name}.", file=sys.stderr)
    return EXIT_NACHSTOSSEN


if __name__ == "__main__":
    sys.exit(main())
