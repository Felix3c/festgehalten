"""Nachweis offenes Modell: Computer-Schritt aus METHODE.md §5 auf einem lokalen
Modell (Ollama) durchlaufen lassen. Schreibt nichts in die Bücher — nur ein
Protokoll (JSONL) zum Vergleich mit den bestehenden Computer-Werten."""
import json, re, sys, time, glob, pathlib, urllib.request, datetime

HEUTE = datetime.date.today().isoformat()
WURZEL = pathlib.Path(__file__).resolve().parents[2]
MODELL = sys.argv[1] if len(sys.argv) > 1 else "qwen3:4b"
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 0
AUSGABE = pathlib.Path(__file__).parent / f"lauf-{HEUTE}-{MODELL.replace(':','-')}.jsonl"

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return m.group(1), m.group(2)

def feld(fm, name):
    m = re.search(rf"^{name}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None

def computer_wert(fm):
    m = re.search(r"- von: Computer\n\s+wert:\s*([\d.,-]+)", fm)
    return m.group(1) if m else None

def offene_wetten():
    for pfad in sorted(glob.glob(str(WURZEL / "buecher/*/wetten/*.md"))):
        fm, body = frontmatter(pathlib.Path(pfad).read_text(encoding="utf-8"))
        if feld(fm, "ersetzt_durch") not in (None, "null"): continue
        if feld(fm, "ausgang") not in (None, "null"): continue
        pa = feld(fm, "pruefung_am")
        if not pa or pa <= HEUTE: continue
        kontext = re.search(r"## Kontext\n(.*?)(?=\n## |\Z)", body, re.S)
        yield dict(id=feld(fm,"id"), institution=feld(fm,"institution"),
                   gesagt_am=feld(fm,"gesagt_am"), zitat=feld(fm,"zitat"),
                   frage=feld(fm,"frage"), typ=feld(fm,"typ"), pruefung_am=pa,
                   einheit=feld(fm,"einheit"), kontext=(kontext.group(1).strip() if kontext else ""),
                   computer_claude=computer_wert(fm))

METHODE = (WURZEL / "METHODE.md").read_text(encoding="utf-8")
TABELLE = METHODE.split("## 3.")[1].split("## 4.")[0]

SYSTEM = f"""Du bist der "Computer" im festgehalten-Format. Du hinterlegst für eine Ankündigung
einer deutschen Kommune eine Prognose. Regel: Basisrate statt Recherche. Du ordnest die Behauptung
einer Referenzklasse aus der Tabelle zu und trägst den Wert dieser Klasse ein. Du recherchierst nicht,
ob das Projekt gerade gut läuft. Nur allgemein bekannte Vorgeschichte darf den Wert verschieben.

Tabelle der Referenzklassen:
{TABELLE}

Antworte NUR mit einem JSON-Objekt, ohne Erklärtext davor oder danach, mit genau diesen Feldern:
{{"klasse": "<Name der Referenzklasse>", "wert": <Zahl>, "begruendung": "<ein bis zwei Sätze>"}}
Bei typ ja_nein ist wert eine Wahrscheinlichkeit zwischen 0 und 1.
Bei typ punkt ist wert eine Zahl in der Einheit der Frage."""

def frage_modell(w):
    nutzer = (f"Institution: {w['institution']}\nGesagt am: {w['gesagt_am']}\nZitat: {w['zitat']}\n"
              f"Frage: {w['frage']}\nTyp: {w['typ']}" + (f"\nEinheit: {w['einheit']}" if w['einheit'] else "")
              + f"\nPrüfung am: {w['pruefung_am']}\nHeute: {HEUTE}\nKontext: {w['kontext'][:800]}")
    body = json.dumps({"model": MODELL, "stream": False, "think": False, "format": "json",
                       "options": {"temperature": 0, "num_ctx": 4096},
                       "messages": [{"role":"system","content":SYSTEM},{"role":"user","content":nutzer}]}).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", data=body, headers={"Content-Type":"application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=1800) as r:
        antwort = json.load(r)
    text = antwort["message"]["content"]
    try: parsed = json.loads(text)
    except Exception: parsed = {"fehler": text[:500]}
    return parsed, round(time.time()-t0, 1)

if __name__ == "__main__":
    wetten = list(offene_wetten())
    if LIMIT: wetten = wetten[:LIMIT]
    fertig = set()
    if AUSGABE.exists():
        fertig = {json.loads(z)["id"] for z in AUSGABE.read_text(encoding="utf-8").splitlines() if z.strip()}
    print(f"{len(wetten)} offene Wetten, {len(fertig)} schon fertig, Modell {MODELL}", flush=True)
    with AUSGABE.open("a", encoding="utf-8") as out:
        for i, w in enumerate(wetten, 1):
            if w["id"] in fertig: continue
            parsed, dauer = frage_modell(w)
            zeile = dict(id=w["id"], typ=w["typ"], pruefung_am=w["pruefung_am"], modell=MODELL,
                         hinterlegt_am=HEUTE, sekunden=dauer, computer_claude=w["computer_claude"], **parsed)
            out.write(json.dumps(zeile, ensure_ascii=False) + "\n"); out.flush()
            print(f"[{i}/{len(wetten)}] {w['id']} claude={w['computer_claude']} lokal={parsed.get('wert')} ({dauer}s)", flush=True)
