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


# --- Frage 453 (Felix 22.10.2026): nach Fensterschluss nur melden, Nachmittag nur vor 15:00 verlangen ---
from datetime import datetime  # noqa: E402

from fenster import ZEITZONE  # noqa: E402


def _ort(text):
    return datetime.fromisoformat(text).replace(tzinfo=ZEITZONE)


def test_montag_vor_15_uhr_verlangt_den_nachmittag():
    # Montag 14:43: Fenster offen, Nachmittag zählt → zwei Abrufe nötig, einer fehlt
    assert waechter.urteil(_ort("2026-10-19T14:43"), 1) == ("nachstossen", 2)


def test_montag_nach_15_uhr_verlangt_den_nachmittag_nicht_mehr():
    # GitHub startet den 12:43-UTC-Lauf montags oft erst gegen 17:00 → kein Fehlalarm
    assert waechter.urteil(_ort("2026-10-19T17:05"), 1) == ("ok", 1)


def test_montag_nach_15_uhr_ohne_jeden_abruf_nur_melden():
    # Fenster zu: Nachstoßen bringt nichts mehr, der Ausfall wird gemeldet, nicht rot
    assert waechter.urteil(_ort("2026-10-19T17:05"), 0) == ("melden", 1)


def test_mittwoch_nach_12_uhr_nur_melden():
    assert waechter.urteil(_ort("2026-10-21T13:30"), 0) == ("melden", 1)


def test_vormittag_fehlt_im_offenen_fenster_wird_nachgestossen():
    assert waechter.urteil(_ort("2026-10-21T11:13"), 0) == ("nachstossen", 1)


def test_main_automatisch_meldet_mit_exit_3(tmp_path, monkeypatch, capsys):
    # Arrange: Montag 17:05, kein Abruf heute
    csv_path = tmp_path / "messwerte-anzeige-github.csv"
    _schreibe(csv_path, messen.ANZEIGE_HEADER, ["2026-10-12T10:00:00+02:00"])
    monkeypatch.setenv("WAECHTER_JETZT", "2026-10-19T17:05:00+02:00")

    # Act
    exit_code = waechter.main(["--csv", str(csv_path)])

    # Assert
    assert exit_code == waechter.EXIT_MELDEN
    assert "Messfenster ist zu" in capsys.readouterr().out


def test_main_automatisch_nachmittag_vor_15_uhr_fehlt(tmp_path, monkeypatch):
    csv_path = tmp_path / "messwerte-anzeige-github.csv"
    _schreibe(csv_path, messen.ANZEIGE_HEADER, ["2026-10-19T10:00:00+02:00"] * 9)
    monkeypatch.setenv("WAECHTER_JETZT", "2026-10-19T14:43:00+02:00")

    assert waechter.main(["--csv", str(csv_path)]) == 1


def test_main_automatisch_montagabend_mit_vormittag_ist_gruen(tmp_path, monkeypatch):
    csv_path = tmp_path / "messwerte-anzeige-github.csv"
    _schreibe(csv_path, messen.ANZEIGE_HEADER, ["2026-10-19T10:00:00+02:00"] * 9)
    monkeypatch.setenv("WAECHTER_JETZT", "2026-10-19T17:05:00+02:00")

    assert waechter.main(["--csv", str(csv_path)]) == 0
