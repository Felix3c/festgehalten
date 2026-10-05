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

Aufruf:  python waechter.py [--erwartet N] [--csv DATEI]   (Standard: 1, messwerte.csv)
Test:    WAECHTER_DATUM=2026-09-11 python waechter.py
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

CSV_PATH = Path(__file__).resolve().parent / "messwerte.csv"
ZEITZONE = ZoneInfo("Europe/Berlin")


def abrufe_am(csv_path: Path, datum: str) -> list[str]:
    """Alle verschiedenen abgerufen_am-Werte, die mit `datum` (YYYY-MM-DD) beginnen."""
    with csv_path.open(newline="", encoding="utf-8") as f:
        return sorted({r["abgerufen_am"] for r in csv.DictReader(f) if r["abgerufen_am"].startswith(datum)})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--erwartet", type=int, default=1, help="Mindestzahl Abrufe heute")
    parser.add_argument(
        "--csv", type=Path, default=CSV_PATH, help="zu prüfende Datei (Standard: messwerte.csv)"
    )
    args = parser.parse_args(argv)
    csv_path = args.csv

    datum = os.environ.get("WAECHTER_DATUM") or datetime.now(ZEITZONE).strftime("%Y-%m-%d")
    if not csv_path.exists():
        print(f"FEHLT: {csv_path} existiert nicht.", file=sys.stderr)
        return 1

    abrufe = abrufe_am(csv_path, datum)
    print(f"{datum}: {len(abrufe)} Abruf(e) in {csv_path.name}, erwartet mindestens {args.erwartet}."
          + (" Zeitpunkte: " + ", ".join(abrufe) if abrufe else ""))
    if len(abrufe) >= args.erwartet:
        print("Messung lief.")
        return 0
    print(f"FEHLT: Messung für {datum} nicht (vollständig) in {csv_path.name}.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
