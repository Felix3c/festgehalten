from pathlib import Path
import subprocess
import sys

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
