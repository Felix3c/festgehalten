# festgehalten: Sammelbuch „Hinterlegt", Buchliste, PR-Prüfung — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Das Repo festgehalten kann hinterlegte Einträge aufnehmen: ein leeres Sammelbuch, eine maschinenlesbare Buchliste für Doorway, und ein Prüf-Workflow, der jeden Pull Request formal prüft.

**Architecture:** Drei kleine Änderungen am Generator (`generator/wettbuch/`): leere Bücher bauen, drei neue optionale BUCH.md-Felder prüfen, `buecher.json` neben `alle.json` schreiben. Dazu ein neues Buch als Ordner und ein zweiter GitHub-Workflow. Keine Formatänderung (FORMAT.md bleibt v1, §8.3 wird nicht ausgelöst).

**Tech Stack:** Python 3.11+, pyyaml, pytest. Bestehende Module `lesen.py`, `pruefen.py`, `cli.py`, `seiten.py`.

**Spec:** `~/doorway/docs/superpowers/specs/2026-09-05-doorway-teil-3-hinterlegung-design.md`, Abschnitt 5.

## Global Constraints

- Keine Änderung an FORMAT.md §0–7. Neue BUCH.md-Felder sind optional und nur für die Buchliste.
- Alle Tests laufen mit `python -m pytest -q` aus `~/wettbuch`; vorher `python -m pip install -e ".[test]"`.
- Deutsch in Code-Kommentaren, Fehlermeldungen und Dateinamen, wie im Bestand.
- Commit-Format wie bisher: `feat: …`, `fix: …`, `docs: …`, `ci: …`.
- `pages.yml` bleibt bis auf `--repo` (Task 4) unverändert.

---

### Task 1: Generator baut ein Buch ohne Einträge

**Files:**
- Test: `generator/tests/test_alle.py` (anhängen)
- Modify (nur falls der Test fehlschlägt): `generator/wettbuch/lesen.py:44-59`, `generator/wettbuch/bewerten.py`, `generator/wettbuch/seiten.py:132-175`

**Interfaces:**
- Consumes: `cli.main(["alle", <buecher>, <ausgabe>]) -> int`, Konstante `BUCH_OK` aus `generator/tests/conftest.py`
- Produces: nichts Neues; garantiert `rc == 0` für ein Buch mit leerem `wetten/`

- [ ] **Step 1: Test schreiben**

```python
# generator/tests/test_alle.py, am Ende anhängen
from conftest import BUCH_OK


def test_alle_baut_buch_ohne_eintraege(tmp_path: Path):
    buecher = tmp_path / "buecher"
    leer = buecher / "leer"
    (leer / "wetten").mkdir(parents=True)
    (leer / "BUCH.md").write_text(BUCH_OK, encoding="utf-8")
    ausgabe = tmp_path / "site"

    rc = cli.main(["alle", str(buecher), str(ausgabe)])

    assert rc == 0
    assert (ausgabe / "leer" / "index.html").exists()
    daten = json.loads((ausgabe / "alle.json").read_text(encoding="utf-8"))
    assert daten[0]["wetten"] == 0 and daten[0]["offen"] == 0
```

Falls `from conftest import BUCH_OK` nicht auflöst (pytest-Importmodus), die Konstante `BUCH_OK` aus `conftest.py` wörtlich in den Test kopieren.

- [ ] **Step 2: Test laufen lassen**

Run: `python -m pytest -q generator/tests/test_alle.py::test_alle_baut_buch_ohne_eintraege`
Expected: PASS oder FAIL. Bei PASS: Schritt 3 überspringen.

- [ ] **Step 3: Nur bei FAIL: Ursache beheben**

Typische Stellen: `lesen.buch_lesen` wirft bei leerem Ordner; `bewerten.buch_bewerten` teilt durch null bei der Trefferquote; `seiten.seiten_schreiben` greift auf `wetten[0]`. Minimal beheben (Leerliste erlauben, Quote `None` bei null Wetten), keine Umbauten.

- [ ] **Step 4: Alle Tests laufen lassen**

Run: `python -m pytest -q`
Expected: alle grün.

- [ ] **Step 5: Commit**

```bash
git add generator/tests/test_alle.py generator/wettbuch
git commit -m "fix: Generator baut auch ein Buch ohne Einträge"
```

---

### Task 2: Neue optionale BUCH.md-Felder prüfen

**Files:**
- Modify: `generator/wettbuch/pruefen.py` (`_meta_pruefen`, Konstanten oben)
- Test: `generator/tests/test_pruefen.py` (anhängen)

**Interfaces:**
- Consumes: `pruefen._meta_pruefen(meta: dict) -> list[Fehler]`
- Produces: akzeptiert `institution` (str), `einreichung` (Mailadresse), `sammelbuch` (bool); liefert `Fehler("BUCH.md", <feld>, <text>)` bei falschem Typ.

- [ ] **Step 1: Tests schreiben**

```python
# generator/tests/test_pruefen.py, anhängen
from datetime import date

from wettbuch import pruefen

META_OK = {"titel": "T", "halter": "H", "seit": date(2026, 8, 28), "format": "v1"}


def test_meta_neue_felder_gueltig():
    meta = dict(META_OK, institution="Stadt Test", einreichung="buch@example.org", sammelbuch=True)
    assert pruefen._meta_pruefen(meta) == []


def test_meta_einreichung_muss_mailadresse_sein():
    f = pruefen._meta_pruefen(dict(META_OK, einreichung="https://example.org"))
    assert [x.feld for x in f] == ["einreichung"]


def test_meta_sammelbuch_muss_bool_sein():
    f = pruefen._meta_pruefen(dict(META_OK, sammelbuch="ja"))
    assert [x.feld for x in f] == ["sammelbuch"]


def test_meta_institution_muss_text_sein():
    f = pruefen._meta_pruefen(dict(META_OK, institution=42))
    assert [x.feld for x in f] == ["institution"]
```

- [ ] **Step 2: Tests laufen lassen, Fehlschlag sehen**

Run: `python -m pytest -q generator/tests/test_pruefen.py -k meta`
Expected: die drei Fehlerfall-Tests FAIL (Felder werden heute ignoriert).

- [ ] **Step 3: Prüfung ergänzen**

```python
# generator/wettbuch/pruefen.py, bei den Konstanten oben:
MAIL_MUSTER = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# in _meta_pruefen, vor `return f`:
    if "institution" in meta and not isinstance(meta["institution"], str):
        f.append(Fehler("BUCH.md", "institution", "muss Text sein"))
    if "einreichung" in meta and not (isinstance(meta["einreichung"], str) and MAIL_MUSTER.match(meta["einreichung"])):
        f.append(Fehler("BUCH.md", "einreichung", "muss eine Mailadresse sein"))
    if "sammelbuch" in meta and not isinstance(meta["sammelbuch"], bool):
        f.append(Fehler("BUCH.md", "sammelbuch", "muss true oder false sein"))
```

- [ ] **Step 4: Tests laufen lassen**

Run: `python -m pytest -q`
Expected: alle grün.

- [ ] **Step 5: Commit**

```bash
git add generator/wettbuch/pruefen.py generator/tests/test_pruefen.py
git commit -m "feat: BUCH.md kennt institution, einreichung, sammelbuch (optional)"
```

---

### Task 3: `buecher.json` schreiben

**Files:**
- Modify: `generator/wettbuch/cli.py` (`_alle`, `main`, `HILFE`)
- Modify: `generator/wettbuch/seiten.py` (neben `uebersicht_schreiben`)
- Test: `generator/tests/test_alle.py` (anhängen)

**Interfaces:**
- Consumes: `seiten.uebersicht_schreiben(uebersicht, ausgabe, build_zeit)`, `buch["meta"]`, Fixture `buecher_ordner` (zwei Bücher `erstes`, `zweites`)
- Produces: `seiten.buecher_schreiben(buecher: list[dict], ausgabe: Path) -> None` schreibt `ausgabe/buecher.json`; `cli.main` akzeptiert `--repo <owner/name>`; `cli._zweig() -> str`; `cli._bucheintrag(name, meta, repo, zweig) -> dict`.

Ein Eintrag in `buecher.json`:

```json
{"ordner": "koeln", "titel": "Köln gegen Köln", "institution": "Stadt Köln",
 "halter": "Felix Lind", "kontakt": "https://belegbar.eu", "einreichung": null,
 "repo": "Felix3c/festgehalten", "zweig": "main", "pfad": "buecher/koeln/wetten",
 "sammelbuch": false}
```

- [ ] **Step 1: Tests schreiben**

```python
# generator/tests/test_alle.py, anhängen
def test_alle_schreibt_buecher_json(buecher_ordner: Path, tmp_path: Path):
    ausgabe = tmp_path / "site"
    buch_md = buecher_ordner / "erstes" / "BUCH.md"
    buch_md.write_text(buch_md.read_text(encoding="utf-8").replace(
        "format: v1", "format: v1\ninstitution: Stadt Erstes\neinreichung: buch@example.org\nsammelbuch: true"),
        encoding="utf-8")

    rc = cli.main(["alle", str(buecher_ordner), str(ausgabe), "--repo", "beispiel/repo"])
    assert rc == 0

    buecher = json.loads((ausgabe / "buecher.json").read_text(encoding="utf-8"))
    nach_ordner = {b["ordner"]: b for b in buecher}
    erstes = nach_ordner["erstes"]
    assert erstes["institution"] == "Stadt Erstes"
    assert erstes["einreichung"] == "buch@example.org"
    assert erstes["sammelbuch"] is True
    assert erstes["repo"] == "beispiel/repo"
    assert erstes["pfad"] == "buecher/erstes/wetten"
    assert isinstance(erstes["zweig"], str) and erstes["zweig"]
    zweites = nach_ordner["zweites"]
    assert zweites["institution"] is None
    assert zweites["sammelbuch"] is False


def test_alle_lehnt_zwei_sammelbuecher_ab(buecher_ordner: Path, tmp_path: Path, capsys):
    for name in ("erstes", "zweites"):
        p = buecher_ordner / name / "BUCH.md"
        p.write_text(p.read_text(encoding="utf-8").replace("format: v1", "format: v1\nsammelbuch: true"), encoding="utf-8")
    rc = cli.main(["alle", str(buecher_ordner), str(tmp_path / "site")])
    assert rc == 1
    assert "sammelbuch" in capsys.readouterr().err
```

- [ ] **Step 2: Tests laufen lassen, Fehlschlag sehen**

Run: `python -m pytest -q generator/tests/test_alle.py -k "buecher_json or sammelbuecher"`
Expected: FAIL (`--repo` unbekannt bzw. `buecher.json` fehlt).

- [ ] **Step 3: Implementieren**

```python
# generator/wettbuch/seiten.py, neben uebersicht_schreiben:
def buecher_schreiben(buecher: list[dict], ausgabe: Path) -> None:
    """Buchliste für Werkzeuge, die Einträge einreichen (Doorway, Spec Teil 3 §5.2)."""
    ausgabe.mkdir(parents=True, exist_ok=True)
    (ausgabe / "buecher.json").write_text(json.dumps(buecher, ensure_ascii=False, indent=2), encoding="utf-8")
```

```python
# generator/wettbuch/cli.py
import subprocess


def _zweig() -> str:
    try:
        r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, check=True)
        z = r.stdout.strip()
        return z if z and z != "HEAD" else "main"
    except (OSError, subprocess.CalledProcessError):
        return "main"


def _bucheintrag(name: str, meta: dict, repo: str | None, zweig: str) -> dict:
    return {
        "ordner": name,
        "titel": str(meta.get("titel", name)),
        "institution": meta.get("institution"),
        "halter": meta.get("halter"),
        "kontakt": meta.get("kontakt"),
        "einreichung": meta.get("einreichung"),
        "repo": repo,
        "zweig": zweig,
        "pfad": f"buecher/{name}/wetten",
        "sammelbuch": bool(meta.get("sammelbuch", False)),
    }
```

In `_alle(...)`: Signatur um `repo: str | None` erweitern. Nach der Schleife über die Bücher und **vor** `if fehler_gesamt:` einfügen (damit der Check auch mit `--pruefen` greift):

```python
    sammel = [name for name, buch, _ in gute if buch["meta"].get("sammelbuch") is True]
    if len(sammel) > 1:
        fehler_gesamt.append(f"{', '.join(sammel)}: sammelbuch — höchstens ein Buch darf sammelbuch: true tragen")
```

Nach `seiten.uebersicht_schreiben(...)`:

```python
    zweig = _zweig()
    seiten.buecher_schreiben([_bucheintrag(name, buch["meta"], repo, zweig) for name, buch, _ in gute], ausgabe)
```

In `main(...)`, direkt nach dem `--pruefen`-Filter:

```python
    repo = None
    if "--repo" in argv:
        i = argv.index("--repo")
        repo = argv[i + 1] if i + 1 < len(argv) else None
        del argv[i:i + 2]
```

und den `alle`-Aufruf mit `repo` versorgen. `HILFE` um `[--repo owner/name]` ergänzen.

- [ ] **Step 4: Tests laufen lassen**

Run: `python -m pytest -q`
Expected: alle grün, auch `test_alle_baut_mehrere_buecher_und_uebersicht` (`alle.json` unverändert).

- [ ] **Step 5: Commit**

```bash
git add generator/wettbuch/cli.py generator/wettbuch/seiten.py generator/tests/test_alle.py
git commit -m "feat: alle schreibt buecher.json (Buchliste für Einreichungen), --repo"
```

---

### Task 4: Sammelbuch anlegen, Stadtbücher um `institution` ergänzen

**Files:**
- Create: `buecher/hinterlegt/BUCH.md`, `buecher/hinterlegt/wetten/.gitkeep`
- Modify: `buecher/{bonn,dortmund,duesseldorf,essen,koeln}/BUCH.md` (Kopf: `institution: Stadt <Name>`)
- Modify: `.github/workflows/pages.yml` (Zeile `python -m wettbuch alle buecher site`)

**Interfaces:**
- Consumes: Felder aus Task 2, `--repo` aus Task 3
- Produces: `buecher.json` auf der Live-Seite mit sechs Einträgen, genau einer `sammelbuch: true`

Die Mailadresse für `einreichung` legt Felix fest. Bis dahin: Feld weglassen; in Doorway fehlt dann nur der Mail-Knopf (Spec §4.3).

- [ ] **Step 1: BUCH.md des Sammelbuchs schreiben**

```markdown
---
titel: Hinterlegt
halter: Felix Lind
kontakt: https://belegbar.eu
seit: 2026-09-05
lizenz: CC0
format: v1
sammelbuch: true
---

Dieses Buch nimmt auf, was jemand vorab, datiert und öffentlich über sich selbst
festhält: eine Erwartung, die andere später nachprüfen können. Jeder Eintrag trägt
`herkunft: hinterlegt` und wird gezählt wie ein zitierter (Format §8.4). Wer ein eigenes
Buch hat (die Städte), hinterlegt dort; alle anderen hier. Eine Institution, die später
ein eigenes Buch bekommt, behält ihre Einträge hier; nichts wird verschoben (§1.3.3).

**Festpreis je hinterlegtem Eintrag: 0 Euro.** Ein Preis über null wird erst
veröffentlicht, wenn als Halter dieses Buches eine eingetragene gemeinnützige
Körperschaft steht und der Betreiber von Doorway eine davon verschiedene eingetragene
Gesellschaft ist. Beides ist im Vereins- bzw. Handelsregister nachprüfbar. Bis dahin:
null, datiert, hier. (05.09.2026)

**Verfall:** Hinterlegte Einträge verfallen sechs Monate nach ihrem Prüfdatum;
`verfall_am` steht in jeder Datei. Wer den Beleg selbst kontrolliert, braucht keine zwei
Jahre, um darauf zu zeigen. (Halter-Regel, 05.09.2026)

**Der Halter dieses Buches hinterlegt nicht im eigenen Buch.**

**Aufnahme.** Einträge kommen als Pull Request (Datei in `wetten/`). Die automatische
Prüfung lehnt formale Fehler ab. Der Halter nimmt an, wenn vier Punkte erfüllt sind:
(1) Die Frage ist am Stichtag ohne Ermessen entscheidbar. (2) Der genannte öffentliche
Ort des Nachweises ist heute schon erreichbar. (3) Eine Bedingung trägt eine Frist.
(4) Die Quelle ist erreichbar und enthält das Zitat; ist die Quelle die Datei in diesem
Buch selbst, entfällt dieser Punkt. Der Halter prüft nicht, ob die Erwartung klug ist.
Annahme und Ablehnung stehen als Kommentar am Pull Request mit Nennung des Punktes. Der
Zeitpunkt der Hinterlegung ist der Merge-Commit.
```

Dazu eine leere Datei `buecher/hinterlegt/wetten/.gitkeep`, damit der Ordner im Git existiert.

- [ ] **Step 2: Stadtbücher ergänzen**

In jeder der fünf `BUCH.md` im Kopf nach `titel:` eine Zeile `institution: Stadt <Name>` (Bonn, Dortmund, Düsseldorf, Essen, Köln). Der Wert muss exakt dem `institution`-Feld der Wetten des Buches entsprechen; prüfen mit:

Run: `for b in bonn dortmund duesseldorf essen koeln; do echo "$b: $(grep -h '^institution:' buecher/$b/wetten/*.md | sort -u | tr '\n' ' ')"; done`

- [ ] **Step 3: pages.yml anpassen**

`- run: python -m wettbuch alle buecher site` wird zu `- run: python -m wettbuch alle buecher site --repo Felix3c/festgehalten`.

- [ ] **Step 4: Lokal bauen und prüfen**

Run: `python -m wettbuch alle buecher site --repo Felix3c/festgehalten && python -c "import json;b=json.load(open('site/buecher.json',encoding='utf-8'));print(len(b),[x['ordner'] for x in b if x['sammelbuch']])"`
Expected: `OK: 6 Bücher …` und `6 ['hinterlegt']`. Ob `site/` committet wird, zeigt `git status`; dem Bestand folgen.

- [ ] **Step 5: Tests und Commit**

Run: `python -m pytest -q` → grün.

```bash
git add buecher .github/workflows/pages.yml
git commit -m "feat: Sammelbuch Hinterlegt; institution in Stadtbüchern; --repo im Deploy"
```

---

### Task 5: Prüf-Workflow für Pull Requests

**Files:**
- Create: `.github/workflows/pruefen.yml`

**Interfaces:**
- Produces: roter Check bei jedem PR mit Formfehler; kein Deploy.

- [ ] **Step 1: Workflow schreiben**

```yaml
name: Pull Request prüfen
on:
  pull_request:
permissions:
  contents: read
jobs:
  pruefen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: python -m pip install -e ".[test]"
      - run: python -m pytest -q
      - run: python -m wettbuch alle buecher site --pruefen
```

- [ ] **Step 2: Commit und pushen**

```bash
git add .github/workflows/pruefen.yml
git commit -m "ci: Pull Requests formal prüfen (Tests + Generator, ohne Deploy)"
git push
```

- [ ] **Step 3: Workflow einmal auslösen**

Zweig `probelauf-ci` mit einer absichtlich fehlerhaften Datei `buecher/hinterlegt/wetten/kaputt.md` (Inhalt nur `---\nid: kaputt\n---\n`) pushen, PR öffnen, warten. Erwartet: Check rot, Meldung enthält `hinterlegt/kaputt.md` und `Pflichtfeld fehlt`. PR schließen, Zweig löschen.

- [ ] **Step 4: Commit-SHA für Doorway notieren**

Run: `git rev-parse HEAD`
Wert in `~/doorway/docs/superpowers/plans/2026-09-05-doorway-teil-3-hinterlegung.md` bei `FESTGEHALTEN_SHA` eintragen. Nach dem Pages-Deploy liegt die Buchliste unter https://felix3c.github.io/festgehalten/buecher.json; der Doorway-Plan kopiert sie in Task 1.

---

## Selbstprüfung gegen die Spec (§5)

- §5.1 Sammelbuch mit Festpreis, Verfall, Halter-Satz, vier Prüfpunkten, PR-Kommentar: Task 4.
- §5.1 „Generator baut leeres Buch": Task 1.
- §5.2 `buecher.json` mit allen zehn Feldern, `--repo`, Zweig aus Git, Prüfung von `einreichung` und höchstens einem Sammelbuch: Tasks 2 und 3.
- §5.3 `pruefen.yml` nur Leserecht, kein Deploy: Task 5. `pages.yml` bekommt abweichend von der Spec eine Änderung (`--repo`), damit `repo` in der Live-Buchliste steht; sonst unverändert.
- Offen: Mailadresse `einreichung` (Entscheidung Felix).
