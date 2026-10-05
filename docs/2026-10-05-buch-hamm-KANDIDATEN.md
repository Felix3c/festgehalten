# Buch „Hamm gegen Hamm" — Kandidaten, recherchiert am 05.10.2026

Status: **10 Wetten angelegt** (`buecher/hamm/wetten/hamm-2026-001` bis `-010`), Zweig `buch-hamm`,
nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Montag 05.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl. IT.NRW, Statistische Berichte „Bevölkerung
der Gemeinden Nordrhein-Westfalens am 30. Juni 2025" (A123 2025 21): Hagen 189 704 (Buch seit 05.10.2026),
**Hamm 179 272** (in der PDF an drei Stellen gleich: Tabelle der kreisfreien Städte, Tabelle der
Bevölkerungsbewegung, Gemeindeverzeichnis). Danach folgen Mülheim an der Ruhr 172 031, Leverkusen 168 262,
Solingen 165 193 (aus dem Gemeindeverzeichnis gelesen; vor dem nächsten Buch die Zahl der Stadt an einer
zweiten Stelle der PDF gegenlesen).

**Methode:** Die Seite `https://www.hamm.de/aktuelles` (abgerufen 05.10.2026, 152 890 Bytes, nicht im
Repository) listet alle Meldungen auf einer einzigen Seite, ohne Blättern und ohne Datum: 231 Adressen der
Form `/aktuelles/<Kurzname>`. Alle 231 Seiten einzeln abgerufen (je rund 350 KB, alle HTTP 200); Datum aus
`<time itemprop="datePublished">`, Text aus dem Block `news news-single`. Verteilung: 2017 bis 2024
zusammen 90, 2025 47, 2026 94 (davon September 21). Eine Suche über alle Sätze aller 231 Meldungen:
Jahreszahlen 2027 bis 2039, „November/Dezember 2026", „Ende Oktober/November/Dezember", „Ende des Jahres",
„Jahresende", „Herbst/Winter 2026", „Jahreswechsel", „viertes Quartal", „im kommenden/nächsten Jahr",
„voraussichtlich bis/im/Ende/Anfang/Mitte", „bis Ende/Mitte/Anfang <Monat>", „Fertigstellung",
„abgeschlossen sein/werden", „im Frühjahr/Sommer/Herbst/Winter", „im Oktober/November/Dezember"; bei
Meldungen vor Juni 2025 nur Sätze mit einer Jahreszahl ab 2026. Ergebnis: 64 Meldungen mit Treffer, alle
Treffersätze gelesen, 14 Meldungen ganz gelesen.
**Grenzen der Methode:** Die Liste ist keine vollständige Pressestelle (94 Meldungen in neun Monaten 2026;
eine eigene Seite der Pressestelle mit Archiv habe ich nicht gefunden, die Adressen `/presse`,
`/pressestelle`, `/pressemitteilungen`, `/pressemeldungen` gibt es nicht). Sätze, die einen Termin nur als
Tagesdatum nennen, findet die Suche nur, wenn eines der Suchwörter danebensteht. Die Unterseiten
`/klima-und-mobilitaet/aktuelles` und `/gesellschaft-soziales-gesundheit/aktuelles` enthalten keine
eigenen Meldungsadressen. Die Sitemap der Stadt führt nur Seiten, keine Meldungen.

**Zugriff:** `robots.txt` (abgerufen 05.10.2026): `User-agent: * / Disallow: /suchergebnisseite`.
`/.well-known/tdmrep.json` und `ai.txt` gibt es nicht (HTTP 404). Abrufe mit gekennzeichnetem Agenten, rund
eine Seite je fünf Sekunden: die Liste, 231 Meldungen, zehn davon ein zweites Mal, dazu Startseite, Sitemap,
zwei Unterlisten und drei Seiten des ASH.

Jedes Zitat steht wörtlich im ersten Abruf und im zweiten (beide Male die Seite der Meldung, getrennte
Abrufe am selben Vormittag), 10 von 10; Titel und Datum der Meldung stehen im zweiten Abruf, 10 von 10.

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „vorgesehen", „voraussichtlich", „Ziel ist
es"; sonst „angekuendigt" (1,00), wie FORMAT.md §1.2. Alle zehn Aussagen tragen einen Vorbehalt.

**Abgrenzung:** Aufgenommen sind Sätze aus dem Mitteilungstext der Stadt. Anders als in den Büchern Hagen
und Oberhausen (dort blieben die Meldungen der Wirtschaftsbetriebe draußen) ist hier eine Aussage über ein
Vorhaben des Betriebs ASH aufgenommen (008), weil sie auf hamm.de im Mitteilungstext steht, der
Oberbürgermeister beim Spatenstich dabei ist und die Seiten des ASH unter hamm.de liegen; die Rechtsform des
ASH ist nicht nachgeschlagen (ungeklärt). Das ist eine Lesart, die der Halter ändern kann; ebenso 006
(Bauherr des Workshop-Gebäudes ungeklärt) und 010 (drei Träger).

**Archivbefund:** 10 von 10. Save Page Now hat alle zehn Adressen am 05.10.2026 angenommen, jede
Archivkopie enthält das Zitat wörtlich und ist byte-gleich mit der lokalen Kopie des zweiten Abrufs
(`recherche/belege/2026-10-05-hamm-<Kurzname>.html`, je rund 350 KB, SHA-256 im Vermerk jeder Wette).

## Angelegt

| Wette | Gesagt | Inhalt | Prüfung | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 29.09.2026 | Rat beschließt am 13.10.2026 das ISEK „Zukunftsplan Innenstadt 2040" | 14.10.2026 | 0,80 | 0,90 |
| 002 | 02.09.2026 | Ausbau Schneckenweg (Heessen) im Dezember abgeschlossen | 01.01.2027 | 0,80 | 0,50 |
| 003 | 01.10.2026 | Spielplatz „Am Pelkumer Bach" bis Jahresende gesperrt, danach wieder offen | 01.02.2027 | 0,80 | 0,35 |
| 004 | 25.09.2026 | Neue Anliegerstraße „Am Maximilianpark" im ersten Quartal 2027 fertig | 01.04.2027 | 0,80 | 0,60 |
| 005 | 11.09.2026 | Baubeginn zweiter Abschnitt „Grüne Umweltachse Werries" Anfang 2027 | 01.04.2027 | 0,80 | 0,45 |
| 006 | 06.05.2026 | Workshop-Gebäude im Maxipark rechtzeitig zur IGA im April 2027 fertig | 24.04.2027 | 0,80 | 0,65 |
| 007 | 02.10.2026 | Mietspiegel 2027 erscheint spätestens im Juli 2027 | 01.08.2027 | 0,80 | 0,80 |
| 008 | 01.09.2026 | Neuer Wertstoffhof spätestens Herbst 2027 in Betrieb | 01.12.2027 | 0,80 | 0,55 |
| 009 | 09.12.2025 | Einzug ins Respekthaus im Herbst 2027 | 01.12.2027 | 0,80 | 0,35 |
| 010 | 15.09.2026 | Umbau Hammer Straße zur Jahresmitte 2028 abgeschlossen | 01.08.2028 | 0,80 | 0,30 |

**Zeitfenster:** 001 (Stichtag 13.10.2026) ist nur ehrlich, wenn das Buch vor dem Stichtag öffentlich ist;
sonst vor dem Merge verwerfen. Die Tagesordnung der Ratssitzung am 13.10.2026 ist nicht angesehen.

**Lesarten, die der Halter ändern kann (vor dem Livegang):** 001 misst nur den Ratsbeschluss, nicht den
Förderantrag; 002 „im Dezember" als Dezember 2026; 003 „bis zum Jahresende gesperrt" als Ankündigung der
Wiederöffnung mit einem Monat Spielraum (31.01.2027), die strengere Lesart wäre der 01.01.2027, die
vorsichtigere gar keine Wette; 005 „Anfang 2027" als erstes Quartal; 006 der bestimmtere der beiden Termine
im Satz (Eröffnung der IGA am 23.04.2027) statt „Frühjahr 2027" (31.05.2027); 008 und 009 „Herbst 2027" als
30.11.2027; 009 Ja schon, wenn eine der vier Einrichtungen eingezogen ist; 010 „zur Jahresmitte 2028" mit
einem Monat Spielraum (31.07.2028); 006, 008, 010 zählen als Aussagen der Stadt (siehe Abgrenzung).

## Verworfen

- Wertstoffhof, Meldung vom 10.09.2025: „Geplant ist der Baustart für Anfang 2026", „Die Fertigstellung und
  Eröffnung ist für Ende 2026/Anfang 2027 geplant": überholt durch die Meldung vom 01.09.2026 (Spatenstich
  am 01.09.2026, Inbetriebnahme spätestens Herbst 2027); steht als Kontext in Wette 008.
- Tierasyl Römerstraße (06.03.2026): „Nach aktueller Einschätzung könnte der Baustart im zweiten Quartal
  2027 erfolgen": „könnte" ist keine Ankündigung.
- Doppelhaushalt (27.03. und 17.06.2026), Kämmerer: „Wir erwarten für 2026 und 2027 negative
  Haushaltsergebnisse in Höhe von jeweils gut 100 Millionen Euro": „gut 100 Millionen" ist keine Messgröße
  mit Schwelle (wie im Buch Hagen der Doppelhaushalt). Schuldenstand „gut 900 Millionen Euro" bis 2030:
  bedingt („Ändern sich die strukturellen Rahmenbedingungen nicht").
- Sportplatz Werries (11.09.2026): Rasenfläche „abhängig von der Witterung … voraussichtlich im Mai/ Juni
  2027 für den Spielbetrieb bereit": ausdrücklich bedingt und von außen kaum belegbar; aus derselben Meldung
  ist der Baubeginn des zweiten Abschnitts genommen (005).
- Deckschichtsanierung Grünstraße (25.09.2026): „Planmäßig und witterungsabhängig sollen die Arbeiten am
  Freitag, 9. Oktober, abgeschlossen werden": Stichtag vier Tage nach dem Hinterlegen, ausdrücklich
  witterungsabhängig.
- Feuerwehrgerätehäuser (05.03.2025): Baubeginn Heessen „im kommenden Jahr", Uentrop zwei Jahre später,
  Bockum 2029: bedingt („Sollte der Rat … zustimmen"); ob der Rat zugestimmt hat und ob in Heessen schon
  gebaut wird, ist am 05.10.2026 nicht geprüft. Kandidat für später.
- Museumsstraße (01.04.2025): „Bis 2026 soll das gesamte Projekt abgeschlossen sein": „bis 2026" ist
  zweideutig, Stand des Projekts am 05.10.2026 nicht geprüft.
- Neue Hauptschule im Hammer Norden (10.03.2023): „soll bis 2030 ein Neubau entstehen", „könnte der
  Baubeschluss in 2027 gefasst … werden": dreieinhalb Jahre alt, ob der Plan noch gilt, ist nicht geprüft.
  Kandidat für später.
- Kanalbau Ludwig-Erhard-Straße (29.04.2026): „Die Arbeiten laufen bis ins Jahr 2027": kein Termin.
- Smart City Strategie 2027 bis 2032 (25.09.2026): „wird derzeit … weiterentwickelt": kein Termin.
- Kaufhof-Areal (18.09.2025): Rückbau „voraussichtlich im Frühjahr 2026": Stichtag beim Hinterlegen
  verstrichen; „Fertigstellung … frühestens 2029 realistisch": keine Zusage. Hitzeaktionsplan „Ende des
  Jahres" (04.06.2025), Raumprogramm Stadtsportbund „bis Ende 2025", Sozialgebäude Wertstoffhof „Mitte des
  Jahres": Stichtage verstrichen.
- Hauptbahnhof (2019), Multi Hub Westfalen (2022/2023), Rechenzentrum (22.01.2026, „ab 2030"): Vorhaben
  Dritter. Masterplan Mobilität (ÖPNV-Anteil 15 Prozent und CO₂ im Verkehr minus 40 Prozent bis 2035),
  Klimawerk (250 Millionen Euro bis 2030): Ziele ohne Messstelle in der Meldung. 10-Minuten-Takt „zunächst
  bis Ende 2026 befristet", „Ways2work" bis Ende 2027: Laufzeiten, keine Ankündigungen.
- Frühjahrsputz März 2027, Herbstleuchten, Fachtag der Elternschule, Literarischer Herbst, Denkmäler-Band
  „erscheint im Frühjahr 2027", Landtagswahl 2027: Veranstaltungskalender oder Dritte.

Nicht angesehen: Ratsinformationssystem (auch die Tagesordnung vom 13.10.2026), Haushaltsplan 2026/2027,
Amtsblatt, Seiten des Maximilianparks, der Stadtwerke und der Hamm.Invest, Rechtsform des ASH, die
Projektseiten der Stadt außerhalb von `/aktuelles` (Baugebiete, IGA, Stadterneuerung).
