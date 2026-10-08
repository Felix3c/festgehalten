"""Wortlaut-Vorschläge für nicht wörtliche Zitate (Vorarbeit zu Frage 61, ändert keine Wette).

Liest `recherche/archiv-quellen.csv` (aus archivsicherung.py), holt für jede Wette mit Status
`zitat_fehlt` die Archivkopie und sucht die Stelle (ein bis drei aufeinanderfolgende Sätze), die das
Zitat am besten deckt. Ergebnis: `recherche/wortlaut-vorschlaege.csv`. Ein Vorschlag ist nur ein
Fundort; ob er als Vermerk in die Wette kommt, entscheidet Felix (Frage 61).

    python werkzeuge/wortlaut_vorschlag.py buecher [--max N]
"""
from __future__ import annotations

import argparse
import csv
import html
import re
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from archivsicherung import UA, roh_url, tabelle_lesen, text_aus_antwort, wetten_sammeln  # noqa: E402

SPALTEN = ["id", "archiv", "zitat", "wortlaut", "deckung", "zahlen_fehlen", "zahl_nicht_auf_seite", "bewertung"]
SCHWELLE = 0.6  # Anteil der Zitat-Wörter, die in der Stelle vorkommen müssen
FENSTER = 3     # höchstens so viele aufeinanderfolgende Sätze
MAX_ZEICHEN = 600
MIN_TEXT = 200  # weniger sichtbarer Text = Bot-Schutz- oder Leerseite im Archiv


def sichtbarer_text(roh: str) -> str:
    """HTML ohne Skripte, Stile und Tags; Blockgrenzen werden Zeilenumbrüche."""
    t = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", roh)
    t = re.sub(r"(?i)</?(p|div|li|h\d|br|tr|td|section|article|header|footer|nav)\b[^>]*>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"[ \t\r\f\v\xa0]+", " ", t)
    return re.sub(r"\n\s*", "\n", t).strip()


ABKUERZUNGEN = {"ca", "rd", "rund", "nr", "bzw", "z", "b", "u", "a", "mio", "mrd", "dr", "st", "inkl", "ggf", "vgl", "abs"}


def saetze(text: str) -> list[str]:
    """Absätze, dann Satzenden (Punkt/!/? + Leerzeichen + Großbuchstabe oder Ziffer); nicht nach Abkürzungen."""
    aus: list[str] = []
    for absatz in text.split("\n"):
        stueck = ""
        for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9„\"])", absatz.strip()):
            stueck = f"{stueck} {s}".strip()
            letztes = re.findall(r"([^\W\d_]+)\.$", stueck)
            if letztes and letztes[0].lower() in ABKUERZUNGEN:
                continue
            if stueck:
                aus.append(stueck)
            stueck = ""
        if stueck:
            aus.append(stueck)
    return aus


def woerter(s: str) -> list[str]:
    return re.findall(r"[^\W_]+|%", s.lower())


def _zahlen(ws: list[str]) -> set[str]:
    return {w for w in ws if w.isdigit()}


def bester_wortlaut(zitat: str, text: str) -> dict:
    """Stelle mit der höchsten Deckung der Zitat-Wörter; bei Gleichstand die kürzere."""
    ziel = woerter(zitat)
    ziel_menge = set(ziel)
    if not ziel_menge:
        return {"wortlaut": "", "deckung": 0.0, "zahlen_fehlen": ""}
    liste = saetze(text)
    menge = [set(woerter(s)) for s in liste]
    best = ("", 0.0, 10**9)
    for i in range(len(liste)):
        vereint: set[str] = set()
        for k in range(FENSTER):
            if i + k >= len(liste):
                break
            vereint |= menge[i + k]
            stelle = " ".join(liste[i:i + k + 1])
            if len(stelle) > MAX_ZEICHEN and k:
                break
            deckung = len(ziel_menge & vereint) / len(ziel_menge)
            if deckung > best[1] + 1e-9 or (abs(deckung - best[1]) < 1e-9 and len(stelle) < best[2]):
                best = (stelle, deckung, len(stelle))
            if deckung == 1.0:
                break
    fehlen = sorted(_zahlen(ziel) - set(woerter(best[0])))
    return {"wortlaut": best[0], "deckung": round(best[1], 2), "zahlen_fehlen": " ".join(fehlen)}


def zahlen_nicht_auf_seite(zitat: str, text: str) -> str:
    """Zahlen des Zitats (wie geschrieben, z. B. 97,0), die nirgends auf der Seite stehen."""
    seite = re.sub(r"\s+", " ", text)
    fehlen = [z for z in dict.fromkeys(re.findall(r"\d+(?:[.,]\d+)*", zitat))
              if not re.search(rf"(?<![\d.,]){re.escape(z)}(?![\d]|[.,]\d)", seite)]
    return " ".join(fehlen)


def bewerten(treffer: dict, textlaenge: int = MIN_TEXT) -> str:
    if textlaenge < MIN_TEXT:
        return "archiv_leer"
    if treffer["deckung"] >= SCHWELLE and not treffer["zahlen_fehlen"]:
        return "vorschlag"
    if treffer["deckung"] >= SCHWELLE:
        return "zahl_abweichend"
    return "kein_treffer"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("ordner", nargs="+", type=Path)
    p.add_argument("--tabelle", type=Path, default=Path("recherche/archiv-quellen.csv"))
    p.add_argument("--aus", type=Path, default=Path("recherche/wortlaut-vorschlaege.csv"))
    p.add_argument("--max", type=int, default=0)
    a = p.parse_args(argv)

    tabelle = tabelle_lesen(a.tabelle)
    zitate = {w["id"]: w["zitat"] for w in wetten_sammeln(a.ordner)}
    offen = [z for z in tabelle.values() if z["status"] == "zitat_fehlt" and z["archiv"] and z["id"] in zitate]
    if a.max:
        offen = offen[: a.max]
    sitzung = requests.Session()
    sitzung.headers["User-Agent"] = UA
    zeilen = []
    for nr, z in enumerate(offen, 1):
        zeile = {"id": z["id"], "archiv": z["archiv"], "zitat": " ".join(zitate[z["id"]].split())}
        try:
            antwort = sitzung.get(roh_url(z["archiv"]), timeout=120)
            if antwort.status_code != 200:
                raise ValueError(f"HTTP {antwort.status_code}")
            text, pdf = text_aus_antwort(antwort)
            sichtbar = text if pdf else sichtbarer_text(text)
            treffer = bester_wortlaut(zeile["zitat"], sichtbar)
            zeile.update(treffer, bewertung=bewerten(treffer, len(sichtbar)),
                         zahl_nicht_auf_seite=zahlen_nicht_auf_seite(zeile["zitat"], sichtbar))
        except (requests.RequestException, ValueError) as e:
            zeile.update(wortlaut="", deckung="", zahlen_fehlen="", zahl_nicht_auf_seite="", bewertung=f"fehler {e}"[:80])
        zeilen.append(zeile)
        print(f"{nr}/{len(offen)} {zeile['id']}: {zeile['bewertung']} {zeile['deckung']}", flush=True)
        time.sleep(1)
    a.aus.parent.mkdir(parents=True, exist_ok=True)
    with a.aus.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SPALTEN)
        w.writeheader()
        w.writerows(sorted(zeilen, key=lambda r: r["id"]))
    zahl: dict[str, int] = {}
    for r in zeilen:
        b = r["bewertung"].split(" ")[0]
        zahl[b] = zahl.get(b, 0) + 1
    print("Stand:", ", ".join(f"{k} {v}" for k, v in sorted(zahl.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
