# Köln — Wartezeit in den Kundenzentren (Monatsreihe)

## Zweck

Diese Monatsreihe belegt die sechs Wetten `koeln-2026-077` bis `koeln-2026-082`
(buecher/koeln/wetten/) sowie Wette 9 im privaten Wettbuch. Die Stadt Köln hat
im beschlossenen Haushaltsplan 2025/2026 (Band 3, S. 101, Produktgruppe 0207
Einwohnerangelegenheiten) als Planwert festgeschrieben: „Durchschnittliche
Wartezeit ohne Termin in Min." — Plan 2025: 20,00, Plan 2026: 20,00. Diese
Zahl misst dieser Ordner monatlich nach, mit dem Open-Data-Feed, den die
Stadt selbst live veröffentlicht.

Quelle: `KOELN-FALL-KANDIDATEN-2026-09.md` (Kandidat 1), Abschnitt 4.

## Aufruf

```bash
# Messwert abrufen und an messwerte.csv anhängen (nur im Messfenster, je Slot einmal)
python recherche/koeln-wartezeit/messen.py

# Funktionstest: immer messen, auch außerhalb des Fensters
python recherche/koeln-wartezeit/messen.py --erzwingen

# Monatsreihe auswerten (alle Monate)
python recherche/koeln-wartezeit/auswerten.py

# nur einen Monat
python recherche/koeln-wartezeit/auswerten.py --monat 2026-10
```

`messen.py` braucht keine Zugangsdaten und keine Abhängigkeit außer der
Python-Standardbibliothek (3.11+). Ohne `--erzwingen` misst es nur im Messfenster
(Mo 7:30–15:00, Mi 7:30–12:00 Ortszeit) und je Slot (vormittag/nachmittag) nur
einmal am Tag, sonst endet es mit Exit 0 und „keine Messung". Es ruft
`https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php` ab (bis 03.10.2026 `http://`, das seit 20.09. umleitet und jetzt 403 liefert),
schreibt eine Zeile je Kundenzentrum an `messwerte.csv` und löst danach eine
Wayback-Archivierung des Feeds aus (`https://web.archive.org/save/<feed-url>`).
Schlägt die Archivierung fehl, bleibt `wayback_url` in der Zeile leer — das
Skript bricht deswegen nicht ab. Schlägt der Feed-Abruf selbst fehl, beendet
sich das Skript mit Exit-Code 1 und einer Meldung auf stderr.

### Zweite Quelle: die Anzeige der Bürger-Seite (seit 05.10.2026 Messquelle der Wetten)

```bash
python recherche/koeln-wartezeit/messen.py --quelle anzeige
```

Die Seite „Wartezeiten in unseren Kundenzentren“ lädt ihre Werte aus
`https://www.stadt-koeln.de/interne-dienste/wartezeiten/wartezeiten.json`. Am Mo 05.10.2026
war diese Datei frisch (Stände 07:50, 08:00, 08:10, also alle zehn Minuten), während der
Open-Data-Feed weiter auf dem 16.09. stand. `--quelle anzeige` misst diese Datei mit demselben
Messfenster und denselben Slots und schreibt nach `messwerte-anzeige.csv` (Spalten
`abgerufen_am, kundenzentrum, wartezeit_minuten, stand_iso, status, quelle, wayback_url,
beleg_sha256`), nie nach `messwerte.csv`: Das Skript verweigert jede Zieldatei ohne „anzeige“
im Namen oder mit fremder Kopfzeile. Eine Zeile gibt es nur, wenn `stand_iso` von heute ist.
Gezählt wird nur der Bereich `meldeangelegenheiten` (neun Kundenzentren, auf die Schreibweise
des Feeds abgebildet), nicht die Führerscheinstellen.

Beleg: Jeder Abruf wird unverändert nach `belege-anzeige/` gelegt, der SHA-256 steht in der
Zeile. Die Wayback-Spalte ist hier schwächer als beim Feed: Save Page Now leitet oft auf eine
wenige Minuten ältere Aufnahme um, die einen anderen Stand zeigen kann, und am 05.10.2026 war
die Aufnahme nicht abspielbar (404).

**Entschieden am 05.10.2026 (Halter):** Solange der Open-Data-Feed eingefroren ist, werden die
Wetten koeln-2026-077 bis -082 an dieser Datei gemessen. Frage und Kopf der Wetten nennen weiter
den Feed und bleiben unverändert; jede der sechs Wetten trägt dazu einen Vermerk vom 05.10.2026.
Ausgewertet wird mit

```bash
python recherche/koeln-wartezeit/auswerten.py --quelle anzeige --monat 2026-10
```

Gezählt werden nur Abrufe im Messfenster **mit Rohkopie**: `auswerten.py` rechnet den SHA-256
jeder Datei in `belege-anzeige/` nach und zählt eine Zeile nur, wenn ihr `beleg_sha256` dazu passt. Zeilen ohne
Beleg weist der Kopf aus, sie zählen nicht. Das trifft den ersten Abruf vom Mo 05.10.2026 08:12
(neun Zeilen): Er lief, bevor die Rohkopie eingebaut war. Zeitplan: die drei Aufgaben der
Windows-Aufgabenplanung auf dem Rechner des Halters (siehe unten), seit 05.10.2026 wieder
eingeschaltet. Der Actions-Workflow misst weiter nur den Feed. Kommt der Feed zurück, ist neu zu
entscheiden, welche Quelle zählt; beide Dateien bleiben getrennt.
Zwei Messstellen (vorbereitet 05.10.2026, wirksam erst nach dem Push des Halters): Neben dem
Laptop misst der GitHub-Workflow `koeln-wartezeit.yml` die Anzeige, mit demselben Messfenster und
denselben Slots, in eine eigene Datei `messwerte-anzeige-github.csv`; die Rohkopie liegt ebenfalls
in `belege-anzeige/`, und jeder Messwert kommt als Commit von GitHub (Zeitbeleg, unabhängig vom
Laptop). `auswerten.py --quelle anzeige` liest beide Dateien. Regel ohne Ermessen: Je Slot (Tag,
Vormittag oder Nachmittag) zählt nur der früheste Abruf mit Beleg, gleich von welcher Messstelle;
spätere Abrufe im selben Slot stehen in der Kopfzeile der Auswertung, werden aber nicht gemittelt.
Es bleibt bei höchstens drei gezählten Abrufen je Woche. `.gitattributes` nimmt `belege-anzeige/`
von der Zeilenenden-Umwandlung aus, sonst passte der nachgerechnete SHA-256 auf einem
Windows-Rechner nicht mehr zur Rohkopie, die GitHub eingecheckt hat. Der Wächter
(`koeln-waechter.yml`) prüft seitdem `messwerte-anzeige-github.csv`. Ungeklärt bis zum ersten Lauf:
ob stadt-koeln.de Abrufe von GitHub-Adressen durchlässt; scheitert der Abruf, schreibt der Lauf
keine Zeile, und es zählt wie bisher allein der Laptop.

**Ungeklärt:** ob Feed und Anzeige dieselbe Messung zeigen, was `status` bedeutet (bisher nur
`1` gesehen) und wie die Datei aussieht, wenn ein Kundenzentrum geschlossen ist.

## Stichtage und automatische Messung (GitHub Actions, seit 11.09.2026)

Terminfreie Zeiten laut Stadt: Montag 7:30–15:00, Mittwoch 7:30–12:00. Dienstag,
Donnerstag und Freitag liefert der Feed „nur mit Terminvereinbarung" / 0 Minuten,
das zählt nicht als Vergleichswert.

Die Messung läuft **nicht auf einem privaten Rechner**, sondern als Workflow
`.github/workflows/koeln-wartezeit.yml` auf GitHub. Ziel sind drei Abrufe je Woche,
je einer pro **Slot**: Montag vormittag, Montag nachmittag, Mittwoch vormittag.

**GitHubs Zeitplan ist unzuverlässig.** Mo 14.09.2026: beide Läufe nie gestartet.
Mi 16.09.2026: der Lauf kam 5 h 20 min zu spät (15:27 MESZ, nach Schließung), der
Wächter gar nicht. Seit 16.09. deshalb zwei Schichten:

1. **Viele Startversuche.** Der Workflow hat neun Cron-Einträge, über das ganze
   Fenster verteilt (Vormittag Mo+Mi: 06:37, 07:11, 07:43, 08:19, 08:51, 09:27 UTC;
   Montag nachmittag: 11:17, 11:47, 12:13 UTC). Die Minuten sind so gewählt, dass
   jeder Versuch in Sommer- und Winterzeit im Fenster liegt.
2. **Das Skript entscheidet selbst.** `messen.py` misst nur, wenn die Ortszeit im
   Messfenster liegt (Mo 7:30–15:00, Mi 7:30–12:00, `fenster.py`) und
   `messwerte.csv` für heute im selben Slot noch keinen Abruf hat. Der Slot richtet
   sich nach dem geplanten Cron-Eintrag (`KOELN_CRON`), nicht nach der Startzeit. Regel:
   ein Vormittagslauf schreibt nur als erster Abruf des Tages, ein Nachmittagslauf nur
   als zweiter und frühestens 60 Minuten nach dem letzten. Sonst beendet es
   sich mit Exit 0 und „keine Messung". Verspätete oder doppelte Starts erzeugen
   also keine Zeile. Für Funktionstests gibt es `--erzwingen` (im Actions-Dialog
   „Run workflow" als Häkchen).

Der Workflow committet `messwerte.csv` direkt auf master (Commit-Autor
„koeln-wartezeit (GitHub Actions)", Betreff „data: Köln Wartezeit …"). Jeder Messwert
hat damit zwei Fremdbelege: den Wayback-Snapshot des Feeds und den GitHub-Commit mit
Zeitstempel. Zeitpläne laufen nur auf dem Standardzweig. Manuell auslösen: Reiter
„Actions", Workflow wählen, „Run workflow".

Kontrolle nach jedem Montag: unter
https://github.com/Felix3c/festgehalten/commits/master zwei neue „data:"-Commits
(Mittwoch einer), je 9 neue Zeilen in `messwerte.csv`. Läufe, die mit „keine Messung"
enden, sind normal und erzeugen keinen Commit. Vor jeder lokalen Änderung an
`messwerte.csv` erst `git pull`, sonst kollidiert die Datei mit den Actions-Commits.

Erster gezählter Monat: Oktober 2026 (`koeln-2026-077`); September ist Probelauf.
Alle September-Zeilen liegen außerhalb des Messfensters (08.09. Dienstag, 11.09.
Freitag abends, 16.09. Mittwoch 15:27 nach Schließung) und sind Funktionstests bzw.
der verspätete Lauf. `auswerten.py` zählt Abrufe außerhalb des Messfensters nicht mit,
weist sie aber je Monat aus (`--alle` zeigt sie trotzdem).

Laptop (seit 05.10.2026 wieder eingeschaltet, für die Anzeige die einzige Messung): Auf dem
Rechner des Halters liegen drei Aufgaben der Windows-Aufgabenplanung (`koeln-wartezeit-mo-1000`,
`-mo-1400`, `-mi-1000`, Anmeldemodus „nur interaktiv“), die `messen.cmd` aufrufen (Log
`messen.log`). `messen.cmd` schreibt seit 03.10. **nicht mehr in `messwerte.csv`**, sondern mit
`messen.py --csv` in `messwerte-laptop.csv` (gitignored). Darf deshalb parallel zu Actions
laufen. Seit 05.10.2026 ruft `messen.cmd` danach `messen.py --quelle anzeige` auf; das schreibt
direkt in `messwerte-anzeige.csv` und `belege-anzeige/` (beide versioniert, nach jedem Messtag
von Hand committen; ohne Actions-Commit als Zeitbeleg, die Rohkopie mit SHA-256 trägt). Läuft der
Rechner im Messfenster nicht, fehlt der Abruf. Für den Feed wird von Hand übernommen, nach
`git pull`:

```bash
python recherche/koeln-wartezeit/nachtragen.py              # Probe: was würde übernommen
python recherche/koeln-wartezeit/nachtragen.py --schreiben  # anhängen, dann committen
```

`nachtragen.py` übernimmt einen Laptop-Abruf nur im Messfenster, nur wenn `messwerte.csv` am
selben Tag den Slot (nach Uhrzeit, vor/nach 12:00) noch nicht hat und nur mit 60 Minuten
Abstand zu jedem vorhandenen Abruf. Laptop-Zeilen haben keinen Actions-Commit als
Zeitbeleg, nur die Wayback-Spalte.
Bekannte Grenze: Actions ordnet den Slot nach dem geplanten Cron zu, `nachtragen.py` nach der
Uhrzeit. Ein Actions-Vormittagslauf, der erst nach 12:00 misst, gilt hier als Nachmittag; dann
kann ein Laptop-Vormittag dazukommen (zwei Vormittagswerte). Vor `--schreiben` die Probe lesen.

Wächter (seit 15.09.2026): `.github/workflows/koeln-waechter.yml` läuft nach den
Messläufen (Mo+Mi 09:13 UTC, Mo 12:43 UTC) und ruft `waechter.py` auf. Das Skript zählt
die Abrufzeitpunkte von heute in `messwerte.csv`; fehlt einer, stößt der Workflow den
Messlauf per workflow_dispatch nach und scheitert laut, sodass GitHub eine Mail
schickt. Fällt GitHubs Zeitplan ganz aus, fällt auch der Wächter aus; dann bleibt die
Kontrolle von Hand nach jedem Montag.

## Wie der Monatswert in die Wette kommt

1. `python recherche/koeln-wartezeit/auswerten.py --monat <JJJJ-MM>` nach
   Monatsende laufen lassen; seit 05.10.2026 mit `--quelle anzeige` (Vermerk in den Wetten).
2. Die Zeile „GESAMT (alle Zentren)" liefert Mittelwert und Maximum über alle
   Abrufe des Monats im Messfenster (Abrufe außerhalb weist der Kopf aus, sie
   zählen nicht).
3. Dieser Mittelwert ist der Beleg für `ausgang` der jeweiligen Monatswette
   (`koeln-2026-0NN`): `1`, wenn Mittelwert ≤ 20,0 Min., sonst `0`.
4. `beleg_ausgang` verweist auf den Commit-Hash bzw. -Pfad von
   `messwerte.csv` in diesem Repository plus mindestens einen
   `wayback_url`-Eintrag aus dem betreffenden Monat (Fremdbeleg, siehe unten).

## Grenzen

- **Selbstauskunft der Stadt.** Der Feed wird von der Stadt Köln selbst
  betrieben und befüllt; diese Reihe prüft, ob die Stadt ihr eigenes
  Planziel nach ihren eigenen Zahlen einhält — keine unabhängige Messung vor
  Ort.
- **Der Feed ist veraltet: Befund 03.10.2026.** Seit Mi 16.09.2026 07:45 liefert der Feed
  für alle neun Kundenzentren dieselben Werte (Status „geöffnet“, Chorweiler 71 … Innenstadt
  6 Min.). Wayback-Snapshots 16.09. 13:27 UTC und 20.09. 08:47 UTC haben denselben Digest
  (`5HSZ6PS2…`), am 03.10. ist der Inhalt unverändert:
  https://web.archive.org/web/20261003190545/https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php
  Seitdem bricht `messen.py` ab (Exit 1, keine Zeile, Wayback-Beleg), wenn kein Kundenzentrum
  heute einen `timestamp` hat (`feed_veraltet`); einzelne Zentren mit altem oder künftigem
  `timestamp` fallen still heraus (`frische_records`). `--erzwingen` umgeht die Sperre.
- **Der Feed kann veralten, ohne dass das auffällt.** Im selben Feed steht
  ein Eintrag „Kfz-Zulassungsstelle" mit `timestamp` vom 27.03.2022 — seit
  4,5 Jahren tot, aber weiterhin Teil der Antwort. `messen.py` schließt
  diesen Eintrag namentlich aus (nur `title_anz`, die mit „Kundenzentrum"
  beginnen, werden gezählt), aber auch ein einzelnes Kundenzentrum könnte
  jederzeit denselben Fehler bekommen — deshalb wird `feed_timestamp` je
  Zeile mitgespeichert und sollte vor jeder Auswertung stichprobenartig
  gegen `abgerufen_am` geprüft werden.
- **Stichprobe ist kein Jahresmittel.** Zwei Wochentage zu zwei Uhrzeiten
  ergeben keinen Tagesdurchschnitt und erst recht keinen Jahresdurchschnitt,
  wie ihn der Haushaltsplan ausweist. Die Wetten übersetzen deshalb bewusst
  auf „Mittel aller Abrufe des Feeds an Montagen und Mittwochen", nicht auf
  „Jahresmittel laut Stadt" (siehe Übersetzung in den einzelnen
  Wette-Dateien).
- **`messwerte.csv` wird vom Halter dieses Buchs geführt**, nicht von einer
  unabhängigen dritten Stelle. Beleg-Qualität entsteht erst durch die
  `wayback_url`-Spalte: Jeder Messwert hat einen unabhängigen,
  zeitgestempelten Fremdbeleg im Internet Archive, den auch Dritte
  nachprüfen können, ohne dem Halter zu vertrauen.
