"""Tests für den Unterbefehl `alle` (mehrere Bücher aus einem Ordner bauen)."""
from pathlib import Path
import json

import pytest

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
    assert "Wettbuch" in uebersicht
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
