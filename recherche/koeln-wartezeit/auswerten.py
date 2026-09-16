#!/usr/bin/env python3
"""Wertet messwerte.csv aus: Mittelwert und Maximum je Kalendermonat, je
Kundenzentrum und über alle Zentren, plus Zahl der Messtage im Monat.

Gezählt werden nur Abrufe im Messfenster (Mo 7:30–15:00, Mi 7:30–12:00
Ortszeit, siehe fenster.py), wie es der Wettentext koeln-2026-077 ff.
verlangt. Abrufe außerhalb (Funktionstests, verspätete Zeitplan-Läufe)
werden je Monat gezählt und ausgewiesen, aber nicht gemittelt.

Nur Standardbibliothek.

Aufruf:
    python auswerten.py                 # alle Monate
    python auswerten.py --monat 2026-10 # nur Oktober 2026
    python auswerten.py --csv pfad.csv  # andere CSV-Datei
    python auswerten.py --alle          # auch Abrufe außerhalb des Messfensters
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import fenster

CSV_PATH = Path(__file__).resolve().parent / "messwerte.csv"


def read_rows(csv_path: Path) -> list[dict]:
    """Liest messwerte.csv ein. Gibt eine leere Liste zurück, wenn die Datei
    fehlt oder leer ist."""
    if not csv_path.exists():
        return []
    with csv_path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _monat_von(abgerufen_am: str) -> str:
    """'2026-10-05T10:00:00+02:00' -> '2026-10'"""
    return abgerufen_am[:7]


def _tag_von(abgerufen_am: str) -> str:
    """'2026-10-05T10:00:00+02:00' -> '2026-10-05'"""
    return abgerufen_am[:10]


def _im_messfenster(abgerufen_am: str) -> bool:
    """False bei Abrufen außerhalb der terminfreien Zeiten oder unlesbarem Zeitstempel."""
    try:
        return fenster.im_messfenster(fenster.parse_abgerufen_am(abgerufen_am))
    except ValueError:
        return False


def compute_monthly_stats(
    rows: list[dict], monat: str | None = None, alle: bool = False
) -> dict:
    """Gruppiert Messwerte je Monat und Kundenzentrum.

    Rückgabe: {monat: {"zentren": {name: {"werte": [...], "n": int}},
                        "gesamt": {"werte": [...], "n": int},
                        "messtage": int,
                        "ausgeschlossen": int}}
    Abrufe außerhalb des Messfensters werden nur gezählt ("ausgeschlossen"),
    nicht gemittelt, es sei denn alle=True.
    Nicht-numerische wartezeit_minuten-Werte werden aus den Mittelwert-/
    Maximum-Berechnungen ausgeschlossen, zählen aber als Messtag.
    """
    ergebnis: dict = {}
    for row in rows:
        m = _monat_von(row["abgerufen_am"])
        if monat and m != monat:
            continue
        eintrag = ergebnis.setdefault(
            m, {"zentren": {}, "gesamt": {"werte": []}, "tage": set(), "ausgeschlossen": 0}
        )
        if not alle and not _im_messfenster(row["abgerufen_am"]):
            eintrag["ausgeschlossen"] += 1
            continue
        eintrag["tage"].add(_tag_von(row["abgerufen_am"]))
        zentrum = row["kundenzentrum"]
        z = eintrag["zentren"].setdefault(zentrum, {"werte": []})
        try:
            wert = float(row["wartezeit_minuten"])
        except (TypeError, ValueError):
            continue
        z["werte"].append(wert)
        eintrag["gesamt"]["werte"].append(wert)

    for m, eintrag in ergebnis.items():
        eintrag["messtage"] = len(eintrag.pop("tage"))
    return ergebnis


def _mittel(werte: list[float]) -> float | None:
    return sum(werte) / len(werte) if werte else None


def format_table(stats: dict) -> str:
    zeilen = []
    for monat in sorted(stats):
        eintrag = stats[monat]
        kopf = f"# {monat} (Messtage: {eintrag['messtage']}"
        if eintrag.get("ausgeschlossen"):
            kopf += f", außerhalb des Messfensters nicht gezählt: {eintrag['ausgeschlossen']} Zeilen"
        zeilen.append(kopf + ")")
        zeilen.append(f"{'Kundenzentrum':<28} {'Mittelwert':>10} {'Maximum':>10} {'n':>4}")
        for zentrum in sorted(eintrag["zentren"]):
            werte = eintrag["zentren"][zentrum]["werte"]
            mittel = _mittel(werte)
            maximum = max(werte) if werte else None
            zeilen.append(
                f"{zentrum:<28} "
                f"{('%.1f' % mittel if mittel is not None else '-'):>10} "
                f"{('%.1f' % maximum if maximum is not None else '-'):>10} "
                f"{len(werte):>4}"
            )
        gesamt_werte = eintrag["gesamt"]["werte"]
        gesamt_mittel = _mittel(gesamt_werte)
        gesamt_max = max(gesamt_werte) if gesamt_werte else None
        zeilen.append(
            f"{'GESAMT (alle Zentren)':<28} "
            f"{('%.1f' % gesamt_mittel if gesamt_mittel is not None else '-'):>10} "
            f"{('%.1f' % gesamt_max if gesamt_max is not None else '-'):>10} "
            f"{len(gesamt_werte):>4}"
        )
        zeilen.append("")
    if not zeilen:
        return "Keine Messwerte gefunden.\n"
    return "\n".join(zeilen) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--monat", help="nur diesen Monat auswerten, Format YYYY-MM")
    parser.add_argument(
        "--csv", type=Path, default=CSV_PATH, help="Pfad zu messwerte.csv"
    )
    parser.add_argument(
        "--alle", action="store_true", help="auch Abrufe außerhalb des Messfensters mitteln"
    )
    args = parser.parse_args(argv)

    rows = read_rows(args.csv)
    if not rows:
        print(f"Keine Messwerte in {args.csv} gefunden.", file=sys.stderr)
        return 1

    stats = compute_monthly_stats(rows, monat=args.monat, alle=args.alle)
    if args.monat and args.monat not in stats:
        print(f"Kein Messwert für Monat {args.monat} in {args.csv}.", file=sys.stderr)
        return 1
    if args.monat and not stats[args.monat]["gesamt"]["werte"]:
        print(
            f"Monat {args.monat}: kein Abruf im Messfenster "
            f"({stats[args.monat]['ausgeschlossen']} Zeilen außerhalb; --alle zeigt sie).",
            file=sys.stderr,
        )
        return 1

    print(format_table(stats), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
