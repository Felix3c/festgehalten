"""Tests für waechter.py — ohne Netzzugriff.

Aufruf: python -m pytest recherche/koeln-wartezeit -q
"""
import csv

import messen
import waechter


def _schreibe(csv_path, header, zeitpunkte):
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for z in zeitpunkte:
            writer.writerow([z] + [""] * (len(header) - 1))


def test_waechter_zaehlt_die_angegebene_datei(tmp_path, monkeypatch, capsys):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige-github.csv"
    _schreibe(csv_path, messen.ANZEIGE_HEADER, ["2026-10-07T10:00:00+02:00"] * 9)
    monkeypatch.setenv("WAECHTER_DATUM", "2026-10-07")

    # Act
    exit_code = waechter.main(["--csv", str(csv_path)])

    # Assert
    assert exit_code == 0
    assert "messwerte-anzeige-github.csv" in capsys.readouterr().out


def test_waechter_meldet_fehlenden_abruf(tmp_path, monkeypatch, capsys):
    # Arrange: nur ein Abruf, erwartet zwei
    csv_path = tmp_path / "messwerte-anzeige-github.csv"
    _schreibe(csv_path, messen.ANZEIGE_HEADER, ["2026-10-05T10:00:00+02:00"])
    monkeypatch.setenv("WAECHTER_DATUM", "2026-10-05")

    # Act
    exit_code = waechter.main(["--csv", str(csv_path), "--erwartet", "2"])

    # Assert
    assert exit_code == 1
    assert "FEHLT" in capsys.readouterr().err


def test_waechter_fehlende_datei_ist_ein_fehler(tmp_path, capsys):
    # Act
    exit_code = waechter.main(["--csv", str(tmp_path / "gibt-es-nicht.csv")])

    # Assert
    assert exit_code == 1
    assert "existiert nicht" in capsys.readouterr().err
