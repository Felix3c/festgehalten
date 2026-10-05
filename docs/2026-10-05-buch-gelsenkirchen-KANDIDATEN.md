# Buch „Gelsenkirchen gegen Gelsenkirchen" — Kandidaten, recherchiert am 05.10.2026

Status: **14 Wetten angelegt** (`buecher/gelsenkirchen/wetten/gelsenkirchen-2026-001` bis `-014`), Zweig
`buch-gelsenkirchen`, nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag
05.10.2026, im Dauerlauf (Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Münster 307 979 (Zweig `buch-muenster`),
**Gelsenkirchen 267 733**, Mönchengladbach 266 840, Aachen 262 211. Beim nächsten Buch nach dieser Regel ist
Mönchengladbach dran.

**Methode:** Listenansicht `https://www.gelsenkirchen.de/de/_meta/aktuelles/artikel/seite/N` (67 Seiten, je 10
Einträge, 2 s Abstand) → 655 Meldungen seit 01.01.2026, davon 560 mit Quellenangabe „Stadt Gelsenkirchen" und
27 „GELSENDIENSTE". Ohne „Blitzer" und „Amtsblatt" 536 Meldungen im Volltext abgerufen (kein Fehler, keine
Sperre), Text der linken Spalte von HTML befreit und nach Sätzen mit Zukunftstermin durchsucht: 65 Meldungen
mit Treffer, von Hand gelesen. robots.txt erlaubt `/de/`. Jedes Zitat steht wörtlich im ersten und in einem
zweiten Abruf (13 Quellen, 13 von 13).

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „vorgesehen", „voraussichtlich", „derzeit",
„rechnet mit"; sonst „angekuendigt" (1,00), wie FORMAT.md §1.2.

**Archivbefund:** Save Page Now antwortete am 05.10.2026 beim ersten Versuch mit HTTP 429 (zu viele Anfragen,
Folge der Abrufe für Münster und Bielefeld am Vortag); nach einem Versuch abgebrochen. **Keine der 13 Quellen
hat eine geprüfte Archivkopie.** Ersatz: lokale Kopie des zweiten Abrufs
`recherche/belege/2026-10-05-gelsenkirchen-artikel-<Nummer>.html`, SHA-256 im Vermerk jeder Wette. Nachziehen:
je Quelle einmal `https://web.archive.org/save/<URL>` mit 30 s Abstand, Zitat in der `id_`-Kopie prüfen,
Vermerk ersetzen.

**Nachtrag 05.10.2026 (01:40–01:55):** Nachgezogen. 13 von 13 Quellen haben eine Wayback-Kopie, das Zitat
steht in jeder wörtlich (14 von 14 Wetten, bei 71790 beide Zitate). 12 Kopien sind vom 04.10.2026 (UTC, also
05.10. Ortszeit); für 71270 (IGA 2027) lieferte das Archiv die ältere Kopie vom 20.05.2026, sie trägt das Zitat
ebenfalls. Vermerk in allen 14 Wetten ersetzt. Die Archivkopien sind nicht byte-gleich mit den lokalen Kopien
geprüft (HTML-Seiten, nur der Zitat-Text ist verglichen).

## Angelegt

| Wette | Meldung | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|---|
| 001 | 72807 | 25.09.2026 | Liboriusstraße, Reparatur bis Ende Oktober 2026 | 01.11.2026 | 1,00 | 0,50 |
| 002 | 71978 | 20.07.2026 | Gasleitung Kurt-Schumacher-Straße, Abschluss Oktober 2026 | 01.11.2026 | 0,80 | 0,45 |
| 003 | 71123 | 31.03.2026 | metropolradruhr, mehr als 60 Standorte bis Herbst | 01.12.2026 | 0,80 | 0,40 |
| 004 | 71790 | 26.06.2026 | Gesamtschule Erle, Planungsbeschluss Dezember 2026 | 01.01.2027 | 0,80 | 0,60 |
| 005 | 72341 | 07.09.2026 | Bertlicher Straße, Kanal und Fahrbahn bis Ende 2026 | 01.01.2027 | 1,00 | 0,45 |
| 006 | 71826 | 30.06.2026 | Zugangsbrücke Schloss Horst, Bauzeit bis Jahresende | 01.01.2027 | 0,80 | 0,25 |
| 007 | 71790 | 26.06.2026 | Grundschule Wildenbruchplatz, Baubeginn Januar 2027 | 01.02.2027 | 0,80 | 0,40 |
| 008 | 71270 | 23.04.2026 | IGA 2027, Eröffnung 23.04.2027 (Eichwette) | 24.04.2027 | 1,00 | 0,93 |
| 009 | 72364 | 09.09.2026 | Cranger Straße, fertig Frühjahr 2027 | 01.06.2027 | 0,80 | 0,45 |
| 010 | 72562 | 21.09.2026 | Hiberniastraße, bis Ende Mai 2027 | 01.06.2027 | 0,80 | 0,45 |
| 011 | 70869 | 10.03.2026 | Grundschule Wildenbruchplatz, Betrieb Schuljahr 2028/2029 | 01.09.2028 | 0,80 | 0,35 |
| 012 | 72158 | 18.08.2026 | Schule auf Consol, Übergabe Juli 2029 | 01.08.2029 | 0,80 | 0,35 |
| 013 | 71016 | 24.03.2026 | Kita Feldmark, Inbetriebnahme 2029 | 01.01.2030 | 0,80 | 0,35 |
| 014 | 72440 | 16.09.2026 | Vierfeldsporthalle Buer, bis Frühjahr 2030 | 01.06.2030 | 1,00 | 0,30 |

**Zeitfenster:** 001 und 002 (Stichtag 31.10.2026) sind nur ehrlich, wenn das Buch vor dem Stichtag öffentlich
ist; sonst vor dem Merge verwerfen.

## Verworfen

- Kurzsperrungen bis Mitte Oktober 2026 (72846 Gabelsbergerstraße, 72874 Kurt-Schumacher-Straße Gleisbereich,
  72400, 72399, 73011, 72941, 71511 Munckelstraße): Stichtag liegt vor einer möglichen Veröffentlichung, aussagearm.
- 71022/71000 Amprion-Standort „bis Ende 2026": Zusage eines Dritten, nicht der Stadt.
- 72311 Haushalt 2027 (Fehlbedarf 29,9 Mio. Euro): Planzahl ohne klare Messgröße für den Ausgang; kein Beschlusstermin genannt.
- 72939 Bebauungsplan Nr. 446, Offenlage 2027: Niederschrift in indirekter Rede, kein Mitteilungstext.
- 72717 „noch in diesem Jahr auf weitere Stadtteile ausgeweitet": keine Zahl, kein zählbarer Ausgang.
- 71309/71104 „bis 2032 bis zu 3.000 Wohneinheiten": „bis zu" setzt keine Schwelle.
- 70642/70986 Neue Zeche Westerholt, Vermarktung 2029: Entwicklungsgesellschaft mit der Stadt Herten, später möglich.
- 71790 Grundschule Rotthausen im Volkshaus (2030), Schloss Berge (Haushaltsanmeldung 2027): spätere Ergänzung.
- GELSENDIENSTE (27 Meldungen): kein Satz mit Termin und zählbarem Ausgang gefunden.

Nicht angesehen: Ratsinformationssystem, Haushaltsplan-Entwurf 2027, Meldungen vor dem 01.01.2026.
