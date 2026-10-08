"""Tests für die Archivsicherung (ohne Netz)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import archivsicherung as a  # noqa: E402
import pytest  # noqa: E402


@pytest.fixture(autouse=True)
def _cdx_leeren():
    a._CDX.clear()


def test_zitat_mit_typografie_und_tags_wird_gefunden():
    html = "<p>Der Erweiterungsneubau soll <b>voraussichtlich</b> im Sommer 2027 fertig&nbsp;sein.</p>"
    assert a.zitat_in_text("„Der Erweiterungsneubau soll voraussichtlich im Sommer 2027 fertig sein.“", html) == []


def test_fehlender_teil_wird_gemeldet():
    fehlt = a.zitat_in_text("Die Bibliothek eröffnet 2026 […] mit neuem Café im Erdgeschoss", "Die Bibliothek eröffnet 2026.")
    assert fehlt == ["mit neuem café im erdgeschoss"]


def test_auslassung_teilt_zitat_und_kurze_reste_fallen_weg():
    assert a.zitat_teile("Anfang 2027: Start der Taktverdichtung … auf 903 …") == ["anfang 2027 start der taktverdichtung"]


def test_umlaute_und_prozent_bleiben():
    assert a.norm_text("Grundsteuer-B: 11,0 % über Plan – Köln") == "grundsteuer b 11 0 % über plan köln"


def test_roh_url_setzt_id_einmal():
    url = "https://web.archive.org/web/20260312155054/https://www.dvg-duisburg.de/x"
    assert a.roh_url(url) == "https://web.archive.org/web/20260312155054id_/https://www.dvg-duisburg.de/x"
    assert a.roh_url(a.roh_url(url)) == a.roh_url(url)


def test_wetten_sammeln_liest_kopf_und_ueberspringt_buch_und_docs(tmp_path):
    (tmp_path / "wetten").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / "BUCH.md").write_text("---\nid: buch\nquelle: x\n---\n", encoding="utf-8")
    (tmp_path / "docs" / "notiz.md").write_text("---\nid: notiz\nquelle: x\n---\n", encoding="utf-8")
    (tmp_path / "wetten" / "b.md").write_text(
        '---\nid: stadt-2026-002\nquelle: https://example.org/b\nzitat: "soll 2027"\n---\n\n## Kontext\n', encoding="utf-8")
    (tmp_path / "wetten" / "a.md").write_text(
        "---\nid: stadt-2026-001\nquelle: https://example.org/a\n---\n", encoding="utf-8")
    wetten = a.wetten_sammeln([tmp_path, tmp_path])
    assert [w["id"] for w in wetten] == ["stadt-2026-001", "stadt-2026-002"]
    assert wetten[1]["zitat"] == "soll 2027"


def test_tabelle_rundreise(tmp_path):
    pfad = tmp_path / "r" / "archiv.csv"
    a.tabelle_schreiben(pfad, {"x-1": {"id": "x-1", "quelle": "q", "status": "ok"}})
    assert a.tabelle_lesen(pfad)["x-1"]["status"] == "ok"
    assert a.tabelle_lesen(tmp_path / "fehlt.csv") == {}


class _Antwort:
    def __init__(self, status=200, text="", url="", json_=None):
        self.status_code, self.text, self.url = status, text, url
        self.headers = {"content-type": "text/html"}
        self.content = text.encode()
        self.encoding = "utf-8"
        self._json = json_

    def json(self):
        return self._json


class _Sitzung:
    """Antwortet nach URL; merkt sich, ob Save Page Now angestoßen wurde."""

    def __init__(self, cdx=None, seiten=None, speichern_ziel=None):
        self.cdx, self.seiten, self.speichern_ziel = cdx, seiten or {}, speichern_ziel
        self.gespeichert = False

    def get(self, url, params=None, timeout=None, allow_redirects=True):
        if "/cdx/" in url:
            return _Antwort(text="x" if self.cdx else "", json_=self.cdx)
        if "/save/" in url:
            self.gespeichert = True
            return _Antwort(url=self.speichern_ziel or "https://web.archive.org/save/fehler")
        return _Antwort(text=self.seiten.get(url, ""), status=200 if url in self.seiten else 404)


WETTE = {"id": "w-1", "quelle": "https://example.org/a", "zitat": "soll im Sommer 2027 fertig sein"}


def test_pruefen_vorhandene_kopie_mit_zitat_ist_ok():
    s = _Sitzung(cdx=[["timestamp", "original"], ["20260101000000", "https://example.org/a"]],
                 seiten={"https://web.archive.org/web/20260101000000id_/https://example.org/a": "Es soll im Sommer 2027 fertig sein."})
    z = a.pruefen(s, WETTE, speichern=True)
    assert (z["status"], s.gespeichert) == ("ok", False)
    assert z["archiv"] == "https://web.archive.org/web/20260101000000/https://example.org/a"


def test_pruefen_ohne_kopie_stoesst_an_und_prueft_neue(monkeypatch):
    monkeypatch.setattr(a, "PAUSE_SPEICHERN", 0)
    neu = "https://web.archive.org/web/20261004010101/https://example.org/a"
    s = _Sitzung(speichern_ziel=neu,
                 seiten={"https://web.archive.org/web/20261004010101id_/https://example.org/a": "soll im Sommer 2027 fertig sein"})
    z = a.pruefen(s, WETTE, speichern=True)
    assert (z["status"], z["archiv"], s.gespeichert) == ("ok", neu, True)


def test_pruefen_ohne_speichern_meldet_kein_archiv():
    assert a.pruefen(_Sitzung(), WETTE, speichern=False)["status"] == "kein_archiv"


def test_pruefen_archivquelle_ohne_zitat_wird_nicht_neu_gespeichert():
    quelle = "https://web.archive.org/web/20260312155054/https://www.dvg-duisburg.de/x"
    s = _Sitzung(seiten={a.roh_url(quelle): "ganz anderer Text auf der Seite"})
    z = a.pruefen(s, {"id": "d-7", "quelle": quelle, "zitat": WETTE["zitat"]}, speichern=True)
    assert (z["status"], s.gespeichert) == ("zitat_fehlt", False)


def test_kein_archiv_prueft_live_seite():
    s = _Sitzung(seiten={WETTE["quelle"]: "Das Haus soll im Sommer 2027 fertig sein."})
    z = a.pruefen(s, WETTE, speichern=False)
    assert (z["status"], z["zitat_live"]) == ("kein_archiv", "ja")


def test_live_seite_weg_meldet_status():
    assert a.pruefen(_Sitzung(), WETTE, speichern=False)["zitat_live"] == "404"


def test_speichern_scheitert_trotzdem_live_pruefen(monkeypatch):
    monkeypatch.setattr(a, "PAUSE_SPEICHERN", 0)
    s = _Sitzung(seiten={WETTE["quelle"]: "anderer Text"})
    z = a.pruefen(s, WETTE, speichern=True)
    assert (z["status"], z["zitat_live"], s.gespeichert) == ("speichern_fehlgeschlagen", "nein", True)


def test_utf8_ohne_charset_wird_richtig_gelesen():
    antwort = _Antwort(text="")
    antwort.content = "Neues Café: Konsolidierungsmaßnahmen".encode("utf-8")
    antwort.encoding = "ISO-8859-1"
    antwort.text = antwort.content.decode("latin-1")
    assert a.text_aus_antwort(antwort) == ("Neues Café: Konsolidierungsmaßnahmen", False)


def test_offene_wetten_nur_live_waehlt_live_woertliche_ohne_tragende_kopie():
    wetten = [{"id": i} for i in ("a", "b", "c", "d")]
    tabelle = {"a": {"status": "kein_archiv", "zitat_live": "ja"},
               "b": {"status": "zitat_fehlt", "zitat_live": "nein"},
               "c": {"status": "ok", "zitat_live": ""},
               "d": {"status": "zitat_fehlt", "zitat_live": "ja"}}
    assert [w["id"] for w in a.offene_wetten(wetten, tabelle, nur_live=True)] == ["a", "d"]
    assert [w["id"] for w in a.offene_wetten(wetten, tabelle, nur_live=False)] == ["a", "b", "d"]


def test_fehler_ueberschreibt_vorhandenen_befund_nicht():
    alt = {"id": "x-1", "status": "zitat_fehlt", "fehlt": "wort"}
    neu = {"id": "x-1", "status": "fehler", "fehlt": "ValueError"}
    assert a.zusammenfuehren(alt, neu) == alt


def test_fehler_ohne_vorhandenen_befund_wird_eingetragen():
    neu = {"id": "x-1", "status": "fehler", "fehlt": "ValueError"}
    assert a.zusammenfuehren(None, neu) == neu
    assert a.zusammenfuehren({"id": "x-1", "status": "fehler"}, neu) == neu


def test_neuer_befund_ersetzt_alten():
    alt = {"id": "x-1", "status": "zitat_fehlt"}
    neu = {"id": "x-1", "status": "ok"}
    assert a.zusammenfuehren(alt, neu) == neu
