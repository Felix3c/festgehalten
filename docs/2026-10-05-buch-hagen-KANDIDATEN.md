# Buch „Hagen gegen Hagen" — Kandidaten, recherchiert am 05.10.2026

Status: **4 Wetten angelegt** (`buecher/hagen/wetten/hagen-2026-001` bis `-004`), Zweig `buch-hagen`,
nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag 05.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Oberhausen 213 349 (Buch seit
05.10.2026), **Hagen 189 704** (in der PDF an drei Stellen gleich: Tabelle der kreisfreien Städte, Tabelle der
Bevölkerungsbewegung, Gemeindeverzeichnis). Danach folgen Hamm 179 272, Mülheim an der Ruhr 172 031,
Leverkusen 168 262, Solingen 165 193 (aus dem Gemeindeverzeichnis gelesen; vor dem nächsten Buch die Zahl der
Stadt an einer zweiten Stelle der PDF gegenlesen).

**Methode:** Die Meldungsliste unter `https://www.hagen.de/hagen-aktuell/aktuelle-meldungen/` wird im Browser
aus einer JSON-Datei aufgebaut: `https://www.hagen.de/hagen-aktuell/aktuelle-meldungen/aktuelles-json.json`
(abgerufen 05.10.2026, 374 185 Bytes, SHA-256
`bf58fdd9ebdc48c5fb8180a00f22493916b9ec67e6d1376db2b495b855cbf298`, nicht im Repository). Sie enthält 656
Meldungen mit Titel, Datum, Adresse und vollem Text: 649 von April bis 02.10.2026 (April 103, Mai 79, Juni
103, Juli 112, August 94, September 146, Oktober 12), dazu sieben ältere Dauermeldungen (August 2025 bis März
2026). Bei den vier Quellen der Wetten ist geprüft, dass der Text der JSON-Datei vollständig auf der Seite der
Meldung steht; für die übrigen 652 ist das nicht geprüft. Drei Suchen über die Sätze: (1) Jahreszahlen 2027
bis 2039, „November/Dezember 2026", „Ende Oktober/November/Dezember", „Ende des Jahres", „Jahresende",
„Herbst/Winter 2026", „Jahreswechsel", „viertes Quartal": 36 Meldungen, von Hand gelesen. (2) In den übrigen
Meldungen ab Juni Termine ohne Jahreszahl („im kommenden/nächsten Jahr", „im Herbst/Winter", „voraussichtlich
bis/im/Ende", „bis Ende <Monat>"): 3 Meldungen. (3) Ab 15.06.2026, ohne Kurse, Büchereien und
Veranstaltungen: „Fertigstellung", „Bauzeit", „abgeschlossen sein", „in den kommenden Wochen/Monaten", „im
Frühjahr/Sommer" und Ähnliches: 6 Meldungen, keine neue Wette. Dazu rund 15 Meldungen mit Bau- oder Planbezug
im Titel ganz oder in Teilen gelesen und die vier IGA-Seiten der Stadt (`/hagen-aktuell/iga2027/…`).
**Grenzen der Methode:** Die Liste reicht nur bis April 2026 zurück (warum ältere Meldungen fehlen, ist
ungeklärt). Suche 2 und 3 lassen Meldungen vor Juni aus. Sätze, die einen Termin nur als Tagesdatum nennen,
findet keine der Suchen. Undatierte Seiten der Stadt (IGA-Projektseiten) sind gelesen, aber nicht als Quelle
genommen, weil `gesagt_am` dort nicht belegbar ist.

**Zugriff:** `robots.txt` (abgerufen 05.10.2026): `User-agent: * / Allow: /`. `/.well-known/tdmrep.json` und
`ai.txt` gibt es nicht (HTTP 404). Die Seiten der Meldungen tragen kein `robots`-Meta-Element. Abrufe mit
gekennzeichnetem Agenten: die JSON-Datei, die Sitemap, sechs Übersichtsseiten und die vier Meldungen.

Jedes Zitat steht wörtlich im ersten Abruf (JSON-Datei) und im zweiten (Seite der Meldung), 4 von 4. Das
Datum der Meldung steht auf der Seite (z. B. „23.Juni 2026") und stimmt mit dem Datum der JSON-Datei überein.

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „vorgesehen", „voraussichtlich"; sonst
„angekuendigt" (1,00), wie FORMAT.md §1.2. Alle vier Aussagen tragen einen Vorbehalt.

**Abgrenzung:** Aufgenommen sind nur Sätze aus dem Mitteilungstext der Stadt über Vorhaben der Stadt. Draußen
bleiben Meldungen, in denen der Wirtschaftsbetrieb Hagen (WBH) spricht (Straßen, Brücken, Kanäle,
Ruhrtalradweg), wie im Buch Oberhausen die Wirtschaftsbetriebe; wem der WBH gehört, ist am 05.10.2026 nicht
nachgeschlagen (ungeklärt). Ebenso draußen: Texte des Landes und des Aktionsbündnisses der Kommunen.

**Archivbefund:** 0 von 4. Save Page Now hat alle vier Adressen am 05.10.2026 mit HTTP 523 beantwortet, eine
ältere Kopie der vier Seiten lieferte das Archiv nicht (HTTP 404). Warum (Sperre auf Seiten der Stadt oder
Störung beim Archiv), ist ungeklärt; die Startseite von hagen.de führt das Archiv. Wie im Buch Wuppertal
tragen deshalb vorerst nur die lokalen Kopien des zweiten Abrufs:
`recherche/belege/2026-10-05-hagen-<Kurzname>.html`, je rund 105 KB, SHA-256 im Vermerk jeder Wette.

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 26.05.2026 | Fertiges Klimaschutzkonzept im Herbst 2026 veröffentlicht | 01.12.2026 | 0,80 | 0,35 |
| 002 | 14.04.2026 | Gemeinsame Auftaktveranstaltung der fünf Ruhrtal-Städte zur IGA im Frühjahr 2027 | 01.06.2027 | 0,80 | 0,75 |
| 003 | 23.06.2026 | Rundturnhalle Hohenlimburg bis Ende 2027 nicht nutzbar, danach wieder offen | 01.02.2028 | 0,80 | 0,25 |
| 004 | 28.07.2026 | Neuer Kunstrasenplatz in Hohenlimburg spätestens 2029/2030 | 01.01.2031 | 0,80 | 0,50 |

**Zeitfenster:** 001 (Stichtag 30.11.2026) ist nur ehrlich, wenn das Buch vor dem Stichtag öffentlich ist;
sonst vor dem Merge verwerfen. Ob das Konzept am 05.10.2026 schon veröffentlicht war, ist nur an den Meldungen
der Stadt geprüft (dort seit Mai nichts), nicht am Ratsinformationssystem.

**Lesarten, die der Halter ändern kann (vor dem Livegang):** 001 „Herbst 2026" als 30.11.2026 und
„Veröffentlichung" als abrufbares Dokument; 002 zählt als Vorhaben der Stadt, obwohl fünf Städte es tragen,
„Frühjahr 2027" als 31.05.2027; 003 „bis Ende 2027 nicht nutzbar" als Ankündigung der Wiederöffnung mit einem
Monat Spielraum (31.01.2028), die strengere Lesart wäre der 01.01.2028, die vorsichtigere gar keine Wette,
weil der Satz nur die Sperrung nennt; 004 „2029/2030" als 31.12.2030 und nur ein neu gebauter Platz.

## Verworfen

- Hagen-Pakt „Ziel ist es, in den nächsten 10 Jahren 600 Wohneinheiten zurückzubauen, 1 000 Wohneinheiten zu
  modernisieren" (20.05.2026): Der Text beginnt mit „Das Ministerium für Heimat, Kommunales, Bau und
  Digitalisierung teilt mit"; es spricht das Land.
- Brücke Rehbecke „im ungünstigsten Fall bis in das Frühjahr 2027" (29.05.2026), Ruhrtalradweg „Insgesamt
  dauert der Umbau rund 18 Monate" (12.08.2026), Fußgängerbrücken Saarlandstraße, Bahnhofstraße, Kanal- und
  Asphaltarbeiten: Es spricht der WBH; Rehbecke nennt ausdrücklich keinen Termin.
- Doppelhaushalt (08.09.2026): „Für 2027 sind Erträge von rund 1,0139 Milliarden Euro und Aufwendungen von
  rund 1,1 Milliarden Euro geplant": Die Aufwendungen sind grob gerundet, ein Fehlbetrag lässt sich daraus
  nicht als Messgröße ableiten. Der Bericht an die Bezirksregierung bis 30.11.2026 ist eine Auflage der
  Bezirksregierung, keine Ankündigung der Stadt; Haushaltsausgleich 2034: Pflicht aus dem
  Haushaltssicherungskonzept.
- Cuno-Berufskollegs: „Ende November sollen nahezu alle Unterrichtsräume und Werkstätten wieder sicher
  nutzbar sein" (06.11.2025): Stichtag beim Hinterlegen verstrichen. Standortempfehlung „in den kommenden
  Wochen" im Rat (24.04.2026): kein Datum, beim Hinterlegen ebenfalls verstrichen.
- Zukunftswerkstatt Wohnungslosenhilfe, Mid-Term-Treffen Oktober 2026 und Abschlusstreffen März 2027
  (06.07.2026): internes Projekt mit der FernUniversität, von außen nicht belegbar.
- Café am Hohenhof, Weiterführung „im nächsten Jahr" (21.08.2026): bedingt („bei entsprechendem Erfolg").
- Digitalisierung (Ehe-Online, 23.06.2026), neue Männernotunterkunft Hugo-Preuß-Straße (18.09.2026),
  OGS-Ausbau (06.07.2026): kein Termin.
- IGA-Projektseite SeePark: „Der Teilbereich rund um das SeeBad soll bis zur IGA2027 fertiggestellt werden":
  Seite ohne Datum; der Radweg ist laut Meldung vom 12.08.2026 Sache des WBH.
- Festival „Vielfalt tut gut" am 10.07.2027, Gesundheitsforum März 2027, VHS-Reisen und Kurse,
  Schulanmeldung 2027/28, Heimat-Preis, Förderprogramme des Landes, Gemeindefinanzierungsgesetz 2027:
  Veranstaltungskalender, Fristen oder Dritte.

Nicht angesehen: Ratsinformationssystem, Haushaltsplan 2026/2027 und Haushaltssicherungskonzept, Amtsblatt,
Meldungen vor April 2026, die Seiten des WBH und der Öffentlichkeitsbeteiligung (InSEK City, Stadterneuerung).
