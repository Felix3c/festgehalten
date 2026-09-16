"""Tests für den Unterbefehl `alle` (mehrere Bücher aus einem Ordner bauen)."""
from pathlib import Path
import json

import pytest

from conftest import BUCH_OK
from wettbuch import cli

# Muster wie im buch-Fixture aus conftest.py, für zwei unterschiedliche Bücher.

BUCH_A = """---
titel: Erstes Buch
halter: Halter A
kontakt: https://example.org/a
seit: 2026-01-01
lizenz: CC0
format: v1
---

Buch A Text.
"""

WETTE_A_OFFEN = """---
id: a-2025-001
institution: Stadt A
gesagt_von: Sprecherin A
gesagt_am: 2025-10-01
quelle: https://example.org/a/1
zitat: "Erstes Zitat A."
frage: Erste Frage A?
typ: ja_nein
pruefung_am: 2025-11-01
prognosen:
  - von: Stadt A
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

Kontext A1.
"""

WETTE_A_AUFGELOEST = """---
id: a-2025-002
institution: Stadt A
gesagt_von: Sprecherin A
gesagt_am: 2025-09-01
quelle: https://example.org/a/2
zitat: "Zweites Zitat A."
frage: Zweite Frage A?
typ: ja_nein
pruefung_am: 2025-10-01
prognosen:
  - von: Stadt A
    wert: 1.00
    hinterlegt_am: 2025-09-01
    art: angekuendigt
ausgang: 1
aufgeloest_am: 2025-10-02
beleg_ausgang: https://example.org/a/beleg
vermerke: []
---

Kontext A2.
"""

BUCH_B = """---
titel: Zweites Buch
halter: Halter B
kontakt: https://example.org/b
seit: 2026-02-01
lizenz: CC0
format: v1
---

Buch B Text.
"""

WETTE_B_OFFEN = """---
id: b-2025-001
institution: Stadt B
gesagt_von: Sprecher B
gesagt_am: 2025-10-05
quelle: https://example.org/b/1
zitat: "Zitat B."
frage: Frage B?
typ: ja_nein
pruefung_am: 2025-11-05
prognosen:
  - von: Stadt B
    wert: 1.00
    hinterlegt_am: 2025-10-05
    art: angekuendigt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

Kontext B.
"""


def _buch_anlegen(ordner: Path, buch_md: str, wetten: dict[str, str]) -> None:
    ordner.mkdir(parents=True)
    (ordner / "BUCH.md").write_text(buch_md, encoding="utf-8")
    wetten_ordner = ordner / "wetten"
    wetten_ordner.mkdir()
    for name, inhalt in wetten.items():
        (wetten_ordner / f"{name}.md").write_text(inhalt, encoding="utf-8")


@pytest.fixture
def buecher_ordner(tmp_path: Path) -> Path:
    """Ein Ordner mit zwei gültigen Büchern: 'erstes' (2 Wetten, 1 offen/1 aufgelöst)
    und 'zweites' (1 Wette, offen)."""
    wurzel = tmp_path / "buecher"
    _buch_anlegen(wurzel / "erstes", BUCH_A, {"a-2025-001": WETTE_A_OFFEN, "a-2025-002": WETTE_A_AUFGELOEST})
    _buch_anlegen(wurzel / "zweites", BUCH_B, {"b-2025-001": WETTE_B_OFFEN})
    return wurzel


def test_alle_baut_mehrere_buecher_und_uebersicht(buecher_ordner: Path, tmp_path: Path):
    ausgabe = tmp_path / "site"
    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe)])
    assert rc == 0

    assert (ausgabe / "erstes" / "index.html").exists()
    assert (ausgabe / "zweites" / "index.html").exists()
    assert (ausgabe / "stil.css").exists()

    uebersicht = (ausgabe / "index.html").read_text(encoding="utf-8")
    assert "festgehalten" in uebersicht
    assert "Erstes Buch" in uebersicht
    assert "Zweites Buch" in uebersicht
    assert "erstes/index.html" in uebersicht
    assert "zweites/index.html" in uebersicht

    daten = json.loads((ausgabe / "alle.json").read_text(encoding="utf-8"))
    assert len(daten) == 2
    nach_ordner = {d["ordner"]: d for d in daten}
    assert nach_ordner["erstes"] == {
        "ordner": "erstes", "titel": "Erstes Buch", "wetten": 2, "aufgeloest": 1, "offen": 1,
    }
    assert nach_ordner["zweites"] == {
        "ordner": "zweites", "titel": "Zweites Buch", "wetten": 1, "aufgeloest": 0, "offen": 1,
    }


def test_alle_bricht_bei_fehler_in_einem_buch_komplett_ab(buecher_ordner: Path, tmp_path: Path, capsys):
    fehlerhaft = buecher_ordner / "erstes" / "wetten" / "a-2025-002.md"
    fehlerhaft.write_text(
        fehlerhaft.read_text(encoding="utf-8").replace(
            "beleg_ausgang: https://example.org/a/beleg", "beleg_ausgang: null"
        ),
        encoding="utf-8",
    )
    ausgabe = tmp_path / "site"
    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe)])
    assert rc == 1
    assert not ausgabe.exists()
    err = capsys.readouterr().err
    assert "a-2025-002.md" in err
    assert "beleg_ausgang" in err


def test_alle_ohne_unterbuecher_klare_meldung(tmp_path: Path, capsys):
    leer = tmp_path / "leer"
    leer.mkdir()
    ausgabe = tmp_path / "site"
    rc = cli.main(["alle", str(leer), str(ausgabe)])
    assert rc == 1
    assert not ausgabe.exists()
    err = capsys.readouterr().err
    assert str(leer) in err
    assert "BUCH.md" in err


def test_alle_baut_buch_ohne_eintraege(tmp_path: Path):
    buecher = tmp_path / "buecher"
    leer = buecher / "leer"
    (leer / "wetten").mkdir(parents=True)
    (leer / "BUCH.md").write_text(BUCH_OK, encoding="utf-8")
    ausgabe = tmp_path / "site"

    rc = cli.main(["alle", str(buecher), str(ausgabe)])

    assert rc == 0
    assert (ausgabe / "leer" / "index.html").exists()
    daten = json.loads((ausgabe / "alle.json").read_text(encoding="utf-8"))
    assert daten[0]["wetten"] == 0 and daten[0]["offen"] == 0


def test_alle_schreibt_buecher_json(buecher_ordner: Path, tmp_path: Path):
    ausgabe = tmp_path / "site"
    buch_md = buecher_ordner / "erstes" / "BUCH.md"
    buch_md.write_text(buch_md.read_text(encoding="utf-8").replace(
        "format: v1", "format: v1\ninstitution: Stadt Erstes\neinreichung: buch@example.org\nsammelbuch: true"),
        encoding="utf-8")

    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe), "--repo", "beispiel/repo"])
    assert rc == 0

    buecher = json.loads((ausgabe / "buecher.json").read_text(encoding="utf-8"))
    nach_ordner = {b["ordner"]: b for b in buecher}
    erstes = nach_ordner["erstes"]
    assert erstes["institution"] == "Stadt Erstes"
    assert erstes["einreichung"] == "buch@example.org"
    assert erstes["sammelbuch"] is True
    assert erstes["repo"] == "beispiel/repo"
    assert erstes["pfad"] == "buecher/erstes/wetten"
    assert isinstance(erstes["zweig"], str) and erstes["zweig"]
    zweites = nach_ordner["zweites"]
    assert zweites["institution"] is None
    assert zweites["sammelbuch"] is False


def test_alle_lehnt_zwei_sammelbuecher_ab(buecher_ordner: Path, tmp_path: Path, capsys):
    for name in ("erstes", "zweites"):
        p = buecher_ordner / name / "BUCH.md"
        p.write_text(p.read_text(encoding="utf-8").replace("format: v1", "format: v1\nsammelbuch: true"), encoding="utf-8")
    rc = cli.main(["alle", str(buecher_ordner), str(tmp_path / "site")])
    assert rc == 1
    assert "sammelbuch" in capsys.readouterr().err


def test_alle_lehnt_zwei_sammelbuecher_auch_bei_pruefen_ab(buecher_ordner: Path, tmp_path: Path, capsys):
    for name in ("erstes", "zweites"):
        p = buecher_ordner / name / "BUCH.md"
        p.write_text(p.read_text(encoding="utf-8").replace("format: v1", "format: v1\nsammelbuch: true"), encoding="utf-8")
    rc = cli.main(["alle", str(buecher_ordner), str(tmp_path / "site"), "--pruefen"])
    assert rc == 1
    assert "sammelbuch" in capsys.readouterr().err


IMPRESSUM = """---
titel: Impressum
reihe: 1
---

Felix Muster, Musterstraße 1.
"""

DATENSCHUTZ = """---
titel: Datenschutz
reihe: 2
---

Keine Cookies.
"""


@pytest.fixture
def seiten_ordner(tmp_path: Path) -> Path:
    ordner = tmp_path / "rechtliches"
    ordner.mkdir()
    (ordner / "impressum.md").write_text(IMPRESSUM, encoding="utf-8")
    (ordner / "datenschutz.md").write_text(DATENSCHUTZ, encoding="utf-8")
    return ordner


def test_alle_mit_seiten_baut_impressum_und_datenschutz(buecher_ordner: Path, seiten_ordner: Path, tmp_path: Path):
    ausgabe = tmp_path / "site"
    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe), "--seiten", str(seiten_ordner)])
    assert rc == 0
    impressum = (ausgabe / "impressum" / "index.html").read_text(encoding="utf-8")
    datenschutz = (ausgabe / "datenschutz" / "index.html").read_text(encoding="utf-8")
    assert "<h1>Impressum</h1>" in impressum and "Felix Muster" in impressum
    assert "<h1>Datenschutz</h1>" in datenschutz and "Keine Cookies." in datenschutz
    # Reihenfolge nach `reihe`, nicht alphabetisch; auf jeder Ebene korrekt relativ verlinkt
    fuss = '<a href="{p}impressum/">Impressum</a> · <a href="{p}datenschutz/">Datenschutz</a></footer>'
    assert fuss.format(p="") in (ausgabe / "index.html").read_text(encoding="utf-8")
    assert fuss.format(p="../") in impressum
    assert fuss.format(p="../") in (ausgabe / "erstes" / "index.html").read_text(encoding="utf-8")
    assert fuss.format(p="../../") in (ausgabe / "erstes" / "wette" / "a-2025-001.html").read_text(encoding="utf-8")
    assert fuss.format(p="../../") in (ausgabe / "erstes" / "institution" / "stadt-a.html").read_text(encoding="utf-8")


def test_alle_mit_seiten_lehnt_seite_ohne_titel_ab(buecher_ordner: Path, seiten_ordner: Path, tmp_path: Path, capsys):
    (seiten_ordner / "kaputt.md").write_text("---\nreihe: 3\n---\n\nText.\n", encoding="utf-8")
    rc = cli.main(["alle", str(buecher_ordner), str(tmp_path / "site"), "--seiten", str(seiten_ordner), "--pruefen"])
    assert rc == 1
    assert "rechtliches/kaputt.md: kopf — titel fehlt" in capsys.readouterr().err
