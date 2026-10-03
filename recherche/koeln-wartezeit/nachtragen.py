#!/usr/bin/env python3
"""Rückfallebene: Laptop-Messungen in messwerte.csv nachtragen, nur für fehlende Slots.

Die Windows-Aufgaben auf dem Rechner des Halters schreiben mit
`messen.py --csv messwerte-laptop.csv` in eine eigene, nicht versionierte Datei.
Erst dieses Skript übernimmt daraus, was GitHub Actions am selben Tag NICHT
gemessen hat. So ist die Reihenfolge egal (Laptop vor oder nach Actions), und es
entsteht nie ein zweiter Abruf im selben Slot.

Regel je Laptop-Abruf (alle Zeilen mit demselben abgerufen_am):
- nur im Messfenster (fenster.py), sonst nie;
- nicht, wenn messwerte.csv am selben Tag schon einen Abruf im selben Slot hat
  (Slot nach Uhrzeit: vor 12:00 Vormittag, sonst Nachmittag);
- nicht, wenn er weniger als 60 Minuten neben einem vorhandenen Abruf liegt.

Aufruf (nach `git pull`, vor dem Commit):
    python nachtragen.py              # zeigt nur, was übernommen würde
    python nachtragen.py --schreiben  # hängt es an messwerte.csv an

Nur Standardbibliothek.
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timedelta
from pathlib import Path

import fenster
import messen

ORDNER = Path(__file__).resolve().parent
LAPTOP_PATH = ORDNER / "messwerte-laptop.csv"
MINDESTABSTAND = timedelta(minutes=60)


def _abrufe(csv_path: Path) -> dict[datetime, list[list[str]]]:
    """Zeilen je Abrufzeitpunkt (Ortszeit). Unlesbare Zeitstempel werden übersprungen."""
    if not csv_path.exists():
        return {}
    gruppen: dict[datetime, list[list[str]]] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                zeitpunkt = fenster.ortszeit(fenster.parse_abgerufen_am(row["abgerufen_am"]))
            except (KeyError, TypeError, ValueError):
                continue
            gruppen.setdefault(zeitpunkt, []).append([row.get(k) or "" for k in messen.CSV_HEADER])
    return gruppen


def _slot_nach_uhrzeit(zeitpunkt: datetime) -> str:
    return "vormittag" if zeitpunkt.time() < fenster.MITTAG else "nachmittag"


def _fehlt(zeitpunkt: datetime, vorhandene: list[datetime]) -> bool:
    """True, wenn der Laptop-Abruf einen Slot füllt, den messwerte.csv noch nicht hat."""
    if not fenster.im_messfenster(zeitpunkt):
        return False
    am_tag = [t for t in vorhandene if t.date() == zeitpunkt.date()]
    if any(_slot_nach_uhrzeit(t) == _slot_nach_uhrzeit(zeitpunkt) for t in am_tag):
        return False
    return all(abs(zeitpunkt - t) >= MINDESTABSTAND for t in am_tag)


def nachtragen(haupt: Path, laptop: Path, schreiben: bool = False) -> list[str]:
    """Liefert die übernommenen Abrufzeitpunkte (ISO, wie in der CSV); schreibt nur mit schreiben=True."""
    vorhandene = list(_abrufe(haupt))
    neue_zeilen: list[list[str]] = []
    neu: list[str] = []
    for zeitpunkt, zeilen in sorted(_abrufe(laptop).items()):
        if not _fehlt(zeitpunkt, vorhandene):
            continue
        vorhandene.append(zeitpunkt)  # zwei Laptop-Abrufe im selben Slot: nur der erste
        neue_zeilen.extend(zeilen)
        neu.append(zeilen[0][0])
    if schreiben and neue_zeilen:
        messen.append_csv(haupt, neue_zeilen)
    return neu


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--haupt", default=str(messen.CSV_PATH), help="messwerte.csv (Ziel)")
    parser.add_argument("--laptop", default=str(LAPTOP_PATH), help="messwerte-laptop.csv (Quelle)")
    parser.add_argument("--schreiben", action="store_true", help="wirklich anhängen (sonst nur anzeigen)")
    args = parser.parse_args(argv)

    neu = nachtragen(Path(args.haupt), Path(args.laptop), schreiben=args.schreiben)
    if not neu:
        print("Nichts nachzutragen: jeder Laptop-Abruf ist schon gedeckt oder liegt außerhalb des Fensters.")
        return 0
    verb = "übernommen" if args.schreiben else "würden übernommen (Probe, --schreiben fehlt)"
    print(f"{len(neu)} Laptop-Abrufe {verb}:")
    for zeitpunkt in neu:
        print(f"  {zeitpunkt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
