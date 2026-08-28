# generator/tests/test_seiten.py
import json
from datetime import date
from pathlib import Path

import pytest

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


def test_slug_kollision_wirft(buch: Path, tmp_path: Path):
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    zweite = dict(bew["wetten"][0], id="test-2025-002", institution="Stadt-Test")
    bew["wetten"].append(zweite)
    with pytest.raises(ValueError, match="Slug-Kollision"):
        seiten.seiten_schreiben(b["meta"], bew, tmp_path / "site", build_zeit="x")
