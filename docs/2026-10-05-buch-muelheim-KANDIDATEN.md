# Buch „Mülheim gegen Mülheim" — Kandidaten, recherchiert am 05.10.2026

Status: **9 Wetten angelegt** (`buecher/muelheim/wetten/muelheim-2026-001` bis `-009`), Zweig `buch-muelheim`,
nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag 05.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Hamm 179 272 (Buch seit 05.10.2026),
**Mülheim an der Ruhr 172 031** (in der PDF an drei Stellen gleich: Tabelle der kreisfreien Städte, Tabelle
der Bevölkerungsbewegung, Gemeindeverzeichnis). Danach folgen Leverkusen 168 262 und Solingen 165 193 (beide
an denselben drei Stellen gleich gelesen).

**Methode:** Die Stadt hat ihre Seiten auf `cms.muelheim-ruhr.de` (Drupal); `www.muelheim-ruhr.de` leitet
die Startseite dorthin um, Unterseiten unter `www` antworten mit 404. Die Seite
`https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen` (abgerufen 05.10.2026, 205 312 Bytes,
nicht im Repository) listet 191 Meldungen auf einer Seite, ohne Blättern, jede mit Datum: 06.01.2026 bis
01.10.2026 (Januar 13, Februar 21, März 18, April 22, Mai 23, Juni 19, Juli 25, August 24, September 24,
Oktober 2). 106 Adressen liegen unter `/rathaus/aktuelles/aktuelle-meldungen/`, 85 an anderen Stellen der
Seite (Sport, Stadtraum, IGA, Ämter). Alle 191 einzeln abgerufen (alle HTTP 200); Text aus dem Block
`article.node`, Datum aus der Liste. Die Seiten selbst tragen das Datum nur in den eingebetteten
Strukturdaten (`datePublished`); bei 173 Seiten ist es dasselbe wie in der Liste, 18 Seiten (keine Meldungen
im engen Sinn) haben keins. Zwei Suchläufe über alle Sätze: (1) Jahreszahlen 2027 bis 2030, „Ende 2026",
„Jahresende", „bis Ende", „im Oktober/November/Dezember", „Herbst/Winter 2026", „im Frühjahr", „Quartal",
„voraussichtlich", „geplant", „soll … fertig/abgeschlossen/eröffnet/beginnen/starten": 36 Meldungen mit
Treffer, 54 Sätze; (2) „Fertigstellung", „abgeschlossen", „Eröffnung", „Inbetriebnahme", „Baubeginn",
„Spatenstich", „Bauzeit", „dauern", „nächstes/kommendes Jahr", Ratsbeschlüsse: 40 Meldungen, 47 weitere
Sätze. Alle Treffersätze gelesen, 11 Meldungen ganz gelesen.
**Grenzen der Methode:** Die Liste beginnt im Januar 2026; ältere Meldungen (und damit ältere Zusagen für
2026/2027) sind über sie nicht erreichbar. **Die Liste ist nicht vollständig:** Zwei Meldungen, die am
05.10.2026 auf der Startseite standen, fehlen in ihr (007 Hauskampbrücke, veröffentlicht 15.09.2026, und die
ADFC-Umfrage vom 14.09.2026, ohne Vorhaben der Stadt). Warum, und wie viele Meldungen sonst fehlen, ist
ungeklärt. Nicht angesehen: Ratsinformationssystem, Haushaltsplan, Amtsblatt, die Seiten der Beteiligungen
(MST, medl, Ruhrbahn), die Projektseiten zur IGA 2027.

**Zugriff:** `robots.txt` von `cms.muelheim-ruhr.de` (abgerufen 05.10.2026) ist die Drupal-Standarddatei
(gesperrt sind Verwaltungs-, Such- und Anmeldepfade, nicht die Meldungen). Abrufe mit gekennzeichnetem
Agenten, rund eine Seite je zwei Sekunden: Startseite, Liste, 193 Meldungen, sieben davon ein zweites Mal.

Jedes Zitat steht wörtlich im ersten Abruf und im zweiten (beide Male die Seite der Meldung, getrennte
Abrufe am selben Mittag), 9 von 9; der Titel der Meldung steht im zweiten Abruf, 9 von 9.

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „vorgesehen", „voraussichtlich"; sonst
„angekuendigt" (1,00), wie FORMAT.md §1.2. Acht Aussagen tragen einen Vorbehalt, eine nicht (002).

**Archivbefund:** 8 von 9 Wetten haben eine Archivkopie, in der das Zitat wörtlich steht (sechs Adressen:
fünf Aufnahmen vom 05.10.2026; für die Sporthallen-Meldung, 008 und 009, eine ältere Aufnahme vom
12.04.2026, weil Save Page Now dort heute mit HTTP 520 antwortete). Byte-gleich mit der lokalen Kopie ist
keine (die Seiten enthalten wechselnde Teile). **Nicht archiviert: 001 (Brücke Saarner Straße).** Save Page
Now antwortete zweimal mit HTTP 404, nannte danach die Aufnahme `20261005102106`, die sich am selben Tag
nicht abspielen ließ (404); die Stadt selbst antwortet für die Adresse mit 200. Ursache ungeklärt. Für 001
trägt nur die lokale Kopie mit SHA-256. Lokale Kopien: `recherche/belege/2026-10-05-muelheim-<Kurzname>.html`.

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 21.08.2026 | Belag Brücke Saarner Straße: neun Wochen ab 24.08.2026 | 26.10.2026 | 0,80 | 0,50 |
| 002 | 22.04.2026 | Heimatpreis 2026 im Dezember 2026 prämiert | 01.01.2027 | 1,00 | 0,85 |
| 003 | 18.09.2026 | Grundwasservorerkundung im Straßenraum im Herbst/Winter 2026 | 01.03.2027 | 0,80 | 0,55 |
| 004 | 18.09.2026 | dauerhafte Grundwassermessstellen im Frühjahr 2027 errichtet | 01.06.2027 | 0,80 | 0,35 |
| 005 | 20.02.2026 | neues Hallenbad Heißen im Frühjahr 2027 fertig | 01.06.2027 | 0,80 | 0,40 |
| 006 | 28.05.2026 | Erweiterungsbau Barbaraschule zum Schuljahr 2027/2028 fertig | 01.10.2027 | 0,80 | 0,50 |
| 007 | 21.09.2026 | Hauskampbrücke und Hauskampstraße: rund 15 Monate ab 21.09.2026 | 01.01.2028 | 0,80 | 0,30 |
| 008 | 04.03.2026 | Baubeginn Dreifachsporthalle Luisenschule Anfang 2028 | 01.04.2028 | 0,80 | 0,45 |
| 009 | 04.03.2026 | Dreifachsporthalle Luisenschule zum Schuljahr 2029/2030 fertig | 01.10.2029 | 0,80 | 0,30 |

## Lesarten, die der Halter ändern kann

- **001 und 007 nennen eine Dauer, kein Datum.** 001: „voraussichtlich neun Wochen" ab Montag 24.08.2026,
  gerechnet bis Sonntag 25.10.2026, ohne Puffer. 007: „rund 15 Monate" ab 21.09.2026, wegen „rund" bis
  31.12.2027 gelesen (rechnerisch 21.12.2027). Beide Zitate verbinden zwei Sätze derselben Meldung mit „…"
  (Baubeginn und Dauer); ebenso 003 (Ausschreibung und Termin).
- **007, Datum der Aussage:** Die Seite nennt als Veröffentlichung den 15.09.2026, der Text spricht vom
  Baubeginn am 21.09.2026 in der Vergangenheit, wurde also später überarbeitet. `gesagt_am` ist der
  21.09.2026 (frühester möglicher Tag); belegt ist der Wortlaut erst am 05.10.2026. Eine ältere Archivkopie
  gibt es nicht.
- **002, Heimatpreis:** Die Stadt lobt den Preis gemeinsam mit dem Centrum für bürgerschaftliches Engagement
  aus; der Satz steht ohne Vorbehalt, deshalb 1,00. Eine kleine Wette, aber die einzige ohne Vorbehalt.
- **003 und 004, Grundwasser:** zwei Wetten aus einer Meldung, 004 hängt an 003. Die Beleglage wird dünn
  sein (kleine Maßnahme, vermutlich keine Meldung zum Abschluss); im Zweifel Anfrage an die Untere
  Bodenschutzbehörde. Bei 004 ist „mindestens zwei Messstellen" herausgelesen (der Satz steht in der Mehrzahl).
- **005, Hallenbad:** Das Zitat ist eine Zeile der Eckdaten („Geplante Fertigstellung: Frühjahr 2027"), kein
  ganzer Satz. Gemessen wird die gemeldete Fertigstellung, Übergabe oder Eröffnung.
- **006 und 009, „zum Schuljahr":** Stichtag 30.09. des Jahres, wie im Buch Bonn (Ferienende NRW nicht
  nachgeschlagen).
- **008 und 009:** zwei Wetten aus einem Satz (Baubeginn und Fertigstellung der Sporthalle).

## Draußen

- Dritte Aussage der Grundwasser-Meldung („Die Untersuchungen im Bereich der Spielplatzfläche ist für Sommer
  2027 geplant"): hängt an 003 und 004, Beleglage noch dünner.
- Fritz-Thyssen-Brücke („Ein Abriss der Fritz-Thyssen-Brücke ist nicht vor 2029 geplant", 05.05.2026):
  Verneinung ohne Vorhaben.
- Wasserbahnhof (Sanierung durch die Mülheimer Stadtmarketing und Tourismus GmbH; Biergarten „öffnet
  voraussichtlich Ende März wieder", Termin vorbei): Vorhaben einer Gesellschaft, kein Datum in der Zukunft.
- ADAC-Radservice-Stationen („Bis Ende 2026 sollen weitere acht Standorte hinzukommen"): Aussage über den
  ADAC Nordrhein, nicht über die Stadt.
- CO₂-Pipeline: Vorhaben Dritter, die Stadt lädt nur zur Information ein.
- Ruhrinselweg („Fertigstellung in den Sommerferien", 03.02.2026) und alle Straßenbaustellen mit Dauer bis
  Sommer 2026: Termin vor dem 05.10.2026; ob gehalten, nicht geprüft.
- Sportanlage Mintarder Straße (Spatenstich 22.05.2026, Laufbahn rund 3,5 Mio. €, Skatepark rund
  1,2 Mio. €): die Meldung nennt kein Fertigstellungsdatum.
- Fortschreibung des Nahverkehrsplans, IGA-2027-Projekte („Grüner Stadtring", „MüGa revisited"): kein Satz
  mit Vorhaben und Datum in den Meldungen der Liste.

## Vor dem Merge

- Kommt der Push nach **Sa 24.10.2026**, `muelheim-2026-001` vorher verwerfen (Stichtag So 25.10.2026); nach
  Mi 30.12.2026 auch `-002`.
- Beiläufig prüfen, ob die Aufnahme `20261005102106` der Saarner-Straße-Meldung inzwischen abspielbar ist
  (`https://web.archive.org/web/20261005102106/<Adresse>`); wenn ja und das Zitat darin steht, den Vermerk in
  001 ergänzen.
- Mo 26.10.2026: 001 auflösen (nur wenn das Buch vorher öffentlich war).
