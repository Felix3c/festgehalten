# generator/tests/test_feed.py
"""Atom-Feed „neu aufgelöst“: je Buch feed.xml, in der Übersicht ein Sammelfeed.
Abonnieren, ohne uns zu fragen (GUARD.md: kein Kanal, kein Betreiber)."""
import xml.etree.ElementTree as ET
from pathlib import Path

from conftest import BUCH_OK, WETTE_OK
from wettbuch import bewerten, cli, lesen, seiten

NS = {"a": "http://www.w3.org/2005/Atom"}

WETTE_NEIN = WETTE_OK.replace("id: test-2025-001", "id: test-2025-002").replace(
    "ausgang: null\naufgeloest_am: null\nbeleg_ausgang: null",
    "ausgang: 0\naufgeloest_am: 2025-11-03\nbeleg_ausgang: https://example.org/beleg/2")

WETTE_JA_ALT = WETTE_OK.replace("id: test-2025-001", "id: test-2025-003").replace(
    "ausgang: null\naufgeloest_am: null\nbeleg_ausgang: null",
    "ausgang: 1\naufgeloest_am: 2025-11-01\nbeleg_ausgang: https://example.org/beleg/3")


def _buch_mit(tmp_path: Path, *wetten: str) -> Path:
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "BUCH.md").write_text(BUCH_OK, encoding="utf-8")
    ordner = tmp_path / "wetten"
    ordner.mkdir()
    for i, w in enumerate(wetten, start=1):
        (ordner / f"w{i}.md").write_text(w, encoding="utf-8")
    return tmp_path


def _gebaut(buch: Path, aus: Path, url: str | None = None) -> Path:
    b = lesen.buch_lesen(buch)
    bew = bewerten.buch_bewerten(b)
    seiten.seiten_schreiben(b["meta"], bew, aus, build_zeit="2026-09-15 12:00", url=url)
    return aus


def _feed(pfad: Path) -> ET.Element:
    return ET.fromstring(pfad.read_text(encoding="utf-8"))


def test_feed_ohne_aufgeloeste_ist_gueltig_und_leer(buch: Path, tmp_path: Path):
    aus = _gebaut(buch, tmp_path / "site")
    wurzel = _feed(aus / "feed.xml")
    assert wurzel.tag == "{http://www.w3.org/2005/Atom}feed"
    assert wurzel.find("a:title", NS).text == "Test gegen Test · neu aufgelöst"
    assert wurzel.findall("a:entry", NS) == []


def test_feed_eintrag_traegt_ausgang_link_datum_und_beleg(tmp_path: Path):
    buch = _buch_mit(tmp_path / "buch", WETTE_OK, WETTE_NEIN)
    aus = _gebaut(buch, tmp_path / "site")
    eintraege = _feed(aus / "feed.xml").findall("a:entry", NS)
    assert len(eintraege) == 1
    e = eintraege[0]
    assert e.find("a:title", NS).text == "Nein: Ist das Haus am 31.10.2025 fertig?"
    assert e.find("a:link", NS).get("href") == "wette/test-2025-002.html"
    assert e.find("a:updated", NS).text == "2025-11-03T00:00:00Z"
    assert e.find("a:id", NS).text == "urn:festgehalten:test-2025-002"
    zusammenfassung = e.find("a:summary", NS).text
    assert "Stadt Test" in zusammenfassung
    assert "Das Haus wird Ende Oktober fertig." in zusammenfassung
    assert "https://example.org/beleg/2" in zusammenfassung


def test_feed_neueste_zuerst_und_absolute_links_mit_url(tmp_path: Path):
    buch = _buch_mit(tmp_path / "buch", WETTE_JA_ALT, WETTE_NEIN)
    aus = _gebaut(buch, tmp_path / "site", url="https://example.org/buch/")
    wurzel = _feed(aus / "feed.xml")
    ids = [e.find("a:id", NS).text for e in wurzel.findall("a:entry", NS)]
    assert ids == ["urn:festgehalten:test-2025-002", "urn:festgehalten:test-2025-003"]
    hrefs = [e.find("a:link", NS).get("href") for e in wurzel.findall("a:entry", NS)]
    assert hrefs[0] == "https://example.org/buch/wette/test-2025-002.html"
    selbst = [l for l in wurzel.findall("a:link", NS) if l.get("rel") == "self"]
    assert selbst and selbst[0].get("href") == "https://example.org/buch/feed.xml"


def test_index_verweist_auf_feed(buch: Path, tmp_path: Path):
    aus = _gebaut(buch, tmp_path / "site")
    html = (aus / "index.html").read_text(encoding="utf-8")
    assert '<link rel="alternate" type="application/atom+xml" href="feed.xml"' in html
    assert 'href="feed.xml">Feed' in html
    unter = (aus / "wette" / "test-2025-001.html").read_text(encoding="utf-8")
    assert 'type="application/atom+xml" href="../feed.xml"' in unter


def test_feed_ist_gedeckelt(tmp_path: Path):
    wetten = []
    for i in range(60):
        w = WETTE_OK.replace("id: test-2025-001", f"id: test-2025-{i + 100:03d}").replace(
            "ausgang: null\naufgeloest_am: null\nbeleg_ausgang: null",
            f"ausgang: 1\naufgeloest_am: 2025-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}\n"
            "beleg_ausgang: https://example.org/b")
        wetten.append(w)
    buch = _buch_mit(tmp_path / "buch", *wetten)
    aus = _gebaut(buch, tmp_path / "site")
    assert len(_feed(aus / "feed.xml").findall("a:entry", NS)) == seiten.FEED_MAX


def test_alle_schreibt_sammelfeed(tmp_path: Path):
    buecher = tmp_path / "buecher"
    _buch_mit(buecher / "a", WETTE_NEIN)
    _buch_mit(buecher / "b", WETTE_JA_ALT.replace("test-2025-003", "b-2025-001"))
    aus = tmp_path / "site"
    rc = cli.main(["alle", str(buecher), str(aus), "--url", "https://example.org/"])
    assert rc == 0
    wurzel = _feed(aus / "feed.xml")
    assert wurzel.find("a:title", NS).text == "festgehalten · neu aufgelöst"
    hrefs = [e.find("a:link", NS).get("href") for e in wurzel.findall("a:entry", NS)]
    assert hrefs == ["https://example.org/a/wette/test-2025-002.html",
                     "https://example.org/b/wette/b-2025-001.html"]
    assert (aus / "a" / "feed.xml").exists()
    html = (aus / "index.html").read_text(encoding="utf-8")
    assert 'type="application/atom+xml" href="feed.xml"' in html
