"""Nachrechnen: Wie gut sind die Computer-Prognosen über alle Bücher? (METHODE.md §4–§5)

Liest nur die Wettdateien, schreibt nichts, braucht kein Netz. Gewertet wird mit derselben
Funktion wie auf der Seite (generator/wettbuch/bewerten.py, FORMAT.md §3), damit Seite und
Nachrechnung nie auseinanderlaufen.

Ausgabe (Markdown, zum Einfügen in METHODE.md):
  1. Brier-Schnitt Computer gegen Institution gegen Münze (0,50 auf alles = 0,25).
  2. Kalibrierung: Computer-Werte in Bändern zu 0,20, je Band wie oft die Ankündigung eintrat.
     Ein ehrlicher Wert 0,30 heißt: Von zehn solchen Ankündigungen treten etwa drei ein.
  3. Punkt-Wetten: wer näher dran war.

Aufruf:  python werkzeuge/nachrechnen.py buecher [--einzeln]
--einzeln zeigt für jede aufgelöste Ja/Nein-Wette den Rechenweg, z. B. (0,30 − 1)² = 0,4900.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "generator"))

from wettbuch import bewerten, lesen  # noqa: E402

COMPUTER = "Computer"
MUENZE = 0.25  # Brier von 0,50 auf alles, egal wie es ausgeht (FORMAT.md §3.1)
BAND_BREITE = 20  # in Hundertsteln


def _komma(x: float, stellen: int = 2) -> str:
    return f"{x:.{stellen}f}".replace(".", ",")


def _wert(w: dict, von: str) -> float | None:
    for p in w["prognosen"]:
        if p["von"] == von:
            return float(p["wert"])
    return None


def zeilen(wetten: list[dict]) -> list[dict]:
    """Je aufgelöste Ja/Nein-Wette mit Computer-Prognose eine Zeile mit beiden Brier-Werten."""
    aus = []
    for w in wetten:
        if w.get("typ") != "ja_nein" or bewerten.wette_bewerten(w)["status"] != "aufgeloest":
            continue
        computer = _wert(w, COMPUTER)
        if computer is None:
            continue
        ausgang = int(w["ausgang"])
        inst = _wert(w, w["institution"])
        aus.append({
            "id": w["id"], "institution": w["institution"], "computer": computer,
            "institution_wert": inst, "ausgang": ausgang,
            "brier_computer": bewerten.brier(computer, ausgang),
            "brier_institution": None if inst is None else bewerten.brier(inst, ausgang),
        })
    return aus


def rechenweg(wert: float, ausgang: int) -> str:
    return f"({_komma(wert)} − {ausgang})² = {_komma(bewerten.brier(wert, ausgang), 4)}"


def _schnitt(werte: list[float]) -> float | None:
    return sum(werte) / len(werte) if werte else None


def zusammenfassung(zs: list[dict]) -> dict:
    return {
        "n": len(zs),
        "computer": _schnitt([z["brier_computer"] for z in zs]),
        "institution": _schnitt([z["brier_institution"] for z in zs if z["brier_institution"] is not None]),
        "muenze": MUENZE,
    }


def kalibrierung(zs: list[dict]) -> list[dict]:
    anzahl = 100 // BAND_BREITE
    baender: list[list[dict]] = [[] for _ in range(anzahl)]
    for z in zs:
        # über Hundertstel runden, sonst landet 0,60 durch Gleitkomma im Band darunter
        i = min(round(z["computer"] * 100) // BAND_BREITE, anzahl - 1)
        baender[i].append(z)
    aus = []
    for i, b in enumerate(baender):
        unten, oben = i * BAND_BREITE / 100, (i + 1) * BAND_BREITE / 100
        aus.append({
            "band": f"{_komma(unten)}–{_komma(oben)}", "n": len(b),
            "mittel_computer": _schnitt([z["computer"] for z in b]),
            "eingetreten": _schnitt([z["ausgang"] for z in b]),
        })
    return aus


def punkt_bilanz(wetten: list[dict]) -> dict:
    bilanz = {"n": 0, "computer": 0, "institution": 0, "gleichstand": 0}
    for w in wetten:
        if w.get("typ") != "punkt" or _wert(w, COMPUTER) is None:
            continue
        b = bewerten.wette_bewerten(w)
        if b["status"] != "aufgeloest":
            continue
        bilanz["n"] += 1
        if b["gleichstand"]:
            bilanz["gleichstand"] += 1
        elif b["naeher_dran"] == COMPUTER:
            bilanz["computer"] += 1
        elif b["naeher_dran"] == w["institution"]:
            bilanz["institution"] += 1
    return bilanz


def _alle_wetten(ordner: list[Path]) -> list[dict]:
    wetten = []
    for wurzel in ordner:
        for buch_md in sorted(wurzel.glob("*/BUCH.md")):
            wetten.extend(lesen.buch_lesen(buch_md.parent)["wetten"])
    return wetten


def _oder_strich(x: float | None, stellen: int = 2) -> str:
    return "–" if x is None else _komma(x, stellen)


def bericht(wetten: list[dict], einzeln: bool = False) -> str:
    zs = zeilen(wetten)
    s = zusammenfassung(zs)
    p = punkt_bilanz(wetten)
    out = [f"Aufgelöste Ja/Nein-Wetten mit Computer-Prognose: {s['n']}", "",
           "| Wer | Brier-Schnitt (0 = perfekt, 1 = immer voll daneben) |", "|---|---|",
           f"| Computer | {_oder_strich(s['computer'], 3)} |",
           f"| Institution (angekündigt) | {_oder_strich(s['institution'], 3)} |",
           f"| Münze (0,50 auf alles) | {_komma(s['muenze'], 3)} |", "",
           "Kalibrierung Computer:", "",
           "| Computer-Wert | Wetten | Schnitt Computer | eingetreten |", "|---|---|---|---|"]
    for b in kalibrierung(zs):
        out.append(f"| {b['band']} | {b['n']} | {_oder_strich(b['mittel_computer'])} | "
                   f"{_oder_strich(b['eingetreten'])} |")
    out += ["", f"Punkt-Wetten aufgelöst: {p['n']} — Computer näher dran {p['computer']}, "
                f"Institution näher dran {p['institution']}, Gleichstand {p['gleichstand']}"]
    if einzeln:
        out += ["", "| Wette | Ausgang | Computer | Institution |", "|---|---|---|---|"]
        for z in zs:
            inst = "–" if z["institution_wert"] is None else rechenweg(z["institution_wert"], z["ausgang"])
            out.append(f"| {z['id']} | {z['ausgang']} | {rechenweg(z['computer'], z['ausgang'])} | {inst} |")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ordner", nargs="+", type=Path, help="Ordner mit Büchern (je Unterordner eine BUCH.md)")
    ap.add_argument("--einzeln", action="store_true", help="Rechenweg je Wette zeigen")
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # Windows-Konsole kann sonst „−“ und „²“ nicht ausgeben
    print(bericht(_alle_wetten(a.ordner), a.einzeln))
    return 0


if __name__ == "__main__":
    sys.exit(main())
