"""Einstieg: python -m wettbuch bauen <buch> <ausgabe> [--pruefen]
              python -m wettbuch alle <buecher-ordner> <ausgabe> [--pruefen]"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from . import bewerten, lesen, pruefen, seiten

HILFE = (
    "Aufruf: python -m wettbuch bauen <buch-ordner> <ausgabe-ordner> [--pruefen]\n"
    "        python -m wettbuch alle <buecher-ordner> <ausgabe-ordner> [--pruefen]"
)


def _bauen(buch_ordner: Path, ausgabe: Path, nur_pruefen: bool) -> int:
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
    except seiten.SlugKollision as e:
        print(f"seiten: institution — {e}", file=sys.stderr)
        print("1 Fehler, nichts geschrieben.", file=sys.stderr)
        return 1
    print(f"OK: {n} Wette{plural}, {len(pfade)} Dateien nach {ausgabe}")
    return 0


def _unterbuecher(buecher_ordner: Path) -> list[Path]:
    if not buecher_ordner.is_dir():
        return []
    return sorted(
        (p for p in buecher_ordner.iterdir() if p.is_dir() and (p / "BUCH.md").exists()),
        key=lambda p: p.name,
    )


def _slug_kollision(bewertet: dict) -> str | None:
    slugs: dict[str, str] = {}
    for w in bewertet["wetten"]:
        inst = w["institution"]
        s = seiten.slug(inst)
        if s in slugs and slugs[s] != inst:
            return f"Slug-Kollision: {inst!r} und {slugs[s]!r} ergeben beide {s!r}"
        slugs[s] = inst
    return None


def _alle(buecher_ordner: Path, ausgabe: Path, nur_pruefen: bool) -> int:
    unterordner = _unterbuecher(buecher_ordner)
    if not unterordner:
        print(f"{buecher_ordner}: keine Unterordner mit BUCH.md gefunden", file=sys.stderr)
        return 1

    fehler_gesamt: list[str] = []
    gute: list[tuple[str, dict, dict]] = []

    for pfad in unterordner:
        name = pfad.name
        try:
            buch = lesen.buch_lesen(pfad)
        except lesen.LeseFehler as e:
            fehler_gesamt.append(f"{name}/{e.datei}: kopf — {e.text}")
            continue

        fehler = pruefen.buch_pruefen(buch)
        if fehler:
            for f in fehler:
                fehler_gesamt.append(f"{name}/{f.datei}: {f.feld} — {f.text}")
            continue

        bewertet = bewerten.buch_bewerten(buch)
        kollision = _slug_kollision(bewertet)
        if kollision:
            fehler_gesamt.append(f"{name}: institution — {kollision}")
            continue

        gute.append((name, buch, bewertet))

    if fehler_gesamt:
        for z in fehler_gesamt:
            print(z, file=sys.stderr)
        print(f"{len(fehler_gesamt)} Fehler, nichts geschrieben.", file=sys.stderr)
        return 1

    gesamt_wetten = sum(len(bewertet["wetten"]) for _, _, bewertet in gute)
    plural = "n" if gesamt_wetten != 1 else ""
    buch_wort = "Buch" if len(gute) == 1 else "Bücher"

    if nur_pruefen:
        print(f"OK: {len(gute)} {buch_wort}, {gesamt_wetten} Wette{plural}, keine Fehler.")
        return 0

    build_zeit = datetime.now().strftime("%Y-%m-%d %H:%M")
    uebersicht: list[dict] = []
    for name, buch, bewertet in gute:
        seiten.seiten_schreiben(buch["meta"], bewertet, ausgabe / name, build_zeit)
        wetten = bewertet["wetten"]
        aufgeloest = sum(1 for w in wetten if w["_bewertung"]["status"] == "aufgeloest")
        offen = sum(1 for w in wetten if w["_bewertung"]["status"] == "offen")
        institutionen = sorted({w["institution"] for w in wetten})
        uebersicht.append({
            "ordner": name,
            "titel": str(buch["meta"].get("titel", name)),
            "institutionen": institutionen,
            "wetten": len(wetten),
            "aufgeloest": aufgeloest,
            "offen": offen,
        })

    seiten.uebersicht_schreiben(uebersicht, ausgabe, build_zeit)
    print(f"OK: {len(gute)} {buch_wort}, {gesamt_wetten} Wette{plural}, nach {ausgabe}")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    nur_pruefen = "--pruefen" in argv
    argv = [a for a in argv if a != "--pruefen"]
    if len(argv) != 3 or argv[0] not in ("bauen", "alle"):
        print(HILFE, file=sys.stderr)
        return 2

    ordner, ausgabe = Path(argv[1]), Path(argv[2])
    if argv[0] == "bauen":
        return _bauen(ordner, ausgabe, nur_pruefen)
    return _alle(ordner, ausgabe, nur_pruefen)
