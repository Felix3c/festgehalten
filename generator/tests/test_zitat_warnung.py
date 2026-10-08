"""Warnung „Zitat nicht wörtlich“ (Beschluss Frage 61, 04.10.2026).

Der Generator ruft keine Quellen ab. Welche Zitate nicht wörtlich in Quelle oder Archiv stehen,
liefert die Prüfliste von werkzeuge/archivsicherung.py (Status zitat_fehlt). Gewarnt wird, solange
die Wette keinen Vermerk „Zitat nicht wörtlich …“ trägt. Die Warnung bricht den Bau nicht ab.
"""
from pathlib import Path

from wettbuch import cli, lesen, pruefen

CSV_KOPF = "id,quelle,archiv,status,zitat_live,fehlt,geprueft_am\n"


def _csv(tmp_path: Path, zeilen: list[str]) -> Path:
    p = tmp_path / "archiv-quellen.csv"
    p.write_text(CSV_KOPF + "".join(z + "\n" for z in zeilen), encoding="utf-8")
    return p


def test_liste_liest_nur_zitat_fehlt(tmp_path: Path):
    p = _csv(tmp_path, [
        "a-1,https://x,,zitat_fehlt,nein,wort,2026-10-04",
        "a-2,https://x,https://web.archive.org/web/1/x,ok,ja,,2026-10-04",
        "a-3,https://x,,kein_archiv,ja,,2026-10-04",
    ])
    assert pruefen.nicht_woertlich_lesen(p) == {"a-1"}


def test_warnung_ohne_vermerk(buch: Path):
    b = lesen.buch_lesen(buch)
    w = pruefen.zitat_warnungen(b, {"test-2025-001"})
    assert [(x.datei, x.feld) for x in w] == [("test-2025-001.md", "zitat")]
    assert "nicht wörtlich" in w[0].text


def test_keine_warnung_mit_vermerk(buch: Path):
    b = lesen.buch_lesen(buch)
    b["wetten"][0]["vermerke"] = [
        {"am": "2026-10-08", "text": "Zitat nicht wörtlich; Wortlaut der Quelle: »Das Haus wird Ende Oktober fertig gestellt.«"},
    ]
    assert pruefen.zitat_warnungen(b, {"test-2025-001"}) == []


def test_keine_warnung_wenn_nicht_gelistet(buch: Path):
    assert pruefen.zitat_warnungen(lesen.buch_lesen(buch), {"andere-1"}) == []


def test_anderer_vermerk_reicht_nicht(buch: Path):
    b = lesen.buch_lesen(buch)
    b["wetten"][0]["vermerke"] = [{"am": "2026-10-08", "text": "Archiv: https://web.archive.org/…"}]
    assert len(pruefen.zitat_warnungen(b, {"test-2025-001"})) == 1


def test_cli_warnt_und_baut_trotzdem(buch: Path, tmp_path: Path, capsys):
    p = _csv(tmp_path, ["test-2025-001,https://x,,zitat_fehlt,nein,haus,2026-10-04"])
    rc = cli.main(["bauen", str(buch), str(tmp_path / "site"), "--pruefen", "--zitate", str(p)])
    assert rc == 0
    io = capsys.readouterr()
    assert "Warnung" in io.err and "test-2025-001.md: zitat" in io.err
    assert "1 Warnung" in io.err


def test_cli_alle_warnt(buch: Path, tmp_path: Path, capsys):
    ordner = tmp_path / "buecher"
    ziel = ordner / "test" / "wetten"
    ziel.mkdir(parents=True)
    (ordner / "test" / "BUCH.md").write_bytes((buch / "BUCH.md").read_bytes())
    (ziel / "test-2025-001.md").write_bytes((buch / "wetten" / "test-2025-001.md").read_bytes())
    p = _csv(tmp_path, ["test-2025-001,https://x,,zitat_fehlt,nein,haus,2026-10-04"])
    rc = cli.main(["alle", str(ordner), str(tmp_path / "site"), "--pruefen", "--zitate", str(p)])
    assert rc == 0
    assert "test/test-2025-001.md: zitat" in capsys.readouterr().err


def test_cli_ohne_zitate_keine_warnung(buch: Path, tmp_path: Path, capsys):
    rc = cli.main(["bauen", str(buch), str(tmp_path / "site"), "--pruefen"])
    assert rc == 0
    assert "Warnung" not in capsys.readouterr().err
