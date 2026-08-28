# Wettbuch-Generator v1 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ein Python-Programm, das aus einem Wettbuch-Ordner (Markdown-Dateien mit YAML-Kopf nach `FORMAT.md` v1) eine statische HTML-Seite mit Rangliste erzeugt — plus das erste Buch „Köln gegen Köln" mit fünf Einträgen als Startbestand.

**Architecture:** Ein kleines Python-Paket `wettbuch` mit vier Modulen in klarer Reihenfolge: `lesen` (Dateien → Dicts), `pruefen` (Dicts → Fehlerliste), `bewerten` (Dicts → Scores/Rangliste), `seiten` (alles → HTML + JSON). Ein CLI-Einstieg `python -m wettbuch bauen <buch> <ausgabe>` verbindet sie. Keine Datenbank, kein Server, keine Laufzeit-Abhängigkeiten außer `pyyaml` und `markdown`. Tests mit `pytest` gegen kleine Fixture-Bücher.

**Tech Stack:** Python ≥ 3.11, `pyyaml`, `markdown`, `pytest`. Ausgabe: reines HTML + eine CSS-Datei, kein JavaScript nötig.

**Spec:** `C:\Users\skyla\wettbuch\FORMAT.md` (v1). Der Plan argumentiert aus der Spec; Ausführende lesen beide.

## Global Constraints

- Sprache der Referenz-Implementierung: Python 3, keine Abhängigkeiten außer `pyyaml` und `markdown` (FORMAT.md §5).
- Fehler in Einträgen → **Abbruch mit Dateiname und Feld**, kein Warnhinweis (§5.1, §2.1).
- `ausgang` 0/1/Zahl nur mit `beleg_ausgang` (§2.1). `pruefung_am` ≤ `aufgeloest_am` (§5.1). ids eindeutig (§5.1).
- Brier `(wert − ausgang)²`; Abstand `|wert − ausgang|`; Rang erst ab **10** aufgelösten `ja_nein`-Wetten (§3).
- Reproduzierbar: derselbe Ordner → dieselbe Seite; kein „heute" außer Build-Zeitstempel im Footer (§5.5).
- Alle Texte der Seite auf Deutsch. Feldnamen exakt wie in FORMAT.md §1.1 (`gesagt_am`, `pruefung_am`, `beleg_ausgang`, …).
- Datumsformat in Dateien: ISO `YYYY-MM-DD`. Anzeige: `TT.MM.JJJJ`.
- Commits ohne Co-Author-Zeile; Format `<typ>: <beschreibung>` (Felix' git-workflow-Regel). Git-Identität im Repo: `git -c user.name=Felix -c user.email=felix.h.lind@gmail.com` voranstellen, falls global nicht gesetzt.
- Alle Befehle im Bash-Tool in `C:/Users/skyla/wettbuch` ausführen.

---

## Dateistruktur

```
C:\Users\skyla\wettbuch\
├── FORMAT.md                         (Spec, existiert)
├── WETTBUCH.md                       (manuelles Buch von Felix, bleibt vorerst)
├── koeln\RECHERCHE.md                (31 Behauptungen, existiert)
├── pyproject.toml                    Task 1
├── generator\
│   ├── wettbuch\
│   │   ├── __init__.py               Task 1
│   │   ├── __main__.py               Task 6  (python -m wettbuch)
│   │   ├── lesen.py                  Task 1, 2  — Datei → Dict
│   │   ├── pruefen.py                Task 3     — Dict → Liste[Fehler]
│   │   ├── bewerten.py               Task 4     — Scores, Aggregation, Rangliste
│   │   ├── seiten.py                 Task 5     — HTML + JSON
│   │   ├── cli.py                    Task 6
│   │   └── stil.css                  Task 5
│   └── tests\
│       ├── conftest.py               Task 1     — Fixture-Buch anlegen
│       ├── test_lesen.py             Task 1, 2
│       ├── test_pruefen.py           Task 3
│       ├── test_bewerten.py          Task 4
│       ├── test_seiten.py            Task 5
│       └── test_cli.py               Task 6
├── buecher\
│   └── koeln\
│       ├── BUCH.md                   Task 7
│       └── wetten\
│           ├── koeln-2025-001.md …   Task 7 (fünf Einträge)
└── .github\workflows\pages.yml       Task 8
```

**Verantwortlichkeiten:**
- `lesen.py` kennt Dateien und YAML, sonst nichts. Gibt rohe Dicts zurück.
- `pruefen.py` kennt die Regeln aus FORMAT.md §1–2. Gibt eine Liste `Fehler(datei, feld, text)` zurück, wirft nicht.
- `bewerten.py` kennt Mathematik aus §3. Reine Funktionen über Dicts.
- `seiten.py` kennt HTML. Bekommt fertige Daten, rechnet nichts.
- `cli.py` verbindet in dieser Reihenfolge und bricht bei Fehlern mit Exit 1 ab.

---

### Task 1: Projektgerüst und Wette lesen

**Files:**
- Create: `pyproject.toml`
- Create: `generator/wettbuch/__init__.py`
- Create: `generator/wettbuch/lesen.py`
- Create: `generator/tests/conftest.py`
- Create: `generator/tests/test_lesen.py`

**Interfaces:**
- Produces: `lesen.wette_lesen(pfad: Path) -> dict` — gibt den YAML-Kopf als Dict zurück, ergänzt um `"_datei": str(pfad.name)` und `"_text": str` (Markdown-Body ohne Kopf). Wirft `LeseFehler(datei, text)` bei fehlendem oder kaputtem Kopf.
- Produces: `lesen.LeseFehler(Exception)` mit Attributen `datei`, `text`.

- [ ] **Step 1: pyproject.toml anlegen**

```toml
[project]
name = "wettbuch"
version = "0.1.0"
description = "Referenz-Implementierung des Wettbuch-Formats v1"
requires-python = ">=3.11"
dependencies = ["pyyaml>=6.0", "markdown>=3.5"]

[project.optional-dependencies]
test = ["pytest>=8.0"]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["generator"]

[tool.setuptools.package-data]
wettbuch = ["*.css"]

[tool.pytest.ini_options]
testpaths = ["generator/tests"]
```

- [ ] **Step 2: Paket installieren (editable) und Test-Abhängigkeiten**

Run: `python -m pip install -e ".[test]"`
Expected: `Successfully installed wettbuch-0.1.0` (plus pyyaml, markdown, pytest falls fehlend).

- [ ] **Step 3: Fixture in conftest.py schreiben**

```python
# generator/tests/conftest.py
from pathlib import Path
import pytest

WETTE_OK = """---
id: test-2025-001
institution: Stadt Test
gesagt_von: Stadtdirektorin Muster
gesagt_am: 2025-10-01
quelle: https://example.org/pm/1
zitat: "Das Haus wird Ende Oktober fertig."
frage: Ist das Haus am 31.10.2025 fertig?
typ: ja_nein
pruefung_am: 2025-11-01
prognosen:
  - von: Stadt Test
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
  - von: Computer
    wert: 0.35
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Ein Testeintrag.
"""

BUCH_OK = """---
titel: Test gegen Test
halter: Testhalter
kontakt: https://example.org
seit: 2026-08-28
lizenz: CC0
format: v1
---

Worum es geht.
"""


@pytest.fixture
def buch(tmp_path: Path) -> Path:
    """Ein minimales, gültiges Buch mit einer offenen Wette."""
    (tmp_path / "BUCH.md").write_text(BUCH_OK, encoding="utf-8")
    wetten = tmp_path / "wetten"
    wetten.mkdir()
    (wetten / "test-2025-001.md").write_text(WETTE_OK, encoding="utf-8")
    return tmp_path
```

- [ ] **Step 4: Failing Test für wette_lesen schreiben**

```python
# generator/tests/test_lesen.py
from pathlib import Path
import pytest
from wettbuch import lesen


def test_wette_lesen_liefert_kopf_und_text(buch: Path):
    w = lesen.wette_lesen(buch / "wetten" / "test-2025-001.md")
    assert w["id"] == "test-2025-001"
    assert w["typ"] == "ja_nein"
    assert w["prognosen"][1]["von"] == "Computer"
    assert w["prognosen"][1]["wert"] == 0.35
    assert w["_datei"] == "test-2025-001.md"
    assert "## Kontext" in w["_text"]


def test_wette_lesen_ohne_kopf_wirft(tmp_path: Path):
    p = tmp_path / "kaputt.md"
    p.write_text("kein kopf hier", encoding="utf-8")
    with pytest.raises(lesen.LeseFehler) as e:
        lesen.wette_lesen(p)
    assert e.value.datei == "kaputt.md"
```

- [ ] **Step 5: Test laufen lassen, muss fehlschlagen**

Run: `python -m pytest generator/tests/test_lesen.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'wettbuch'` oder `ImportError: cannot import name 'lesen'`.

- [ ] **Step 6: lesen.py minimal implementieren**

```python
# generator/wettbuch/__init__.py
"""Wettbuch — Referenz-Implementierung des Formats v1."""
```

```python
# generator/wettbuch/lesen.py
"""Dateien lesen. Kennt YAML und Markdown, sonst nichts."""
from __future__ import annotations

from pathlib import Path

import yaml


class LeseFehler(Exception):
    def __init__(self, datei: str, text: str):
        super().__init__(f"{datei}: {text}")
        self.datei = datei
        self.text = text


def _kopf_und_text(pfad: Path) -> tuple[dict, str]:
    roh = pfad.read_text(encoding="utf-8")
    if not roh.startswith("---"):
        raise LeseFehler(pfad.name, "kein YAML-Kopf (Datei beginnt nicht mit ---)")
    teile = roh.split("\n---", 1)
    if len(teile) < 2:
        raise LeseFehler(pfad.name, "YAML-Kopf nicht geschlossen (zweites --- fehlt)")
    kopf_roh = teile[0][3:]
    text = teile[1].lstrip("\n")
    try:
        kopf = yaml.safe_load(kopf_roh) or {}
    except yaml.YAMLError as e:
        raise LeseFehler(pfad.name, f"YAML ungültig: {e}") from e
    if not isinstance(kopf, dict):
        raise LeseFehler(pfad.name, "YAML-Kopf ist kein Mapping")
    return kopf, text


def wette_lesen(pfad: Path) -> dict:
    kopf, text = _kopf_und_text(pfad)
    kopf["_datei"] = pfad.name
    kopf["_text"] = text
    return kopf
```

- [ ] **Step 7: Tests laufen lassen, müssen bestehen**

Run: `python -m pytest generator/tests/test_lesen.py -v`
Expected: 2 passed.

- [ ] **Step 8: Commit**

```bash
git add pyproject.toml generator/
git commit -m "feat: projektgeruest und wette_lesen"
```

---

### Task 2: Buch lesen (BUCH.md + alle Wetten)

**Files:**
- Modify: `generator/wettbuch/lesen.py`
- Modify: `generator/tests/test_lesen.py`

**Interfaces:**
- Consumes: `lesen.wette_lesen`, `lesen._kopf_und_text` aus Task 1.
- Produces: `lesen.buch_lesen(ordner: Path) -> dict` mit Schlüsseln `"meta": dict` (YAML-Kopf von BUCH.md + `"_text"`), `"wetten": list[dict]` (sortiert nach `id`), `"ordner": Path`. Liest alle `*.md` rekursiv außer `BUCH.md`, `README.md`, `FORMAT.md` und Dateien unter `docs/`. Wirft `LeseFehler` wenn `BUCH.md` fehlt.

- [ ] **Step 1: Failing Tests schreiben**

```python
# an generator/tests/test_lesen.py anhängen

def test_buch_lesen_liefert_meta_und_wetten(buch: Path):
    b = lesen.buch_lesen(buch)
    assert b["meta"]["titel"] == "Test gegen Test"
    assert b["meta"]["format"] == "v1"
    assert [w["id"] for w in b["wetten"]] == ["test-2025-001"]
    assert b["ordner"] == buch


def test_buch_lesen_sortiert_nach_id(buch: Path):
    zweite = (buch / "wetten" / "test-2025-001.md").read_text(encoding="utf-8")
    zweite = zweite.replace("id: test-2025-001", "id: test-2024-009")
    (buch / "wetten" / "aaa.md").write_text(zweite, encoding="utf-8")
    b = lesen.buch_lesen(buch)
    assert [w["id"] for w in b["wetten"]] == ["test-2024-009", "test-2025-001"]


def test_buch_lesen_ohne_buch_md_wirft(tmp_path: Path):
    with pytest.raises(lesen.LeseFehler) as e:
        lesen.buch_lesen(tmp_path)
    assert e.value.datei == "BUCH.md"
```

- [ ] **Step 2: Tests laufen lassen, müssen fehlschlagen**

Run: `python -m pytest generator/tests/test_lesen.py -v`
Expected: 3 FAIL mit `AttributeError: module 'wettbuch.lesen' has no attribute 'buch_lesen'`, 2 passed.

- [ ] **Step 3: buch_lesen implementieren**

```python
# an generator/wettbuch/lesen.py anhängen

AUSGESCHLOSSEN = {"BUCH.md", "README.md", "FORMAT.md"}


def buch_lesen(ordner: Path) -> dict:
    buch_md = ordner / "BUCH.md"
    if not buch_md.exists():
        raise LeseFehler("BUCH.md", f"nicht gefunden in {ordner}")
    meta, meta_text = _kopf_und_text(buch_md)
    meta["_text"] = meta_text

    wetten: list[dict] = []
    for pfad in sorted(ordner.rglob("*.md")):
        if pfad.name in AUSGESCHLOSSEN:
            continue
        if "docs" in pfad.relative_to(ordner).parts:
            continue
        wetten.append(wette_lesen(pfad))
    wetten.sort(key=lambda w: str(w.get("id", "")))
    return {"meta": meta, "wetten": wetten, "ordner": ordner}
```

- [ ] **Step 4: Tests laufen lassen, müssen bestehen**

Run: `python -m pytest generator/tests/test_lesen.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add generator/
git commit -m "feat: buch_lesen liest BUCH.md und alle wetten"
```

---

### Task 3: Prüfen (FORMAT.md §1.1, §1.2, §2.1, §5.1)

**Files:**
- Create: `generator/wettbuch/pruefen.py`
- Create: `generator/tests/test_pruefen.py`

**Interfaces:**
- Consumes: Dicts aus `lesen.buch_lesen`.
- Produces: `pruefen.Fehler` (frozen dataclass: `datei: str`, `feld: str`, `text: str`) und `pruefen.buch_pruefen(buch: dict) -> list[Fehler]`. Leere Liste = gültig. Prüft nur Struktur und Regeln, rechnet nichts.

Regeln, die geprüft werden (jede ein eigener Test):
1. Pflichtfelder vorhanden: `id, institution, gesagt_von, gesagt_am, quelle, zitat, frage, typ, pruefung_am, prognosen, ausgang, aufgeloest_am, beleg_ausgang, vermerke`. Fehlt eines, wird **nur** das gemeldet (der Rest ist ohne Pflichtfelder nicht prüfbar).
2. `typ` ∈ {`ja_nein`, `punkt`}.
3. Datumsfelder (`gesagt_am`, `pruefung_am`, `aufgeloest_am` wenn gesetzt, `hinterlegt_am` je Prognose) sind `datetime.date` (pyyaml parst ISO-Daten automatisch) — sonst Fehler.
4. `quelle` und `beleg_ausgang` (wenn gesetzt) beginnen mit `http://` oder `https://`.
5. `prognosen` ist Liste mit ≥1 Eintrag; jeder hat `von, wert, hinterlegt_am, art`; `art` ∈ {`angekuendigt`, `voraussichtlich`, `geschaetzt`}.
6. Bei `ja_nein`: jeder `wert` ist Zahl in [0, 1]. `art: angekuendigt` → `wert == 1.0`; `art: voraussichtlich` → `wert == 0.8`.
7. Bei `punkt`: `einheit` gesetzt; jeder `wert` ist Zahl.
8. `ausgang` ∈ {None, 0, 1, Zahl, `"verfallen"`, `"strittig"`}; bei `ja_nein` und Zahl: nur 0 oder 1.
9. **Beleg-Pflicht:** `ausgang` ist 0/1/Zahl → `beleg_ausgang` gesetzt und `aufgeloest_am` gesetzt.
10. `aufgeloest_am` gesetzt → `pruefung_am <= aufgeloest_am`.
11. ids eindeutig über das Buch.
12. `meta` hat `titel, halter, seit, format`; `format == "v1"`.

- [ ] **Step 1: Failing Tests schreiben**

```python
# generator/tests/test_pruefen.py
from datetime import date
from pathlib import Path
import copy

import pytest
from wettbuch import lesen, pruefen


@pytest.fixture
def gueltig(buch: Path) -> dict:
    return lesen.buch_lesen(buch)


def _wette(b: dict) -> dict:
    return b["wetten"][0]


def test_gueltiges_buch_hat_keine_fehler(gueltig):
    assert pruefen.buch_pruefen(gueltig) == []


def test_pflichtfeld_fehlt(gueltig):
    del _wette(gueltig)["zitat"]
    f = pruefen.buch_pruefen(gueltig)
    assert [(x.datei, x.feld) for x in f] == [("test-2025-001.md", "zitat")]


def test_typ_unbekannt(gueltig):
    _wette(gueltig)["typ"] = "vielleicht"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "typ"


def test_datum_muss_datum_sein(gueltig):
    _wette(gueltig)["gesagt_am"] = "gestern"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "gesagt_am"


def test_quelle_muss_url_sein(gueltig):
    _wette(gueltig)["quelle"] = "Pressemitteilung 27942"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "quelle"


def test_prognose_art_unbekannt(gueltig):
    _wette(gueltig)["prognosen"][1]["art"] = "geraten"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "prognosen[1].art"


def test_angekuendigt_muss_1_sein(gueltig):
    _wette(gueltig)["prognosen"][0]["wert"] = 0.9
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "prognosen[0].wert"


def test_ja_nein_wert_ausserhalb_0_1(gueltig):
    _wette(gueltig)["prognosen"][1]["wert"] = 1.5
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "prognosen[1].wert"


def test_punkt_braucht_einheit(gueltig):
    w = _wette(gueltig)
    w["typ"] = "punkt"
    w["prognosen"][0]["wert"] = 594.8
    w["prognosen"][1]["wert"] = 625
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "einheit"


def test_ausgang_ohne_beleg_ist_fehler(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = 1
    w["aufgeloest_am"] = date(2025, 11, 2)
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "beleg_ausgang"


def test_ausgang_mit_beleg_ist_ok(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = 1
    w["aufgeloest_am"] = date(2025, 11, 2)
    w["beleg_ausgang"] = "https://example.org/pm/2"
    assert pruefen.buch_pruefen(gueltig) == []


def test_aufgeloest_vor_pruefung_ist_fehler(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = 0
    w["aufgeloest_am"] = date(2025, 10, 15)
    w["beleg_ausgang"] = "https://example.org/pm/2"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "aufgeloest_am"


def test_verfallen_braucht_keinen_beleg(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = "verfallen"
    w["aufgeloest_am"] = date(2027, 11, 2)
    assert pruefen.buch_pruefen(gueltig) == []


def test_ids_muessen_eindeutig_sein(gueltig):
    gueltig["wetten"].append(copy.deepcopy(_wette(gueltig)))
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "id"


def test_meta_format_muss_v1_sein(gueltig):
    gueltig["meta"]["format"] = "v2"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].datei == "BUCH.md" and f[0].feld == "format"
```

- [ ] **Step 2: Tests laufen lassen, müssen fehlschlagen**

Run: `python -m pytest generator/tests/test_pruefen.py -v`
Expected: alle FAIL mit `ImportError: cannot import name 'pruefen'`.

- [ ] **Step 3: pruefen.py implementieren**

```python
# generator/wettbuch/pruefen.py
"""Regeln aus FORMAT.md §1–2 prüfen. Wirft nicht, sammelt Fehler."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from numbers import Real

PFLICHT = [
    "id", "institution", "gesagt_von", "gesagt_am", "quelle", "zitat", "frage",
    "typ", "pruefung_am", "prognosen", "ausgang", "aufgeloest_am",
    "beleg_ausgang", "vermerke",
]
TYPEN = {"ja_nein", "punkt"}
ARTEN = {"angekuendigt", "voraussichtlich", "geschaetzt"}
FESTE_WERTE = {"angekuendigt": 1.0, "voraussichtlich": 0.8}
META_PFLICHT = ["titel", "halter", "seit", "format"]
NICHT_AUFGELOEST = {"verfallen", "strittig"}


@dataclass(frozen=True)
class Fehler:
    datei: str
    feld: str
    text: str


def _ist_datum(x) -> bool:
    return isinstance(x, date)


def _ist_zahl(x) -> bool:
    return isinstance(x, Real) and not isinstance(x, bool)


def _ist_url(x) -> bool:
    return isinstance(x, str) and (x.startswith("http://") or x.startswith("https://"))


def _prognosen_pruefen(d: str, typ: str, prognosen) -> list[Fehler]:
    f: list[Fehler] = []
    if not isinstance(prognosen, list) or not prognosen:
        return [Fehler(d, "prognosen", "muss eine Liste mit mindestens einem Eintrag sein")]
    for i, p in enumerate(prognosen):
        pf = f"prognosen[{i}]"
        if not isinstance(p, dict):
            f.append(Fehler(d, pf, "muss ein Mapping sein"))
            continue
        fehlend = [k for k in ("von", "wert", "hinterlegt_am", "art") if k not in p]
        for k in fehlend:
            f.append(Fehler(d, f"{pf}.{k}", "fehlt"))
        if fehlend:
            continue
        if p["art"] not in ARTEN:
            f.append(Fehler(d, f"{pf}.art", f"muss angekuendigt, voraussichtlich oder geschaetzt sein, ist {p['art']!r}"))
        if not _ist_datum(p["hinterlegt_am"]):
            f.append(Fehler(d, f"{pf}.hinterlegt_am", "muss ein Datum sein"))
        if not _ist_zahl(p["wert"]):
            f.append(Fehler(d, f"{pf}.wert", "muss eine Zahl sein"))
            continue
        if typ == "ja_nein":
            if not 0 <= p["wert"] <= 1:
                f.append(Fehler(d, f"{pf}.wert", "muss bei ja_nein zwischen 0 und 1 liegen"))
            elif p["art"] in FESTE_WERTE and abs(p["wert"] - FESTE_WERTE[p["art"]]) > 1e-9:
                f.append(Fehler(d, f"{pf}.wert", f"bei art {p['art']} muss wert {FESTE_WERTE[p['art']]} sein"))
    return f


def _ausgang_pruefen(d: str, w: dict) -> list[Fehler]:
    f: list[Fehler] = []
    a = w["ausgang"]
    if a is None or a in NICHT_AUFGELOEST:
        return f
    if not _ist_zahl(a):
        return [Fehler(d, "ausgang", "muss null, 0, 1, Zahl, 'verfallen' oder 'strittig' sein")]
    if w["typ"] == "ja_nein" and a not in (0, 1):
        f.append(Fehler(d, "ausgang", "bei ja_nein nur 0 oder 1"))
    if w["beleg_ausgang"] is None:
        f.append(Fehler(d, "beleg_ausgang", "Beleg-Pflicht: ausgang gesetzt, aber kein beleg_ausgang (FORMAT.md §2.1)"))
    if w["aufgeloest_am"] is None:
        f.append(Fehler(d, "aufgeloest_am", "ausgang gesetzt, aber kein aufgeloest_am"))
    return f


def _wette_pruefen(w: dict) -> list[Fehler]:
    d = w.get("_datei", "?")
    fehlend = [feld for feld in PFLICHT if feld not in w]
    if fehlend:
        return [Fehler(d, feld, "Pflichtfeld fehlt") for feld in fehlend]

    f: list[Fehler] = []
    typ = w["typ"]
    if typ not in TYPEN:
        f.append(Fehler(d, "typ", f"muss ja_nein oder punkt sein, ist {typ!r}"))
    for feld in ("gesagt_am", "pruefung_am"):
        if not _ist_datum(w[feld]):
            f.append(Fehler(d, feld, "muss ein Datum YYYY-MM-DD sein"))
    if w["aufgeloest_am"] is not None and not _ist_datum(w["aufgeloest_am"]):
        f.append(Fehler(d, "aufgeloest_am", "muss ein Datum YYYY-MM-DD oder null sein"))
    if not _ist_url(w["quelle"]):
        f.append(Fehler(d, "quelle", "muss eine http(s)-URL sein"))
    if w["beleg_ausgang"] is not None and not _ist_url(w["beleg_ausgang"]):
        f.append(Fehler(d, "beleg_ausgang", "muss eine http(s)-URL oder null sein"))
    f.extend(_prognosen_pruefen(d, typ, w["prognosen"]))
    if typ == "punkt" and not w.get("einheit"):
        f.append(Fehler(d, "einheit", "bei typ punkt Pflicht (z. B. 'Mio EUR')"))
    f.extend(_ausgang_pruefen(d, w))
    if (_ist_datum(w["aufgeloest_am"]) and _ist_datum(w["pruefung_am"])
            and w["aufgeloest_am"] < w["pruefung_am"]):
        f.append(Fehler(d, "aufgeloest_am", "liegt vor pruefung_am (FORMAT.md §2.5)"))
    if not isinstance(w["vermerke"], list):
        f.append(Fehler(d, "vermerke", "muss eine Liste sein"))
    return f


def _meta_pruefen(meta: dict) -> list[Fehler]:
    f = [Fehler("BUCH.md", k, "Pflichtfeld fehlt") for k in META_PFLICHT if k not in meta]
    if "format" in meta and meta["format"] != "v1":
        f.append(Fehler("BUCH.md", "format", f"dieser Generator kennt nur v1, Buch sagt {meta['format']!r}"))
    return f


def buch_pruefen(buch: dict) -> list[Fehler]:
    fehler = _meta_pruefen(buch["meta"])
    gesehen: dict[str, str] = {}
    for w in buch["wetten"]:
        fehler.extend(_wette_pruefen(w))
        wid = str(w.get("id"))
        if wid in gesehen:
            fehler.append(Fehler(w.get("_datei", "?"), "id", f"doppelt, auch in {gesehen[wid]}"))
        else:
            gesehen[wid] = w.get("_datei", "?")
    return fehler
```

- [ ] **Step 4: Tests laufen lassen, müssen bestehen**

Run: `python -m pytest generator/tests/test_pruefen.py -v`
Expected: 15 passed.

- [ ] **Step 5: Commit**

```bash
git add generator/
git commit -m "feat: pruefen — regeln aus FORMAT.md, beleg-pflicht"
```

---

### Task 4: Bewerten (FORMAT.md §3)

**Files:**
- Create: `generator/wettbuch/bewerten.py`
- Create: `generator/tests/test_bewerten.py`

**Interfaces:**
- Consumes: geprüfte Dicts aus `lesen.buch_lesen`.
- Produces:
  - `bewerten.RANG_AB = 10`
  - `bewerten.brier(wert: float, ausgang: int) -> float`
  - `bewerten.abstand(wert: float, ausgang: float) -> float`
  - `bewerten.wette_bewerten(w: dict) -> dict` — `{"status": "offen"|"aufgeloest"|"verfallen"|"strittig", "scores": {von: float|None}, "naeher_dran": str|None}`; bei `punkt` ist `naeher_dran` der `von` mit kleinstem Abstand (Gleichstand: alphabetisch erster).
  - `bewerten.buch_bewerten(buch: dict) -> dict` — `{"wetten": [w + {"_bewertung": ...}], "tabelle": list[Zeile], "rang_ab": 10}`. `Zeile`: `{"von": str, "ist_institution": bool, "ja_nein_n": int, "ja_nein_schnitt": float|None, "rang": int|None, "punkt_gewonnen": int, "punkt_n": int, "rechenschaft_verfallen": int, "wetten_gesamt": int}`. Sortierung: erst alle mit Rang (aufsteigend nach Schnitt, dann Name), dann ohne Rang (nach `ja_nein_n` absteigend, dann Name).

- [ ] **Step 1: Failing Tests schreiben**

```python
# generator/tests/test_bewerten.py
from datetime import date

import pytest
from wettbuch import bewerten


def _wette(id_="w1", typ="ja_nein", ausgang=None, prognosen=None, institution="Stadt Test", einheit=None):
    w = {
        "id": id_, "institution": institution, "typ": typ, "ausgang": ausgang,
        "prognosen": prognosen or [
            {"von": "Stadt Test", "wert": 1.0, "art": "angekuendigt", "hinterlegt_am": date(2025, 1, 1)},
            {"von": "Computer", "wert": 0.35, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
        ],
        "_datei": f"{id_}.md",
    }
    if einheit:
        w["einheit"] = einheit
    return w


def _punkt(id_="p"):
    return _wette(id_=id_, typ="punkt", ausgang=610.0, einheit="Mio EUR", prognosen=[
        {"von": "Stadt Test", "wert": 594.8, "art": "angekuendigt", "hinterlegt_am": date(2025, 1, 1)},
        {"von": "Computer", "wert": 625, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
    ])


def test_brier():
    assert bewerten.brier(1.0, 1) == 0.0
    assert bewerten.brier(1.0, 0) == 1.0
    assert bewerten.brier(0.5, 1) == pytest.approx(0.25)
    assert bewerten.brier(0.35, 0) == pytest.approx(0.1225)


def test_abstand():
    assert bewerten.abstand(594.8, 610.0) == pytest.approx(15.2)
    assert bewerten.abstand(625, 610.0) == pytest.approx(15.0)


def test_wette_offen():
    b = bewerten.wette_bewerten(_wette())
    assert b["status"] == "offen"
    assert b["scores"] == {"Stadt Test": None, "Computer": None}
    assert b["naeher_dran"] is None


def test_wette_ja_nein_aufgeloest_nein():
    b = bewerten.wette_bewerten(_wette(ausgang=0))
    assert b["status"] == "aufgeloest"
    assert b["scores"]["Stadt Test"] == 1.0
    assert b["scores"]["Computer"] == pytest.approx(0.1225)


def test_wette_verfallen():
    b = bewerten.wette_bewerten(_wette(ausgang="verfallen"))
    assert b["status"] == "verfallen"
    assert b["scores"] == {"Stadt Test": None, "Computer": None}


def test_wette_punkt_naeher_dran():
    b = bewerten.wette_bewerten(_punkt())
    assert b["naeher_dran"] == "Computer"
    assert b["scores"]["Stadt Test"] == pytest.approx(15.2)


def test_tabelle_rang_erst_ab_10():
    wetten = [_wette(id_=f"w{i}", ausgang=0) for i in range(9)]
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    assert computer["ja_nein_n"] == 9
    assert computer["ja_nein_schnitt"] == pytest.approx(0.1225)
    assert computer["rang"] is None

    wetten.append(_wette(id_="w9", ausgang=0))
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    assert computer["rang"] == 1
    assert stadt["rang"] == 2
    assert stadt["ist_institution"] is True
    assert computer["ist_institution"] is False
    assert [z["von"] for z in t] == ["Computer", "Stadt Test"]


def test_tabelle_rechenschaft_zaehlt_verfallene_der_institution():
    wetten = [_wette(id_="a", ausgang="verfallen"), _wette(id_="b", ausgang="strittig"), _wette(id_="c")]
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    computer = next(z for z in t if z["von"] == "Computer")
    assert stadt["rechenschaft_verfallen"] == 2
    assert stadt["wetten_gesamt"] == 3
    assert computer["rechenschaft_verfallen"] == 0
    assert computer["wetten_gesamt"] == 0


def test_tabelle_punkt_gewonnen():
    t = bewerten.buch_bewerten({"meta": {}, "wetten": [_punkt()]})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    assert (computer["punkt_gewonnen"], computer["punkt_n"]) == (1, 1)
    assert (stadt["punkt_gewonnen"], stadt["punkt_n"]) == (0, 1)


def test_buch_bewerten_haengt_bewertung_an_wetten():
    r = bewerten.buch_bewerten({"meta": {}, "wetten": [_wette(ausgang=1)]})
    assert r["wetten"][0]["_bewertung"]["status"] == "aufgeloest"
    assert r["rang_ab"] == 10
```

- [ ] **Step 2: Tests laufen lassen, müssen fehlschlagen**

Run: `python -m pytest generator/tests/test_bewerten.py -v`
Expected: alle FAIL mit `ImportError: cannot import name 'bewerten'`.

- [ ] **Step 3: bewerten.py implementieren**

```python
# generator/wettbuch/bewerten.py
"""Mathematik aus FORMAT.md §3. Reine Funktionen über Dicts."""
from __future__ import annotations

RANG_AB = 10
NICHT_AUFGELOEST = {"verfallen", "strittig"}


def brier(wert: float, ausgang: int) -> float:
    return (wert - ausgang) ** 2


def abstand(wert: float, ausgang: float) -> float:
    return abs(wert - ausgang)


def _status(w: dict) -> str:
    a = w.get("ausgang")
    if a is None:
        return "offen"
    if a in NICHT_AUFGELOEST:
        return a
    return "aufgeloest"


def wette_bewerten(w: dict) -> dict:
    status = _status(w)
    scores: dict[str, float | None] = {p["von"]: None for p in w["prognosen"]}
    naeher: str | None = None
    if status == "aufgeloest":
        if w["typ"] == "ja_nein":
            for p in w["prognosen"]:
                scores[p["von"]] = brier(float(p["wert"]), int(w["ausgang"]))
        else:
            for p in w["prognosen"]:
                scores[p["von"]] = abstand(float(p["wert"]), float(w["ausgang"]))
            if len(w["prognosen"]) >= 2:
                naeher = min(sorted(scores), key=lambda k: scores[k])
    return {"status": status, "scores": scores, "naeher_dran": naeher}


def _neue_zeile(von: str) -> dict:
    return {
        "von": von, "ist_institution": False, "ja_nein_n": 0, "_ja_nein_summe": 0.0,
        "ja_nein_schnitt": None, "rang": None, "punkt_gewonnen": 0, "punkt_n": 0,
        "rechenschaft_verfallen": 0, "wetten_gesamt": 0,
    }


def buch_bewerten(buch: dict) -> dict:
    wetten: list[dict] = []
    zeilen: dict[str, dict] = {}

    for roh in buch["wetten"]:
        b = wette_bewerten(roh)
        w = {**roh, "_bewertung": b}
        wetten.append(w)

        inst = zeilen.setdefault(w["institution"], _neue_zeile(w["institution"]))
        inst["ist_institution"] = True
        inst["wetten_gesamt"] += 1
        if b["status"] in NICHT_AUFGELOEST:
            inst["rechenschaft_verfallen"] += 1

        for p in w["prognosen"]:
            z = zeilen.setdefault(p["von"], _neue_zeile(p["von"]))
            s = b["scores"][p["von"]]
            if b["status"] != "aufgeloest" or s is None:
                continue
            if w["typ"] == "ja_nein":
                z["ja_nein_n"] += 1
                z["_ja_nein_summe"] += s
            elif b["naeher_dran"] is not None:
                z["punkt_n"] += 1
                if b["naeher_dran"] == p["von"]:
                    z["punkt_gewonnen"] += 1

    for z in zeilen.values():
        if z["ja_nein_n"]:
            z["ja_nein_schnitt"] = z["_ja_nein_summe"] / z["ja_nein_n"]
        del z["_ja_nein_summe"]

    mit_rang = sorted(
        (z for z in zeilen.values() if z["ja_nein_n"] >= RANG_AB),
        key=lambda z: (z["ja_nein_schnitt"], z["von"]),
    )
    for i, z in enumerate(mit_rang, start=1):
        z["rang"] = i
    ohne_rang = sorted(
        (z for z in zeilen.values() if z["ja_nein_n"] < RANG_AB),
        key=lambda z: (-z["ja_nein_n"], z["von"]),
    )
    return {"wetten": wetten, "tabelle": mit_rang + ohne_rang, "rang_ab": RANG_AB}
```

- [ ] **Step 4: Tests laufen lassen, müssen bestehen**

Run: `python -m pytest generator/tests/test_bewerten.py -v`
Expected: 10 passed.

- [ ] **Step 5: Commit**

```bash
git add generator/
git commit -m "feat: bewerten — brier, abstand, tabelle mit rang ab 10 und rechenschaft"
```

---

### Task 5: Seiten (HTML + JSON)

**Files:**
- Create: `generator/wettbuch/seiten.py`
- Create: `generator/wettbuch/stil.css`
- Create: `generator/tests/test_seiten.py`

**Interfaces:**
- Consumes: `buch["meta"]`, Ergebnis von `bewerten.buch_bewerten`.
- Produces: `seiten.seiten_schreiben(meta: dict, bewertet: dict, ausgabe: Path, build_zeit: str) -> list[Path]` — schreibt `index.html`, `stil.css`, `wettbuch.json`, `institution/<slug>.html` je Institution, `wette/<id>.html` je Wette; gibt die geschriebenen Pfade zurück. Hilfsfunktionen: `seiten.slug(text: str) -> str`, `seiten.datum(d) -> str` (`TT.MM.JJJJ` oder `–`), `seiten.zahl(x, stellen=2) -> str` (deutsches Komma, `–` bei None).
- Markdown-Body wird mit `markdown.markdown(text)` gerendert. Kein JavaScript. CSS mit `prefers-color-scheme: dark`.

- [ ] **Step 1: Failing Tests schreiben**

```python
# generator/tests/test_seiten.py
import json
from datetime import date
from pathlib import Path

from wettbuch import bewerten, lesen, seiten


def _gebaut(buch: Path, tmp_path: Path, build_zeit: str = "2026-08-28 03:00") -> Path:
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    aus = tmp_path / "site"
    seiten.seiten_schreiben(b["meta"], bew, aus, build_zeit=build_zeit)
    return aus


def test_slug_und_datum_und_zahl():
    assert seiten.slug("Stadt Köln") == "stadt-koeln"
    assert seiten.datum(date(2026, 8, 28)) == "28.08.2026"
    assert seiten.datum(None) == "–"
    assert seiten.zahl(0.1225) == "0,12"
    assert seiten.zahl(None) == "–"


def test_seiten_schreiben_erzeugt_alle_dateien(buch: Path, tmp_path: Path):
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    aus = tmp_path / "site"
    pfade = seiten.seiten_schreiben(b["meta"], bew, aus, build_zeit="x")
    namen = {p.relative_to(aus).as_posix() for p in pfade}
    assert {"index.html", "stil.css", "wettbuch.json",
            "institution/stadt-test.html", "wette/test-2025-001.html"} <= namen


def test_index_enthaelt_rangliste_und_footer(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "index.html").read_text(encoding="utf-8")
    assert "Test gegen Test" in html
    assert "noch kein Rang" in html
    assert "Rechenschaft" in html
    assert "2026-08-28 03:00" in html
    assert "<script" not in html


def test_wettenseite_zeigt_zitat_und_markdown(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "Das Haus wird Ende Oktober fertig." in html
    assert "<h2>Kontext</h2>" in html
    assert "https://example.org/pm/1" in html


def test_json_ist_maschinenlesbar(buch: Path, tmp_path: Path):
    daten = json.loads((_gebaut(buch, tmp_path) / "wettbuch.json").read_text(encoding="utf-8"))
    assert daten["format"] == "v1"
    assert daten["wetten"][0]["id"] == "test-2025-001"
    assert daten["wetten"][0]["gesagt_am"] == "2025-10-01"
    assert "_text" not in daten["wetten"][0]
    assert daten["wetten"][0]["_bewertung"]["status"] == "offen"
    assert daten["tabelle"][0]["von"] in ("Computer", "Stadt Test")
```

- [ ] **Step 2: Tests laufen lassen, müssen fehlschlagen**

Run: `python -m pytest generator/tests/test_seiten.py -v`
Expected: alle FAIL mit `ImportError: cannot import name 'seiten'`.

- [ ] **Step 3: stil.css schreiben**

```css
/* generator/wettbuch/stil.css */
:root { --bg:#fbfaf7; --fg:#1b1b1b; --mute:#6b6b6b; --line:#d9d5cc; --ok:#2a7a3b; --bad:#a83232; --acc:#2b4a7a; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#151515; --fg:#e8e6e1; --mute:#9a9a9a; --line:#333; --ok:#6fcf80; --bad:#e07b7b; --acc:#8fb3e8; }
}
body { margin:0 auto; padding:2rem 1rem; max-width:64rem; background:var(--bg); color:var(--fg);
  font:16px/1.5 Georgia, "Times New Roman", serif; }
h1,h2,h3 { line-height:1.2; }
a { color:var(--acc); }
table { border-collapse:collapse; width:100%; margin:1rem 0; font-size:.95rem; }
th,td { text-align:left; padding:.4rem .6rem; border-bottom:1px solid var(--line); vertical-align:top; }
th { color:var(--mute); font-weight:normal; }
.zahl { text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }
.mute { color:var(--mute); }
.ja { color:var(--ok); } .nein { color:var(--bad); }
.status { font-size:.85rem; padding:.1rem .4rem; border:1px solid var(--line); border-radius:.3rem; }
blockquote { margin:1rem 0; padding:.5rem 1rem; border-left:3px solid var(--line); }
.tabelle-wrap { overflow-x:auto; }
footer { margin-top:3rem; color:var(--mute); font-size:.85rem; border-top:1px solid var(--line); padding-top:1rem; }
```

- [ ] **Step 4: seiten.py implementieren**

```python
# generator/wettbuch/seiten.py
"""HTML und JSON erzeugen. Rechnet nichts, bekommt fertige Daten."""
from __future__ import annotations

import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

import markdown

STIL = Path(__file__).with_name("stil.css")
UMLAUTE = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"})


def slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", text.translate(UMLAUTE)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "x"


def datum(d) -> str:
    return d.strftime("%d.%m.%Y") if isinstance(d, date) else "–"


def zahl(x, stellen: int = 2) -> str:
    return "–" if x is None else f"{x:.{stellen}f}".replace(".", ",")


def _e(x) -> str:
    return html.escape(str(x), quote=True)


def _seite(titel: str, koerper: str, tiefe: int, build_zeit: str, buch_titel: str) -> str:
    wurzel = "../" * tiefe
    return (
        '<!doctype html>\n<html lang="de"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{_e(titel)} · {_e(buch_titel)}</title>\n"
        f'<link rel="stylesheet" href="{wurzel}stil.css"></head>\n<body>\n'
        f'<p class="mute"><a href="{wurzel}index.html">{_e(buch_titel)}</a></p>\n'
        f"{koerper}\n"
        f'<footer>Wettbuch-Format v1 · gebaut {_e(build_zeit)} · <a href="{wurzel}wettbuch.json">wettbuch.json</a></footer>\n'
        "</body></html>\n"
    )


def _status_text(w: dict) -> str:
    s = w["_bewertung"]["status"]
    if s != "aufgeloest":
        return f'<span class="status">{_e(s)}</span>'
    if w["typ"] == "ja_nein":
        return '<span class="status ja">ja</span>' if w["ausgang"] == 1 else '<span class="status nein">nein</span>'
    return f'<span class="status">{zahl(w["ausgang"])} {_e(w.get("einheit", ""))}</span>'


def _tabelle_html(tabelle: list[dict], rang_ab: int) -> str:
    z = ['<div class="tabelle-wrap"><table><thead><tr>',
         "<th>Rang</th><th>Wer</th><th class=zahl>Trefferquote (Brier)</th><th class=zahl>Ja/Nein aufgelöst</th>",
         "<th class=zahl>Näher dran</th><th class=zahl>Rechenschaft (verfallen/strittig)</th><th class=zahl>Wetten</th>",
         "</tr></thead><tbody>"]
    for r in tabelle:
        rang = str(r["rang"]) if r["rang"] else f'<span class="mute">noch kein Rang (ab {rang_ab})</span>'
        wer = _e(r["von"])
        if r["ist_institution"]:
            wer = f'<a href="institution/{slug(r["von"])}.html">{wer}</a>'
        z.append(f"<tr><td>{rang}</td><td>{wer}</td><td class=zahl>{zahl(r['ja_nein_schnitt'])}</td>"
                 f"<td class=zahl>{r['ja_nein_n']}</td><td class=zahl>{r['punkt_gewonnen']} von {r['punkt_n']}</td>"
                 f"<td class=zahl>{r['rechenschaft_verfallen']}</td><td class=zahl>{r['wetten_gesamt']}</td></tr>")
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wettenliste_html(wetten: list[dict], tiefe: int) -> str:
    p = "../" * tiefe
    z = ['<div class="tabelle-wrap"><table><thead><tr><th>Wette</th><th>Institution</th>'
         '<th>gesagt am</th><th>Prüfung ab</th><th>Ausgang</th></tr></thead><tbody>']
    for w in wetten:
        z.append(f'<tr><td><a href="{p}wette/{_e(w["id"])}.html">{_e(w["frage"])}</a></td>'
                 f'<td><a href="{p}institution/{slug(w["institution"])}.html">{_e(w["institution"])}</a></td>'
                 f'<td>{datum(w["gesagt_am"])}</td><td>{datum(w["pruefung_am"])}</td><td>{_status_text(w)}</td></tr>')
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wette_html(w: dict) -> str:
    b = w["_bewertung"]
    z = [f"<h1>{_e(w['frage'])}</h1>",
         f'<p><strong>{_e(w["institution"])}</strong> · {_e(w["gesagt_von"])} · gesagt am {datum(w["gesagt_am"])} · '
         f'<a href="{_e(w["quelle"])}">Quelle</a></p>',
         f"<blockquote>{_e(w['zitat'])}</blockquote>",
         f"<p>Typ: {_e(w['typ'])} · Prüfung ab {datum(w['pruefung_am'])} · Status: {_status_text(w)}</p>",
         "<table><thead><tr><th>Wer</th><th class=zahl>Prognose</th><th>Art</th><th>hinterlegt am</th>"
         "<th class=zahl>Score</th></tr></thead><tbody>"]
    for p in w["prognosen"]:
        s = b["scores"].get(p["von"])
        z.append(f"<tr><td>{_e(p['von'])}</td><td class=zahl>{zahl(p['wert'])}</td><td>{_e(p['art'])}</td>"
                 f"<td>{datum(p['hinterlegt_am'])}</td><td class=zahl>{zahl(s)}</td></tr>")
    z.append("</tbody></table>")
    if b["status"] == "aufgeloest":
        naeher = f' · näher dran: <strong>{_e(b["naeher_dran"])}</strong>' if b["naeher_dran"] else ""
        z.append(f'<p>Aufgelöst am {datum(w["aufgeloest_am"])} · <a href="{_e(w["beleg_ausgang"])}">Beleg</a>{naeher}</p>')
    if w.get("vermerke"):
        z.append("<h2>Vermerke</h2><ul>")
        for v in w["vermerke"]:
            z.append(f"<li>{datum(v.get('am'))}: {_e(v.get('text', ''))}</li>")
        z.append("</ul>")
    z.append(markdown.markdown(w.get("_text", "")))
    return "\n".join(z)


def _json_faehig(x):
    if isinstance(x, date):
        return x.isoformat()
    if isinstance(x, dict):
        return {k: _json_faehig(v) for k, v in x.items() if not k.startswith("_") or k == "_bewertung"}
    if isinstance(x, list):
        return [_json_faehig(v) for v in x]
    return x


def seiten_schreiben(meta: dict, bewertet: dict, ausgabe: Path, build_zeit: str) -> list[Path]:
    ausgabe.mkdir(parents=True, exist_ok=True)
    (ausgabe / "institution").mkdir(exist_ok=True)
    (ausgabe / "wette").mkdir(exist_ok=True)
    titel = str(meta.get("titel", "Wettbuch"))
    geschrieben: list[Path] = []

    def schreib(rel: str, inhalt: str) -> None:
        p = ausgabe / rel
        p.write_text(inhalt, encoding="utf-8")
        geschrieben.append(p)

    schreib("stil.css", STIL.read_text(encoding="utf-8"))

    koerper = [f"<h1>{_e(titel)}</h1>",
               f'<p class="mute">Halter: {_e(meta.get("halter", ""))} · seit {datum(meta.get("seit"))} · Format {_e(meta.get("format", ""))}</p>',
               markdown.markdown(meta.get("_text", "")),
               "<h2>Rangliste</h2>", _tabelle_html(bewertet["tabelle"], bewertet["rang_ab"]),
               "<h2>Alle Wetten</h2>", _wettenliste_html(bewertet["wetten"], 0)]
    schreib("index.html", _seite("Rangliste", "\n".join(koerper), 0, build_zeit, titel))

    nach_inst: dict[str, list[dict]] = {}
    for w in bewertet["wetten"]:
        nach_inst.setdefault(w["institution"], []).append(w)
    for inst, ws in nach_inst.items():
        koerper = [f"<h1>{_e(inst)}</h1>", _wettenliste_html(ws, 1)]
        schreib(f"institution/{slug(inst)}.html", _seite(inst, "\n".join(koerper), 1, build_zeit, titel))

    for w in bewertet["wetten"]:
        schreib(f"wette/{w['id']}.html", _seite(w["frage"], _wette_html(w), 1, build_zeit, titel))

    daten = {"format": "v1", "titel": titel, "halter": meta.get("halter"), "gebaut": build_zeit,
             "tabelle": bewertet["tabelle"], "wetten": _json_faehig(bewertet["wetten"])}
    schreib("wettbuch.json", json.dumps(daten, ensure_ascii=False, indent=2))
    return geschrieben
```

- [ ] **Step 5: Tests laufen lassen, müssen bestehen**

Run: `python -m pytest generator/tests/test_seiten.py -v`
Expected: 5 passed. Falls `stil.css` nicht gefunden wird: `python -m pip install -e ".[test]"` erneut (package-data).

- [ ] **Step 6: Commit**

```bash
git add generator/
git commit -m "feat: seiten — index mit rangliste, institution, wette, json, css"
```

---

### Task 6: CLI und End-to-End

**Files:**
- Create: `generator/wettbuch/cli.py`
- Create: `generator/wettbuch/__main__.py`
- Create: `generator/tests/test_cli.py`

**Interfaces:**
- Consumes: alle vier Module.
- Produces: `cli.main(argv: list[str] | None = None) -> int`. Aufruf `python -m wettbuch bauen <buch-ordner> <ausgabe-ordner>`; optional `--pruefen` (nur prüfen, nichts schreiben). Exit 0 bei Erfolg, 1 bei Fehlern (jeder Fehler eine Zeile `DATEI: FELD — TEXT` auf stderr), 2 bei Bedienfehler. `build_zeit` = aktuelle Zeit `YYYY-MM-DD HH:MM` (der einzige „heute"-Wert, §5.5).

- [ ] **Step 1: Failing Tests schreiben**

```python
# generator/tests/test_cli.py
from pathlib import Path
import subprocess
import sys

from wettbuch import cli


def test_bauen_erzeugt_seite(buch: Path, tmp_path: Path, capsys):
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 0
    assert (aus / "index.html").exists()
    assert "1 Wette" in capsys.readouterr().out


def test_bauen_bricht_bei_fehler_ab(buch: Path, tmp_path: Path, capsys):
    p = buch / "wetten" / "test-2025-001.md"
    p.write_text(p.read_text(encoding="utf-8").replace("ausgang: null", "ausgang: 1"), encoding="utf-8")
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 1
    assert not aus.exists()
    err = capsys.readouterr().err
    assert "test-2025-001.md: beleg_ausgang" in err


def test_nur_pruefen(buch: Path, tmp_path: Path):
    rc = cli.main(["bauen", str(buch), str(tmp_path / "site"), "--pruefen"])
    assert rc == 0
    assert not (tmp_path / "site").exists()


def test_bedienfehler():
    assert cli.main([]) == 2


def test_python_m_wettbuch_laeuft(buch: Path, tmp_path: Path):
    r = subprocess.run([sys.executable, "-m", "wettbuch", "bauen", str(buch), str(tmp_path / "s")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
```

- [ ] **Step 2: Tests laufen lassen, müssen fehlschlagen**

Run: `python -m pytest generator/tests/test_cli.py -v`
Expected: alle FAIL mit `ImportError: cannot import name 'cli'`.

- [ ] **Step 3: cli.py und __main__.py implementieren**

```python
# generator/wettbuch/cli.py
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
        print(f"{e.datei}: {e.text}", file=sys.stderr)
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
    pfade = seiten.seiten_schreiben(buch["meta"], bewertet, ausgabe, build_zeit)
    print(f"OK: {n} Wette{plural}, {len(pfade)} Dateien nach {ausgabe}")
    return 0
```

```python
# generator/wettbuch/__main__.py
import sys

from .cli import main

sys.exit(main())
```

- [ ] **Step 4: Alle Tests laufen lassen**

Run: `python -m pytest -v`
Expected: 40 passed (5 lesen + 15 pruefen + 10 bewerten + 5 seiten + 5 cli).

- [ ] **Step 5: Commit**

```bash
git add generator/
git commit -m "feat: cli — python -m wettbuch bauen, abbruch bei fehlern"
```

---

### Task 7: Erstes Buch — „Köln gegen Köln", fünf Einträge

**Files:**
- Create: `.gitignore`
- Create: `buecher/koeln/BUCH.md`
- Create: `buecher/koeln/wetten/koeln-2025-001.md` … `koeln-2025-005.md`

**Interfaces:**
- Consumes: FORMAT.md §1, Recherche `koeln/RECHERCHE.md` (Nr. 11, 12, 13, 8).
- Produces: ein gültiges Buch, das `python -m wettbuch bauen buecher/koeln site` ohne Fehler baut.

Hinweis: Die Computer-Prognosen unten sind die des Autors (Claude, 28.08.2026) und werden **so übernommen** — nicht neu schätzen. Zitate stammen wörtlich aus `koeln/RECHERCHE.md`. Drei der fünf Ereignisse liegen in der Vergangenheit; die Wetten werden trotzdem **offen** angelegt — Auflösung ist eine eigene, belegte Handlung (§2.1), nicht Teil dieses Tasks. Der Ausführende schlägt den Ausgang **nicht** nach.

- [ ] **Step 1: .gitignore**

```
site/
__pycache__/
*.egg-info/
.pytest_cache/
```

- [ ] **Step 2: BUCH.md**

```markdown
---
titel: Köln gegen Köln
halter: Felix Lind
kontakt: https://belegbar.eu
seit: 2026-08-28
lizenz: CC0
format: v1
---

Die Stadt Köln sagt laufend, was sie erwartet: Defizite, Termine, Plätze. Dieses
Buch schreibt es auf, wartet, und schaut nach. Es zitiert nur, was die Stadt selbst
öffentlich gesagt hat. Ausgewählt werden Aussagen mit Zahl und Datum; Absichten
ohne beides bleiben draußen. Fehler melden: Kontakt oben.

Der „Computer" in diesem Buch ist ein Sprachmodell (Claude, Anthropic) mit Zugriff
auf öffentliche Quellen, keine Spezialsoftware. Es steht in derselben Liste wie die
Stadt, nach denselben Regeln.
```

- [ ] **Step 3: Fünf Wetten anlegen**

`buecher/koeln/wetten/koeln-2025-001.md`:
```markdown
---
id: koeln-2025-001
institution: Stadt Köln
gesagt_von: Stadtdirektorin Andrea Blome
gesagt_am: 2025-10-01
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27942/index.html
zitat: "Das Opernhaus wird Ende Oktober fertig, Ende November folgt dann das Schauspiel und bis Jahresende werden auch die Kinderoper sowie das Kleine Haus baulich abgeschlossen sein."
frage: Ist das Opernhaus am Offenbachplatz am 31.10.2025 baulich fertiggestellt?
typ: ja_nein
pruefung_am: 2025-11-01
prognosen:
  - von: Stadt Köln
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
  - von: Computer
    wert: 0.30
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-08-28
    text: "Computer-Prognose nach dem Ereignis hinterlegt, ohne Nachschlagen des Ausgangs; Basisraten-Schätzung für Bühnen-Termine, kein Wissen. Regel 2 formal verletzt, deshalb dieser Vermerk."
---

## Kontext
Pressemitteilung zur Bühnen-Sanierung vom 01.10.2025. Die Aussage nennt drei
Termine; dieses Buch führt sie als drei Wetten (001–003).

## Übersetzung
„wird Ende Oktober fertig" → Ja/Nein am 31.10.2025. „Baulich fertiggestellt" nach dem
Sprachgebrauch der Stadt selbst (Mitteilung vom 29.08.2024: „bauliche Fertigstellung",
nicht Spielbetrieb).

## Begründung Computer
Die Bühnen-Sanierung hat seit 2012 jeden angekündigten Termin gerissen. 30 % ist die
Wahrscheinlichkeit, dass ein Termin, der vier Wochen vorher bestätigt wird, diesmal
hält.
```

`buecher/koeln/wetten/koeln-2025-002.md`:
```markdown
---
id: koeln-2025-002
institution: Stadt Köln
gesagt_von: Stadtdirektorin Andrea Blome
gesagt_am: 2025-10-01
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27942/index.html
zitat: "Ende November folgt dann das Schauspiel"
frage: Ist das Schauspielhaus am Offenbachplatz am 30.11.2025 baulich fertiggestellt?
typ: ja_nein
pruefung_am: 2025-12-01
prognosen:
  - von: Stadt Köln
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
  - von: Computer
    wert: 0.30
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-08-28
    text: "Siehe Vermerk in koeln-2025-001."
---

## Kontext
Zweiter Termin aus derselben Mitteilung wie koeln-2025-001.

## Übersetzung
„Ende November" → 30.11.2025, baulich fertiggestellt.
```

`buecher/koeln/wetten/koeln-2025-003.md`:
```markdown
---
id: koeln-2025-003
institution: Stadt Köln
gesagt_von: Oberbürgermeisterin Henriette Reker
gesagt_am: 2025-10-01
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27942/index.html
zitat: "Spielbetrieb am Offenbachplatz im September 2026; Eröffnungsfest 19./20.09.2026, Festakt 24.09.2026"
frage: Findet der Festakt zur Wiedereröffnung der Bühnen am Offenbachplatz am 24.09.2026 statt?
typ: ja_nein
pruefung_am: 2026-09-25
prognosen:
  - von: Stadt Köln
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
  - von: Computer
    wert: 0.70
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Dritter Termin aus der Mitteilung vom 01.10.2025; einziger, der bei Anlage des Buchs
noch in der Zukunft liegt.

## Übersetzung
Festakt am genannten Tag → Ja/Nein. Ein verschobener Festakt ist Nein (§2.2).

## Begründung Computer
Vier Wochen vor dem Termin, Programm öffentlich: 70 %. Nicht höher, weil bei diesem
Bauwerk auch vier Wochen vorher schon Termine gefallen sind.
```

`buecher/koeln/wetten/koeln-2025-004.md`:
```markdown
---
id: koeln-2025-004
institution: Stadt Köln
gesagt_von: Amt für Brücken, Tunnel und Stadtbahnbau
gesagt_am: 2025-06-12
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27660/index.html
zitat: "Am 15. September 2025 sollen die KVB-Linien 13 und 18 auf der Brücke wieder in Betrieb genommen werden."
frage: Fahren die KVB-Linien 13 und 18 am 15.09.2025 wieder über die Mülheimer Brücke?
typ: ja_nein
pruefung_am: 2025-09-16
prognosen:
  - von: Stadt Köln
    wert: 0.80
    hinterlegt_am: 2025-06-12
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-08-28
    text: "Computer-Prognose nach dem Ereignis hinterlegt, ohne Nachschlagen des Ausgangs. Siehe koeln-2025-001."
---

## Kontext
Mitteilung zur Instandsetzung der Mülheimer Brücke, 12.06.2025.

## Übersetzung
„sollen … wieder in Betrieb genommen werden" trägt einen Vorbehalt → `voraussichtlich`,
0,80 (§1.2). Frage: Linienbetrieb am genannten Tag.

## Begründung Computer
Drei Monate Vorlauf, Bahnbetrieb hängt an Abnahmen Dritter (TAB, KVB). 55 %.
```

`buecher/koeln/wetten/koeln-2025-005.md`:
```markdown
---
id: koeln-2025-005
institution: Stadt Köln
gesagt_von: Oberbürgermeister Torsten Burmester / Kämmerin Prof. Dr. Dörte Diemert
gesagt_am: 2025-11-04
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28019/index.html
zitat: "Fehlbetrag 2025 rund 582 Millionen Euro"
frage: Wie hoch ist der Fehlbetrag der Stadt Köln im Haushaltsjahr 2025 laut festgestelltem Jahresabschluss (Mio EUR)?
typ: punkt
einheit: Mio EUR
toleranz: 0.10
pruefung_am: 2026-06-01
verfall_am: 2028-12-31
prognosen:
  - von: Stadt Köln
    wert: 582
    hinterlegt_am: 2025-11-04
    art: angekuendigt
  - von: Computer
    wert: 560
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Novemberprognose 2025 mit Haushaltssperre bis Jahresende. Ursprünglicher Plan
(14.11.2024): 395,1 Mio; genehmigt (31.03.2025): 399,34 Mio.

## Übersetzung
Punktschätzung in Mio EUR; Nebenfrage „innerhalb ±10 %" (524–640) wird bei Auflösung
im Vermerk beantwortet.

## Begründung Computer
Novemberprognosen mit Haushaltssperre fallen am Jahresende meist etwas besser aus
als angekündigt — Sperre wirkt, Einmaleffekte kommen. 560.
```

- [ ] **Step 4: Buch bauen, muss ohne Fehler laufen**

Run: `python -m wettbuch bauen buecher/koeln site`
Expected: `OK: 5 Wetten, 9 Dateien nach site` (index, stil, json, 1 Institution, 5 Wetten). `site/index.html` zeigt „Stadt Köln — noch kein Rang (ab 10)" und „Computer — noch kein Rang (ab 10)", Rechenschaft 0, fünf Wetten „offen".

- [ ] **Step 5: Commit**

```bash
git add .gitignore buecher/
git commit -m "feat: erstes buch koeln gegen koeln, fuenf eintraege"
```

---

### Task 8: GitHub Pages und README

**Files:**
- Create: `.github/workflows/pages.yml`
- Create: `README.md`

**Interfaces:**
- Consumes: `python -m wettbuch bauen buecher/koeln site`.
- Produces: bei jedem Push auf `main`/`master` eine gebaute Seite unter GitHub Pages.

Hinweis: Das Repo `~/wettbuch` hat kein Remote. Anlegen des öffentlichen GitHub-Repos ist eine Veröffentlichung und damit Felix' Handlung; dieser Task bereitet nur vor und testet lokal.

- [ ] **Step 1: Workflow schreiben**

```yaml
# .github/workflows/pages.yml
name: Wettbuch bauen und veröffentlichen
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
        with: { python-version: "3.12" }
      - run: python -m pip install -e ".[test]"
      - run: python -m pytest -q
      - run: python -m wettbuch bauen buecher/koeln site
      - uses: actions/upload-pages-artifact@v3
        with: { path: site }
  veroeffentlichen:
    needs: bauen
    runs-on: ubuntu-latest
    environment: { name: github-pages }
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: README.md**

```markdown
# Wettbuch

Ein offenes Format, um Institutionen an ihren eigenen Prognosen zu messen.

- **Format:** [FORMAT.md](FORMAT.md) — wer diese Regeln einhält, führt ein Wettbuch.
- **Generator:** `python -m wettbuch bauen <buch> <ausgabe>` — macht aus einem Ordner
  eine statische Seite mit Rangliste. Nur `pyyaml` und `markdown`.
- **Erstes Buch:** [buecher/koeln](buecher/koeln) — „Köln gegen Köln".

## Selbst ein Buch führen

1. Ordner anlegen, `BUCH.md` nach FORMAT.md §4.
2. Eine Datei pro Wette nach FORMAT.md §1 in einen Unterordner `wetten/`.
3. `python -m pip install -e .` und `python -m wettbuch bauen <ordner> site`.
4. `site/` irgendwo hinlegen. Fertig. Niemanden fragen.

Halter-Disziplin, die kein Programm prüfen kann: Einträge nach dem Commit nicht mehr
ändern (FORMAT.md §1.3.3), Teilerfüllung als Nein auflösen (§2.2), zurückgezogene
Aussagen als neue Wette führen (§1.3.5). Git zeigt, ob man sich daran hält.

## Entwickeln

    python -m pip install -e ".[test]"
    python -m pytest

Lizenz: Code MIT, Bücher CC0.
```

- [ ] **Step 3: Lokal alles einmal durchlaufen lassen**

Run: `python -m pytest -q && python -m wettbuch bauen buecher/koeln site && ls site`
Expected: `40 passed`, `OK: 5 Wetten, 9 Dateien nach site`, Verzeichnis mit `index.html`, `stil.css`, `wettbuch.json`, `institution/`, `wette/`.

- [ ] **Step 4: Commit**

```bash
git add .github/ README.md
git commit -m "ci: github pages workflow, readme"
```

- [ ] **Step 5: Felix entscheidet über das Remote**

Kein Befehl. Felix legt das öffentliche Repo an (Vorschlag `wettbuch`) und pusht; danach in den Repo-Settings Pages → Source „GitHub Actions". Das ist die Veröffentlichung, die Wette 6 auflöst — sie gehört ihm.

---

## Self-Review

**Spec coverage (FORMAT.md):**
- §0/§4 Buch, BUCH.md, Halter → Task 2 (lesen), Task 3 Regel 12, Task 7.
- §1.1 Pflichtfelder, Typen, Datumsformat, URLs → Task 3 Regeln 1–4, 8.
- §1.2 Prognosen, feste Werte 1,00/0,80 → Task 3 Regeln 5–6.
- §1.3: Regel 1 (Quelle) → Task 3 Regel 4. Regeln 2, 3, 4, 5 sind Halter-Disziplin, nicht maschinell prüfbar → README nennt sie ausdrücklich; Git-Historie ist der Nachweis.
- §2.1 Beleg-Pflicht → Task 3 Regel 9, Task 6 Abbruch mit Exit 1. §2.2 Teilerfüllung → Halter-Regel, README. §2.3 Verfall → Task 4 Status `verfallen`; `verfall_am` wird gelesen, aber v1 setzt Verfall nicht automatisch (§6: keine automatische Auflösung). §2.4 strittig → Task 3/4. §2.5 → Task 3 Regel 10.
- §3.1–3.4 → Task 4 vollständig. `toleranz`-Nebenfrage: v1 rechnet sie nicht automatisch; Task 7 Übersetzung sagt, dass sie bei Auflösung im Vermerk beantwortet wird. Bewusste Lücke, in FORMAT.md §3.2 als „kann" formuliert.
- §5.1–5.5 Generator → Task 5 (Ausgabe), Task 6 (Validierung, Abbruch, einziges „heute" = build_zeit). Reproduzierbar ✓.
- §6 nichts davon gebaut ✓.

**Placeholder scan:** Keine TBD/TODO/„similar to". Jeder Code-Schritt hat vollständigen Code.

**Type consistency:** `lesen.buch_lesen` → `{"meta","wetten","ordner"}` in Task 2, 3, 5, 6 gleich. `pruefen.Fehler(datei, feld, text)` in Task 3 und 6 gleich. `bewerten.buch_bewerten` → `{"wetten","tabelle","rang_ab"}` in Task 4 und 5 gleich; Zeilen-Schlüssel in Task 4 Tests und Task 5 `_tabelle_html` gleich. `seiten.seiten_schreiben(meta, bewertet, ausgabe, build_zeit)` in Task 5 und 6 gleich. Testzahl: 5 + 15 + 10 + 5 + 5 = 40, in Task 6 und 8 gleich. Dateizahl Task 7/8: 3 + 1 + 5 = 9 ✓.
