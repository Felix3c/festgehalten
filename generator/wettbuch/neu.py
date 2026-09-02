"""Gerüst für ein neues Buch: BUCH.md, eine Beispielwette, ein Pages-Workflow.

Mehr nicht. Alles, was hier angelegt wird, baut ohne Änderung durch; die
Platzhalter sind als solche zu erkennen und stehen in FORMAT.md §1 und §4.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

BUCH_MD = """---
titel: {stadt} gegen {stadt}
halter: DEIN NAME
kontakt: https://DEINE-SEITE.example
seit: {heute}
lizenz: CC0
format: v1
---

Worum es geht: {stadt} sagt laufend, was sie erwartet — Termine, Zahlen, Plätze.
Dieses Buch schreibt es auf, wartet, und schaut nach.

Auswahlregel: Aussagen mit Zahl und Datum aus öffentlichen Quellen; Absichten
ohne beides bleiben draußen. (Pflicht für Anerkennung, FORMAT.md §8.1.)

Fehler melden: Kontakt oben.

Der Halter nimmt von der gemessenen Stelle kein Geld außer einem veröffentlichten
Festpreis für selbst hinterlegte Einträge (festgehalten-Format v1, §8.4). Bisher: keins.
"""

WETTE_MD = """---
id: {kurz}-{jahr}-001
institution: {stadt}
gesagt_von: WER HAT ES GESAGT (Amt, Person, Gremium)
gesagt_am: {heute}
quelle: https://QUELLE.example/pressemitteilung
zitat: "WÖRTLICHES ZITAT, gekürzt mit …"
frage: IST X AM TT.MM.JJJJ EINGETRETEN?
typ: ja_nein
pruefung_am: {in_einem_jahr}
prognosen:
  - von: {stadt}
    wert: 1.00
    hinterlegt_am: {heute}
    art: angekuendigt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Woher die Aussage stammt, was drumherum gesagt wurde.

## Übersetzung
Wie aus dem Zitat die Ja/Nein-Frage wurde (FORMAT.md §1.3.4).
"""

PAGES_YML = """name: Buch bauen und veröffentlichen
on:
  push:
    branches: [main, master]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  bauen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {{ python-version: "3.12" }}
      - run: python -m pip install "festgehalten @ git+https://github.com/Felix3c/festgehalten"
      - run: festgehalten bauen . site
      - uses: actions/upload-pages-artifact@v3
        with: {{ path: site }}
  veroeffentlichen:
    needs: bauen
    runs-on: ubuntu-latest
    environment: {{ name: github-pages }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
"""


def _kurz(name: str) -> str:
    erlaubt = "abcdefghijklmnopqrstuvwxyz0123456789-"
    roh = name.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    k = "".join(c if c in erlaubt else "-" for c in roh).strip("-")
    return k or "buch"


def buch_anlegen(ziel: Path, stadt: str | None = None, heute: date | None = None) -> list[Path]:
    """Legt das Gerüst an. Weigert sich, wenn der Ordner schon Dateien enthält."""
    if ziel.exists() and any(ziel.iterdir()):
        raise FileExistsError(f"{ziel}: nicht leer, nichts geschrieben.")
    heute = heute or date.today()
    stadt = stadt or ziel.name
    werte = {
        "stadt": stadt,
        "kurz": _kurz(stadt),
        "heute": heute.isoformat(),
        "jahr": heute.year,
        "in_einem_jahr": heute.replace(year=heute.year + 1).isoformat(),
    }
    dateien = {
        ziel / "BUCH.md": BUCH_MD.format(**werte),
        ziel / "wetten" / f"{werte['kurz']}-{werte['jahr']}-001.md": WETTE_MD.format(**werte),
        ziel / ".github" / "workflows" / "pages.yml": PAGES_YML.format(**werte),
    }
    for pfad, inhalt in dateien.items():
        pfad.parent.mkdir(parents=True, exist_ok=True)
        pfad.write_text(inhalt, encoding="utf-8")
    return list(dateien)
