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
