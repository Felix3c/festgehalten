"""Tests für messen.py und auswerten.py — ohne Netzzugriff.

Aufruf: python -m pytest recherche/koeln-wartezeit -q
"""
import csv
import json
from pathlib import Path

import auswerten
import messen

BEISPIEL_FEED = {
    "success": True,
    "items": [
        {
            "title_anz": "Kundenzentrum Chorweiler",
            "timestamp": "2026-10-05 09:00:02",
            "link": "http://www.stadt-koeln.de/service/adressen/00179/index.html",
            "status": "1",
            "sondertext": "",
            "wartezeit_minuten": "15",
        },
        {
            "title_anz": "Kundenzentrum Innenstadt",
            "timestamp": "2026-10-05 09:00:03",
            "link": "http://www.stadt-koeln.de/service/adressen/00183/index.html",
            "status": "1",
            "sondertext": "",
            "wartezeit_minuten": "25",
        },
        {
            "title_anz": "Kundenzentrum Ehrenfeld ",
            "timestamp": "2026-10-05 09:00:04",
            "link": "http://www.stadt-koeln.de/service/adressen/00180/index.html",
            "status": "3",
            "sondertext": "nur mit Terminvereinbarung",
            "wartezeit_minuten": "0",
        },
        {
            "title_anz": "Kfz-Zulassungsstelle",
            "timestamp": "2022-03-27 03:05:02",
            "link": "http://www.stadt-koeln.de/service/adressen/00205/index.html",
            "status": "2",
            "sondertext": "",
            "wartezeit_minuten": "5",
        },
    ],
}


def test_parse_feed_extrahiert_nur_kundenzentren():
    # Arrange
    data = json.dumps(BEISPIEL_FEED).encode("utf-8")

    # Act
    records = messen.parse_feed(data)

    # Assert
    namen = [r["kundenzentrum"] for r in records]
    assert namen == ["Kundenzentrum Chorweiler", "Kundenzentrum Innenstadt", "Kundenzentrum Ehrenfeld"]
    assert "Kfz-Zulassungsstelle" not in namen


def test_parse_feed_wandelt_wartezeit_in_int():
    # Arrange
    data = json.dumps(BEISPIEL_FEED).encode("utf-8")

    # Act
    records = messen.parse_feed(data)

    # Assert
    assert records[0]["wartezeit_minuten"] == 15
    assert records[1]["wartezeit_minuten"] == 25
    assert records[0]["feed_timestamp"] == "2026-10-05 09:00:02"


def test_parse_feed_leere_items_liste():
    # Arrange
    data = json.dumps({"success": True, "items": []}).encode("utf-8")

    # Act
    records = messen.parse_feed(data)

    # Assert
    assert records == []


def test_build_rows_haengt_wayback_url_an():
    # Arrange
    records = [{"kundenzentrum": "Kundenzentrum Kalk", "wartezeit_minuten": 10, "feed_timestamp": "t"}]

    # Act
    rows = messen.build_rows(records, "2026-10-05T09:00:00+02:00", "https://web.archive.org/web/x/y")

    # Assert
    assert rows == [
        ["2026-10-05T09:00:00+02:00", "Kundenzentrum Kalk", 10, "t", "https://web.archive.org/web/x/y"]
    ]


def test_build_rows_leere_wayback_url_wird_leerstring():
    # Arrange
    records = [{"kundenzentrum": "Kundenzentrum Kalk", "wartezeit_minuten": 10, "feed_timestamp": "t"}]

    # Act
    rows = messen.build_rows(records, "2026-10-05T09:00:00+02:00", None)

    # Assert
    assert rows[0][4] == ""


def test_append_csv_schreibt_header_nur_einmal(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    rows_1 = [["2026-10-05T09:00:00+02:00", "Kundenzentrum Kalk", 10, "t", ""]]
    rows_2 = [["2026-10-08T09:00:00+02:00", "Kundenzentrum Kalk", 12, "t2", ""]]

    # Act
    messen.append_csv(csv_path, rows_1)
    messen.append_csv(csv_path, rows_2)

    # Assert
    with csv_path.open(encoding="utf-8") as f:
        zeilen = list(csv.reader(f))
    assert zeilen[0] == messen.CSV_HEADER
    assert len(zeilen) == 3


def _schreibe_beispiel_csv(pfad: Path) -> None:
    with pfad.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(messen.CSV_HEADER)
        writer.writerow(["2026-10-05T09:00:00+02:00", "Kundenzentrum Chorweiler", "10", "t1", "wb1"])
        writer.writerow(["2026-10-05T09:00:00+02:00", "Kundenzentrum Innenstadt", "20", "t2", "wb1"])
        writer.writerow(["2026-10-07T09:00:00+02:00", "Kundenzentrum Chorweiler", "30", "t3", "wb2"])
        writer.writerow(["2026-10-07T09:00:00+02:00", "Kundenzentrum Innenstadt", "40", "t4", "wb2"])
        writer.writerow(["2026-11-04T09:00:00+02:00", "Kundenzentrum Chorweiler", "5", "t5", "wb3"])


def test_read_rows_liest_csv(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)

    # Act
    rows = auswerten.read_rows(csv_path)

    # Assert
    assert len(rows) == 5
    assert rows[0]["kundenzentrum"] == "Kundenzentrum Chorweiler"


def test_read_rows_fehlende_datei_gibt_leere_liste(tmp_path):
    # Arrange
    csv_path = tmp_path / "nicht-vorhanden.csv"

    # Act
    rows = auswerten.read_rows(csv_path)

    # Assert
    assert rows == []


def test_compute_monthly_stats_mittelwert_und_maximum(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)
    rows = auswerten.read_rows(csv_path)

    # Act
    stats = auswerten.compute_monthly_stats(rows)

    # Assert
    okt = stats["2026-10"]
    assert okt["zentren"]["Kundenzentrum Chorweiler"]["werte"] == [10.0, 30.0]
    assert okt["zentren"]["Kundenzentrum Innenstadt"]["werte"] == [20.0, 40.0]
    assert okt["gesamt"]["werte"] == [10.0, 20.0, 30.0, 40.0]
    assert okt["messtage"] == 2
    nov = stats["2026-11"]
    assert nov["gesamt"]["werte"] == [5.0]
    assert nov["messtage"] == 1


def test_compute_monthly_stats_filtert_nach_monat(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)
    rows = auswerten.read_rows(csv_path)

    # Act
    stats = auswerten.compute_monthly_stats(rows, monat="2026-11")

    # Assert
    assert list(stats.keys()) == ["2026-11"]


def test_format_table_enthaelt_gesamtzeile(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)
    rows = auswerten.read_rows(csv_path)
    stats = auswerten.compute_monthly_stats(rows)

    # Act
    text = auswerten.format_table(stats)

    # Assert
    assert "GESAMT (alle Zentren)" in text
    assert "2026-10" in text
    assert "2026-11" in text


def test_format_table_ohne_messwerte():
    # Arrange
    stats = {}

    # Act
    text = auswerten.format_table(stats)

    # Assert
    assert "Keine Messwerte" in text


def test_main_ohne_datei_gibt_exit_code_1(tmp_path, capsys):
    # Arrange
    csv_path = tmp_path / "nicht-vorhanden.csv"

    # Act
    exit_code = auswerten.main(["--csv", str(csv_path)])

    # Assert
    assert exit_code == 1


def test_main_mit_unbekanntem_monat_gibt_exit_code_1(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)

    # Act
    exit_code = auswerten.main(["--csv", str(csv_path), "--monat", "2027-01"])

    # Assert
    assert exit_code == 1


def test_main_mit_bekanntem_monat_gibt_exit_code_0(tmp_path, capsys):
    # Arrange
    csv_path = tmp_path / "messwerte.csv"
    _schreibe_beispiel_csv(csv_path)

    # Act
    exit_code = auswerten.main(["--csv", str(csv_path), "--monat", "2026-10"])
    out = capsys.readouterr().out

    # Assert
    assert exit_code == 0
    assert "2026-10" in out
    assert "2026-11" not in out


# --- waechter.py ---------------------------------------------------------

WAECHTER_CSV = (
    "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"
    "2026-09-11T20:02:38+02:00,Kundenzentrum Nippes,0,2026-09-11 11:25:03,\n"
    "2026-09-11T20:02:38+02:00,Kundenzentrum Porz,0,2026-09-10 14:55:08,\n"
    "2026-09-14T10:07:00+02:00,Kundenzentrum Nippes,12,2026-09-14 10:05:00,\n"
    "2026-09-14T13:37:00+02:00,Kundenzentrum Nippes,8,2026-09-14 13:35:00,\n"
)


def test_waechter_zaehlt_abrufzeitpunkte_je_tag(tmp_path):
    import waechter

    csv_datei = tmp_path / "messwerte.csv"
    csv_datei.write_text(WAECHTER_CSV, encoding="utf-8")

    # Ein Messlauf = ein Zeitpunkt, egal wie viele Kundenzentren-Zeilen
    assert waechter.abrufe_am(csv_datei, "2026-09-11") == ["2026-09-11T20:02:38+02:00"]
    assert len(waechter.abrufe_am(csv_datei, "2026-09-14")) == 2
    assert waechter.abrufe_am(csv_datei, "2026-09-15") == []


def test_waechter_exit_code_haengt_an_erwarteter_zahl(tmp_path, monkeypatch):
    import sys

    import waechter

    csv_datei = tmp_path / "messwerte.csv"
    csv_datei.write_text(WAECHTER_CSV, encoding="utf-8")
    monkeypatch.setattr(waechter, "CSV_PATH", csv_datei)

    monkeypatch.setenv("WAECHTER_DATUM", "2026-09-14")
    monkeypatch.setattr(sys, "argv", ["waechter.py", "--erwartet", "2"])
    assert waechter.main() == 0

    monkeypatch.setattr(sys, "argv", ["waechter.py", "--erwartet", "3"])
    assert waechter.main() == 1

    monkeypatch.setenv("WAECHTER_DATUM", "2026-09-15")
    monkeypatch.setattr(sys, "argv", ["waechter.py"])
    assert waechter.main() == 1


# --- Messfenster und Slot-Schutz (seit 16.09.2026) -----------------------
# Hintergrund: GitHub startete den Zeitplan am Mi 16.09. erst um 15:27 MESZ,
# also nach Schließung der Kundenzentren (Mi 7:30–12:00). Die Wetten
# koeln-2026-077 ff. zählen nur Abrufe in den terminfreien Zeiten.

from datetime import datetime, timezone

import fenster


def _dt(text: str) -> datetime:
    return datetime.fromisoformat(text)


def test_im_messfenster_montag_und_mittwoch():
    assert fenster.im_messfenster(_dt("2026-10-05T10:07:00+02:00"))  # Mo Vormittag
    assert fenster.im_messfenster(_dt("2026-10-05T13:37:00+02:00"))  # Mo Nachmittag
    assert fenster.im_messfenster(_dt("2026-10-07T11:59:00+02:00"))  # Mi kurz vor Schluss
    assert not fenster.im_messfenster(_dt("2026-10-05T15:00:00+02:00"))  # Mo Schluss
    assert not fenster.im_messfenster(_dt("2026-10-05T07:29:00+02:00"))  # Mo vor Öffnung
    assert not fenster.im_messfenster(_dt("2026-09-16T15:27:49+02:00"))  # der Fall vom 16.09.
    assert not fenster.im_messfenster(_dt("2026-10-06T10:00:00+02:00"))  # Dienstag


def test_im_messfenster_rechnet_in_ortszeit():
    # 13:27 UTC am Mi 16.09. ist 15:27 MESZ: außerhalb
    assert not fenster.im_messfenster(datetime(2026, 9, 16, 13, 27, tzinfo=timezone.utc))
    # 06:35 UTC am Mi 04.11. ist 07:35 MEZ: innerhalb
    assert fenster.im_messfenster(datetime(2026, 11, 4, 6, 35, tzinfo=timezone.utc))


def test_slot_vormittag_nachmittag_oder_keiner():
    assert fenster.slot(_dt("2026-10-05T10:07:00+02:00")) == "vormittag"
    assert fenster.slot(_dt("2026-10-05T13:37:00+02:00")) == "nachmittag"
    assert fenster.slot(_dt("2026-10-07T10:07:00+02:00")) == "vormittag"
    assert fenster.slot(_dt("2026-10-07T15:27:00+02:00")) is None


def test_schon_gemessen_erkennt_gleichen_slot(tmp_path):
    csv_path = tmp_path / "messwerte.csv"
    csv_path.write_text(
        "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"
        "2026-10-05T10:07:00+02:00,Kundenzentrum Nippes,12,t,\n"
        "2026-10-05T10:07:00+02:00,Kundenzentrum Porz,8,t,\n",
        encoding="utf-8",
    )
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T10:40:00+02:00")) == "2026-10-05T10:07:00+02:00"
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T13:37:00+02:00")) is None
    # Nachmittag: zweiter Abruf erst 60 Minuten nach dem letzten
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T12:30:00+02:00"), "nachmittag") is None
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T11:00:00+02:00"), "nachmittag") == "2026-10-05T10:07:00+02:00"
    assert messen.schon_gemessen(csv_path, _dt("2026-10-07T10:07:00+02:00")) is None
    assert messen.schon_gemessen(tmp_path / "fehlt.csv", _dt("2026-10-05T10:40:00+02:00")) is None


def _feed_stub(monkeypatch, aufrufe: list):
    def fetch_feed(*args, **kwargs):
        aufrufe.append(1)
        return json.dumps(BEISPIEL_FEED).encode("utf-8")

    monkeypatch.setattr(messen, "fetch_feed", fetch_feed)
    monkeypatch.setattr(messen, "trigger_wayback", lambda *a, **k: None)


def test_main_ausserhalb_des_fensters_misst_nicht(tmp_path, monkeypatch, capsys):
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-09-16T15:27:49+02:00"))
    aufrufe: list = []
    _feed_stub(monkeypatch, aufrufe)

    assert messen.main([]) == 0
    assert aufrufe == []
    assert not csv_path.exists()
    assert "Messfenster" in capsys.readouterr().out


def test_main_erzwingen_misst_auch_ausserhalb(tmp_path, monkeypatch):
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-09-16T15:27:49+02:00"))
    _feed_stub(monkeypatch, [])

    assert messen.main(["--erzwingen"]) == 0
    with csv_path.open(encoding="utf-8") as f:
        assert len(list(csv.reader(f))) == 4  # Header + 3 Kundenzentren


def test_main_zweiter_lauf_im_selben_slot_schreibt_nichts(tmp_path, monkeypatch, capsys):
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    _feed_stub(monkeypatch, [])
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T10:07:00+02:00"))
    assert messen.main([]) == 0

    aufrufe: list = []
    _feed_stub(monkeypatch, aufrufe)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T10:51:00+02:00"))
    assert messen.main([]) == 0
    assert aufrufe == []
    assert "bereits gemessen" in capsys.readouterr().out
    with csv_path.open(encoding="utf-8") as f:
        assert len(list(csv.reader(f))) == 4

    # Nachmittag ist ein eigener Slot
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T13:37:00+02:00"))
    assert messen.main([]) == 0
    with csv_path.open(encoding="utf-8") as f:
        assert len(list(csv.reader(f))) == 7


def test_compute_monthly_stats_ignoriert_abrufe_ausserhalb_des_fensters(tmp_path):
    csv_path = tmp_path / "messwerte.csv"
    csv_path.write_text(
        "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"
        "2026-10-05T10:07:00+02:00,Kundenzentrum Nippes,10,t,\n"
        "2026-10-06T10:07:00+02:00,Kundenzentrum Nippes,90,t,\n"   # Dienstag
        "2026-10-07T15:27:00+02:00,Kundenzentrum Nippes,90,t,\n"   # Mi nach Schluss
        "2026-10-07T10:07:00+02:00,Kundenzentrum Nippes,20,t,\n",
        encoding="utf-8",
    )
    rows = auswerten.read_rows(csv_path)

    stats = auswerten.compute_monthly_stats(rows)
    assert stats["2026-10"]["gesamt"]["werte"] == [10.0, 20.0]
    assert stats["2026-10"]["messtage"] == 2
    assert stats["2026-10"]["ausgeschlossen"] == 2

    alle = auswerten.compute_monthly_stats(rows, alle=True)
    assert alle["2026-10"]["gesamt"]["werte"] == [10.0, 90.0, 90.0, 20.0]


# --- nach Review 16.09.: Slot nach geplantem Lauf, kaputte Zeitstempel ----------

def test_slot_aus_cron_vormittag_oder_nachmittag():
    assert fenster.slot_aus_cron("37 6 * * 1,3") == "vormittag"
    assert fenster.slot_aus_cron("27 9 * * 1,3") == "vormittag"
    assert fenster.slot_aus_cron("17 11 * * 1") == "nachmittag"
    assert fenster.slot_aus_cron("13 12 * * 1") == "nachmittag"
    assert fenster.slot_aus_cron("") is None
    assert fenster.slot_aus_cron("kaputt") is None


def test_schon_gemessen_ueberlebt_zeitstempel_ohne_offset(tmp_path):
    csv_path = tmp_path / "messwerte.csv"
    csv_path.write_text(
        "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"
        "2026-10-05T10:07:00,Kundenzentrum Nippes,12,t,\n"
        "kaputt,Kundenzentrum Porz,8,t,\n"
        "2026-10-05T10:09:00+02:00,Kundenzentrum Porz,8,t,\n",
        encoding="utf-8",
    )
    # naive und kaputte Zeilen werden übersprungen, die gültige zählt
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T10:40:00+02:00")) == "2026-10-05T10:09:00+02:00"


def test_verspaeteter_vormittagslauf_belegt_nicht_den_nachmittag(tmp_path, monkeypatch, capsys):
    """Montag: der 09:27-UTC-Lauf startet erst 12:07 MESZ. Mit KOELN_CRON gilt er als
    Vormittagslauf und belegt den Vormittags-Slot; der echte Nachmittagslauf um 13:17
    schreibt danach seine eigene Zeile."""
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    _feed_stub(monkeypatch, [])

    monkeypatch.setenv("KOELN_CRON", "27 9 * * 1,3")
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T12:07:00+02:00"))
    assert messen.main([]) == 0
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T10:00:00+02:00"), "vormittag")
    assert messen.schon_gemessen(csv_path, _dt("2026-10-05T13:17:00+02:00"), "nachmittag") is None

    # ein zweiter, noch spaeterer Vormittagslauf schreibt nichts
    aufrufe: list = []
    _feed_stub(monkeypatch, aufrufe)
    monkeypatch.setenv("KOELN_CRON", "51 8 * * 1,3")
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T12:30:00+02:00"))
    assert messen.main([]) == 0
    assert aufrufe == []

    monkeypatch.setenv("KOELN_CRON", "17 11 * * 1")
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T13:17:00+02:00"))
    assert messen.main([]) == 0
    with csv_path.open(encoding="utf-8") as f:
        assert len(list(csv.reader(f))) == 7  # Header + 2 Abrufe x 3 Zentren


def test_main_monat_ohne_abrufe_im_fenster_gibt_exit_code_1(tmp_path, capsys):
    csv_path = tmp_path / "messwerte.csv"
    csv_path.write_text(
        "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"
        "2026-09-16T15:27:49+02:00,Kundenzentrum Nippes,58,t,\n",
        encoding="utf-8",
    )
    assert auswerten.main(["--csv", str(csv_path), "--monat", "2026-09"]) == 1
    assert "Messfenster" in capsys.readouterr().err
    assert auswerten.main(["--csv", str(csv_path), "--monat", "2026-09", "--alle"]) == 0
