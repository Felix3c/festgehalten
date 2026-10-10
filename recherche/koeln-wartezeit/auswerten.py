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
    python auswerten.py --quelle anzeige --monat 2026-10  # Anzeige-Datei (siehe unten)

Seit 05.10.2026 werden die Wetten an der Anzeige der Bürger-Seite gemessen
(messwerte-anzeige.csv, Vermerk in jeder der sechs Wetten), weil der
Open-Data-Feed seit 16.09.2026 eingefroren ist. Mit --quelle anzeige zählen
nur Zeilen, deren beleg_sha256 zu einer Rohkopie in belege-anzeige/ passt
(Hash aus dem Dateiinhalt nachgerechnet); Zeilen ohne Beleg werden je Monat
ausgewiesen, aber nicht gemittelt.

Zwei Messstellen: Neben messwerte-anzeige.csv (Laptop) wird, wenn vorhanden,
messwerte-anzeige-github.csv (GitHub-Workflow) mitgelesen. Je Slot (Tag und
Vormittag/Nachmittag) zählt nur der früheste Abruf mit Beleg, gleich aus
welcher Datei; spätere Abrufe im selben Slot werden ausgewiesen, aber nicht
gemittelt. So bleibt es bei höchstens drei gezählten Abrufen je Woche.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path

import fenster

CSV_PATH = Path(__file__).resolve().parent / "messwerte.csv"
ANZEIGE_CSV_PATH = Path(__file__).resolve().parent / "messwerte-anzeige.csv"
ANZEIGE_GITHUB_NAME = "messwerte-anzeige-github.csv"
ANZEIGE_QUELLE = "anzeige"
BELEG_SPALTE = "beleg_sha256"
BELEG_ORDNER = "belege-anzeige"


def read_rows(csv_path: Path) -> list[dict]:
    """Liest messwerte.csv ein. Gibt eine leere Liste zurück, wenn die Datei
    fehlt oder leer ist."""
    if not csv_path.exists():
        return []
    with csv_path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def beleg_hashes(ordner: Path) -> set[str]:
    """SHA-256 jeder Rohkopie im Belegordner, aus dem Inhalt nachgerechnet (nicht aus dem Namen)."""
    if not ordner.is_dir():
        return set()
    return {hashlib.sha256(p.read_bytes()).hexdigest() for p in ordner.glob("*.json")}


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


def _slot_schluessel(abgerufen_am: str) -> tuple | None:
    """(Tag in Ortszeit, Slot) eines Abrufs; None bei unlesbarem Zeitstempel oder
    außerhalb des Messfensters (dort gibt es keinen Slot, also auch nichts zusammenzulegen)."""
    try:
        zeitpunkt = fenster.parse_abgerufen_am(abgerufen_am)
    except ValueError:
        return None
    slot = fenster.slot(zeitpunkt)
    if slot is None:
        return None
    return (fenster.ortszeit(zeitpunkt).date(), slot)


def frueheste_je_slot(rows: list[dict]) -> dict:
    """Je Slot der früheste Abrufzeitpunkt unter den übergebenen (schon gefilterten) Zeilen."""
    fruehester: dict = {}
    for row in rows:
        schluessel = _slot_schluessel(row["abgerufen_am"])
        if schluessel is None:
            continue
        zeitpunkt = fenster.parse_abgerufen_am(row["abgerufen_am"])
        if schluessel not in fruehester or zeitpunkt < fruehester[schluessel]:
            fruehester[schluessel] = zeitpunkt
    return fruehester


def compute_monthly_stats(
    rows: list[dict],
    monat: str | None = None,
    alle: bool = False,
    belege: set[str] | None = None,
    je_slot: bool = False,
) -> dict:
    """Gruppiert Messwerte je Monat und Kundenzentrum.

    Rückgabe: {monat: {"zentren": {name: {"werte": [...], "n": int}},
                        "gesamt": {"werte": [...], "n": int},
                        "messtage": int,
                        "ausgeschlossen": int,
                        "ohne_beleg": int}}
    Abrufe außerhalb des Messfensters werden nur gezählt ("ausgeschlossen"),
    nicht gemittelt, es sei denn alle=True.
    Mit belege (Anzeige-Datei: die Hashes der vorhandenen Rohkopien) werden
    Zeilen, deren beleg_sha256 zu keiner Rohkopie passt, nur gezählt
    ("ohne_beleg"), nicht gemittelt.
    Zeilen an einem von der Stadt angekündigten Schließtag (fenster.RUHETAGE) werden nur
    gezählt ("ruhetag"), nicht gemittelt, es sei denn alle=True.
    Nicht-numerische wartezeit_minuten-Werte werden aus den Mittelwert-/
    Maximum-Berechnungen ausgeschlossen, zählen aber als Messtag.
    """
    def _draussen(row: dict) -> bool:
        return not alle and not _im_messfenster(row["abgerufen_am"])

    def _ruhetag(row: dict) -> bool:
        if alle:
            return False
        try:
            return fenster.ruhetag(fenster.parse_abgerufen_am(row["abgerufen_am"])) is not None
        except ValueError:
            return False

    def _ohne_beleg(row: dict) -> bool:
        return belege is not None and (row.get(BELEG_SPALTE) or "").strip() not in belege

    # Zwei Messstellen: je Slot zählt nur der früheste Abruf, der beide Filter besteht.
    fruehester = (
        frueheste_je_slot(
            [r for r in rows if not _draussen(r) and not _ruhetag(r) and not _ohne_beleg(r)]
        )
        if je_slot
        else None
    )

    ergebnis: dict = {}
    for row in rows:
        m = _monat_von(row["abgerufen_am"])
        if monat and m != monat:
            continue
        eintrag = ergebnis.setdefault(
            m,
            {
                "zentren": {},
                "gesamt": {"werte": []},
                "tage": set(),
                "ausgeschlossen": 0,
                "ohne_beleg": 0,
                "ruhetag": 0,
                "doppelt": 0,
            },
        )
        if _draussen(row):
            eintrag["ausgeschlossen"] += 1
            continue
        if _ruhetag(row):
            eintrag["ruhetag"] += 1
            continue
        if _ohne_beleg(row):
            eintrag["ohne_beleg"] += 1
            continue
        if fruehester is not None:
            schluessel = _slot_schluessel(row["abgerufen_am"])
            if schluessel is not None and (
                fenster.parse_abgerufen_am(row["abgerufen_am"]) != fruehester[schluessel]
            ):
                eintrag["doppelt"] += 1
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
        if eintrag.get("ohne_beleg"):
            kopf += f", ohne Beleg nicht gezählt: {eintrag['ohne_beleg']} Zeilen"
        if eintrag.get("ruhetag"):
            kopf += f", Ruhetag laut Stadt nicht gezählt: {eintrag['ruhetag']} Zeilen"
        if eintrag.get("doppelt"):
            kopf += f", im selben Slot später gemessen, nicht gezählt: {eintrag['doppelt']} Zeilen"
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
        "--csv", type=Path, default=None, help="Pfad zur CSV-Datei (Standard: je nach --quelle)"
    )
    parser.add_argument(
        "--quelle",
        choices=["feed", ANZEIGE_QUELLE],
        default="feed",
        help="feed = messwerte.csv (Standard); anzeige = messwerte-anzeige.csv und, wenn vorhanden, "
        "messwerte-anzeige-github.csv; nur Zeilen mit Beleg, je Slot der früheste Abruf",
    )
    parser.add_argument(
        "--alle", action="store_true", help="auch Abrufe außerhalb des Messfensters mitteln"
    )
    args = parser.parse_args(argv)
    ist_anzeige = args.quelle == ANZEIGE_QUELLE
    if args.csv is None:
        args.csv = ANZEIGE_CSV_PATH if ist_anzeige else CSV_PATH
        dateien = [args.csv]
        if ist_anzeige:
            # zweite Messstelle (GitHub-Workflow), liegt neben der Laptop-Datei
            dateien.append(args.csv.with_name(ANZEIGE_GITHUB_NAME))
    else:
        dateien = [args.csv]

    gelesen = [(datei, read_rows(datei)) for datei in dateien]
    rows = [row for _, teil in gelesen for row in teil]
    if not rows:
        print(f"Keine Messwerte in {args.csv} gefunden.", file=sys.stderr)
        return 1
    if ist_anzeige and any(BELEG_SPALTE not in row for row in rows):
        print(
            f"Fehler: {args.csv} ist keine Anzeige-Datei (Spalte {BELEG_SPALTE} fehlt).",
            file=sys.stderr,
        )
        return 1

    belege = beleg_hashes(args.csv.parent / BELEG_ORDNER) if ist_anzeige else None
    stats = compute_monthly_stats(
        rows, monat=args.monat, alle=args.alle, belege=belege, je_slot=ist_anzeige
    )
    if args.monat and args.monat not in stats:
        print(f"Kein Messwert für Monat {args.monat} in {args.csv}.", file=sys.stderr)
        return 1
    if args.monat and not stats[args.monat]["gesamt"]["werte"]:
        print(
            f"Monat {args.monat}: kein gezählter Abruf "
            f"({stats[args.monat]['ausgeschlossen']} Zeilen außerhalb des Messfensters, --alle zeigt sie; "
            f"{stats[args.monat]['ohne_beleg']} Zeilen ohne Beleg).",
            file=sys.stderr,
        )
        return 1

    if ist_anzeige:
        namen = ", ".join(datei.name for datei, teil in gelesen if teil)
        print(f"Quelle: {ANZEIGE_QUELLE} ({namen}), nur Zeilen mit Beleg, je Slot der früheste Abruf")
    print(format_table(stats), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
