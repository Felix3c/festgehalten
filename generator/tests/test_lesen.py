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
