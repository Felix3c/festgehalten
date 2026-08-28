# generator/tests/test_ende_zu_ende.py
"""Regressionstests: ein gemischtes Buch quer durch alle Module, und Reproduzierbarkeit."""
from pathlib import Path

from wettbuch import bewerten, cli, lesen, seiten

BUCH_MD = """---
titel: Zwei Städte
halter: Testhalter
kontakt: https://example.org
seit: 2026-08-28
lizenz: CC0
format: v1
---

Worum es geht.
"""

WETTE_A_JA_NEIN_1 = """---
id: a-2025-001
institution: Stadt A
gesagt_von: Buergermeister A
gesagt_am: 2025-01-01
quelle: https://example.org/a/1
zitat: "Das Bad wird 2025 fertig."
frage: Ist das Bad am 31.12.2025 fertig?
typ: ja_nein
pruefung_am: 2026-01-01
prognosen:
  - von: Stadt A
    wert: 1.00
    hinterlegt_am: 2025-01-01
    art: angekuendigt
  - von: Computer
    wert: 0.70
    hinterlegt_am: 2025-01-02
    art: geschaetzt
ausgang: 1
aufgeloest_am: 2026-01-02
beleg_ausgang: https://example.org/a/1-beleg
vermerke: []
---

## Kontext
Test A1.
"""

WETTE_A_JA_NEIN_VERFALLEN = """---
id: a-2025-002
institution: Stadt A
gesagt_von: Buergermeister A
gesagt_am: 2025-02-01
quelle: https://example.org/a/2
zitat: "Der Park wird 2025 begruent."
frage: Ist der Park am 31.12.2025 begruent?
typ: ja_nein
pruefung_am: 2026-01-01
prognosen:
  - von: Stadt A
    wert: 1.00
    hinterlegt_am: 2025-02-01
    art: angekuendigt
  - von: Computer
    wert: 0.40
    hinterlegt_am: 2025-02-02
    art: geschaetzt
ausgang: verfallen
aufgeloest_am: 2028-01-02
beleg_ausgang: null
vermerke:
  - am: 2028-01-02
    text: Kein Beleg auffindbar.
---

## Kontext
Test A2.
"""

WETTE_B_OFFEN = """---
id: b-2025-001
institution: Stadt B
gesagt_von: Buergermeisterin B
gesagt_am: 2026-01-01
quelle: https://example.org/b/1
zitat: "Die Bruecke wird 2027 fertig."
frage: Ist die Bruecke am 31.12.2027 fertig?
typ: ja_nein
pruefung_am: 2028-01-01
prognosen:
  - von: Stadt B
    wert: 1.00
    hinterlegt_am: 2026-01-01
    art: angekuendigt
  - von: Computer
    wert: 0.50
    hinterlegt_am: 2026-01-02
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Test B1.
"""

WETTE_B_PUNKT = """---
id: b-2025-002
institution: Stadt B
gesagt_von: Buergermeisterin B
gesagt_am: 2025-06-01
quelle: https://example.org/b/2
zitat: "Der Haushalt betraegt 500 Mio EUR."
frage: Wie hoch ist der Haushalt 2026?
typ: punkt
einheit: Mio EUR
pruefung_am: 2026-01-01
prognosen:
  - von: Stadt B
    wert: 500.0
    hinterlegt_am: 2025-06-01
    art: angekuendigt
  - von: Computer
    wert: 480.0
    hinterlegt_am: 2025-06-02
    art: geschaetzt
ausgang: 490.0
aufgeloest_am: 2026-02-01
beleg_ausgang: https://example.org/b/2-beleg
vermerke: []
---

## Kontext
Test B2.
"""


def _gemischtes_buch(tmp_path: Path) -> Path:
    ordner = tmp_path / "buch"
    ordner.mkdir()
    (ordner / "BUCH.md").write_text(BUCH_MD, encoding="utf-8")
    wetten = ordner / "wetten"
    wetten.mkdir()
    (wetten / "a-2025-001.md").write_text(WETTE_A_JA_NEIN_1, encoding="utf-8")
    (wetten / "a-2025-002.md").write_text(WETTE_A_JA_NEIN_VERFALLEN, encoding="utf-8")
    (wetten / "b-2025-001.md").write_text(WETTE_B_OFFEN, encoding="utf-8")
    (wetten / "b-2025-002.md").write_text(WETTE_B_PUNKT, encoding="utf-8")
    return ordner


def test_gemischtes_buch_ende_zu_ende(tmp_path: Path, capsys):
    buch = _gemischtes_buch(tmp_path)
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 0

    assert (aus / "institution" / "stadt-a.html").exists()
    assert (aus / "institution" / "stadt-b.html").exists()

    index = (aus / "index.html").read_text(encoding="utf-8")
    assert "Stadt A" in index
    assert "Stadt B" in index

    import json
    daten = json.loads((aus / "wettbuch.json").read_text(encoding="utf-8"))
    assert len(daten["wetten"]) == 4
    namen = {r["von"] for r in daten["tabelle"]}
    assert {"Stadt A", "Stadt B", "Computer"} <= namen


def test_reproduzierbar(tmp_path: Path):
    buch = _gemischtes_buch(tmp_path)
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)

    aus1 = tmp_path / "site1"
    aus2 = tmp_path / "site2"
    seiten.seiten_schreiben(b["meta"], bew, aus1, build_zeit="2026-08-28 12:00")
    seiten.seiten_schreiben(b["meta"], bew, aus2, build_zeit="2026-08-28 12:00")

    dateien1 = sorted(p.relative_to(aus1).as_posix() for p in aus1.rglob("*") if p.is_file())
    dateien2 = sorted(p.relative_to(aus2).as_posix() for p in aus2.rglob("*") if p.is_file())
    assert dateien1 == dateien2

    for rel in dateien1:
        assert (aus1 / rel).read_bytes() == (aus2 / rel).read_bytes(), rel
