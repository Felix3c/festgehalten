"""Tests für die zweite Quelle von messen.py (wartezeiten.json der Bürger-Seite) — ohne Netzzugriff.

Beispieldatei: testdaten/wartezeiten-2026-10-05-0800.json, echter Abruf vom Mo 05.10.2026 08:05.

Aufruf: python -m pytest recherche/koeln-wartezeit -q
"""
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

import messen

BEISPIEL = Path(__file__).resolve().parent / "testdaten" / "wartezeiten-2026-10-05-0800.json"
# Schreibweise des Open-Data-Feeds (title_anz, ohne Leerzeichen am Ende), Abruf 05.10.2026.
NAMEN_IM_FEED = {
    "Kundenzentrum Chorweiler",
    "Kundenzentrum Innenstadt",
    "Kundenzentrum Ehrenfeld",
    "Kundenzentrum Kalk",
    "Kundenzentrum Lindenthal",
    "Kundenzentrum Mülheim",
    "Kundenzentrum Nippes",
    "Kundenzentrum Porz",
    "Kundenzentrum Rodenkirchen",
}
IM_FENSTER = "2026-10-05T08:05:00+02:00"  # Montag, fünf Minuten nach dem Stand der Beispieldatei


def _dt(text: str) -> datetime:
    return datetime.fromisoformat(text)


def _stub(monkeypatch, daten: bytes, jetzt: str):
    """Ersetzt Netz und Uhr; liefert die Listen der abgerufenen und der archivierten Adressen."""
    abrufe: list = []
    archiviert: list = []

    def fetch_feed(url=messen.FEED_URL, *args, **kwargs):
        abrufe.append(url)
        return daten

    def trigger_wayback(url=messen.FEED_URL, *args, **kwargs):
        archiviert.append(url)
        return "https://web.archive.org/web/20261005060500/" + url

    monkeypatch.setattr(messen, "fetch_feed", fetch_feed)
    monkeypatch.setattr(messen, "trigger_wayback", trigger_wayback)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt(jetzt))
    return abrufe, archiviert


def _zeilen(pfad: Path) -> list[dict]:
    with pfad.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_parse_anzeige_liefert_die_neun_kundenzentren_in_feed_schreibweise():
    # Act
    kopf, records = messen.parse_anzeige(BEISPIEL.read_bytes())

    # Assert
    assert kopf == {"stand_iso": "2026-10-05T08:00:04+02:00", "status": 1}
    assert {r["kundenzentrum"] for r in records} == NAMEN_IM_FEED
    assert len(records) == 9  # die acht Führerscheinstellen zählen nicht mit


def test_parse_anzeige_nimmt_die_wartezeit_der_kundenzentren_nicht_der_fuehrerscheinstellen():
    # Act
    _, records = messen.parse_anzeige(BEISPIEL.read_bytes())

    # Assert: Rodenkirchen steht in beiden Bereichen (Kundenzentrum 94, Führerscheinstelle 0)
    werte = {r["kundenzentrum"]: r["wartezeit_minuten"] for r in records}
    assert werte["Kundenzentrum Rodenkirchen"] == 94
    assert werte["Kundenzentrum Ehrenfeld"] == 19


def test_parse_anzeige_laesst_unlesbare_wartezeit_als_rohwert_stehen():
    # Arrange
    payload = {
        "stand_iso": "2026-10-05T08:00:04+02:00",
        "status": 1,
        "bereiche": [
            {
                "id": "meldeangelegenheiten",
                "gruppen": [{"id": "x", "eintraege": [{"name": " Kalk ", "wartezeit": None}]}],
            }
        ],
    }

    # Act
    _, records = messen.parse_anzeige(json.dumps(payload).encode("utf-8"))

    # Assert
    assert records == [{"kundenzentrum": "Kundenzentrum Kalk", "wartezeit_minuten": None}]


def test_anzeige_frisch_nur_mit_stand_von_heute():
    jetzt = _dt(IM_FENSTER)

    assert messen.anzeige_frisch("2026-10-05T08:00:04+02:00", jetzt)
    assert messen.anzeige_frisch("2026-10-05T06:00:04+00:00", jetzt)  # derselbe Augenblick in UTC
    assert not messen.anzeige_frisch("2026-10-04T08:00:04+02:00", jetzt)  # gestern
    assert not messen.anzeige_frisch("2026-10-05T09:00:00+02:00", jetzt)  # Zukunft
    assert not messen.anzeige_frisch("2026-10-05T08:00:04", jetzt)  # ohne Zeitzone
    assert not messen.anzeige_frisch("08:00", jetzt)
    assert not messen.anzeige_frisch("", jetzt)


def test_main_anzeige_schreibt_in_eigene_datei_mit_quelle_und_stand(tmp_path, monkeypatch):
    # Arrange
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    feed_csv = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    monkeypatch.setattr(messen, "CSV_PATH", feed_csv)
    abrufe, archiviert = _stub(monkeypatch, BEISPIEL.read_bytes(), IM_FENSTER)

    # Act
    code = messen.main(["--quelle", "anzeige"])

    # Assert
    assert code == 0
    assert abrufe == [messen.ANZEIGE_URL]
    assert archiviert == [messen.ANZEIGE_URL]
    assert not feed_csv.exists()
    zeilen = _zeilen(anzeige_csv)
    assert len(zeilen) == 9
    assert list(zeilen[0]) == messen.ANZEIGE_HEADER
    assert {z["quelle"] for z in zeilen} == {"anzeige"}
    assert {z["stand_iso"] for z in zeilen} == {"2026-10-05T08:00:04+02:00"}
    assert {z["abgerufen_am"] for z in zeilen} == {IM_FENSTER}
    assert all(z["wayback_url"].endswith(messen.ANZEIGE_URL) for z in zeilen)


def test_main_anzeige_legt_die_rohdatei_byte_gleich_ab_und_traegt_den_hash_ein(
    tmp_path, monkeypatch
):
    # Arrange
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    rohdaten = BEISPIEL.read_bytes()
    _stub(monkeypatch, rohdaten, IM_FENSTER)

    # Act
    messen.main(["--quelle", "anzeige"])

    # Assert
    sha = hashlib.sha256(rohdaten).hexdigest()
    belege = list((tmp_path / messen.ANZEIGE_BELEG_ORDNER).iterdir())
    assert [b.name for b in belege] == [f"wartezeiten-20261005-080500-{sha[:8]}.json"]
    assert belege[0].read_bytes() == rohdaten
    assert {z["beleg_sha256"] for z in _zeilen(anzeige_csv)} == {sha}


def test_sichere_beleg_liefert_den_hash_auch_wenn_die_kopie_nicht_schreibbar_ist(tmp_path, capsys):
    # Arrange: der Zielordner ist eine Datei, mkdir scheitert
    blockiert = tmp_path / "belege-anzeige"
    blockiert.write_text("keine Mappe", encoding="utf-8")

    # Act
    sha = messen.sichere_beleg(b"{}", blockiert, _dt(IM_FENSTER))

    # Assert
    assert sha == hashlib.sha256(b"{}").hexdigest()
    assert "Belegkopie nicht geschrieben" in capsys.readouterr().err


def test_main_anzeige_schreibt_nie_in_eine_feed_datei(tmp_path, monkeypatch, capsys):
    # Arrange: eine Datei mit der Kopfzeile des Feeds, wie messwerte.csv
    feed_csv = tmp_path / "messwerte.csv"
    messen.append_csv(feed_csv, [["2026-09-08T16:50:40+02:00", "Kundenzentrum Kalk", 5, "x", ""]])
    vorher = feed_csv.read_bytes()
    abrufe, _ = _stub(monkeypatch, BEISPIEL.read_bytes(), IM_FENSTER)

    # Act
    code = messen.main(["--quelle", "anzeige", "--csv", str(feed_csv)])

    # Assert
    assert code == 1
    assert abrufe == []
    assert feed_csv.read_bytes() == vorher
    assert "keine Anzeige-Datei" in capsys.readouterr().err


def test_main_anzeige_legt_keine_datei_ohne_anzeige_im_namen_an(tmp_path, monkeypatch, capsys):
    # Arrange: messwerte.csv fehlt noch — die Kopfzeile kann die Sperre hier nicht auslösen
    feed_csv = tmp_path / "messwerte.csv"
    abrufe, _ = _stub(monkeypatch, BEISPIEL.read_bytes(), IM_FENSTER)

    # Act
    code = messen.main(["--quelle", "anzeige", "--erzwingen", "--csv", str(feed_csv)])

    # Assert
    assert code == 1
    assert abrufe == []
    assert not feed_csv.exists()
    assert "keine Anzeige-Datei" in capsys.readouterr().err


def test_main_feed_schreibt_nie_in_eine_anzeige_datei(tmp_path, monkeypatch, capsys):
    # Arrange
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    messen.append_csv(anzeige_csv, [["x"] * len(messen.ANZEIGE_HEADER)], messen.ANZEIGE_HEADER)
    vorher = anzeige_csv.read_bytes()
    abrufe, _ = _stub(monkeypatch, b"{}", IM_FENSTER)

    # Act
    code = messen.main(["--csv", str(anzeige_csv)])

    # Assert
    assert code == 1
    assert abrufe == []
    assert anzeige_csv.read_bytes() == vorher
    assert "keine Feed-Datei" in capsys.readouterr().err


def test_main_anzeige_unbrauchbare_antwort_gibt_exit_code_1_statt_absturz(tmp_path, monkeypatch):
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)

    for daten in (b"[]", b"<html>", b'{"bereiche": null}', b"\xff\xfe", b"[" * 100_000):
        _stub(monkeypatch, daten, IM_FENSTER)
        assert messen.main(["--quelle", "anzeige"]) == 1
    assert not anzeige_csv.exists()


def test_parse_anzeige_liest_auch_mit_bom():
    kopf, records = messen.parse_anzeige(b"\xef\xbb\xbf" + BEISPIEL.read_bytes())

    assert kopf["stand_iso"] == "2026-10-05T08:00:04+02:00"
    assert len(records) == 9


def test_main_anzeige_veralteter_stand_schreibt_nichts_und_sichert_den_beleg(
    tmp_path, monkeypatch, capsys
):
    # Arrange: die Beispieldatei vom Montag, abgerufen am Mittwoch darauf
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    _, archiviert = _stub(monkeypatch, BEISPIEL.read_bytes(), "2026-10-07T08:05:00+02:00")

    # Act
    code = messen.main(["--quelle", "anzeige"])

    # Assert
    assert code == 1
    assert not anzeige_csv.exists()
    assert archiviert == [messen.ANZEIGE_URL]
    assert "veraltet" in capsys.readouterr().err


def test_main_anzeige_ausserhalb_des_fensters_misst_nicht(tmp_path, monkeypatch, capsys):
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    abrufe, _ = _stub(monkeypatch, BEISPIEL.read_bytes(), "2026-10-06T08:05:00+02:00")  # Dienstag

    assert messen.main(["--quelle", "anzeige"]) == 0
    assert abrufe == []
    assert not anzeige_csv.exists()
    assert "Messfenster" in capsys.readouterr().out


def test_main_anzeige_zweiter_lauf_im_selben_slot_schreibt_nichts(tmp_path, monkeypatch, capsys):
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    _stub(monkeypatch, BEISPIEL.read_bytes(), IM_FENSTER)
    assert messen.main(["--quelle", "anzeige"]) == 0

    abrufe, _ = _stub(monkeypatch, BEISPIEL.read_bytes(), "2026-10-05T08:40:00+02:00")
    assert messen.main(["--quelle", "anzeige"]) == 0

    assert abrufe == []
    assert "bereits gemessen" in capsys.readouterr().out
    assert len(_zeilen(anzeige_csv)) == 9


def test_main_anzeige_ohne_bereich_meldeangelegenheiten_gibt_exit_code_1(
    tmp_path, monkeypatch, capsys
):
    # Arrange: Aufbau geändert, nur noch die Führerscheinstellen
    payload = json.loads(BEISPIEL.read_text(encoding="utf-8"))
    payload["bereiche"] = [b for b in payload["bereiche"] if b["id"] != "meldeangelegenheiten"]
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    _stub(monkeypatch, json.dumps(payload).encode("utf-8"), IM_FENSTER)

    # Act
    code = messen.main(["--quelle", "anzeige"])

    # Assert
    assert code == 1
    assert not anzeige_csv.exists()
    assert "meldeangelegenheiten" in capsys.readouterr().err


def test_main_ohne_quelle_misst_weiter_den_feed(tmp_path, monkeypatch):
    # Arrange: der Standardweg darf sich durch die zweite Quelle nicht ändern
    feed_csv = tmp_path / "messwerte.csv"
    anzeige_csv = tmp_path / "messwerte-anzeige.csv"
    monkeypatch.setattr(messen, "CSV_PATH", feed_csv)
    monkeypatch.setattr(messen, "ANZEIGE_CSV_PATH", anzeige_csv)
    feed = {
        "items": [
            {
                "title_anz": "Kundenzentrum Kalk",
                "timestamp": "2026-10-05 08:00:02",
                "wartezeit_minuten": "28",
            }
        ]
    }
    abrufe, _ = _stub(monkeypatch, json.dumps(feed).encode("utf-8"), IM_FENSTER)

    # Act
    code = messen.main([])

    # Assert
    assert code == 0
    assert abrufe == [messen.FEED_URL]
    assert not anzeige_csv.exists()
    assert list(_zeilen(feed_csv)[0]) == messen.CSV_HEADER
