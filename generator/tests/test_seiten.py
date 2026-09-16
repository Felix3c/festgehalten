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
    assert daten["seit"] == "2026-08-28"
    assert daten["lizenz"] == "CC0"


def test_tabellen_spalte_wetten_als_institution(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "index.html").read_text(encoding="utf-8")
    assert "Wetten als Institution" in html


def test_body_html_wird_escaped(buch: Path, tmp_path: Path):
    p = buch / "wetten" / "test-2025-001.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n<script>alert(1)</script>\n", encoding="utf-8")
    html = (_gebaut(buch, tmp_path) / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "<script" not in html
    assert "&lt;script&gt;" in html


def test_slug_kollision_wirft(buch: Path, tmp_path: Path):
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    zweite = dict(bew["wetten"][0], id="test-2025-002", institution="Stadt-Test")
    bew["wetten"].append(zweite)
    with pytest.raises(ValueError, match="Slug-Kollision"):
        seiten.seiten_schreiben(b["meta"], bew, tmp_path / "site", build_zeit="x")


def test_slug_kollision_ist_eigene_exception(buch: Path, tmp_path: Path):
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    zweite = dict(bew["wetten"][0], id="test-2025-002", institution="Stadt-Test")
    bew["wetten"].append(zweite)
    with pytest.raises(seiten.SlugKollision):
        seiten.seiten_schreiben(b["meta"], bew, tmp_path / "site", build_zeit="x")


def test_wettenseite_zeigt_herkunft_standard_zitiert(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "Herkunft: zitiert" in html


def test_wettenseite_zeigt_herkunft_hinterlegt(buch: Path, tmp_path: Path):
    p = buch / "wetten" / "test-2025-001.md"
    p.write_text(p.read_text(encoding="utf-8").replace("typ: ja_nein", "typ: ja_nein\nherkunft: hinterlegt"),
                 encoding="utf-8")
    html = (_gebaut(buch, tmp_path) / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "Herkunft: hinterlegt" in html
    assert "Herkunft: zitiert" not in html


def test_wettenliste_hat_spalte_herkunft(buch: Path, tmp_path: Path):
    p = buch / "wetten" / "test-2025-001.md"
    p.write_text(p.read_text(encoding="utf-8").replace("typ: ja_nein", "typ: ja_nein\nherkunft: hinterlegt"),
                 encoding="utf-8")
    aus = _gebaut(buch, tmp_path)
    index = (aus / "index.html").read_text(encoding="utf-8")
    inst = (aus / "institution" / "stadt-test.html").read_text(encoding="utf-8")
    assert "<th>Herkunft</th>" in index
    assert "<td>hinterlegt</td>" in index
    assert "<td>hinterlegt</td>" in inst


def test_index_zeigt_lizenz(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "index.html").read_text(encoding="utf-8")
    assert "Lizenz CC0" in html


def test_ersetzte_wette_heisst_ersetzt_nicht_offen(buch: Path, tmp_path: Path):
    alt = (buch / "wetten" / "test-2025-001.md")
    text = alt.read_text(encoding="utf-8").replace("ausgang: null", "ersetzt_durch: test-2025-002\nausgang: null")
    alt.write_text(text, encoding="utf-8")
    neu = text.replace("test-2025-001", "test-2025-002").replace("ersetzt_durch: test-2025-002\n", "")
    (buch / "wetten" / "test-2025-002.md").write_text(neu, encoding="utf-8")
    aus = _gebaut(buch, tmp_path)
    liste = (aus / "index.html").read_text(encoding="utf-8")
    assert "ersetzt durch test-2025-002" in liste
    seite = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert 'href="test-2025-002.html"' in seite
    daten = json.loads((aus / "wettbuch.json").read_text(encoding="utf-8"))
    status = {w["id"]: w["_bewertung"]["status"] for w in daten["wetten"]}
    assert status == {"test-2025-001": "ersetzt", "test-2025-002": "offen"}


def test_offene_wette_mit_vermerk_zeigt_letzte_suche(buch: Path, tmp_path: Path):
    f = buch / "wetten" / "test-2025-001.md"
    f.write_text(f.read_text(encoding="utf-8").replace(
        "vermerke: []", 'vermerke:\n  - am: 2026-08-30\n    text: "3. Lauf: nichts gefunden"'), encoding="utf-8")
    html = (_gebaut(buch, tmp_path) / "index.html").read_text(encoding="utf-8")
    assert "Beleg gesucht, zuletzt 30.08.2026" in html


def test_fusszeile_ohne_zusatzlinks_bleibt_wie_bisher(buch: Path, tmp_path: Path):
    html = (_gebaut(buch, tmp_path) / "index.html").read_text(encoding="utf-8")
    assert "Impressum" not in html


def test_fusszeile_mit_zusatzlinks_relativ_zur_tiefe(buch: Path, tmp_path: Path):
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    aus = tmp_path / "site"
    links = [("Impressum", "../impressum/"), ("Datenschutz", "../datenschutz/")]
    seiten.seiten_schreiben(b["meta"], bew, aus, build_zeit="x", fuss_links=links)
    index = (aus / "index.html").read_text(encoding="utf-8")
    wette = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert '<a href="../impressum/">Impressum</a> · <a href="../datenschutz/">Datenschutz</a></footer>' in index
    assert '<a href="../../impressum/">Impressum</a> · <a href="../../datenschutz/">Datenschutz</a></footer>' in wette


def test_zusatzseiten_schreiben_rendert_markdown_escaped(tmp_path: Path):
    zusatz = [{"name": "impressum", "titel": "Impressum", "_text": "## Angaben\n\nFelix <b>Lind</b>"}]
    pfade = seiten.zusatzseiten_schreiben(zusatz, tmp_path, "x", fuss_links=[("Impressum", "impressum/")])
    assert pfade == [tmp_path / "impressum" / "index.html"]
    html = pfade[0].read_text(encoding="utf-8")
    assert "<h1>Impressum</h1>" in html and "<h2>Angaben</h2>" in html
    assert "&lt;b&gt;Lind&lt;/b&gt;" in html and "<b>" not in html
    assert 'href="../stil.css"' in html and 'href="../index.html"' in html
    assert '<a href="../impressum/">Impressum</a></footer>' in html
    assert "feed.xml" not in html
