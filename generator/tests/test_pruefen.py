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


def test_ausgang_ungueltiger_wert(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = "vielleicht"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "ausgang"


def test_ja_nein_ausgang_nur_0_oder_1(gueltig):
    w = _wette(gueltig)
    w["ausgang"] = 0.5
    w["aufgeloest_am"] = date(2025, 11, 2)
    w["beleg_ausgang"] = "https://example.org/pm/2"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "ausgang"


def test_id_zeichensatz(gueltig):
    _wette(gueltig)["id"] = "../../index"
    f = pruefen.buch_pruefen(gueltig)
    assert f and f[0].feld == "id"


def test_von_doppelt_in_einer_wette(gueltig):
    w = _wette(gueltig)
    w["prognosen"][1]["von"] = "Stadt Test"
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "prognosen[1].von" for x in f)


def test_institution_muss_text_sein(gueltig):
    _wette(gueltig)["institution"] = ["Stadt Test"]
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "institution" and "Text" in x.text for x in f)


def test_gesagt_von_muss_text_sein(gueltig):
    _wette(gueltig)["gesagt_von"] = ["jemand"]
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "gesagt_von" and "Text" in x.text for x in f)


def test_zitat_muss_text_sein(gueltig):
    _wette(gueltig)["zitat"] = 123
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "zitat" and "Text" in x.text for x in f)


def test_frage_muss_text_sein(gueltig):
    _wette(gueltig)["frage"] = 123
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "frage" and "Text" in x.text for x in f)


def test_prognose_von_muss_text_sein(gueltig):
    _wette(gueltig)["prognosen"][1]["von"] = 42
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "prognosen[1].von" and "Text" in x.text for x in f)


def test_vermerk_muss_mapping_sein(gueltig):
    w = _wette(gueltig)
    w["vermerke"] = ["nur text"]
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "vermerke[0]" and "Mapping" in x.text for x in f)


def test_vermerk_am_und_text_werden_geprueft(gueltig):
    w = _wette(gueltig)
    w["vermerke"] = [{"am": "gestern", "text": 123}]
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "vermerke[0].am" for x in f)
    assert any(x.feld == "vermerke[0].text" for x in f)


def test_meta_titel_und_halter_muessen_text_sein(gueltig):
    gueltig["meta"]["titel"] = 123
    gueltig["meta"]["halter"] = 456
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.feld == "titel" for x in f)
    assert any(x.feld == "halter" for x in f)


def test_meta_seit_muss_datum_sein(gueltig):
    gueltig["meta"]["seit"] = "2026-08-28"
    f = pruefen.buch_pruefen(gueltig)
    assert any(x.datei == "BUCH.md" and x.feld == "seit" and "Datum" in x.text for x in f)


def test_unhashbare_werte_werfen_nicht(gueltig):
    w = _wette(gueltig)
    w["typ"] = ["ja_nein"]
    w["ausgang"] = {"x": 1}
    w["prognosen"][1]["art"] = ["geschaetzt"]
    f = pruefen.buch_pruefen(gueltig)  # darf nicht werfen
    assert any(x.feld == "typ" for x in f)
    assert any(x.feld == "ausgang" for x in f)
    assert any(x.feld == "prognosen[1].art" for x in f)
