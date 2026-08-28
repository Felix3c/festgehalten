"""Einstieg: python -m wettbuch bauen <buch> <ausgabe> [--pruefen]"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from . import bewerten, lesen, pruefen, seiten

HILFE = "Aufruf: python -m wettbuch bauen <buch-ordner> <ausgabe-ordner> [--pruefen]"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    nur_pruefen = "--pruefen" in argv
    argv = [a for a in argv if a != "--pruefen"]
    if len(argv) != 3 or argv[0] != "bauen":
        print(HILFE, file=sys.stderr)
        return 2
    buch_ordner, ausgabe = Path(argv[1]), Path(argv[2])

    try:
        buch = lesen.buch_lesen(buch_ordner)
    except lesen.LeseFehler as e:
        print(f"{e.datei}: kopf — {e.text}", file=sys.stderr)
        print("1 Fehler, nichts geschrieben.", file=sys.stderr)
        return 1

    fehler = pruefen.buch_pruefen(buch)
    if fehler:
        for f in fehler:
            print(f"{f.datei}: {f.feld} — {f.text}", file=sys.stderr)
        print(f"{len(fehler)} Fehler, nichts geschrieben.", file=sys.stderr)
        return 1

    n = len(buch["wetten"])
    plural = "n" if n != 1 else ""
    if nur_pruefen:
        print(f"OK: {n} Wette{plural}, keine Fehler.")
        return 0

    bewertet = bewerten.buch_bewerten(buch)
    build_zeit = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        pfade = seiten.seiten_schreiben(buch["meta"], bewertet, ausgabe, build_zeit)
    except ValueError as e:
        print(f"seiten: institution — {e}", file=sys.stderr)
        print("1 Fehler, nichts geschrieben.", file=sys.stderr)
        return 1
    print(f"OK: {n} Wette{plural}, {len(pfade)} Dateien nach {ausgabe}")
    return 0
