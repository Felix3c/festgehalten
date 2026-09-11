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
