"""Tests für die Rückfallebene: messen.py --csv und nachtragen.py — ohne Netzzugriff.

Aufruf: python -m pytest recherche/koeln-wartezeit -q
"""
import csv
import json
from datetime import datetime

import messen
import nachtragen

KOPF = "abgerufen_am,kundenzentrum,wartezeit_minuten,feed_timestamp,wayback_url\n"


def _dt(text: str) -> datetime:
    return datetime.fromisoformat(text)


def _schreibe(pfad, *abrufe: str) -> None:
    """Je Abrufzeitpunkt zwei Zeilen (zwei Kundenzentren), wie messen.py sie schreibt."""
    zeilen = [KOPF]
    for zeitpunkt in abrufe:
        zeilen.append(f"{zeitpunkt},Kundenzentrum Nippes,12,t,https://web.archive.org/x\n")
        zeilen.append(f"{zeitpunkt},Kundenzentrum Porz,8,t,https://web.archive.org/x\n")
    pfad.write_text("".join(zeilen), encoding="utf-8")


def _zeilen(pfad) -> list[list[str]]:
    with pfad.open(newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def test_main_mit_csv_schreibt_in_die_angegebene_datei(tmp_path, monkeypatch):
    # Arrange
    haupt = tmp_path / "messwerte.csv"
    laptop = tmp_path / "messwerte-laptop.csv"
    monkeypatch.setattr(messen, "CSV_PATH", haupt)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T10:00:00+02:00"))
    monkeypatch.setattr(messen, "fetch_feed", lambda *a, **k: json.dumps(
        {"items": [{"title_anz": "Kundenzentrum Porz", "timestamp": "2026-10-05 09:55:00", "wartezeit_minuten": "9"}]}
    ).encode("utf-8"))
    monkeypatch.setattr(messen, "trigger_wayback", lambda *a, **k: None)

    # Act
    assert messen.main(["--csv", str(laptop)]) == 0

    # Assert
    assert not haupt.exists()
    assert len(_zeilen(laptop)) == 2


def test_nachtragen_uebernimmt_fehlenden_slot(tmp_path):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    _schreibe(haupt, "2026-10-05T10:31:00+02:00")  # Actions hat den Vormittag
    _schreibe(laptop, "2026-10-05T10:00:00+02:00", "2026-10-05T14:00:00+02:00")

    neu = nachtragen.nachtragen(haupt, laptop, schreiben=True)

    assert neu == ["2026-10-05T14:00:00+02:00"]
    assert len(_zeilen(haupt)) == 1 + 4


def test_nachtragen_ohne_schreiben_aendert_nichts(tmp_path):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    _schreibe(haupt)
    _schreibe(laptop, "2026-10-07T10:00:00+02:00")
    vorher = haupt.read_text(encoding="utf-8")

    neu = nachtragen.nachtragen(haupt, laptop, schreiben=False)

    assert neu == ["2026-10-07T10:00:00+02:00"]
    assert haupt.read_text(encoding="utf-8") == vorher


def test_nachtragen_ignoriert_abrufe_ausserhalb_des_fensters(tmp_path):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    _schreibe(haupt)
    # Mittwoch 14:00 ist nach Schließung, Dienstag nie im Fenster
    _schreibe(laptop, "2026-10-07T14:00:00+02:00", "2026-10-06T10:00:00+02:00")

    assert nachtragen.nachtragen(haupt, laptop, schreiben=True) == []
    assert len(_zeilen(haupt)) == 1


def test_nachtragen_haelt_60_minuten_abstand_zu_actions(tmp_path):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    # Verspäteter Actions-Vormittagslauf um 12:20 zählt nach Uhrzeit als Nachmittag;
    # der Laptop-Nachmittag 13:00 läge zu nah dran, der Laptop-Vormittag fehlt aber noch.
    _schreibe(haupt, "2026-10-05T12:20:00+02:00")
    _schreibe(laptop, "2026-10-05T10:00:00+02:00", "2026-10-05T13:00:00+02:00")

    assert nachtragen.nachtragen(haupt, laptop, schreiben=False) == ["2026-10-05T10:00:00+02:00"]


def test_nachtragen_zweimal_ergibt_keine_doppelzeilen(tmp_path):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    _schreibe(haupt)
    _schreibe(laptop, "2026-10-05T10:00:00+02:00")

    nachtragen.nachtragen(haupt, laptop, schreiben=True)
    assert nachtragen.nachtragen(haupt, laptop, schreiben=True) == []
    assert len(_zeilen(haupt)) == 1 + 2


def test_nachtragen_ohne_laptop_datei_gibt_leere_liste(tmp_path):
    haupt = tmp_path / "messwerte.csv"
    _schreibe(haupt)

    assert nachtragen.nachtragen(haupt, tmp_path / "fehlt.csv", schreiben=True) == []


def test_main_trocken_ist_standard(tmp_path, capsys):
    haupt, laptop = tmp_path / "messwerte.csv", tmp_path / "laptop.csv"
    _schreibe(haupt)
    _schreibe(laptop, "2026-10-05T10:00:00+02:00")

    assert nachtragen.main(["--haupt", str(haupt), "--laptop", str(laptop)]) == 0

    assert len(_zeilen(haupt)) == 1
    assert "2026-10-05T10:00:00+02:00" in capsys.readouterr().out


def _feed_mit_zeitstempel(monkeypatch, zeitstempel: str, archiv: list):
    monkeypatch.setattr(messen, "fetch_feed", lambda *a, **k: json.dumps(
        {"items": [
            {"title_anz": "Kundenzentrum Porz", "timestamp": zeitstempel, "wartezeit_minuten": "35"},
            {"title_anz": "Kfz-Zulassungsstelle", "timestamp": "2026-10-05 09:58:00", "wartezeit_minuten": "5"},
        ]}
    ).encode("utf-8"))
    monkeypatch.setattr(messen, "trigger_wayback", lambda *a, **k: archiv.append(1) or "https://web.archive.org/y")


def test_main_veralteter_feed_schreibt_nichts_und_archiviert(tmp_path, monkeypatch, capsys):
    # Feed eingefroren seit Mi 16.09.2026 07:45 (Befund 03.10.2026), Messung Mo 05.10.
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T10:00:00+02:00"))
    archiv: list = []
    _feed_mit_zeitstempel(monkeypatch, "2026-09-16 07:45:03", archiv)

    assert messen.main([]) == 1

    assert not csv_path.exists()
    assert archiv == [1]
    fehler = capsys.readouterr().err
    assert "veraltet" in fehler and "2026-09-16 07:45:03" in fehler


def test_main_frischer_feed_misst(tmp_path, monkeypatch):
    csv_path = tmp_path / "messwerte.csv"
    monkeypatch.setattr(messen, "CSV_PATH", csv_path)
    monkeypatch.setattr(messen, "_jetzt", lambda: _dt("2026-10-05T10:00:00+02:00"))
    _feed_mit_zeitstempel(monkeypatch, "2026-10-05 09:55:03", [])

    assert messen.main([]) == 0
    assert len(_zeilen(csv_path)) == 2


def test_feed_veraltet_unlesbarer_zeitstempel_gilt_als_veraltet():
    records = [{"kundenzentrum": "Kundenzentrum Porz", "wartezeit_minuten": 3, "feed_timestamp": "kaputt"}]

    assert messen.feed_veraltet(records, _dt("2026-10-05T10:00:00+02:00")) == "kaputt"


def test_feed_url_ist_https():
    # http:// liefert seit spätestens 03.10.2026 403 (vorher seit 20.09. 301 auf https)
    assert messen.FEED_URL.startswith("https://")
