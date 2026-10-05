# Buch „Aachen gegen Aachen" — Kandidaten, recherchiert am 05.10.2026

Status: **13 Wetten angelegt** (`buecher/aachen/wetten/aachen-2026-001` bis `-013`), Zweig `buch-aachen`,
nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag 05.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Gelsenkirchen 267 733 (Zweig
`buch-gelsenkirchen`), Mönchengladbach 266 840 (Zweig `buch-moenchengladbach`), **Aachen 262 211**, Krefeld
231 116. Beim nächsten Buch nach dieser Regel ist Krefeld dran.
**Berichtigung:** In den Büchern Gelsenkirchen und Mönchengladbach stand für Aachen 263 948; das ist in der
Tabelle die Zahl des Kreises Heinsberg. Am 05.10.2026 an der PDF nachgelesen (Zeile „05 334 002 Aachen,
kreisfreie Stadt … 262 211") und auf beiden Zweigen berichtigt. Die Reihenfolge ändert sich nicht.

**Methode:** Die Liste unter `https://www.aachen.de/services/presse/pressemitteilungen/` wird per Skript
nachgeladen und ist ohne Browser nicht blätterbar. Aufgezählt über die Sitemap der Stadt
(`https://www.aachen.de/sitemap.xml`, abgerufen 05.10.2026): 664 Adressen unter
`/services/presse/pressemitteilungen/2026/` (Januar 80, Februar 73, März 83, April 80, Mai 63, Juni 78,
Juli 78, August 46, September 76, Oktober 7). Alle 664 im Volltext abgerufen (2 s Abstand, kein Fehler),
Text von HTML befreit und nach Sätzen mit Zukunftstermin durchsucht: 72 Meldungen mit Treffer, von Hand gelesen.
**Grenze der Methode:** Die Sitemap ist die Liste der Stadt; ob sie jede Meldung enthält, ist nicht geprüft.
Meldungen vor dem 01.01.2026 (Sitemap: 953 aus 2025, 209 aus 2024) sind nicht angesehen.

**Zugriff:** aachen.de hat keine robots.txt (HTTP 404). Die Fehlerseite trägt den Vermerk
`noai, noindex, nofollow, noarchive`; Startseite, Presseliste und die Meldungsseiten tragen keinen
Robots-Vermerk, es gibt keine `tdmrep.json`, keine `ai.txt` (alle am 05.10.2026 geprüft).

Jedes Zitat steht wörtlich im ersten und in einem zweiten Abruf (13 Quellen, 13 von 13). Bei 012 kodiert
die Quelle das „ü" in „für" als u mit Trema-Zeichen (U+0308); verglichen wurde nach Unicode-Vereinheitlichung (NFC).

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „vorgesehen", „voraussichtlich"; sonst
„angekuendigt" (1,00), wie FORMAT.md §1.2. Fünf der dreizehn Aussagen stehen ohne Vorbehalt (002, 005, 010, 011, 013).

**Abgrenzung:** Aufgenommen sind nur Sätze aus dem Mitteilungstext der Stadt über Vorhaben der Stadt und des
Aachener Stadtbetriebs (003, 011). Vorhaben von Regionetz, ASEAG, Sparkasse und StädteRegion bleiben draußen.

**Archivbefund:** 13 von 13 Quellen haben eine Wayback-Kopie vom 05.10.2026 (Save Page Now, 30 s Abstand; bei
den Quellen 1, 2 und 4 meldete die Sicherung zuerst HTTP 520, die Kopien lagen nach dem zweiten bzw. dritten
Anlauf vor), das Zitat steht in jeder Archivkopie wörtlich. Keine Kopie ist byte-gleich mit der lokalen
(dynamische Seitenteile). Lokale Kopien des zweiten Abrufs: `recherche/belege/2026-10-05-aachen-<Kurzname>.html`,
je rund 170 bis 210 KB (zusammen rund 2,3 MB), SHA-256 im Vermerk jeder Wette.

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 17.07.2026 | Skateanlage Schagenstraße (Brand), Verbindungsweg gesperrt bis Ende Oktober 2026 | 01.11.2026 | 0,80 | 0,40 |
| 002 | 18.09.2026 | Premiumfußwege, Info-Tafeln an den zehn Zielorten noch im Herbst 2026 | 01.12.2026 | 1,00 | 0,35 |
| 003 | 02.10.2026 | Brücke Münsterstraße (Rollefbach), fertig im Dezember 2026 | 01.01.2027 | 0,80 | 0,35 |
| 004 | 28.07.2026 | Ulla-Klinger-Halle, Sanierung Ende Februar 2027 abgeschlossen | 01.03.2027 | 0,80 | 0,45 |
| 005 | 11.09.2026 | Freibad Hangeweiher öffnet am 1. Mai 2027 (Eichwette) | 02.05.2027 | 1,00 | 0,85 |
| 006 | 22.07.2026 | Krönungssaal, Augmented-Reality-Führung ab Mitte 2027 | 01.08.2027 | 0,80 | 0,35 |
| 007 | 30.07.2026 | Altes Polizeipräsidium (Sportpark Soers), Rückbau im Sommer 2027 fertig | 01.09.2027 | 0,80 | 0,45 |
| 008 | 09.06.2026 | Bismarckstraße, Bauarbeiten im Sommer 2027 abgeschlossen | 01.09.2027 | 0,80 | 0,40 |
| 009 | 16.09.2026 | Klappergasse/Rennbahn, Baubeginn im Herbst 2027 | 01.12.2027 | 0,80 | 0,35 |
| 010 | 29.01.2026 | Theaterstraße, Bauarbeiten Ende 2027 abgeschlossen | 01.01.2028 | 1,00 | 0,35 |
| 011 | 08.01.2026 | Hahner Straße, Indestützmauer bis Ende 2027 saniert | 01.01.2028 | 1,00 | 0,40 |
| 012 | 16.07.2026 | Theaterplatz, Umgestaltung bis Ende 2028 | 01.01.2029 | 0,80 | 0,30 |
| 013 | 09.03.2026 | Haus der Neugier (ehemals Horten), umgestaltet bis 2029 | 01.01.2030 | 1,00 | 0,25 |

**Zeitfenster:** 001 (Stichtag 31.10.2026) ist nur ehrlich, wenn das Buch vor dem Stichtag öffentlich ist; sonst
vor dem Merge verwerfen. 002 entsprechend bis 30.11.2026, 003 bis 31.12.2026.

## Verworfen

- Theaterplatz, Meldung vom 29.01.2026: „rechnet die Stadt bis zum Ende des Jahres 2028" (durch die Aussage vom
  16.07.2026 vertreten, 012), „im Laufe des Jahres 2027" (Theaterboulevard, weicher als der Satz in 010),
  Nordseite „im Laufe des Jahres 2028" (in 012 enthalten).
- Bismarckstraße, Meldung vom 22.05.2026 („Nach bisheriger Planung … Sommer 2027"): gleiche Aussage wie 008, die jüngere steht.
- Altes Polizeipräsidium: „Rückbau bis Mitte 2027 geplant" (Zwischenüberschrift) und „bis ca. Mai 2027": derselbe
  Rückbau wie 007, dort steht der ausformulierte Satz.
- Haus der Neugier, 04.03.2026 („ab 2029"): Nebensatz in einer Meldung über Schaufenster, 013 trägt die Aussage.
- Adenauerallee (26.06.2026, „voraussichtlich bis Ende 2026"): Bauherr ist der Netzbetreiber Regionetz.
- Elisenbrunnen (22.04.2026, „voraussichtlich bis zum Frühjahr 2028"): Sanierung des Sparkassengebäudes, kein Vorhaben der Stadt.
- Euregiobike (10.09.2026, Übernacht-Tarif und Rabatt „bis Ende des Jahres"): Umsetzung durch ASEAG, Nextbike und App-Entwickler.
- Haarbachtal (17.04.2026, Renaturierung „voraussichtlich bis zum Jahresende 2026"): Bauherr im Text nicht genannt
  (im Zusammenhang mit dem Neubau der Haarbachtalbrücke), Abschluss von außen kaum belegbar.
- Friedhofsentwicklungskonzept („läuft … noch bis Ende des Jahres 2026") und Verkehrsprojekt „DiMoGro" (bis Ende
  Juni 2027): Projektlaufzeiten, kein zählbares Ergebnis.
- Neuer Kämmerer ab 01.01.2027 (16.07.2026): Personalie mit Ratsbeschluss, keine Ankündigung eines Vorhabens.
- Klimaneutralität 2030: die Stadt sagt am 02.04.2026 selbst, das Zieljahr sei „leider nicht zu halten"; keine neue Zahl mit Datum.
- Nachpflanzung Krefelder Straße/Salierallee (Pflanzsaison 2026/2027): von außen kaum belegbar.
- Ausstellungen, Spielzeiten, Trautermine, Schulanmeldung, Chorbiennale 2027: Veranstaltungskalender.
- StädteRegion (Schwimminitiative), Olympia-Bewerbung, Land NRW (Wohnraumförderung): Dritte.

Nicht angesehen: Ratsinformationssystem, Haushaltsplan-Entwurf 2027, Meldungen vor dem 01.01.2026.
