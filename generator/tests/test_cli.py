from pathlib import Path
import subprocess
import sys
import types

from wettbuch import cli


def test_bauen_erzeugt_seite(buch: Path, tmp_path: Path, capsys):
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 0
    assert (aus / "index.html").exists()
    assert "1 Wette" in capsys.readouterr().out


def test_bauen_bricht_bei_fehler_ab(buch: Path, tmp_path: Path, capsys):
    p = buch / "wetten" / "test-2025-001.md"
    p.write_text(p.read_text(encoding="utf-8").replace("ausgang: null", "ausgang: 1"), encoding="utf-8")
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 1
    assert not aus.exists()
    err = capsys.readouterr().err
    assert "test-2025-001.md: beleg_ausgang" in err


def test_nur_pruefen(buch: Path, tmp_path: Path):
    rc = cli.main(["bauen", str(buch), str(tmp_path / "site"), "--pruefen"])
    assert rc == 0
    assert not (tmp_path / "site").exists()


def test_bedienfehler():
    assert cli.main([]) == 2


def test_python_m_wettbuch_laeuft(buch: Path, tmp_path: Path):
    r = subprocess.run([sys.executable, "-m", "wettbuch", "bauen", str(buch), str(tmp_path / "s")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_slug_kollision_bricht_sauber_ab(buch: Path, tmp_path: Path, capsys):
    src = (buch / "wetten" / "test-2025-001.md").read_text(encoding="utf-8")
    zweite = src.replace("id: test-2025-001", "id: test-2025-002").replace("institution: Stadt Test", "institution: Stadt-Test")
    (buch / "wetten" / "test-2025-002.md").write_text(zweite, encoding="utf-8")
    aus = tmp_path / "site"
    rc = cli.main(["bauen", str(buch), str(aus)])
    assert rc == 1
    assert not aus.exists()
    assert "Slug-Kollision" in capsys.readouterr().err


def test_lesefehler_format(tmp_path: Path, capsys):
    rc = cli.main(["bauen", str(tmp_path), str(tmp_path / "site")])
    assert rc == 1
    err = capsys.readouterr().err
    assert "BUCH.md: kopf — " in err
    assert "1 Fehler, nichts geschrieben." in err


def test_neu_legt_gueltiges_buch_an(tmp_path: Path, capsys):
    ziel = tmp_path / "meinbuch"
    rc = cli.main(["neu", str(ziel)])
    assert rc == 0
    assert (ziel / "BUCH.md").exists()
    assert (ziel / ".github" / "workflows" / "pages.yml").exists()
    beispiele = list((ziel / "wetten").glob("*.md"))
    assert len(beispiele) == 1
    assert "OK:" in capsys.readouterr().out
    # Das Gerüst baut ohne Änderung durch.
    rc = cli.main(["bauen", str(ziel), str(tmp_path / "site")])
    assert rc == 0
    assert (tmp_path / "site" / "index.html").exists()


def test_neu_ueberschreibt_nichts(tmp_path: Path, capsys):
    ziel = tmp_path / "meinbuch"
    ziel.mkdir()
    (ziel / "BUCH.md").write_text("eigenes", encoding="utf-8")
    rc = cli.main(["neu", str(ziel)])
    assert rc == 1
    assert (ziel / "BUCH.md").read_text(encoding="utf-8") == "eigenes"
    assert "nicht leer" in capsys.readouterr().err


def test_neu_per_python_m(tmp_path: Path):
    r = subprocess.run([sys.executable, "-m", "wettbuch", "neu", str(tmp_path / "b")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_zweig_faellt_bei_git_fehler_auf_main_zurueck(tmp_path: Path, monkeypatch):
    def kaputt(*args, **kwargs):
        raise OSError("git nicht gefunden")

    monkeypatch.setattr(subprocess, "run", kaputt)
    assert cli._zweig(tmp_path) == "main"


def test_zweig_nutzt_origin_head_bei_detached_head(tmp_path: Path, monkeypatch):
    def fake_run(args, **kwargs):
        if "origin/HEAD" in args:
            return types.SimpleNamespace(stdout="origin/master\n")
        return types.SimpleNamespace(stdout="HEAD\n")

    monkeypatch.setattr(subprocess, "run", fake_run)
    assert cli._zweig(tmp_path) == "master"


def test_zweig_liest_aktuellen_branch(tmp_path: Path, monkeypatch):
    def fake_run(args, **kwargs):
        if "origin/HEAD" in args:
            raise AssertionError("origin/HEAD sollte hier nicht gebraucht werden")
        return types.SimpleNamespace(stdout="hinterlegt-sammelbuch\n")

    monkeypatch.setattr(subprocess, "run", fake_run)
    assert cli._zweig(tmp_path) == "hinterlegt-sammelbuch"
