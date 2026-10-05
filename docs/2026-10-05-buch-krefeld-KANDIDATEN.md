# Buch „Krefeld gegen Krefeld" — Kandidaten, recherchiert am 05.10.2026

Status: **15 Wetten angelegt** (`buecher/krefeld/wetten/krefeld-2026-001` bis `-015`), Zweig `buch-krefeld`,
nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag 05.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Mönchengladbach 266 840 (Zweig
`buch-moenchengladbach`), Aachen 262 211 (Zweig `buch-aachen`), **Krefeld 231 116**. Welche Stadt danach kommt,
ist am 05.10.2026 nicht nachgeschlagen (ungeklärt; vor dem nächsten Buch in der PDF nachlesen).

**Methode:** Die Stadt führt eine blätterbare Liste aller Pressemeldungen unter
`https://www.krefeld.de/press-releases?page=N` (10 je Seite, neueste zuerst). Seiten 0 bis 72 abgerufen
(05.10.2026), bis die Liste den 19.12.2025 erreichte: 718 Meldungen mit Datum ab 01.01.2026 (Januar 46,
Februar 52, März 93, April 77, Mai 74, Juni 101, Juli 88, August 60, September 116, Oktober 11). Alle 718 im
Volltext abgerufen (2 s Abstand, kein Fehler), Text des Hauptbereichs von HTML befreit, den Block „Neuigkeiten
in …" am Seitenende abgeschnitten und nach Sätzen mit Zukunftstermin durchsucht (Jahreszahlen 2027 bis 2039,
„Ende Oktober/November/Dezember", „Ende des Jahres", „Jahresende", „Herbst/Winter 2026", „viertes Quartal"):
58 Meldungen mit Treffer, von Hand gelesen.
**Grenzen der Methode:** Sätze, die einen Termin nur mit Monat oder Jahreszeit ohne Jahr nennen („im Dezember",
„im Herbst"), findet die Suche nicht. Meldungen vor dem 01.01.2026 sind nicht angesehen. In den Seiten stehen
mitten im Text Hinweis-Kästen auf andere Seiten („Info: …", „News: …"); Sätze daraus sind nicht aufgenommen.

**Zugriff:** `robots.txt` (abgerufen 05.10.2026) sperrt nur Verwaltungs- und Suchpfade (`/admin/`, `/search/`,
`/user/…`, `/core/`), nicht die Meldungen. Keine `tdmrep.json`, keine `ai.txt` (beide HTTP 404), kein
Robots-Vermerk im Seitenkopf der Presseliste und der Startseite, kein `X-Robots-Tag` auf einer Meldungsseite.

Jedes Zitat steht wörtlich im ersten und in einem zweiten Abruf (13 Quellen für 15 Wetten, 15 von 15). Zwei
Meldungen tragen je zwei Wetten: Elfrather See (001, 015) und Stadtwaldhaus (012, 014).

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „will", „peilt an", „nach aktueller Planung";
sonst „angekuendigt" (1,00), wie FORMAT.md §1.2. Drei der fünfzehn Aussagen stehen ohne Vorbehalt (001, 012, 014).

**Abgrenzung:** Aufgenommen sind nur Sätze aus dem Mitteilungstext der Stadt über Vorhaben der Stadt, ihres
Zentralen Gebäudemanagements (ZGM) und des Kommunalbetriebs Krefeld (KBK). Vorhaben von Stadtwerken und
Netzgesellschaft Niederrhein, Zoo und privaten Investoren (Surfpark) bleiben draußen. 005 (Rheinlandhallen):
gebaut im Auftrag der Stadt. 010 (Bettensteuer) gibt einen Ratsbeschluss wieder, den die Stadt im
Mitteilungstext berichtet.

**Archivbefund:** 12 von 13 Quellen haben eine Wayback-Kopie, in der das Zitat wörtlich steht (am 05.10.2026
geprüft): zehn Kopien vom 05.10.2026 (Save Page Now, acht davon byte-gleich mit der lokalen Kopie), dazu für
006 eine Kopie vom 04.10.2026 und für 007 eine vom 06.05.2026 (die neue Sicherung meldete bei beiden HTTP 520).
Für 011 (OGS-Bericht) gibt es keine Archivkopie: Die Sicherung antwortete zweimal mit HTTP 404, obwohl die Seite
selbst erreichbar ist; nachziehen. Lokale Kopien des zweiten Abrufs: `recherche/belege/2026-10-05-krefeld-<Adresse>.html`,
je rund 125 bis 200 KB (zusammen rund 2,0 MB), SHA-256 im Vermerk jeder Wette.

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 18.09.2026 | Elfrather See, Vereinstreffpunkt am CRC-Gebäude ab Ende Oktober | 01.11.2026 | 1,00 | 0,45 |
| 002 | 07.08.2026 | Schinkenplatz, Umbau bis Ende des Jahres abgeschlossen | 01.01.2027 | 0,80 | 0,45 |
| 003 | 22.05.2026 | Notschlafstelle Feldstraße, Beginn des Umbaus zum Ende des Jahres | 01.01.2027 | 0,80 | 0,30 |
| 004 | 22.01.2026 | Inklusionsplan fertig in der ersten Jahreshälfte 2027 | 01.07.2027 | 0,80 | 0,35 |
| 005 | 16.06.2026 | Rheinlandhallen, Eröffnung im Sommer 2027 | 01.09.2027 | 0,80 | 0,50 |
| 006 | 01.10.2026 | Glockenspitzhalle, Sanierung ab Mitte 2027 | 01.09.2027 | 0,80 | 0,35 |
| 007 | 30.04.2026 | Feuerwache Gellep-Stratum, Fertigstellung Oktober 2027 | 01.11.2027 | 0,80 | 0,50 |
| 008 | 07.05.2026 | Stadtbad Neusser Straße (Freischwimmer), Bauarbeiten Ende 2027 abgeschlossen | 01.01.2028 | 0,80 | 0,35 |
| 009 | 09.06.2026 | Promenade Trift/Weiden, Baubeginn Rampe und Straße im Jahr 2027 | 01.01.2028 | 0,80 | 0,40 |
| 010 | 16.07.2026 | Bettensteuer mit Erträgen ab 2027 | 01.01.2028 | 0,80 | 0,55 |
| 011 | 13.01.2026 | Offener Ganztag, Versorgungsquote 68 Prozent bis 2027 | 01.01.2028 | 0,80 | 0,45 |
| 012 | 17.07.2026 | Stadtwaldhaus ab 1. Januar 2028 geschlossen (Eichwette) | 02.01.2028 | 1,00 | 0,80 |
| 013 | 07.09.2026 | Fabrik Heeder, Studiobühne I ab März 2028 bespielbar | 01.04.2028 | 0,80 | 0,35 |
| 014 | 17.07.2026 | Stadtwaldhaus, Grundsanierung beginnt im April 2028 | 01.05.2028 | 1,00 | 0,40 |
| 015 | 18.09.2026 | Elfrather See, Badesee-Areal fertig im Winter 2028/2029 | 01.03.2029 | 0,80 | 0,25 |

**Zeitfenster:** 001 (Stichtag 31.10.2026) ist nur ehrlich, wenn das Buch vor dem Stichtag öffentlich ist; sonst
vor dem Merge verwerfen. 002 und 003 entsprechend bis 31.12.2026.

**Lesarten, die der Halter ändern kann (vor dem Livegang):** 006 Stichtag 31.08.2027 statt 31.07.2027 („ab Mitte
2027", im selben Text „im Sommer 2027"); 010 Stichtag 31.12.2027 (Steuer wird im Jahr 2027 erhoben) statt
01.01.2027; 011 „bis 2027" als bis 31.12.2027 gemeldete Quote; 004 „Fertigstellung" als veröffentlicht oder dem
Rat vorgelegt.

## Verworfen

- Hubert-Houben-Kampfbahn: „im Mai 2027 beendet" (13.05.2026) und Baustart Ascheplatz „Ende Oktober"
  (29.06.2026): Die Stadt meldet am 18.09.2026 selbst, der Baubeginn verzögere sich, ohne neues Datum.
- Elfrather See, Multispielfeld „bis zum Jahresende" (26.06.2026): Die jüngere Meldung vom 18.09.2026 nennt für
  den vierten und fünften Bewegungspark kein Datum mehr. Badesee „Mitte 2029" (26.06.2026): durch die jüngere
  Aussage vertreten (015).
- Unterführung Weiden, Vollsperrung „bis voraussichtlich Ende Oktober" (15.07.2026): Bauherr der
  Kanalbaumaßnahme im Text nicht genannt.
- Rheinlandhallen „Bis zum Sommer 2027 soll das Bauwerk fertig sein" (29.01.2026) und „Ab Mitte 2027 … nutzbar"
  (01.10.2026): gleiche Aussage wie 005; 005 trägt den Satz zur Eröffnung.
- Fabrik Heeder „Im Dezember 2027 soll die erste Instandsetzung beendet sein" (16.03.2026): durch die Planung vom
  07.09.2026 überholt (013). Generalsanierung „im Herbst 2029": steht unter dem Vorbehalt der politischen
  Zustimmung zur gesamten Planung, Beginn von außen kaum belegbar.
- Stadtbad „soll voraussichtlich 2028 in Betrieb gehen" (07.05.2026): Betrieb durch den Verein; 008 misst den
  Abschluss der Bauarbeiten.
- Zoo, Orang-Utan-Anlage (24.02.2026 „Inbetriebnahme … für Frühjahr 2028 geplant", 23.04.2026 „für 2028
  geplant"): Vorhaben des Zoos, nicht der Stadtverwaltung.
- Surfpark (26.02.2026, 05.06.2026): privater Investor.
- Philadelphiastraße: Fernwärme „für 2027/2028 vorgesehen" (Netzgesellschaft Niederrhein), Straßenbau „bis 2029"
  hängt daran.
- Offener Ganztag „rund 80 Prozent … bis 2029" (11.03.2026): gleiche Messgröße wie 011, Prüfung erst 2030.
- Kita-Bedarfsplanung „zum Stichtag 31. Dezember 2026 noch insgesamt 571 rechnerisch fehlende Plätze"
  (05.06.2026): Planwert mit festgesetzten Quoten, laut Stadt nicht die tatsächliche Lücke.
- Bevölkerungsprognose „im Jahr 2030 bei rund 237.000" (08.07.2026): Prognose der Statistikstelle, kein Vorhaben.
- Haushaltssicherungskonzept „ab 2027", je 50 Stellen 2027 bis 2029 (16.07.2026, 01.09.2026): Auftrag des Rates
  an die Verwaltung; Einsparung von außen erst mit den Stellenplänen prüfbar (später ergänzen).
- Weihnachtsmärkte „ab 2027 räumlich und konzeptionell verändern" (02.10.2026): kein zählbares Ergebnis.
- Special Olympics Landesspiele 2029 oder 2031 (13.07.2026): Bewerbung, Vergabe liegt bei Dritten.
- Promenade, „Vollsperrung Anfang 2027" (09.06.2026): Zwischenzustand einer Leitungsbaustelle.
- Theater: neuer Generalintendant ab 2028/29 (Personalie der Theater-Gesellschaft); Ausstellungen, Spielzeiten,
  Heimatreisen, Anmeldefristen: Veranstaltungskalender.
- Olympia-Bewerbung 2036/2040/2044, Förderprogramme von Land und Bund: Dritte.

Nicht angesehen: Ratsinformationssystem, Haushaltsplan-Entwurf 2027, Meldungen vor dem 01.01.2026.
