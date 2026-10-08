"""Archivsicherung: für jede Wette eine Wayback-Kopie der Quelle, in der das Zitat wörtlich steht.

FORMAT.md §1.3 Regel 1 empfiehlt einen Archiv-Link zusätzlich zur Quelle. Stand 04.10.2026 hatten
15 von 216 öffentlichen Wetten einen; die DVG-Seite hinter duisburg-2026-007 war da schon 404.
Ein 200 vom Archiv reicht nicht: Erst wenn das Zitat in der archivierten Seite steht, trägt die
Kopie, falls die Stadt die Seite ändert (gleiche Regel wie belegbar.eu, lib/archiv.js).

Die Wettdateien bleiben unverändert (Kopf ist nach dem Commit eingefroren, §1.3 Regel 3).
Ergebnis ist eine Tabelle: recherche/archiv-quellen.csv (id, quelle, archiv, status, fehlt, geprueft_am).

Aufruf:  python werkzeuge/archivsicherung.py buecher [weitere Ordner …] [--speichern] [--nur-live] [--max N]
Ohne --speichern wird nur nach vorhandenen Kopien gesucht, nichts beim Archiv angestoßen.
Läuft fortsetzbar: Zeilen mit Status ok/pdf_ok werden übersprungen.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import time
from datetime import date
from pathlib import Path

import requests
import yaml

UA = "festgehalten-archivsicherung/0.1 (+https://felix3c.github.io/festgehalten/)"
SPALTEN = ["id", "quelle", "archiv", "status", "zitat_live", "fehlt", "geprueft_am"]
FERTIG = {"ok", "pdf_ok"}
PAUSE_SPEICHERN = 15  # Sekunden zwischen Save-Page-Now-Aufrufen (ohne Konto gedrosselt)


def norm_text(s: str) -> str:
    """Nur Buchstaben, Ziffern und %; Trennzeichen sind im Zitat Typografie, nicht Wortlaut."""
    s = re.sub(r"<[^>]+>", " ", str(s))
    s = re.sub(r"&[#\w]+;", " ", s)
    s = re.sub(r"[^\w%]+|_", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def zitat_teile(zitat: str) -> list[str]:
    """Auslassungen ([…], …, ...) teilen ein Zitat in Teile, die einzeln vorkommen müssen."""
    teile = re.split(r"\[\s*(?:…|\.\.\.)\s*\]|…|\.\.\.", str(zitat))
    return [t for t in (norm_text(x) for x in teile) if len(t.split(" ")) >= 3]


def zitat_in_text(zitat: str, text: str) -> list[str]:
    """Liefert die fehlenden Zitat-Teile (leer = Zitat steht vollständig drin)."""
    rein = norm_text(text)
    return [t for t in zitat_teile(zitat) if t not in rein]


def roh_url(archiv: str) -> str:
    """Wayback liefert mit „id_“ die Seite ohne eigene Leiste und ohne umgeschriebene Links."""
    return re.sub(r"/web/(\d+)(?:id_)?/", r"/web/\1id_/", archiv, count=1)


def ist_archiv(url: str) -> bool:
    return "web.archive.org/web/" in url


def wetten_sammeln(ordner: list[Path]) -> list[dict]:
    """Alle Wetten mit id, quelle, zitat aus den Ordnern; doppelte ids zählen einmal."""
    gesehen: dict[str, dict] = {}
    for wurzel in ordner:
        for pfad in sorted(wurzel.rglob("*.md")):
            if pfad.name in {"BUCH.md", "README.md", "FORMAT.md"} or "docs" in pfad.parts:
                continue
            roh = pfad.read_text(encoding="utf-8")
            if not roh.startswith("---"):
                continue
            kopf = yaml.safe_load(roh.split("\n---", 1)[0][3:]) or {}
            if not isinstance(kopf, dict) or not kopf.get("id") or not kopf.get("quelle"):
                continue
            gesehen.setdefault(str(kopf["id"]), {
                "id": str(kopf["id"]), "quelle": str(kopf["quelle"]).strip(),
                "zitat": str(kopf.get("zitat") or ""),
            })
    return sorted(gesehen.values(), key=lambda w: w["id"])


def text_aus_antwort(antwort: requests.Response) -> tuple[str, bool]:
    """(Text, ist_pdf). PDFs werden mit pypdf ausgelesen."""
    art = antwort.headers.get("content-type", "")
    if "pdf" in art or antwort.content[:5] == b"%PDF-":
        from pypdf import PdfReader
        leser = PdfReader(io.BytesIO(antwort.content))
        return " ".join((s.extract_text() or "") for s in leser.pages), True
    # Ohne charset im Kopf rät requests ISO-8859-1; dann wäre jedes Umlaut-Zitat „fehlt“.
    if "charset" not in art.lower():
        try:
            return antwort.content.decode("utf-8"), False
        except UnicodeDecodeError:
            antwort.encoding = antwort.apparent_encoding
    return antwort.text, False


_CDX: dict[str, str | None] = {}


def vorhandene_kopie(sitzung: requests.Session, url: str) -> str | None:
    """Jüngste Wayback-Kopie über die CDX-API (nur Status 200); je URL einmal, ein zweiter Versuch."""
    if url in _CDX:
        return _CDX[url]
    for versuch in range(2):
        try:
            _CDX[url] = _cdx_abfragen(sitzung, url)
            return _CDX[url]
        except (requests.RequestException, ValueError):
            if versuch:
                raise
            time.sleep(5)
    return None


def _cdx_abfragen(sitzung: requests.Session, url: str) -> str | None:
    r = sitzung.get("https://web.archive.org/cdx/search/cdx", params={
        "url": url, "output": "json", "filter": "statuscode:200", "limit": "-1", "fl": "timestamp,original",
    }, timeout=60)
    if r.status_code != 200:
        raise ValueError(f"CDX {r.status_code}")
    if not r.text.strip():
        return None
    zeilen = r.json()
    if len(zeilen) < 2:
        return None
    zeit, original = zeilen[-1]
    return f"https://web.archive.org/web/{zeit}/{original}"


def kopie_anstossen(sitzung: requests.Session, url: str) -> str | None:
    """Save Page Now ohne Konto; liefert die neue Kopie oder None."""
    r = sitzung.get(f"https://web.archive.org/save/{url}", timeout=180, allow_redirects=True)
    if ist_archiv(r.url):
        return r.url
    ort = r.headers.get("content-location", "")
    if ort.startswith("/web/"):
        return "https://web.archive.org" + ort
    return None


def pruefen(sitzung: requests.Session, wette: dict, speichern: bool) -> dict:
    zeile = {"id": wette["id"], "quelle": wette["quelle"], "archiv": "", "status": "", "zitat_live": "",
             "fehlt": "", "geprueft_am": date.today().isoformat()}
    kandidaten = [wette["quelle"]] if ist_archiv(wette["quelle"]) else []
    try:
        if not kandidaten:
            vorhanden = vorhandene_kopie(sitzung, wette["quelle"])
            if vorhanden:
                kandidaten.append(vorhanden)
        for runde in range(2):
            for archiv in kandidaten:
                antwort = sitzung.get(roh_url(archiv), timeout=120)
                if antwort.status_code != 200:
                    continue
                text, pdf = text_aus_antwort(antwort)
                fehlt = zitat_in_text(wette["zitat"], text)
                zeile.update(archiv=archiv, fehlt=" | ".join(fehlt))
                if not fehlt:
                    zeile["status"] = "pdf_ok" if pdf else "ok"
                    return zeile
                zeile["status"] = "zitat_fehlt"
            if runde == 0 and speichern and not ist_archiv(wette["quelle"]):
                neu = kopie_anstossen(sitzung, wette["quelle"])
                time.sleep(PAUSE_SPEICHERN)
                if not neu:
                    zeile["status"] = zeile["status"] or "speichern_fehlgeschlagen"
                    break
                kandidaten = [neu]
            else:
                break
        zeile["status"] = zeile["status"] or "kein_archiv"
        if not ist_archiv(wette["quelle"]):
            zeile["zitat_live"] = live_pruefen(sitzung, wette)
    except (requests.RequestException, ValueError) as e:
        zeile["status"] = "fehler"
        zeile["fehlt"] = type(e).__name__
    return zeile


def live_pruefen(sitzung: requests.Session, wette: dict) -> str:
    """Steht das Zitat auf der Live-Seite? ja / nein / http-Status (trennt „Seite geändert“ von „nie wörtlich“)."""
    try:
        antwort = sitzung.get(wette["quelle"], timeout=60)
    except requests.RequestException as e:
        return type(e).__name__
    if antwort.status_code != 200:
        return str(antwort.status_code)
    text, _ = text_aus_antwort(antwort)
    return "nein" if zitat_in_text(wette["zitat"], text) else "ja"


def offene_wetten(wetten: list[dict], tabelle: dict[str, dict], nur_live: bool) -> list[dict]:
    """Noch nicht tragende Wetten; mit nur_live nur die, deren Zitat zuletzt live wörtlich stand."""
    offen = [w for w in wetten if tabelle.get(w["id"], {}).get("status") not in FERTIG]
    if nur_live:
        offen = [w for w in offen if tabelle.get(w["id"], {}).get("zitat_live") == "ja"]
    return offen


def tabelle_lesen(pfad: Path) -> dict[str, dict]:
    if not pfad.exists():
        return {}
    with pfad.open(encoding="utf-8", newline="") as f:
        return {z["id"]: z for z in csv.DictReader(f)}


def tabelle_schreiben(pfad: Path, zeilen: dict[str, dict]) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    tmp = pfad.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SPALTEN)
        w.writeheader()
        for i in sorted(zeilen):
            w.writerow({k: zeilen[i].get(k, "") for k in SPALTEN})
    tmp.replace(pfad)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("ordner", nargs="+", type=Path)
    p.add_argument("--tabelle", type=Path, default=Path("recherche/archiv-quellen.csv"))
    p.add_argument("--speichern", action="store_true", help="fehlende Kopien bei Save Page Now anstoßen")
    p.add_argument("--nur-live", action="store_true", help="nur Wetten mit zitat_live=ja aus der Tabelle")
    p.add_argument("--max", type=int, default=0, help="höchstens N Wetten bearbeiten (0 = alle)")
    a = p.parse_args(argv)

    tabelle = tabelle_lesen(a.tabelle)
    offen = offene_wetten(wetten_sammeln(a.ordner), tabelle, a.nur_live)
    if a.max:
        offen = offen[: a.max]
    sitzung = requests.Session()
    sitzung.headers["User-Agent"] = UA
    for nr, wette in enumerate(offen, 1):
        zeile = pruefen(sitzung, wette, a.speichern)
        tabelle[wette["id"]] = zeile
        tabelle_schreiben(a.tabelle, tabelle)
        print(f"{nr}/{len(offen)} {zeile['id']}: {zeile['status']}", flush=True)
    zahl: dict[str, int] = {}
    for z in tabelle.values():
        zahl[z["status"]] = zahl.get(z["status"], 0) + 1
    print("Stand:", ", ".join(f"{k} {v}" for k, v in sorted(zahl.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
