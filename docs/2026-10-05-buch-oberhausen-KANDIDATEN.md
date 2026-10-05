# Buch „Oberhausen gegen Oberhausen" — Kandidaten, recherchiert am 05.10.2026

Status: **12 Wetten angelegt** (`buecher/oberhausen/wetten/oberhausen-2026-001` bis `-012`), Zweig
`buch-oberhausen`, nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag
05.10.2026, im Dauerlauf (Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Aachen 262 211 (Zweig `buch-aachen`),
Krefeld 231 116 (Zweig `buch-krefeld`), **Oberhausen 213 349** (in der PDF an drei Stellen gleich: Tabelle der
kreisfreien Städte, Tabelle der Bevölkerungsbewegung, Gemeindeverzeichnis). Danach folgen Hagen 189 704, Hamm
179 272, Mülheim an der Ruhr 172 031, Leverkusen 168 262, Solingen 165 193 (aus dem Gemeindeverzeichnis der PDF
gelesen; vor dem nächsten Buch die Zahl der Stadt an einer zweiten Stelle der PDF gegenlesen).

**Methode:** Die Stadt führt eine blätterbare Liste ihrer Pressemeldungen unter
`https://www.oberhausen.de/de/index/rathaus/aktuelle-pressemeldungen.php?pagePresse=N&aktYear=` (10 je Seite,
neueste zuerst). Seiten 1 bis 41 abgerufen (05.10.2026), ab Seite 40 kamen keine neuen Einträge mehr: 385
Meldungen, älteste vom 05.01.2026 (Januar 33, Februar 28, März 49, April 51, Mai 42, Juni 50, Juli 45, August
31, September 49, Oktober 7). 383 im Volltext abgerufen (2 s Abstand); zwei Bekanntmachungen „Ruhezeiten von
Reihengräbern sind abgelaufen" ließen sich nicht abrufen (Leerzeichen in der Adresse) und sind nicht gelesen.
Text des Artikelbereichs von HTML befreit und nach Sätzen mit Zukunftstermin durchsucht (Jahreszahlen 2027 bis
2039, „Ende Oktober/November/Dezember", „Ende des Jahres", „Jahresende", „Herbst/Winter 2026", „viertes
Quartal"): 61 Meldungen mit Treffer, von Hand gelesen. Zweite Suche nach Terminen ohne Jahreszahl („im
kommenden/nächsten Jahr", „im Herbst/Winter", „im November/Dezember", „Herbst dieses Jahres", „zweiten
Halbjahr", für Meldungen ab Juni auch „voraussichtlich bis/im/Ende" und „bis Ende <Monat>"): daraus kam die
Wette 008 (Nachwuchskräfte) und der Kontext zu 005.
**Grenzen der Methode:** Ob die Liste vollständig ist, ist nicht geprüft (die Stadt führt daneben ein Archiv
je Jahr; für 2026 nicht dagegen gehalten). Meldungen vor dem 01.01.2026 sind nicht angesehen. Sätze, die einen
Termin nur als Wochentag oder Tagesdatum ohne die Suchwörter nennen, findet keine der beiden Suchen.

**Zugriff:** `robots.txt` (abgerufen 05.10.2026) sperrt nur `/administration/`. `tdmrep.json`, `ai.txt` und
`sitemap.xml` gibt es nicht (die Adressen leiten auf die Startseite um). Seitenkopf der Presseliste und der
Meldungen: `index, follow`; kein `X-Robots-Tag`.

Jedes Zitat steht wörtlich im ersten und in einem zweiten Abruf (12 Quellen für 12 Wetten, 12 von 12).
Verglichen wird nach Entfernen unsichtbarer Trennzeichen (weiche Trennstriche, breitenlose Leerzeichen) und
mehrfacher Leerzeichen; die Seite der Stadt setzt solche Zeichen in einzelne Meldungen. Die Meldung zu 006
(Pocket-Park) hat auf der eigenen Seite keine Überschrift; der Titel im Eintrag stammt aus der Presseliste.

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „voraussichtlich", „nach derzeitiger Planung";
sonst „angekuendigt" (1,00), wie FORMAT.md §1.2. Zwei der zwölf Aussagen stehen ohne Vorbehalt (001, 003).

**Abgrenzung:** Aufgenommen sind nur Sätze aus dem Mitteilungstext der Stadt über Vorhaben der Stadt.
Vorhaben von DB InfraGO, Emschergenossenschaft, Oberhausener Netzgesellschaft, RWW, EVO, Westnetz, Autobahn,
LVR und privaten Investoren bleiben draußen, ebenso Baustellen, die im Text den Wirtschaftsbetrieben Oberhausen
(WBO) zugeschrieben werden, und reine Kanalbaustellen ohne genannten Bauherrn. Zwei Lesarten sind Halter-Sache:
002 und 004 (Straßenausbau, Bauherr im Text nicht genannt) und 010 (Ebertbad-Gastronomie; für den Bau spricht
der Geschäftsführer der GVO Grundstücksverwaltungsgesellschaft Oberhausen mbH). Wem WBO und GVO gehören, ist
am 05.10.2026 nicht nachgeschlagen (ungeklärt).

**Archivbefund:** 12 von 12 Quellen haben eine Wayback-Kopie vom 05.10.2026 (Save Page Now), in der das Zitat
wörtlich steht (am 05.10.2026 geprüft). Keine Kopie ist byte-gleich mit der lokalen Kopie; die Seiten werden
bei jedem Abruf neu erzeugt (Sitzungskennung). Lokale Kopien des zweiten Abrufs:
`recherche/belege/2026-10-05-oberhausen-<Kurzname>.html`, je rund 285 KB (zusammen rund 3,4 MB), SHA-256 im
Vermerk jeder Wette.

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 11.08.2026 | Hans-Sachs-Berufskolleg, Steganlage im Herbst 2026 fertig | 01.12.2026 | 1,00 | 0,45 |
| 002 | 21.04.2026 | Kewerstraße/Bebelstraße, Vollsperrung bis Ende Dezember 2026 | 01.01.2027 | 0,80 | 0,40 |
| 003 | 28.08.2026 | Jahrbuch für 2027 erscheint Ende 2026 (Eichwette) | 01.01.2027 | 1,00 | 0,85 |
| 004 | 08.06.2026 | Hessenstraße, Kanal und Straßenvollausbau Ende März 2027 abgeschlossen | 01.04.2027 | 0,80 | 0,35 |
| 005 | 29.01.2026 | Ruhrpark, Baumaßnahme rechtzeitig zur IGA 2027 abgeschlossen | 24.04.2027 | 0,80 | 0,15 |
| 006 | 22.09.2026 | Pocket-Park Marktstraße, erste Vorentwürfe im Frühjahr 2027 | 01.06.2027 | 0,80 | 0,45 |
| 007 | 29.09.2026 | Gesamtkonzept Containerstandorte bis zur Sommerpause 2027 | 01.08.2027 | 0,80 | 0,40 |
| 008 | 25.08.2026 | Rund 130 Nachwuchskräfte beginnen 2027 bei der Stadt | 01.10.2027 | 0,80 | 0,60 |
| 009 | 28.09.2026 | Neue Gesamtschule an der Eschenstraße startet zum Schuljahr 2027/28 | 01.10.2027 | 0,80 | 0,65 |
| 010 | 27.04.2026 | Ebertbad-Gastronomie, Fertigstellung Dezember 2027 | 01.01.2028 | 0,80 | 0,35 |
| 011 | 20.07.2026 | NEWAG-Areal, Ergebnisse der Beteiligung Anfang 2028 | 01.04.2028 | 0,80 | 0,40 |
| 012 | 30.09.2026 | Sophie-Scholl-Gymnasium, Erweiterungsneubau im Frühjahr 2029 fertig | 01.06.2029 | 0,80 | 0,30 |

**Zeitfenster:** 001 (Stichtag 30.11.2026) ist nur ehrlich, wenn das Buch vor dem Stichtag öffentlich ist;
sonst vor dem Merge verwerfen. 002 und 003 entsprechend bis 31.12.2026.

**Lesarten, die der Halter ändern kann (vor dem Livegang):** 005 „rechtzeitig zur IGA 2027" als bis zum
Eröffnungstag 23.04.2027 (das Datum stammt aus der Meldung der Stadt Gelsenkirchen, Oberhausen schreibt nur
„im April 2027"); 007 „Sommerpause 2027" als 31.07.2027; 008 „rund 130" als mindestens 120; 009 Start der
Schule zählt, die Zahl von vier Klassen nicht; 011 „Anfang 2028" als erstes Quartal; dazu die Abgrenzung bei
002, 004 und 010 (oben). 005 ist die älteste Aussage (Januar 2026); die Stadt hat sie nicht zurückgenommen,
in der Meldung vom 10.09.2026 aber keinen Fertigstellungstermin mehr genannt.

## Verworfen

- Hessenstraße „Die gesamte Maßnahme soll bis zum 31. Juli 2026 abgeschlossen werden" (31.03.2026): Stichtag
  beim Hinterlegen verstrichen; die Stadt nennt seit 08.06.2026 Ende März 2027 (004). Steht im Kontext von 004.
- Eisenbahnbrücken Osterfelder Straße (04.03.2026: Beginn Anfang 2027, Brücke Nord Mai 2028, Süd Ende 2029,
  Straßenbau Juni 2030, Rampen Wittekindstraße Ende 2031): Bauherrin ist laut Meldung die DB InfraGO; der
  Straßenbau der Stadt hängt daran.
- Bahnhofstraße Sterkrade: Leitungsverlegung „bis Ende Januar 2027" und „November 2027" (02.07.2026):
  Versorger (RWW, EVO, Westnetz). Umbau selbst (01.10.2026, Start 05.10.2026): kein Enddatum in den Meldungen.
- Danziger Straße „voraussichtlich Ende Oktober 2026" (21.07. und 27.07.2026): Oberhausener Netzgesellschaft.
- Köperstraße „für August 2027 geplant" (20.07.2026) und Oranienstraße „rund zwei Jahre" (02.10.2026): reine
  Kanalerneuerung, Bauherr im Text nicht genannt; Oranienstraße ohne festes Datum.
- Marktstraße, Kanalbau „voraussichtlich im Sommer 2027" (17.09.2026): im Text den WBO zugeschrieben; RWW ab
  Herbst 2026.
- A516, Vollsperrung Alsfeldstraße bis November 2026 (30.06.2026): Brückenneubau an der Autobahn.
- Seniorenresidenz Sterkrade-Mitte „zum Jahreswechsel 2026/27" (11.02.2026): Übergabe an einen privaten
  Betreiber, kein Vorhaben der Stadt.
- LVR-Industriemuseum, Wiedereröffnung „im kommenden Jahr" (11.08.2026): Landschaftsverband.
- Containerstandorte: Pilotprojekte 2027 („sofern die politischen Gremien zustimmen"), Auswertung 2028,
  stadtweite Umsetzung „könnte … ab 2029" (29.09.2026): bedingt.
- Gesamtschule: Räume des Wunderhofs „voraussichtlich erst ab dem Schuljahr 2028/29" (28.09.2026): Bedarf,
  kein Vorhaben mit Termin.
- Ruhrpark „Gesamtbaustart" zum Jahresende (10.09.2026): Der Termin steht nur in einer Zwischenüberschrift
  („Weitere 15 Hektar werden zum Jahresende umgestaltet"), der Satz dazu nennt kein Datum.
- Hundebestandsaufnahme bis 28.02.2027 (24.09.2026) und Mobilfunkmessungen „bis Ende des Jahres" (22.05.2026):
  Abschluss von außen nicht belegbar.
- Citymanagement Sterkrade bis 2028 (18.02.2026): Vertragslaufzeit. Beigeordneter Motschull, Pension Ende
  August 2027 (14.07.2026): Personalie. Jugendparlament bis 2028: Amtszeit.
- Linie 105 (29.09.2026) und Musikschule im Rathaus Sterkrade (29.09.2026): kein Termin für ein Ergebnis.
- Berufsfeuerwehr stellt 2027 „voraussichtlich wieder" ein (20.04.2026, 29.05.2026): keine Zahl.
- Olympia-Bewerbung, eREGIONALE 2033, IGA-Eröffnung, Special Olympics, Förderprogramme des Landes: Dritte.
- Schulsport-Großveranstaltung 12.05.2027, Fronleichnamskirmes 2029, Lesestadt, Filmreihen, Kurse, verkaufsoffene
  Sonntage, Antragsfristen: Veranstaltungskalender.

Nicht angesehen: Ratsinformationssystem, Haushalt 2027, Meldungen vor dem 01.01.2026, das Jahresarchiv der
Pressestelle, Seiten der Stadtteilprojekte (Brückenschlag, Klima.Quartier Sterkrade).
