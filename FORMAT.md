# Wettbuch-Format v1 — Spezifikation

Stand 28.08.2026 (Entwurf, beschlossen von Felix Lind mit Claude). Dieses Dokument
beschreibt, wie ein Wettbuch auf der Platte aussieht, wie Einträge aufgelöst und
bewertet werden und was der Generator daraus macht. Wer diese Regeln einhält, führt
ein Wettbuch — ohne Erlaubnis, ohne Plattform, ohne den Autor zu fragen.

## 0. Was ein Wettbuch ist

Eine öffentliche, datierte, unveränderliche Sammlung von Zukunftsaussagen, ergänzt um
die Auflösung nach Ablauf und eine Bewertung. Es hat einen **Halter** (wer es führt).
Es hat keinen Betreiber: Es gibt keine zentrale Stelle, der alle Bücher gehören.

Ein Wettbuch ist ein Ordner. Darin: eine Datei pro Wette, eine `BUCH.md` mit
Metadaten, optional Unterordner je Institution. Aus dem Ordner erzeugt der Generator
eine statische Seite. Der Ordner liegt idealerweise in einem Git-Repository, weil der
Commit-Hash der billigste unveränderliche Zeitstempel ist, den es gibt.

## 1. Eine Wette ist eine Datei

Eine Markdown-Datei mit YAML-Kopf. Der Kopf trägt, was die Maschine braucht. Der Text
darunter trägt, was Menschen lesen: Zitat im Kontext, Übersetzung, Begründungen,
Vermerke. Dateiname: `<id>.md`.

```markdown
---
id: koeln-2025-011
institution: Stadt Köln
gesagt_von: Stadtdirektorin Andrea Blome
gesagt_am: 2025-10-01
quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27942/index.html
zitat: "Das Opernhaus wird Ende Oktober fertig, Ende November folgt dann das Schauspiel …"
frage: Ist das Opernhaus am 31.10.2025 baulich fertiggestellt?
typ: ja_nein
pruefung_am: 2025-11-01
prognosen:
  - von: Stadt Köln
    wert: 1.00
    hinterlegt_am: 2025-10-01
    art: angekuendigt
  - von: Computer
    wert: 0.35
    hinterlegt_am: 2026-08-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke: []
---

## Kontext
Pressemitteilung zur Bühnen-Sanierung, 01.10.2025. Die Aussage nennt drei Termine;
diese Wette betrifft nur das Opernhaus. Schauspiel und Kleines Haus sind eigene Wetten
(koeln-2025-012, -013).

## Übersetzung
„wird Ende Oktober fertig" → Ja/Nein am 31.10.2025. „Baulich fertiggestellt" nach dem
Sprachgebrauch der Stadt selbst (Mitteilung vom 29.08.2024: „bauliche Fertigstellung"
≠ Spielbetrieb).

## Begründung Computer
…
```

### 1.1 Pflichtfelder

| Feld | Typ | Bedeutung |
|---|---|---|
| `id` | Text | eindeutig im Buch; nur Kleinbuchstaben, Ziffern, Bindestrich; Empfehlung `<institution-kurz>-<jahr>-<lfd>` |
| `institution` | Text | die Stelle, deren Aussage gemessen wird |
| `gesagt_von` | Text | Person oder Organ, das die Aussage gemacht hat |
| `gesagt_am` | Datum | wann die Aussage gemacht wurde (Datum der Quelle) |
| `quelle` | URL | öffentliche Quelle der Aussage; ohne Quelle keine Wette |
| `zitat` | Text | wörtlich, gekürzt mit … ; keine Paraphrase |
| `frage` | Text | die aufgelöste Form: eine Ja/Nein-Frage oder eine Zahl-Frage mit Einheit |
| `typ` | `ja_nein` \| `punkt` | Auflösungsart |
| `pruefung_am` | Datum | frühester Tag, an dem aufgelöst werden darf |
| `prognosen` | Liste | mindestens ein Eintrag; siehe 1.2 |
| `ausgang` | `null` \| `0` \| `1` \| Zahl \| `verfallen` \| `strittig` | leer bis zur Auflösung |
| `aufgeloest_am` | `null` \| Datum | |
| `beleg_ausgang` | `null` \| URL | Pflicht, sobald `ausgang` 0/1/Zahl ist |
| `vermerke` | Liste von `{am, text}` | Änderungswünsche, Streit, Hinweise — nie Änderungen |

Optionale Felder: `einheit` (bei `punkt`, z. B. `Mio EUR`), `toleranz` (bei `punkt`,
z. B. `0.10` = ±10 % für die Nebenfrage „innerhalb Korridor"), `verfall_am` (Datum,
ab dem eine unaufgelöste Wette als verfallen gilt; Standard: `pruefung_am` + 2 Jahre),
`ersetzt_durch` (id), `tags`.

### 1.2 Prognosen

Jede Prognose hat `von`, `wert`, `hinterlegt_am`, `art`.

- `wert` bei `ja_nein`: Wahrscheinlichkeit 0,00–1,00. Bei `punkt`: Zahl in `einheit`.
- `art`:
  - `angekuendigt` — die Institution hat es ohne Vorbehalt gesagt. `wert` ist dann
    **1,00** (bzw. bei `punkt` die genannte Zahl). Wer „wird fertig" sagt, hat 100 %
    gesagt.
  - `voraussichtlich` — die Aussage trug einen Vorbehalt („voraussichtlich",
    „geplant", „soll"). `wert` **0,80**. Die Übersetzungsregel steht im Textteil.
  - `geschaetzt` — eine Seite hat aktiv eine Zahl hinterlegt (Computer, Halter,
    Dritte).
- Die Institution steht immer als erste Prognose. Sie hat nicht gewettet — sie hat
  gesprochen. Das Buch nimmt sie beim Wort.

### 1.3 Regeln für Einträge

1. **Ohne Quelle keine Wette.** `quelle` muss öffentlich erreichbar sein. Archiv-Link
   (Wayback) zusätzlich empfohlen.
2. **Gleichzeitig hinterlegen.** Sehen sich zwei Schätzende gegenseitig, wird das im
   Vermerk festgehalten.
3. **Nichts wird geändert.** Ein Eintrag, der einmal committet ist, bekommt nur noch
   `ausgang`, `aufgeloest_am`, `beleg_ausgang` und `vermerke`. Alles andere ist
   eingefroren. Korrektur eines Tippfehlers im Kopf: neuer Eintrag mit Verweis, alter
   bleibt mit `ersetzt_durch`.
4. **Frist + Menge wird übersetzt**, nicht als eigener Typ geführt: „bis 2026 2.000
   Plätze" → `ja_nein` „Plätze am 31.12.2026 ≥ 2.000?" oder `punkt` „Plätze am
   31.12.2026?". Die Übersetzung steht im Abschnitt „Übersetzung" des Textteils.
   Beides anlegen ist erlaubt (zwei Wetten, zwei ids).
5. **Zurückgezogene Aussagen bleiben.** Sagt die Institution später etwas anderes, ist
   das eine neue Wette, keine Korrektur. Beide werden aufgelöst.

## 2. Auflösung

1. **Beleg-Pflicht.** `ausgang` darf nur auf 0/1/Zahl gesetzt werden, wenn
   `beleg_ausgang` eine öffentliche Quelle nennt, aus der der Ausgang hervorgeht. Der
   Generator lehnt Einträge mit Ausgang ohne Beleg ab (Fehler, kein Warnhinweis).
2. **Teilerfüllung ist Nein.** Bei `ja_nein` gilt die Frage wörtlich. Fertig am
   15.11. statt 31.10. → `0`, Vermerk „16 Tage später". Wer Milde will, stellt die
   Frage vorher weicher.
3. **Verfall.** Ist nach `verfall_am` kein Beleg auffindbar, wird `ausgang: verfallen`
   gesetzt, mit Vermerk, was gesucht wurde. Verfallene Wetten zählen nicht in die
   Trefferquote, aber in die Rechenschaft (3.3).
4. **Streit.** Wer den Ausgang bestreitet, bekommt einen Vermerk mit seiner Sicht und
   Quelle. Der Ausgang bleibt, wie belegt. Bei zwei gleichwertigen, widersprechenden
   Belegen: `ausgang: strittig`, zählt wie verfallen.
5. **Nicht vor `pruefung_am`.** Auch wenn das Ergebnis früher bekannt ist.

## 3. Bewertung

### 3.1 Ja/Nein — Brier-Score

`brier = (wert − ausgang)²`, ausgang ∈ {0, 1}. Kleiner ist besser. 0,25 ist der Wert
von „50 %, keine Ahnung". Eine `angekuendigt`-Prognose, die eintritt: 0,00; die nicht
eintritt: 1,00.

### 3.2 Punkt — Abstand

`abstand = |wert − ausgang|` in `einheit`. Verglichen wird nur zwischen Prognosen
derselben Wette: „näher dran" gewinnt. Ist `toleranz` gesetzt, entsteht zusätzlich die
Ja/Nein-Nebenfrage „Institution innerhalb ±toleranz?", für die Schätzende eine
Wahrscheinlichkeit hinterlegen können — damit auch hier ein Brier-Wert entsteht.
Bei gleichem Abstand gewinnt niemand; die Wette zählt für alle Beteiligten als
gewertet.

### 3.3 Je Prognostizierendem (Institution, Computer, Halter, …)

- **Trefferquote** = Mittelwert der Brier-Werte aller aufgelösten `ja_nein`-Wetten.
- **Näher dran** = „x von y" über alle aufgelösten `punkt`-Wetten mit ≥2 Prognosen.
- **Rechenschaft** = Anzahl verfallener/strittiger Wetten, bei denen dieser
  Prognostizierende die Institution war — neben der Anzahl Wetten insgesamt. Eine
  Institution, die nichts Prüfbares sagt, hat leere Trefferquote und volle
  Rechenschaftsspalte.

### 3.4 Rangliste

- Sortiert nach Trefferquote, aufsteigend.
- **Ein Rang erst ab 10 aufgelösten `ja_nein`-Wetten.** Darunter erscheint der
  Eintrag ohne Platz: „7 von 10 — noch kein Rang", Schnitt sichtbar.
- Ja/Nein und Punkt werden nicht verrechnet; Punkt steht als eigene Spalte.
- **Der Computer steht in derselben Liste**, mit denselben Regeln. Kein Sonderstatus.
- Ein Prognostizierender ist innerhalb eines Buchs derselbe, wenn `von` gleich ist.
  Ein Verzeichnis über Bücher hinweg ist nicht Teil von v1.

## 4. Das Buch

`BUCH.md` im Wurzelordner, YAML-Kopf:

```yaml
---
titel: Köln gegen Köln
halter: Felix Lind
kontakt: https://…
seit: 2026-08-28
lizenz: CC0
format: v1
---
```

Darunter frei: Worum es geht, wie ausgewählt wird, wie man Fehler meldet.

Der Halter verpflichtet sich zu nichts außer den Regeln in diesem Dokument. Er wählt
die Behauptungen aus; deshalb steht sein Name dran, und deshalb darf jede Institution
ihr eigenes Buch führen, das dieselben Regeln nutzt.

## 5. Der Generator (Referenz-Implementierung)

Ein Programm, das aus einem Buch-Ordner eine statische Seite baut. Anforderungen:

1. Liest alle `*.md` mit YAML-Kopf (außer `BUCH.md`), validiert gegen Abschnitt 1
   (Pflichtfelder, Typen, Beleg-Pflicht bei Auflösung, `pruefung_am` ≤
   `aufgeloest_am`, eindeutige ids). Fehler → Abbruch mit Dateiname und Feld.
2. Berechnet 3.1–3.4.
3. Erzeugt: Startseite (Rangliste, Rechenschaft), eine Seite je Institution (alle
   Wetten), eine Seite je Wette (Kopf lesbar + Textteil), ein `wettbuch.json` mit
   allen Einträgen für Maschinen.
4. Keine Datenbank, kein Server, keine externen Dienste zur Laufzeit. Ergebnis ist
   ein Ordner mit HTML, hostbar auf GitHub Pages oder jedem Webspace.
5. Reproduzierbar: Derselbe Ordner erzeugt dieselbe Seite. Kein Datum „heute" im
   Output außer dem Build-Zeitstempel im Footer.

Sprache der Referenz-Implementierung: Python 3, keine Abhängigkeiten außer
`pyyaml` und `markdown`. Andere Implementierungen sind ausdrücklich erwünscht; das
Format ist die Vereinbarung, nicht der Code.

Die Referenz-Implementierung kann mit `alle` mehrere Bücher aus einem Ordner bauen
und eine Übersicht erzeugen; die Übersicht ist kein Verzeichnis im Sinne von §6, nur
eine lokale Liste.

## 6. Was v1 nicht tut

- Kein Verzeichnis aller Wettbücher. (Später: eine Datei, die Bücher auflistet — auch
  nur ein Format.)
- Keine Prognosen mit Verteilungen oder Intervallen. Punkt + Toleranz reicht.
- Keine Gewichtung nach Wichtigkeit der Wette. Alle zählen gleich.
- Keine Identitätsprüfung der Schätzenden. Wer im Buch steht, steht drin, weil der
  Halter ihn eingetragen hat.
- Keine automatische Auflösung. Jeder Ausgang wird von Hand belegt.
- Die Nebenfrage aus §3.2 („Institution innerhalb ±toleranz?") wird nicht automatisch
  berechnet; `toleranz` wird gelesen und angezeigt, mehr nicht.
- Kein „zählt nicht"-Kennzeichen für Prognosen, die nach dem Ereignis hinterlegt
  wurden; das steht nur im Vermerk.

## 7. Versionierung

Dieses Dokument ist v1. Änderungen, die bestehende Einträge ungültig machen, ergeben
v2. Ein Buch nennt in `BUCH.md`, welcher Version es folgt.
