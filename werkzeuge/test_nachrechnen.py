"""Tests ohne Netz für nachrechnen.py (pytest werkzeuge/test_nachrechnen.py)."""
import pytest

from nachrechnen import kalibrierung, punkt_bilanz, rechenweg, zeilen, zusammenfassung


def _jn(id_, computer, ausgang, inst=1.0, **extra):
    w = {"id": id_, "institution": "Stadt X", "typ": "ja_nein", "ausgang": ausgang,
         "prognosen": [{"von": "Stadt X", "wert": inst}]}
    if computer is not None:
        w["prognosen"].append({"von": "Computer", "wert": computer})
    w.update(extra)
    return w


def _pk(id_, computer, inst, ausgang):
    return {"id": id_, "institution": "Stadt X", "typ": "punkt", "ausgang": ausgang,
            "prognosen": [{"von": "Stadt X", "wert": inst}, {"von": "Computer", "wert": computer}]}


def test_zeilen_nur_aufgeloeste_ja_nein_mit_computer():
    wetten = [
        _jn("a", 0.3, 0), _jn("b", 0.3, None), _jn("c", None, 1), _jn("d", 0.9, "verfallen"),
        _jn("e", 0.4, 1, ersetzt_durch="f"), _pk("g", 10, 12, 11),
    ]
    assert [z["id"] for z in zeilen(wetten)] == ["a"]


def test_zeile_rechnet_brier_fuer_computer_und_institution():
    z = zeilen([_jn("a", 0.3, 0)])[0]
    assert z["brier_computer"] == pytest.approx(0.09)
    assert z["brier_institution"] == pytest.approx(1.0)


def test_rechenweg_zeigt_formel_mit_komma():
    z = zeilen([_jn("a", 0.3, 1)])[0]
    assert rechenweg(z["computer"], z["ausgang"]) == "(0,30 − 1)² = 0,4900"


def test_zusammenfassung_mit_muenze_als_massstab():
    s = zusammenfassung(zeilen([_jn("a", 0.3, 0), _jn("b", 0.6, 1)]))
    assert s["n"] == 2
    assert s["computer"] == pytest.approx((0.09 + 0.16) / 2)
    assert s["institution"] == pytest.approx(0.5)
    assert s["muenze"] == 0.25


def test_zusammenfassung_leer():
    assert zusammenfassung([]) == {"n": 0, "computer": None, "institution": None, "muenze": 0.25}


def test_kalibrierung_baender():
    zs = zeilen([_jn("a", 0.3, 0), _jn("b", 0.35, 1), _jn("c", 0.9, 1), _jn("d", 1.0, 1)])
    k = {b["band"]: b for b in kalibrierung(zs)}
    assert k["0,20–0,40"]["n"] == 2
    assert k["0,20–0,40"]["mittel_computer"] == pytest.approx(0.325)
    assert k["0,20–0,40"]["eingetreten"] == pytest.approx(0.5)
    assert k["0,80–1,00"]["n"] == 2  # 1,00 gehört ins oberste Band
    assert k["0,00–0,20"]["n"] == 0 and k["0,00–0,20"]["eingetreten"] is None


def test_punkt_bilanz_naeher_dran():
    b = punkt_bilanz([_pk("a", 10, 12, 11.5), _pk("b", 10, 12, 9), _pk("c", 10, 12, 11),
                      _pk("d", 10, 12, None), _jn("e", 0.3, 0)])
    assert b == {"n": 3, "computer": 1, "institution": 1, "gleichstand": 1}


# --- Frage 468 (Felix 22.10.2026): „Was die Worte der Stadt wert waren“, nur Anzeige ---
def _wort(id_, institution, art, ausgang, wert=None):
    wert = {"angekuendigt": 1.0, "voraussichtlich": 0.8}[art] if wert is None else wert
    return {"id": id_, "institution": institution, "typ": "ja_nein", "ausgang": ausgang,
            "prognosen": [{"von": institution, "wert": wert, "art": art}]}


def test_worte_bilanz_zaehlt_je_stadt_und_wort():
    from nachrechnen import worte_bilanz
    wetten = [
        _wort("a", "Stadt Köln", "angekuendigt", 1), _wort("b", "Stadt Köln", "angekuendigt", 0),
        _wort("c", "Stadt Köln", "voraussichtlich", 1), _wort("d", "Stadt Bonn", "angekuendigt", 1),
    ]
    zeilen_ = {(z["institution"], z["art"]): z for z in worte_bilanz(wetten)}
    assert zeilen_[("Stadt Köln", "angekuendigt")]["n"] == 2
    assert zeilen_[("Stadt Köln", "angekuendigt")]["eingetreten"] == 1
    assert zeilen_[("Stadt Köln", "voraussichtlich")]["versprochen"] == pytest.approx(0.8)
    assert zeilen_[("Alle", "angekuendigt")]["n"] == 3
    assert zeilen_[("Alle", "angekuendigt")]["eingetreten"] == 2


def test_worte_bilanz_ohne_offene_verfallene_ersetzte_und_punkt():
    from nachrechnen import worte_bilanz
    wetten = [
        _wort("a", "Stadt X", "angekuendigt", None), _wort("b", "Stadt X", "angekuendigt", "verfallen"),
        dict(_wort("c", "Stadt X", "angekuendigt", 1), ersetzt_durch="d"),
        _pk("e", 10, 12, 11), _wort("f", "Stadt X", "voraussichtlich", 0),
    ]
    assert [(z["institution"], z["art"], z["n"]) for z in worte_bilanz(wetten)] == [
        ("Stadt X", "voraussichtlich", 1), ("Alle", "voraussichtlich", 1)]


def test_bericht_zeigt_die_worte_tabelle():
    from nachrechnen import bericht
    text = bericht([_wort("a", "Stadt Köln", "angekuendigt", 1), _wort("b", "Stadt Köln", "angekuendigt", 0)])
    assert "Was die Worte der Institution wert waren" in text
    assert "| Stadt Köln | angekündigt (1,00) | 2 | 1 von 2 (0,50) |" in text
