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
