# generator/tests/test_sprache.py
"""Sprach-Schalter `sprache: en` in BUCH.md (FORMAT.md §4). Standard bleibt Deutsch."""
from datetime import date
from pathlib import Path

import pytest

from wettbuch import bewerten, feed, lesen, pruefen, seiten, sprache
from conftest import BUCH_OK, WETTE_OK


def _buch_en(tmp_path: Path, wette: str = WETTE_OK) -> Path:
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "BUCH.md").write_text(BUCH_OK.replace("format: v1", "format: v1\nsprache: en"), encoding="utf-8")
    (tmp_path / "wetten").mkdir()
    (tmp_path / "wetten" / "test-2025-001.md").write_text(wette, encoding="utf-8")
    return tmp_path


def _bauen(buch: Path, tmp_path: Path) -> Path:
    b = lesen.buch_lesen(buch)
    aus = tmp_path / "site"
    seiten.seiten_schreiben(b["meta"], bewerten.buch_bewerten(b), aus, build_zeit="2026-10-07 16:00")
    return aus


AUFGELOEST = (WETTE_OK.replace("beleg_ausgang: null", "beleg_ausgang: https://example.org/beleg")
              .replace("ausgang: null", "ausgang: 0")
              .replace("aufgeloest_am: null", "aufgeloest_am: 2025-11-03"))


def test_datum_und_zahl_je_sprache():
    assert sprache.datum(date(2026, 10, 7), "de") == "07.10.2026"
    assert sprache.datum(date(2026, 10, 7), "en") == "7 October 2026"
    assert sprache.datum(None, "en") == "–"
    assert sprache.zahl(0.1225, 2, "de") == "0,12"
    assert sprache.zahl(0.1225, 2, "en") == "0.12"
    assert sprache.zahl(None, 2, "en") == "–"


def test_jeder_text_hat_beide_sprachen():
    assert set(sprache.TEXTE["de"]) == set(sprache.TEXTE["en"])
    assert set(sprache.WERTE["de"]) == set(sprache.WERTE["en"])


def test_feste_werte_werden_nur_fuer_die_anzeige_uebersetzt():
    assert sprache.wert("angekuendigt", "en") == "announced"
    assert sprache.wert("angekuendigt", "de") == "angekuendigt"
    assert sprache.wert("unbekannt", "en") == "unbekannt"


def test_unbekannte_sprache_ist_ein_pruefungsfehler(tmp_path: Path):
    (tmp_path / "BUCH.md").write_text(BUCH_OK.replace("format: v1", "format: v1\nsprache: fr"), encoding="utf-8")
    (tmp_path / "wetten").mkdir()
    fehler = pruefen.buch_pruefen(lesen.buch_lesen(tmp_path))
    assert any(f.feld == "sprache" for f in fehler)


def test_ohne_feld_bleibt_alles_deutsch(buch: Path, tmp_path: Path):
    aus = _bauen(buch, tmp_path)
    index = (aus / "index.html").read_text(encoding="utf-8")
    assert '<html lang="de">' in index
    assert "Alle Wetten" in index
    wette = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "gesagt am 01.10.2025" in wette


def test_englisches_buch_ist_ganz_englisch(tmp_path: Path):
    aus = _bauen(_buch_en(tmp_path / "b"), tmp_path)
    index = (aus / "index.html").read_text(encoding="utf-8")
    assert '<html lang="en">' in index
    assert "All bets" in index and "Ranking" in index
    assert "since 28 August 2026" in index
    wette = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "said on 1 October 2025" in wette
    assert "announced" in wette and "estimated" in wette
    assert "open" in wette
    for deutsch in ("gesagt am", "Prüfung ab", "Rangliste", "Alle Wetten", "Herkunft", "hinterlegt am",
                    "Typ:", "Quelle<", "gebaut ", "angekuendigt", "geschaetzt", "zitiert", "ja_nein", "offen<"):
        assert deutsch not in index + wette, deutsch


def test_englisches_buch_aufgeloest_und_feed(tmp_path: Path):
    aus = _bauen(_buch_en(tmp_path / "b", AUFGELOEST), tmp_path)
    wette = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert "Resolved on 3 November 2025" in wette
    assert '<span class="status nein">no</span>' in wette
    xml = (aus / "feed.xml").read_text(encoding="utf-8")
    assert "<title>No: Ist das Haus" in xml
    assert "Outcome: No. Evidence: https://example.org/beleg" in xml
    assert "“Das Haus wird Ende Oktober fertig.”" in xml
    assert "newly resolved" in xml
    assert "Ausgang" not in xml and "neu aufgelöst" not in xml


def test_feed_eintrag_bleibt_deutsch_ohne_sprache():
    w = {"id": "x", "typ": "ja_nein", "ausgang": 1, "institution": "I", "zitat": "Z", "gesagt_von": "V",
         "gesagt_am": date(2026, 1, 2), "frage": "F?", "aufgeloest_am": date(2026, 2, 1), "beleg_ausgang": "B"}
    e = feed.eintrag(w, "wette/x.html")
    assert e["titel"] == "Ja: F?"
    assert "Ausgang: Ja. Beleg: B" in e["zusammenfassung"]


def test_alle_mit_englischem_buch(tmp_path: Path):
    from wettbuch import cli
    buecher = tmp_path / "buecher"
    _buch_en(buecher / "london")
    assert cli.main(["alle", str(buecher), str(tmp_path / "site")]) == 0
    index = (tmp_path / "site" / "london" / "index.html").read_text(encoding="utf-8")
    assert '<html lang="en">' in index
