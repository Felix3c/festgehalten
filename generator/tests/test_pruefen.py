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
