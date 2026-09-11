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
# Messwert abrufen und an messwerte.csv anhängen
python recherche/koeln-wartezeit/messen.py

# Monatsreihe auswerten (alle Monate)
python recherche/koeln-wartezeit/auswerten.py

# nur einen Monat
python recherche/koeln-wartezeit/auswerten.py --monat 2026-10
```

`messen.py` braucht keine Argumente, keine Zugangsdaten, keine Abhängigkeit
außer der Python-Standardbibliothek (3.11+). Es ruft
`http://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php` ab,
schreibt eine Zeile je Kundenzentrum an `messwerte.csv` und löst danach eine
Wayback-Archivierung des Feeds aus (`https://web.archive.org/save/<feed-url>`).
Schlägt die Archivierung fehl, bleibt `wayback_url` in der Zeile leer — das
Skript bricht deswegen nicht ab. Schlägt der Feed-Abruf selbst fehl, beendet
sich das Skript mit Exit-Code 1 und einer Meldung auf stderr.

## Stichtage und automatische Messung (GitHub Actions, seit 11.09.2026)

Terminfreie Zeiten laut Stadt: Montag 7:30–15:00, Mittwoch 7:30–12:00. Dienstag,
Donnerstag und Freitag liefert der Feed „nur mit Terminvereinbarung" / 0 Minuten,
das zählt nicht als Vergleichswert.

Die Messung läuft **nicht auf einem privaten Rechner**, sondern als Workflow
`.github/workflows/koeln-wartezeit.yml` auf GitHub, drei Abrufe je Woche:

| Zeitplan (UTC) | Sommerzeit | Winterzeit |
|---|---|---|
| Montag und Mittwoch 08:00 | 10:00 | 09:00 |
| Montag 11:30 | 13:30 | 12:30 |

Der Workflow ruft `messen.py` auf und committet `messwerte.csv` direkt auf master
(Commit-Autor „koeln-wartezeit (GitHub Actions)", Betreff „data: Köln Wartezeit …").
Jeder Messwert hat damit zwei Fremdbelege: den Wayback-Snapshot des Feeds und den
GitHub-Commit mit Zeitstempel. Zeitpläne laufen nur auf dem Standardzweig; GitHub
startet sie manchmal mit Verzögerung, deshalb liegt der Nachmittagsabruf mit Reserve
vor 15:00. Manuell auslösen: Reiter „Actions", Workflow wählen, „Run workflow".

Kontrolle nach jedem Montag: unter
https://github.com/Felix3c/festgehalten/commits/master zwei neue „data:"-Commits
(Mittwoch einer), je 9 neue Zeilen in `messwerte.csv`. Bleibt ein Lauf aus, steht
der Fehler im Actions-Protokoll. Vor jeder lokalen Änderung an `messwerte.csv`
erst `git pull`, sonst kollidiert die Datei mit den Actions-Commits.

Erster gezählter Monat: Oktober 2026 (`koeln-2026-077`); September ist Probelauf.
Die Zeile vom 08.09. (Dienstag, außerhalb der Öffnungszeit) ist ein Funktionstest.

Rückfallebene, abgeschaltet: Auf dem Rechner des Halters liegen drei deaktivierte
Aufgaben der Windows-Aufgabenplanung (`koeln-wartezeit-mo-1000`, `-mo-1400`,
`-mi-1000`), die `messen.cmd` in diesem Ordner aufrufen (Log `messen.log`,
gitignored). Nur einschalten, wenn GitHub Actions ausfällt, und dann die CSV von Hand
committen; beides gleichzeitig erzeugt doppelte Zeilen.

## Wie der Monatswert in die Wette kommt

1. `python recherche/koeln-wartezeit/auswerten.py --monat <JJJJ-MM>` nach
   Monatsende laufen lassen.
2. Die Zeile „GESAMT (alle Zentren)" liefert Mittelwert und Maximum über alle
   Abrufe des Monats.
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
