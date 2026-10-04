# Dortmund: die sechs „kein Treffer“-Zitate nachgeprüft (04.10.2026)

Dauerlauf, 04.10.2026 ~06:05–06:25. Grundlage: `recherche/wortlaut-vorschlaege.csv`, Bewertung `kein_treffer`,
nur `dortmund-*` (6). Je Wette die Archivkopie aus der CSV (`id_`-Abruf mit `requests`) gelesen. Wettdateien unverändert.

| Wette | Archivkopie | Ergebnis |
|---|---|---|
| dortmund-2025-005 | 20241113015424 (Ruhr Nachrichten) | **Befund A.** Standortzahlen und Termin stehen nicht in der Quelle. |
| dortmund-2025-006 | 20241113015424 | **Befund A.** wie -005 |
| dortmund-2025-007 | 20241113015424 | **Befund A.** wie -005 |
| dortmund-2025-012 | 20260515015057 (airportzentrale.de) | **gedeckt.** van Bebber: „Unser sehr ambitioniertes Ziel ist es, dass Passagiervolumen des Jahres 2024 auch in 2025 zu erreichen.“ und „Wir erwarten für das Gesamtjahr ein Passagiervolumen von 3,1 Millionen Reisenden“. Das Zitat der Wette ist eine Umschreibung; Wortlaut-Vorschlag aus der CSV passt. |
| dortmund-2025-013 | 20250119094950 (electrive.net) | **Befund B.** 155/55 Mio sind eine Vergleichsrechnung, kein Plan. |
| dortmund-2025-014 | 20250119094950 | **Befund B.** wie -013 |

## Befund A: Kita-Wetten 005–007 zitieren die falsche Quelle mit dem falschen Datum

Die Ruhr-Nachrichten-Kopie vom 13.11.2024 (Artikel vollständig, keine Bezahlschranke im Text) und die städtische
Pressemitteilung zum Wirtschaftsplan (dortmund.de, „163 Millionen und 174 Millionen Euro …“) sagen nur:

> „Bis Ende 2025 sollen vier Einrichtungen an den Standorten Burgweg (Innenstadt-Nord), Kleyer Weg (Lütgendortmund),
> Buschei (Scharnhorst) und Schragmüllerstraße (Mengede) mit insgesamt [26 Gruppen und] 491 Betreuungsplätzen eröffnet werden.“

Platzzahl je Standort, Gruppen und die Starttermine 1.10./1.12. stehen dort **nicht**. Sie stammen aus einer
späteren Meldung der Stadt:

- **dortmund.de, „Jetzt anmelden: FABIDO eröffnet drei neue Kitas“**, `datePublished` **2025-07-07**,
  https://www.dortmund.de/newsroom/nachrichten-dortmund.de/jetzt-anmelden-fabido-eroeffnet-drei-neue-kitas.html
  - live abgerufen 04.10.2026, SHA-256 `d1c4a1fdad6c8f9da6767465bbd2232155bbbe6f58ed4630c5a21f565473a674`,
    lokale Kopie `recherche/belege/2026-10-04-dortmund-fabido-drei-neue-kitas-2025-07-07.html`
  - Wayback neu gespeichert **20261004040434** (id_-Abruf HTTP 200, Stellen enthalten); ältere Kopie 20260511054905
  - Wortlaut: „Beide Kitas eröffnen zum 1. Oktober. In Scharnhorst eröffnet die Kita Buschei zum 1. Dezember.“ ·
    „Sie wird über zehn Gruppen und 200 Plätze verfügen. […] Die Betreuung startet zum 1. Oktober.“ ·
    „72 Plätze wird es in der Kita Kleyer Weg in Lütgendortmund geben. […] Start: 1. Oktober.“ ·
    „Zum 1. Dezember startet die Kita Buschei in Scharnhorst mit sechs Gruppen und 108 Plätzen …“
- Ruhr Nachrichten berichten dasselbe am 09.07.2025 (`datePublished` 2025-07-09, w1051543), Pressewiedergabe.

**Folge:** `gesagt_am` und `hinterlegt_am` 2024-11-12 sind falsch; die Stadt hat die Termine am 07.07.2025 genannt,
also rund drei statt elf Monate vorher (Buschei: knapp fünf statt zwölf Monate). Ausgänge bleiben: 005 JA, 006 JA,
007 NEIN (Buschei erst 01.06.2026). Für die Wertung ändert sich nur der Vorhersage-Abstand; die Bilanz der Stadt wird
dadurch nicht besser oder schlechter, aber das Buch behauptet eine frühere Festlegung, als es sie gab.

**Vorschlag (Frage an Felix, nichts geändert):** in 005–007 `quelle` auf die dortmund.de-Meldung, `gesagt_am` und
`hinterlegt_am` auf 2025-07-07, `zitat` wörtlich aus den Stellen oben, Vermerk „Quelle korrigiert 04.10.2026“.
Optional eine neue Wette aus dem Satz vom 12.11.2024 („vier Einrichtungen … bis Ende 2025“), Ausgang NEIN
(Buschei 01.06.2026; Schragmüllerstraße ungeklärt).

## Befund B: Dieselbus-Wetten 013/014 werten eine Rechnung als Ankündigung

Wortlaut electrive.net (21.10.2024, beruft sich auf Ruhr Nachrichten hinter Bezahlschranke):

> „Daher wird in dem Artikel kalkuliert, dass die bisherigen E-Bus-Pläne mit knapp 200 statt 155 Fahrzeugen rund
> 140 Millionen Euro kosten würde – eine reine Diesel-Neubeschaffung von 155 Bussen aber nur 55 Millionen Euro.“

> „Konkret heißt das, dass bei zwölf ausgemusterten Altfahrzeugen pro Jahr nur noch acht durch einen E-Bus ersetzt
> werden sollen und zusätzlich vier neue Diesel angeschafft werden.“

- 155 Busse / 55 Mio € sind ein Kostenvergleich („würde … kosten“) für einen hypothetischen Komplett-Ersatz, gerechnet
  „in dem Artikel“, nicht von DSW21 als Plan angekündigt. Das Zitat der Wette („155 neue Dieselbusse für rund 55 Mio. €
  geplant“) steht so nirgends. `gesagt_von` Fligge ist für diese Zahlen nicht belegt (Fligge wird nur zu Mehrkosten
  und Förderung zitiert). Deckt sich mit dem Vermerk vom 30.08.2026 („155 war der Bestand“).
- Angekündigt war laut Bericht: **vier Diesel pro Jahr** (acht E-Busse plus vier Diesel bei zwölf Ausmusterungen).
- Beide Wetten sind offen (Ausgang null, Prüfung seit 01.01.2026 überfällig), es ist also noch nichts falsch gewertet.

**Vorschlag (Frage an Felix, nichts geändert):** 013 und 014 mit Vermerk „keine Ankündigung, Rechnung der Presse“
schließen (nicht werten). Falls ersetzt werden soll: eine Wette „Beschafft DSW21 im Jahr 2026 höchstens vier neue
Dieselbusse?“ aus dem Satz oben — Quelle ist allerdings nur Pressewiedergabe einer Pressewiedergabe; besser erst die
DSW21-Stellungnahme (wirindortmund, Okt. 2024, im Vermerk 30.08. genannt) wörtlich prüfen.

Verbleibend „kein Treffer“: Bonn 17, Essen 13.
