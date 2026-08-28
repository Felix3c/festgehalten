from datetime import date

import pytest
from wettbuch import bewerten


def _wette(id_="w1", typ="ja_nein", ausgang=None, prognosen=None, institution="Stadt Test", einheit=None):
    w = {
        "id": id_, "institution": institution, "typ": typ, "ausgang": ausgang,
        "prognosen": prognosen or [
            {"von": "Stadt Test", "wert": 1.0, "art": "angekuendigt", "hinterlegt_am": date(2025, 1, 1)},
            {"von": "Computer", "wert": 0.35, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
        ],
        "_datei": f"{id_}.md",
    }
    if einheit:
        w["einheit"] = einheit
    return w


def _punkt(id_="p"):
    return _wette(id_=id_, typ="punkt", ausgang=610.0, einheit="Mio EUR", prognosen=[
        {"von": "Stadt Test", "wert": 594.8, "art": "angekuendigt", "hinterlegt_am": date(2025, 1, 1)},
        {"von": "Computer", "wert": 625, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
    ])


def test_brier():
    assert bewerten.brier(1.0, 1) == 0.0
    assert bewerten.brier(1.0, 0) == 1.0
    assert bewerten.brier(0.5, 1) == pytest.approx(0.25)
    assert bewerten.brier(0.35, 0) == pytest.approx(0.1225)


def test_abstand():
    assert bewerten.abstand(594.8, 610.0) == pytest.approx(15.2)
    assert bewerten.abstand(625, 610.0) == pytest.approx(15.0)


def test_wette_offen():
    b = bewerten.wette_bewerten(_wette())
    assert b["status"] == "offen"
    assert b["scores"] == {"Stadt Test": None, "Computer": None}
    assert b["naeher_dran"] is None


def test_wette_ja_nein_aufgeloest_nein():
    b = bewerten.wette_bewerten(_wette(ausgang=0))
    assert b["status"] == "aufgeloest"
    assert b["scores"]["Stadt Test"] == 1.0
    assert b["scores"]["Computer"] == pytest.approx(0.1225)


def test_wette_verfallen():
    b = bewerten.wette_bewerten(_wette(ausgang="verfallen"))
    assert b["status"] == "verfallen"
    assert b["scores"] == {"Stadt Test": None, "Computer": None}


def test_wette_punkt_naeher_dran():
    b = bewerten.wette_bewerten(_punkt())
    assert b["naeher_dran"] == "Computer"
    assert b["scores"]["Stadt Test"] == pytest.approx(15.2)
    assert b["gleichstand"] is False


def test_punkt_gleichstand_niemand_gewinnt():
    w = _wette(typ="punkt", ausgang=100.0, einheit="Mio EUR", prognosen=[
        {"von": "Alpha", "wert": 90.0, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
        {"von": "Zeta", "wert": 110.0, "art": "geschaetzt", "hinterlegt_am": date(2025, 1, 1)},
    ])
    b = bewerten.wette_bewerten(w)
    assert b["naeher_dran"] is None
    assert b["gleichstand"] is True

    t = bewerten.buch_bewerten({"meta": {}, "wetten": [w]})["tabelle"]
    alpha = next(z for z in t if z["von"] == "Alpha")
    zeta = next(z for z in t if z["von"] == "Zeta")
    assert (alpha["punkt_n"], alpha["punkt_gewonnen"]) == (1, 0)
    assert (zeta["punkt_n"], zeta["punkt_gewonnen"]) == (1, 0)


def test_tabelle_rang_erst_ab_10():
    wetten = [_wette(id_=f"w{i}", ausgang=0) for i in range(9)]
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    assert computer["ja_nein_n"] == 9
    assert computer["ja_nein_schnitt"] == pytest.approx(0.1225)
    assert computer["rang"] is None

    wetten.append(_wette(id_="w9", ausgang=0))
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    assert computer["rang"] == 1
    assert stadt["rang"] == 2
    assert stadt["ist_institution"] is True
    assert computer["ist_institution"] is False
    assert [z["von"] for z in t] == ["Computer", "Stadt Test"]


def test_tabelle_rechenschaft_zaehlt_verfallene_der_institution():
    wetten = [_wette(id_="a", ausgang="verfallen"), _wette(id_="b", ausgang="strittig"), _wette(id_="c")]
    t = bewerten.buch_bewerten({"meta": {}, "wetten": wetten})["tabelle"]
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    computer = next(z for z in t if z["von"] == "Computer")
    assert stadt["rechenschaft_verfallen"] == 2
    assert stadt["wetten_gesamt"] == 3
    assert computer["rechenschaft_verfallen"] == 0
    assert computer["wetten_gesamt"] == 0


def test_tabelle_punkt_gewonnen():
    t = bewerten.buch_bewerten({"meta": {}, "wetten": [_punkt()]})["tabelle"]
    computer = next(z for z in t if z["von"] == "Computer")
    stadt = next(z for z in t if z["von"] == "Stadt Test")
    assert (computer["punkt_gewonnen"], computer["punkt_n"]) == (1, 1)
    assert (stadt["punkt_gewonnen"], stadt["punkt_n"]) == (0, 1)


def test_buch_bewerten_haengt_bewertung_an_wetten():
    r = bewerten.buch_bewerten({"meta": {}, "wetten": [_wette(ausgang=1)]})
    assert r["wetten"][0]["_bewertung"]["status"] == "aufgeloest"
    assert r["rang_ab"] == 10
