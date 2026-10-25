# generator/tests/test_sitemap.py
"""sitemap.xml bei `alle --url`: jede gebaute Seite mit absoluter Adresse, damit Google auch Wetten findet,
auf die keine Presse-Mail verlinkt. lastmod = letztes Datum in den Daten der Wette, nie das Baudatum."""
import xml.etree.ElementTree as ET
from pathlib import Path

from test_alle import buecher_ordner, seiten_ordner  # noqa: F401  (Fixtures)
from wettbuch import cli, sitemap

NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
URL = "https://example.org/festgehalten/"


def _eintraege(pfad: Path) -> dict[str, str | None]:
    wurzel = ET.fromstring(pfad.read_text(encoding="utf-8"))
    assert wurzel.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset"
    aus = {}
    for u in wurzel.findall("s:url", NS):
        lm = u.find("s:lastmod", NS)
        aus[u.find("s:loc", NS).text] = lm.text if lm is not None else None
    return aus


def test_alle_mit_url_schreibt_sitemap_mit_allen_seiten(buecher_ordner: Path, seiten_ordner: Path,
                                                         tmp_path: Path):
    ausgabe = tmp_path / "site"
    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe), "--url", URL, "--seiten", str(seiten_ordner)])
    assert rc == 0
    e = _eintraege(ausgabe / "sitemap.xml")
    gebaut = {URL + p.relative_to(ausgabe).as_posix() for p in ausgabe.rglob("*.html")}
    assert set(e) == gebaut
    assert URL + "index.html" in e
    assert URL + "erstes/wette/a-2025-001.html" in e
    assert URL + "impressum/index.html" in e


def test_lastmod_ist_letztes_datum_der_wette_nicht_baudatum(buecher_ordner: Path, tmp_path: Path):
    ausgabe = tmp_path / "site"
    assert cli.main(["alle", str(buecher_ordner), str(ausgabe), "--url", URL]) == 0
    e = _eintraege(ausgabe / "sitemap.xml")
    lm = e[URL + "erstes/wette/a-2025-001.html"]
    assert lm is not None and len(lm) == 10 and lm < "2026-10-25"
    # Buchseite: das jüngste Datum ihrer Wetten
    assert e[URL + "erstes/index.html"] >= lm
    # Zusatzseiten haben kein Datum in den Daten → kein lastmod
    assert all(v is None for k, v in e.items() if "/impressum/" in k)


def test_ohne_url_keine_sitemap(buecher_ordner: Path, tmp_path: Path):
    # Eine Sitemap braucht absolute Adressen; ohne --url wäre sie falsch.
    ausgabe = tmp_path / "site"
    assert cli.main(["alle", str(buecher_ordner), str(ausgabe)]) == 0
    assert not (ausgabe / "sitemap.xml").exists()


def test_letztes_datum_nimmt_jedes_datumsfeld():
    w = {"gesagt_am": "2025-10-01", "aufgeloest_am": None,
         "prognosen": [{"hinterlegt_am": "2026-08-28"}, {"hinterlegt_am": "2025-10-01"}],
         "vermerke": [{"am": "2026-09-03", "text": "x"}]}
    assert sitemap.letztes_datum(w) == "2026-09-03"
    w["aufgeloest_am"] = "2026-10-02"
    assert sitemap.letztes_datum(w) == "2026-10-02"


def test_sitemap_xml_maskiert_adressen():
    xml = sitemap.sitemap_xml([("https://example.org/a&b.html", None)])
    assert "a&amp;b.html" in xml
    ET.fromstring(xml)
