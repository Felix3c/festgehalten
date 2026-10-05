"""Tests für auswerten.py an der Anzeige-Datei (messwerte-anzeige.csv) — ohne Netzzugriff.

Seit 05.10.2026 (Freigabe des Halters) wird der Monatswert der Wetten koeln-2026-077 ff. an der
Anzeige-Datei gemessen. Gezählt werden dort nur Zeilen mit Rohkopie (beleg_sha256).

Aufruf: python -m pytest recherche/koeln-wartezeit -q
"""
import csv
import hashlib

import auswerten
import messen

ROHKOPIE = b'{"stand_iso": "2026-10-07T10:00:03+02:00"}'
SHA = hashlib.sha256(ROHKOPIE).hexdigest()
MO_VORMITTAG = "2026-10-05T10:00:00+02:00"  # Montag im Messfenster
MI_VORMITTAG = "2026-10-07T10:00:00+02:00"  # Mittwoch im Messfenster


def _schreibe_anzeige_csv(csv_path, zeilen):
    """zeilen: Liste aus (abgerufen_am, kundenzentrum, minuten, beleg_sha256)."""
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(messen.ANZEIGE_HEADER)
        for abgerufen_am, zentrum, minuten, sha in zeilen:
            writer.writerow([abgerufen_am, zentrum, minuten, abgerufen_am, 1, "anzeige", "", sha])


def _lege_rohkopie(tmp_path):
    ordner = tmp_path / auswerten.BELEG_ORDNER
    ordner.mkdir()
    (ordner / "wartezeiten-20261007-100000-abcdef12.json").write_bytes(ROHKOPIE)
    return ordner


def test_zeile_ohne_beleg_wird_nicht_gemittelt_aber_ausgewiesen(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(
        csv_path,
        [
            (MO_VORMITTAG, "Kundenzentrum Kalk", 90, ""),
            (MI_VORMITTAG, "Kundenzentrum Kalk", 30, SHA),
        ],
    )
    rows = auswerten.read_rows(csv_path)

    # Act
    stats = auswerten.compute_monthly_stats(rows, belege={SHA})

    # Assert
    okt = stats["2026-10"]
    assert okt["gesamt"]["werte"] == [30.0]
    assert okt["ohne_beleg"] == 1
    assert okt["messtage"] == 1


def test_ohne_schalter_zaehlt_jede_zeile_wie_bisher(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(csv_path, [(MO_VORMITTAG, "Kundenzentrum Kalk", 90, "")])
    rows = auswerten.read_rows(csv_path)

    # Act
    stats = auswerten.compute_monthly_stats(rows)

    # Assert
    assert stats["2026-10"]["gesamt"]["werte"] == [90.0]
    assert stats["2026-10"]["ohne_beleg"] == 0


def test_format_table_nennt_zeilen_ohne_beleg(tmp_path):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(
        csv_path,
        [(MO_VORMITTAG, "Kundenzentrum Kalk", 90, ""), (MI_VORMITTAG, "Kundenzentrum Kalk", 30, SHA)],
    )
    stats = auswerten.compute_monthly_stats(auswerten.read_rows(csv_path), belege={SHA})

    # Act
    text = auswerten.format_table(stats)

    # Assert
    assert "ohne Beleg nicht gezählt: 1 Zeilen" in text


def test_main_quelle_anzeige_liest_die_anzeige_datei(tmp_path, monkeypatch, capsys):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(
        csv_path,
        [(MO_VORMITTAG, "Kundenzentrum Kalk", 90, ""), (MI_VORMITTAG, "Kundenzentrum Kalk", 30, SHA)],
    )
    _lege_rohkopie(tmp_path)
    monkeypatch.setattr(auswerten, "ANZEIGE_CSV_PATH", csv_path)

    # Act
    exit_code = auswerten.main(["--quelle", "anzeige", "--monat", "2026-10"])
    out = capsys.readouterr().out

    # Assert
    assert exit_code == 0
    assert "Quelle: anzeige" in out
    assert "30.0" in out
    assert "90.0" not in out


def test_main_quelle_anzeige_nur_zeilen_ohne_beleg_gibt_exit_code_1(tmp_path, monkeypatch, capsys):
    # Arrange
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(csv_path, [(MO_VORMITTAG, "Kundenzentrum Kalk", 90, "")])
    monkeypatch.setattr(auswerten, "ANZEIGE_CSV_PATH", csv_path)

    # Act
    exit_code = auswerten.main(["--quelle", "anzeige", "--monat", "2026-10"])
    err = capsys.readouterr().err

    # Assert
    assert exit_code == 1
    assert "ohne Beleg" in err


def test_main_quelle_anzeige_verweigert_feed_datei(tmp_path, capsys):
    # Arrange: Datei mit der Kopfzeile des Feeds, ohne Spalte beleg_sha256
    csv_path = tmp_path / "messwerte.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(messen.CSV_HEADER)
        writer.writerow(["2026-10-05T10:00:00+02:00"] + [""] * (len(messen.CSV_HEADER) - 1))

    # Act
    exit_code = auswerten.main(["--quelle", "anzeige", "--csv", str(csv_path)])
    err = capsys.readouterr().err

    # Assert
    assert exit_code == 1
    assert "keine Anzeige-Datei" in err


def test_hash_in_der_spalte_ohne_rohkopie_zaehlt_nicht(tmp_path, monkeypatch, capsys):
    # Arrange: Spalte gefüllt, aber keine Datei im Belegordner
    csv_path = tmp_path / "messwerte-anzeige.csv"
    _schreibe_anzeige_csv(csv_path, [(MI_VORMITTAG, "Kundenzentrum Kalk", 30, SHA)])
    monkeypatch.setattr(auswerten, "ANZEIGE_CSV_PATH", csv_path)

    # Act
    exit_code = auswerten.main(["--quelle", "anzeige", "--monat", "2026-10"])

    # Assert
    assert exit_code == 1
    assert "1 Zeilen ohne Beleg" in capsys.readouterr().err


def test_beleg_hashes_rechnet_aus_dem_inhalt_nicht_aus_dem_namen(tmp_path):
    # Arrange
    ordner = _lege_rohkopie(tmp_path)
    (ordner / f"wartezeiten-20261007-110000-{'b' * 8}.json").write_bytes(b"anderer Inhalt")

    # Act
    hashes = auswerten.beleg_hashes(ordner)

    # Assert
    assert SHA in hashes
    assert "b" * 64 not in hashes
    assert auswerten.beleg_hashes(tmp_path / "gibt-es-nicht") == set()
