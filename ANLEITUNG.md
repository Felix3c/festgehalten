# Ein Buch in einer Stunde

Für alle, die eine Stadt, einen Verband, einen Verein oder einen Konzern beim Wort
nehmen wollen. Am Ende steht eine öffentliche Seite mit fünf Wetten, die niemand
mehr ändern kann. Du brauchst: Python 3.11 oder neuer, Git, ein GitHub-Konto, einen
Texteditor. Niemanden fragen.

Ehrlich vorweg: Die Stunde stimmt, wenn du die fünf Zitate schon hast. Das Suchen
ist der lange Teil; alles andere ist mechanisch. Wer sein Presseportal zum ersten Mal
durchsucht, braucht für Schritt 0:10 eher einen Abend als zwanzig Minuten. Das ist
normal, nicht langsam.

Die Regeln stehen in [FORMAT.md](FORMAT.md). Diese Seite ist nur der Weg.

## 0:00 — Installieren und Gerüst anlegen (5 Minuten)

```
python -m pip install "festgehalten @ git+https://github.com/Felix3c/festgehalten"
festgehalten neu meinbuch --stadt "Stadt Musterstadt"
```

(Auf Windows heißt Python manchmal `py`. Wenn `festgehalten` danach nicht gefunden
wird, geht `python -m wettbuch` mit denselben Argumenten.)

Der Ordner `meinbuch` enthält jetzt drei Dateien: `BUCH.md`, eine Beispielwette in
`wetten/`, ein Workflow in `.github/workflows/`. Alles darin baut sofort; alles in
GROSSBUCHSTABEN ist ein Platzhalter.

## 0:05 — BUCH.md ausfüllen (5 Minuten)

Titel, dein Name, eine Kontaktadresse. Darunter drei Dinge, die für die Anerkennung
später Pflicht sind (FORMAT.md §8.1): worum es geht, nach welcher Regel du auswählst,
der Satz zum Geld (§8.4, steht schon drin). Die Auswahlregel im Gerüst — „Aussagen
mit Zahl und Datum aus öffentlichen Quellen" — kannst du übernehmen.

## 0:10 — Fünf Behauptungen finden (20 Minuten)

Presseportal der Stadt, Haushaltsrede, Ratsvorlagen. Suchwörter: „wird", „soll",
„voraussichtlich", „bis Ende", „ab dem", „Millionen". Eine Behauptung taugt, wenn sie
drei Dinge hat:

1. eine **Zahl oder ein Ereignis** („eröffnet", „2.000 Plätze", „Defizit 395 Mio"),
2. ein **Datum**, bis wann,
3. eine **öffentliche URL**, in der das wörtlich steht.

Kopiere pro Behauptung: URL, Datum der Mitteilung, wer es gesagt hat, den Satz
wörtlich. Archiviere die URL bei web.archive.org (ein Klick, spart später Ärger).
Keine Absichten ohne Zahl und Datum („wir wollen die Stadt attraktiver machen"),
keine Paraphrasen.

## 0:30 — Fünf Wetten schreiben (15 Minuten)

Die Beispielwette fünfmal kopieren, umbenennen (`musterstadt-2026-001.md` bis
`-005.md`), ausfüllen. Die Felder stehen in FORMAT.md §1.1; drei sind entscheidend:

- **`zitat`**: wörtlich, gekürzt mit „…". Nie umformulieren.
- **`frage`**: die Ja/Nein-Form mit Datum. „Ist das Bad am 31.12.2027 eröffnet?"
  Schreib sie so hart, wie du sie später auflösen willst: Teilerfüllung ist Nein
  (§2.2). Wer Milde will, stellt die Frage vorher weicher.
- **`art`** der ersten Prognose: `angekuendigt` (Wert 1,00), wenn die Stelle es ohne
  Vorbehalt gesagt hat; `voraussichtlich` (Wert 0,80), wenn „voraussichtlich", „soll",
  „geplant" dabeistand.

Hast du eine Zahl statt eines Ereignisses („Defizit 395,1 Mio", „2.000 Plätze"),
wird sie mit ihrem Datum zur Ja/Nein-Frage: „Beträgt das Defizit 2025 laut
Jahresabschluss höchstens 395,1 Mio EUR?" (FORMAT.md §1.3.4). Der Typ `punkt`, bei dem
die Zahl selbst verglichen wird, existiert auch; für das erste Buch brauchst du ihn nicht.

Unter dem Kopf zwei Absätze: **Kontext** (woher, was drumherum) und **Übersetzung**
(wie aus dem Satz die Frage wurde). Wenn du selbst schätzen willst, häng eine zweite
Prognose an: `von: Dein Name`, `wert: 0.40`, `art: geschaetzt`, `hinterlegt_am: heute`.
Du stehst dann in derselben Rangliste wie die Stadt. Basisraten zum Anlehnen:
[METHODE.md](METHODE.md).

## 0:45 — Bauen (5 Minuten)

```
festgehalten bauen meinbuch site --pruefen
```

Meldet Fehler mit Dateiname und Feld („musterstadt-2026-003.md: pruefung_am — kein
Datum"). Beheben, wiederholen, bis „OK: 5 Wetten, keine Fehler" kommt. Dann ohne
`--pruefen` bauen und `site/index.html` im Browser öffnen: Rangliste, eine Seite je
Institution, eine je Wette, ein `wettbuch.json`.

## 0:50 — Veröffentlichen (10 Minuten)

```
cd meinbuch
git init && git add . && git commit -m "Erstes Buch: fünf Wetten"
```

Auf GitHub ein neues, öffentliches Repository anlegen (ohne README). **Vor dem ersten
Push** dort unter **Settings → Pages → Source** „GitHub Actions" wählen; sonst schlägt
der erste Lauf beim Veröffentlichen fehl. Dann:

```
git remote add origin https://github.com/DEIN-NAME/meinbuch.git
git push -u origin master
```

Der Workflow aus dem Gerüst baut die Seite bei jedem Push; nach ein bis zwei Minuten
steht sie unter `https://DEIN-NAME.github.io/meinbuch/`. Hast du die Pages-Quelle erst
nach dem Push gesetzt: unter **Actions** den fehlgeschlagenen Lauf mit „Re-run jobs"
wiederholen.

Der Workflow im Gerüst ist vom Workflow dieses Repos abgeleitet, aber noch nie in einem
fremden Repo gelaufen. Wenn er hakt, schreib an den Kontakt in
[buecher/koeln/BUCH.md](buecher/koeln/BUCH.md); der erste, bei dem es hakt, hilft allen danach.

Der Commit-Hash ist dein Zeitstempel. Ab jetzt gilt §1.3.3: Einträge werden nicht mehr
geändert, nur noch aufgelöst und mit Vermerken versehen.

## Danach

- **Auflösen** (§2): Nach `pruefung_am` nachschauen, Beleg-URL eintragen, `ausgang`
  setzen, committen. Ohne Beleg lehnt der Generator den Ausgang ab.
- **Rang**: ab zehn aufgelösten Ja/Nein-Wetten (§3.4). Fünf Wetten sind ein Anfang,
  kein Urteil.
- **Anerkennung** (§8.1): Zitat in jeder Quelle, Beleg in jeder Auflösung, Auswahlregel
  in BUCH.md, öffentliche Git-Historie, der Geld-Satz. Prüft heute der Hüter; schreib
  an den Kontakt in [buecher/koeln/BUCH.md](buecher/koeln/BUCH.md). Anerkannte Bücher
  stehen in der Übersicht und tragen den Namen „festgehalten".
- **Gegenbuch**: Wer findet, dass „Musterstadt gegen Musterstadt" unfair auswählt, führt
  „Musterstadt über Musterstadt" nach denselben Regeln. Beide stehen nebeneinander (§8.7).
