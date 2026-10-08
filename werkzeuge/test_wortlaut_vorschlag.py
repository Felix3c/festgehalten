"""Tests ohne Netz für wortlaut_vorschlag.py (pytest werkzeuge/test_wortlaut_vorschlag.py)."""
from wortlaut_vorschlag import bester_wortlaut, saetze, sichtbarer_text, woerter

SEITE = """<html><head><title>Haushalt</title><script>var x = "Defizit 97";</script></head><body>
<nav>Startseite Presse</nav>
<p>Der Stadtrat hat den Haushalt 2025/2026 beschlossen. Für 2025 weist der Haushaltsplan ein
Defizit von 97,0 Millionen Euro aus.</p><p>Die Kita-Versorgung soll steigen: Die U3-Quote liegt
künftig bei 42 Prozent. Weitere Infos folgen.</p></body></html>"""


def test_sichtbarer_text_ohne_skript_und_tags():
    text = sichtbarer_text(SEITE)
    assert "var x" not in text and "<p>" not in text
    assert "97,0 Millionen Euro" in text


def test_saetze_trennt_an_satzende_und_absatz():
    s = saetze(sichtbarer_text(SEITE))
    assert "Der Stadtrat hat den Haushalt 2025/2026 beschlossen." in s
    assert any(x.startswith("Für 2025 weist") for x in s)


def test_saetze_nicht_nach_abkuerzung():
    assert saetze("Der Etat liegt bei ca. 1,8 Milliarden Euro. Danach folgt mehr.") == [
        "Der Etat liegt bei ca. 1,8 Milliarden Euro.", "Danach folgt mehr."]


def test_woerter_trennt_zahlen_und_mio():
    assert woerter("Defizit 97,0 Mio. €") == ["defizit", "97", "0", "mio"]


def test_stichwortzitat_findet_vollen_satz():
    treffer = bester_wortlaut("U3-Quote 42 %", sichtbarer_text(SEITE))
    assert treffer["wortlaut"] == "Die Kita-Versorgung soll steigen: Die U3-Quote liegt künftig bei 42 Prozent."
    assert treffer["deckung"] >= 0.6


def test_zusammengezogenes_zitat_nimmt_zwei_saetze():
    zitat = "Der Stadtrat hat den Haushalt 2025/2026 beschlossen, Defizit von 97,0 Millionen Euro"
    treffer = bester_wortlaut(zitat, sichtbarer_text(SEITE))
    assert treffer["wortlaut"].startswith("Der Stadtrat hat")
    assert treffer["wortlaut"].endswith("Millionen Euro aus.")
    assert treffer["deckung"] == 1.0


def test_zahl_muss_stimmen():
    """Ein Satz ohne die Zahl des Zitats ist kein Wortlaut-Vorschlag."""
    treffer = bester_wortlaut("Defizit von 123,0 Millionen Euro", sichtbarer_text(SEITE))
    assert treffer["zahlen_fehlen"] == "123"


def test_kein_treffer_bei_fremdem_text():
    treffer = bester_wortlaut("Neubau der Feuerwache Hamborn bis 2028", sichtbarer_text(SEITE))
    assert treffer["deckung"] < 0.6


def test_zahlen_nicht_auf_seite():
    from wortlaut_vorschlag import zahlen_nicht_auf_seite
    text = sichtbarer_text(SEITE)
    assert zahlen_nicht_auf_seite("Defizit von 97,0 Millionen Euro 2025", text) == ""
    assert zahlen_nicht_auf_seite("Defizit von 98,7 Millionen Euro", text) == "98,7"
    assert zahlen_nicht_auf_seite("Defizit von 97 Millionen Euro", text) == "97"


def test_leere_archivseite_ist_kein_befund():
    from wortlaut_vorschlag import bewerten
    roh = "<html><head><script>var challenge = 1;</script></head><body></body></html>"
    text = sichtbarer_text(roh)
    assert bewerten(bester_wortlaut("Defizit 214,5 Mio", text), len(text)) == "archiv_leer"
