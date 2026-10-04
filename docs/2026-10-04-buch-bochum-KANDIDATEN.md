# Buch „Bochum gegen Bochum" — Kandidaten, recherchiert am 04.10.2026

Status: **12 Wetten angelegt** (`buecher/bochum/wetten/bochum-2026-001` bis `-012`), Zweig `buch-bochum`,
nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude, Sonntag 04.10.2026, im Dauerlauf
(Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl (IT.NRW). Vorhandene Bücher:
Köln, Düsseldorf, Dortmund, Essen, Duisburg (Zweig), Bonn. Nächste Stadt: **Bochum**.
Quelle: IT.NRW, Statistische Berichte „Bevölkerung der Gemeinden Nordrhein-Westfalens am 30. Juni 2025"
(Artikel-Nr. A123 2025 21, erschienen November 2025),
https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/NWHeft_derivate_00022899/a123202521.pdf,
abgerufen 04.10.2026: Bochum 358 426, Wuppertal 357 900, Bielefeld 330 825 (Bonn 323 245, Münster 307 979).
Zum Stand 31.12.2025 (Landesdatenbank NRW, Tabelle 12411-01i) nennt die Wikipedia-Vorlage
„Metadaten Einwohnerzahl DE-NW" Bochum 358 880, Wuppertal 357 243, Bielefeld 331 419; die
Landesdatenbank selbst war per curl nicht lesbar (JavaScript), diese Zahlen sind also nur
sekundär geprüft. Beide Stichtage ergeben Bochum, der Abstand zu Wuppertal ist aber knapp (rund 500
bzw. 1.600 Einwohner). Beim nächsten Buch nach dieser Regel ist Wuppertal dran.

**Methode:** Jede Seite wurde am 04.10.2026 per `curl`/Python (`urllib`) abgerufen, HTML-Tags entfernt,
Entities aufgelöst, Leerraum vereinheitlicht. Die Zitate unten sind aus diesem Text kopiert. Ein
Prüfskript hat jedes Zitat (Teile zwischen „…") gegen einen zweiten, frischen Abruf geprüft: alle 12
angelegten Zitate stehen wörtlich im Live-Text. Beim Haus der Musik (K12) steht zwischen zwei Sätzen
eine Bildunterschrift, deshalb dort ein „…". Bochumer Pressemitteilungen wurden über die Listenansicht
auf bochum.de (Seiten 1–10, Mitteilungen 04.09.–02.10.2026) und gezielte Suchen gefunden.

**Vorbehalt-Spalte:** „voraussichtlich" (0,80), wenn der Satz „soll", „geplant", „vorgesehen",
„voraussichtlich", „derzeit" oder einen Bedingungssatz enthält; sonst „angekuendigt" (1,00), wie in
FORMAT.md §1.2 und in den Duisburg-Wetten.

**Wayback:** Availability-API (`https://archive.org/wayback/available?url=…&timestamp=2026`) per Skript.
Vorher hatte nur die Haus-des-Wissens-Seite eine Kopie (13.05.2026). Für alle anderen Quellen wurde am
04.10.2026 je einmal `https://web.archive.org/save/<URL>` ausgelöst (15 s Pause). Das Ergebnis der
Wortlautprüfung im Archiv steht unten unter „Archivbefund" (11 von 12 tragen).

---

## bo-K01 — Haushalt 2027: Ratsbeschluss im Dezember 2026 → **bochum-2026-001**

- **URL:** https://www.bochum.de/Pressemeldungen/1-Oktober-2026/Haushaltsentwurf-2027
- **gesagt_am:** 01.10.2026 (Pressemitteilung der Stadt zur Einbringung)
- **Wer:** Stadt Bochum; Kämmerin Dr. Eva Maria Hubbert bringt ein. Der Terminsatz ist Mitteilungstext.
- **Zitat:** „Heute, 1. Oktober, hat Kämmerin Dr. Eva Maria Hubbert dem Rat der Stadt Bochum den Entwurf für
  den Haushalt 2027 vorgelegt." … „Die Verabschiedung des Haushalts durch den Rat ist für Dezember vorgesehen."
- **Vorbehalt:** voraussichtlich („vorgesehen")
- **Frage:** Beschließt der Rat der Stadt Bochum die Haushaltssatzung 2027 bis zum 31.12.2026?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** Ratsinformationssystem, Pressemitteilung der Stadt, Radio Bochum.
- **Wahrscheinlichkeit: 0,80.** Termin steht in der Mitteilung, Dezemberbeschlüsse sind üblich. Risiko:
  erstes Haushaltssicherungskonzept seit Jahren, Streit um Kürzungen kann in den Januar schieben.

## bo-K02 — Stadtpark: Wiedereröffnung am 06.11.2026 → **bochum-2026-002**

- **URL:** https://www.radiobochum.de/artikel/sanierung-im-bochumer-stadtpark-verzoegert-sich-2726631
- **gesagt_am:** 14.08.2026 (Radio Bochum, „Wie die Stadt mitgeteilt hat")
- **Wer:** Stadt Bochum (Umwelt- und Grünflächenamt), wiedergegeben von Radio Bochum. Eine eigene
  Pressemitteilung der Stadt mit dem 6. November wurde nicht gefunden (ungeklärt, ob es eine gibt).
- **Zitat:** „Wie die Stadt mitgeteilt hat, soll der zweite Bauabschnitt im mittleren Bereich des Stadtparks im
  September abgeschlossen werden." … „Wenn es keine weiteren baustellenbedingten Verzögerungen gibt, soll der
  neugestaltete Stadtpark am 6. November im Rahmen einer kleinen Eröffnungsfeier wieder für die Öffentlichkeit
  freigegeben werden."
- **Vorbehalt:** voraussichtlich („soll", Bedingungssatz)
- **Frage:** Wird der neugestaltete Stadtpark Bochum spätestens am 06.11.2026 offiziell wieder für die
  Öffentlichkeit freigegeben?
- **Stichtag:** 06.11.2026 · **Prüfdatum:** 07.11.2026 (erste Auflösung im Buch)
- **Beleg später:** Pressemitteilung Stadt / Bochum Marketing, Radio Bochum, WAZ.
- **Wahrscheinlichkeit: 0,70.** Konkreter Termin mit Feier; aber das Projekt ist schon gerutscht
  (Sommer 2026 → November), Weiher und Fontänen hingen im August noch.

## bo-K03 — Trianel Windpark Sundern (Stadtwerke Bochum): fertig Ende 2026 → **bochum-2026-003**

- **URL:** https://www.stadtwerke-bochum.de/privatkunden/ihre-stadtwerke/presse-medien/pressemeldung/trianel-windpark-sundern-erreicht-wichtigen-meilenstein
- **gesagt_am:** 28.08.2026 (Pressemeldung Stadtwerke Bochum)
- **Wer:** Stadtwerke Bochum (städtische Tochter), zitiert wird Geschäftsführerin Elke Temme. Terminsatz ist
  Mitteilungstext.
- **Zitat:** „Gemeinsam mit der Trianel Wind und Solar GmbH & Co. KG realisieren die Stadtwerke Bochum im
  Hochsauerlandkreis insgesamt neun Windenergieanlagen." … „Nach der geplanten Fertigstellung Ende dieses
  Jahres wird der Trianel Windpark Sundern aus neun Windenergieanlagen mit einer Gesamtleistung von rund
  50 Megawatt bestehen."
- **Vorbehalt:** voraussichtlich („geplanten")
- **Frage:** Sind bis zum 31.12.2026 alle neun Anlagen fertiggestellt und in Betrieb?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** Meldung Stadtwerke/Trianel, Marktstammdatenregister (Inbetriebnahmedaten).
- **Wahrscheinlichkeit: 0,45.** Ende August standen erst die ersten Anlagen; vier Monate mit Spätherbst für
  den Rest. Hinweis: Der Windpark liegt nicht in Bochum; aufgenommen, weil die Aussage von der
  städtischen Tochter stammt.

## bo-K04 — Buslinie SB33 ab Januar 2027 eingestellt → **bochum-2026-004**

- **URL:** https://www.radiobochum.de/artikel/bogestra-fahrten-fallen-weg-2750440
- **gesagt_am:** 09.09.2026 (Radio Bochum)
- **Wer:** Stadt Bochum (Sparvorschlag), wiedergegeben von Radio Bochum: „Die Stadt will damit rund
  912.000 Euro pro Jahr sparen." Ob der Rat schon beschlossen hat: ungeklärt.
- **Zitat:** „Ab Januar 2027 sollen in Bochum mehrere Busverbindungen gestrichen oder gekürzt werden.
  Hintergrund ist die angespannte Haushaltslage der Stadt." … „Die Linie SB33 zwischen Wattenscheid und
  Querenburg soll komplett eingestellt werden."
- **Vorbehalt:** voraussichtlich („sollen")
- **Frage:** Ist die Buslinie SB33 am 31.01.2027 eingestellt (kein regulärer Fahrplan bei der BOGESTRA)?
- **Stichtag:** 31.01.2027 · **Prüfdatum:** 01.02.2027
- **Beleg später:** BOGESTRA-Fahrplanwechsel-Meldung, Linienfahrplan, VRR-Auskunft.
- **Wahrscheinlichkeit: 0,75.** Teil des Sparkurses, Fahrplanwechsel zum Jahreswechsel sind üblich;
  Risiko politische Rücknahme.

## bo-K05 — OSTPARK: Wasserspielplatz Anfang 2027 fertig → **bochum-2026-005**

- **URL:** https://www.bochum.de/Pressemeldungen/1-Juli-2026/OSTPARK-Arbeiten-fuer-Wasserspielplatz-im-Quartier-Feldmark-beginnen
- **gesagt_am:** 01.07.2026 (Pressemitteilung, Spatenstich 30.06.2026)
- **Wer:** Stadt Bochum, zitiert wird Philipp Heidt (Leiter Umwelt- und Grünflächenamt); Terminsatz ist
  Mitteilungstext.
- **Zitat:** „Im Zentrum des Quartiers Feldmark im OSTPARK entsteht ein multifunktionaler Wasserspielplatz mit
  einer Gesamtfläche von 4.800 Quadratmetern" … „Der Wasserspielplatz wird voraussichtlich Anfang 2027
  fertiggestellt."
- **Vorbehalt:** voraussichtlich
- **Frage:** Ist der Wasserspielplatz bis zum 31.03.2027 fertiggestellt?
- **Stichtag:** 31.03.2027 · **Prüfdatum:** 01.04.2027
- **Beleg später:** OSTPARK-News auf bochum.de, Pressemitteilung, IGA-Berichte.
- **Wahrscheinlichkeit: 0,40.** Winterbauzeit, Wassertechnik; die IGA (ab April 2027) drückt, aber
  „zur IGA" wäre schon zu spät.

## bo-K06 — Alleestraße: Einbahnstraße bis März 2027 aufgehoben → **bochum-2026-006**

- **URL:** https://www.bochum.de/Pressemeldungen/1-Oktober-2026/Einbahnstrassenregelung-auf-der-Alleestrasse-verlaengert-sich
- **gesagt_am:** 01.10.2026 (Pressemitteilung)
- **Wer:** Stadt Bochum
- **Zitat:** „Durch die Anpassung der Bauzeit muss die Einbahnstraße zwischen der Zufahrt Westtor-Center und
  dem Westring noch bis März 2027 bestehen bleiben." … „Im März 2027 wird dann mit Aufhebung der Einbahnstraße
  auch der Bereich zwischen Westring und der Brücke der Deutschen Bahn nahezu komplett fertiggestellt sein."
- **Vorbehalt:** angekuendigt („wird … sein", 1,00)
- **Frage:** Ist die Einbahnstraßenregelung zwischen Zufahrt Westtor-Center und Westring bis zum
  31.03.2027 aufgehoben?
- **Stichtag:** 31.03.2027 · **Prüfdatum:** 01.04.2027
- **Beleg später:** Pressemitteilung der Stadt zur Aufhebung, Verkehrsmeldungen.
- **Wahrscheinlichkeit: 0,40.** Mehrfach verzögert (alte Leitungen), Winter dazwischen.

## bo-K07 — Haus des Wissens: Baufertigstellung Ende Juni 2027 → **bochum-2026-007**

- **URL:** https://www.bochum.de/Haus-des-Wissens/Baustellen-Stream
- **gesagt_am:** 13.05.2026 (letzter Wayback-Schnappschuss mit diesem Wortlaut; derselbe Satz steht laut
  Wayback schon am 10.08.2024, 09.12.2024 und 24.06.2025 auf der Seite und am 04.10.2026 live).
  Das Datum der Erstveröffentlichung ist ungeklärt.
- **Wer:** Stadt Bochum, Projektseite
- **Zitat:** „Bis zur Baufertigstellung Ende Juni 2027 wird das Gebäude von aktuell 6.000 Quadratmetern (altes
  Telekomgebäude) auf 11.500 Quadratmeter erweitert."
- **Vorbehalt:** angekuendigt (1,00). Die Strategieseite der Stadt sagt vorsichtiger „Angestrebt wird, dass das
  Haus des Wissens im Jahr 2027 fertiggestellt ist."
- **Frage:** Ist das Haus des Wissens bis zum 30.06.2027 baulich fertiggestellt?
- **Stichtag:** 30.06.2027 · **Prüfdatum:** 01.07.2027
- **Beleg später:** Fertigstellungs-, Übergabe- oder Eröffnungsmeldung der Stadt. „Baulich fertig" ist schwer
  zu belegen; in der Wette gilt: ohne Meldung bis zum Prüftag Nein.
- **Wahrscheinlichkeit: 0,20.** Kosten von 73 auf über 150 Mio. €, Decken erst 2026, früherer Termin (Eröffnung
  Ende 2026) schon gerissen.

## bo-K08 — 11. Gymnasium startet zum Schuljahr 2027/28 → **bochum-2026-008**

- **URL:** https://www.bochum-journal.de/2026/05/15/braucht-bochum-ein-11-gymnasium/
- **gesagt_am:** 15.05.2026 (Bochum Journal über die Verwaltungsvorlage 20261122)
- **Wer:** Stadt Bochum (Verwaltung), wiedergegeben vom Bochum Journal („Nach Angaben der Verwaltung").
  Die Vorlage selbst war nicht abrufbar (Ratsinformationssystem session.bochum.de per curl nicht erreichbar).
  Laut ratskompass.de (Drittportal) am 16.07.2026 im Rat beschlossen, 60 zu 27 Stimmen.
- **Zitat:** „Nach Angaben der Verwaltung reichen die vorhandenen Kapazitäten perspektivisch nicht mehr aus,
  weshalb die Gründung eines weiteren Gymnasiums zum Schuljahr 2027/2028 vorgesehen ist." … „Da die Zeit bis
  zum geplanten Start im Schuljahr 2027/2028 knapp ist, soll das Gymnasium zunächst in Interimscontainern
  entstehen."
- **Vorbehalt:** voraussichtlich
- **Frage:** Nimmt ein neu gegründetes elftes städtisches Gymnasium bis zum 30.09.2027 den Unterricht auf?
- **Stichtag:** 30.09.2027 (Puffer; Ferienende NRW 2027 nicht geprüft, ungeklärt) · **Prüfdatum:** 01.10.2027
- **Beleg später:** Anmeldeverfahren 2027/28 der Stadt, Schulhomepage, Radio Bochum/WAZ zum ersten Schultag.
- **Wahrscheinlichkeit: 0,65.** Bedarf festgestellt, Containerlösung machbar; Risiken Gründung,
  Genehmigung, Anmeldungen, 22 Mio. € Container im Haushaltssicherungskonzept.

## bo-K09 — Lothringentrasse: neue Brücke über die A 43 ab Oktober 2027 → **bochum-2026-009**

- **URL:** https://www.bochum.de/Pressemeldungen/15-Juni-2026/Neue-Bruecke-der-Lothringentrasse-ueber-die-A-43
- **gesagt_am:** 15.06.2026 (Pressemitteilung)
- **Wer:** Stadt Bochum
- **Zitat:** „Mit der Fertigstellung der die neue Brücke erschließenden Wegebauarbeiten wird die Maßnahme
  voraussichtlich im Oktober 2027 abgeschlossen sein. Die Gesamtkosten betragen rund 7,4 Millionen Euro." …
  „Der Rad- und Fußverkehr kann die neue Brücke erst nach Fertigstellung – also voraussichtlich ab Oktober
  2027 – nutzen."
- **Vorbehalt:** voraussichtlich
- **Frage:** Ist die neue Brücke bis zum 31.10.2027 für den Rad- und Fußverkehr freigegeben?
- **Stichtag:** 31.10.2027 · **Prüfdatum:** 01.11.2027
- **Beleg später:** Freigabemeldung der Stadt.
- **Wahrscheinlichkeit: 0,40.** Kette Fernwärme (Stadtwerke) → Ausstattung → Wegebau.

## bo-K10 — Dreifachsporthalle Markstraße: fertig im 4. Quartal 2027 → **bochum-2026-010**

- **URL:** https://www.bochum.de/Pressemeldungen/22-Juni-2026/Baubeginn-fuer-neue-Dreifachsporthalle-an-der-Markstrasse
- **gesagt_am:** 22.06.2026 (Pressemitteilung zum Baubeginn)
- **Wer:** Stadt Bochum
- **Zitat:** „Nachdem die durch einen Brand zerstörte Dreifachturnhalle an der Markstraße 193 bis Ende 2024
  abgebrochen und der Untergrund gesichert und stabilisiert worden ist, beginnen nun die Arbeiten für den
  Wiederaufbau der Sportstätte." … „Die Arbeiten sollen im vierten Quartal 2027 abgeschlossen sein. Die
  Gesamtkosten liegen bei rund 20 Millionen Euro."
- **Vorbehalt:** voraussichtlich („sollen")
- **Frage:** Ist die neue Dreifachsporthalle bis zum 31.12.2027 fertiggestellt?
- **Stichtag:** 31.12.2027 · **Prüfdatum:** 01.01.2028
- **Beleg später:** Übergabemeldung der Stadt, Lokalpresse.
- **Wahrscheinlichkeit: 0,35.** 18 Monate sind knapp; Hallenbauten rutschen oft ein bis zwei Quartale.

## bo-K11 — Bebauungsplan „Wilhelm-Leithe-Weg Nord": Satzungsbeschluss Ende 2027 → **bochum-2026-011**

- **URL:** https://www.bochum.de/Pressemeldungen/29-September-2026/Neuer-suedlicher-Zugang-am-Bahnhof-Wattenscheid-geht-in-Betrieb
- **gesagt_am:** 29.09.2026 (Pressemitteilung)
- **Wer:** Stadt Bochum
- **Zitat:** „Die Stadt Bochum entwickelt gemeinsam mit der Bochum Wirtschaftsentwicklung das Plangebiet
  „Wilhelm-Leithe-Weg Nord"." … „Der Satzungsbeschluss für den Bebauungsplan ist derzeit für Ende 2027
  vorgesehen."
- **Vorbehalt:** voraussichtlich („derzeit … vorgesehen")
- **Frage:** Beschließt der Rat den Bebauungsplan bis zum 31.12.2027 als Satzung?
- **Stichtag:** 31.12.2027 · **Prüfdatum:** 01.01.2028
- **Beleg später:** Ratsinformationssystem, Amtsblatt der Stadt Bochum.
- **Wahrscheinlichkeit: 0,40.** Gutachten laufen noch; B-Pläne brauchen meist länger.

## bo-K12 — Haus der Musik (Musikschule): erste Schüler im Sommer 2028 → **bochum-2026-012**

- **URL:** https://www.bochum.de/Pressemeldungen/27-Maerz-2026/-Haus-der-Musik--Bauen-fuer-den-Musikunterricht-der-Zukunft
- **gesagt_am:** 27.03.2026 (Pressemitteilung)
- **Wer:** Stadt Bochum, mit Kulturdezernent Dietmar Dieckmann und Musikschulleiter Norbert Koop (Terminsatz
  ist Mitteilungstext)
- **Zitat:** „Im Sommer 2028 soll hier das „Haus der Musik" die ersten Schülerinnen und Schüler begrüßen." …
  „Rund 23,5 Millionen Euro investiert die Stadt in den Umbau, federführend ist das Architekturbüro Dreibund."
- **Vorbehalt:** voraussichtlich („soll")
- **Frage:** Findet bis zum 30.09.2028 Unterricht im „Haus der Musik" statt?
- **Stichtag:** 30.09.2028 · **Prüfdatum:** 01.10.2028
- **Beleg später:** Eröffnungsmeldung Stadt/Musikschule.
- **Wahrscheinlichkeit: 0,35.** Bestandsumbau mit Rohbau, Sparhaushalt.

---

## Brauchbar, aber nicht angelegt

- **bo-K13 — BOGESTRA: bargeldlos zahlen in allen Fahrzeugen 2026.**
  https://www.bogestra.de/unternehmen/alle-news/news-details/bilanz-2025 (17.07.2026): „Die Einführung digitaler
  Bezahlmöglichkeiten in unseren Bussen und Bahnen wurde in Absprache mit dem VRR 2025 gestartet und wird
  planmäßig in diesem Jahr abgeschlossen, sodass dann in allen Fahrzeugen mit Ticketverkauf (Straßenbahnen und
  Busse) auch die digitale, bargeldlose Bezahlmöglichkeit vorhanden ist." Frage wäre: in allen Fahrzeugen mit
  Ticketverkauf bis 31.12.2026? Nicht angelegt, weil „in allen Fahrzeugen" von außen kaum belegbar ist und
  unklar bleibt, ob „planmäßig" als Vorbehalt zählt. Schätzung 0,55. BOGESTRA ist Beteiligung von Bochum und
  Gelsenkirchen.
- **bo-K14 — Bockholtteich: Arbeiten Ende Februar 2027 abgeschlossen.**
  https://www.bochum.de/Pressemeldungen/30-September-2026/Sanierung-des-Bockholtteichs-startet-Anfang-Oktober
  (30.09.2026): „Die Arbeiten sollen voraussichtlich Ende Februar 2027 abgeschlossen werden." Nicht angelegt:
  kleines Projekt, ein Abschluss wird selten gemeldet. Schätzung 0,40.
- **bo-K15 — Husemannplatz: alle Arbeiten im Herbst 2026 abgeschlossen.**
  https://www.bochum.de/Pressemeldungen/12-Maerz-2026/Baufortschritt-auf-dem-Husemannplatz (12.03.2026): „Mit der
  bauausführenden Firma und allen anderen Baubeteiligten ist die Stadt bemüht, alle Arbeiten im Herbst 2026
  komplett abgeschlossen zu haben." Nicht angelegt: „bemüht" ist eine Absicht, „Herbst" unscharf.
- **bo-K16 — Stadtwerke: Fernwärme Agnes-/Wielandstraße bis Ende März 2027.**
  https://www.stadtwerke-bochum.de/privatkunden/ihre-stadtwerke/presse-medien/pressemeldung/stadtwerke-verdichten-fernwaermenetz-im-stadtparkviertel
  (29.09.2026): „Beide Baumaßnahmen starten ab dem 5. Oktober und werden voraussichtlich bis Ende März 2027
  dauern." Nicht angelegt: Bauende einer Leitungsbaustelle ist kaum belegbar.
- **bo-K17 — Alleestraße: Bauzeitende Dezember 2027.** Gleiche Quelle wie K06: „Die Stadt strebt nun ein
  Bauzeitende im Dezember 2027 an statt im Herbst 2027." Nicht angelegt: gleiches Projekt wie K06
  (keine zwei Wetten zum selben Projekt).

---

## Zusammenfassung

| ID | Wette | Thema | Stichtag | Stadt | Computer |
|---|---|---|---|---|---|
| bo-K01 | bochum-2026-001 | Haushalt 2027 beschlossen | 31.12.2026 | 0,80 | 0,80 |
| bo-K02 | bochum-2026-002 | Stadtpark wieder offen | 06.11.2026 | 0,80 | 0,70 |
| bo-K03 | bochum-2026-003 | Windpark Sundern fertig | 31.12.2026 | 0,80 | 0,45 |
| bo-K04 | bochum-2026-004 | SB33 eingestellt | 31.01.2027 | 0,80 | 0,75 |
| bo-K05 | bochum-2026-005 | Wasserspielplatz OSTPARK | 31.03.2027 | 0,80 | 0,40 |
| bo-K06 | bochum-2026-006 | Alleestraße Einbahnstraße weg | 31.03.2027 | 1,00 | 0,40 |
| bo-K07 | bochum-2026-007 | Haus des Wissens fertig | 30.06.2027 | 1,00 | 0,20 |
| bo-K08 | bochum-2026-008 | 11. Gymnasium startet | 30.09.2027 | 0,80 | 0,65 |
| bo-K09 | bochum-2026-009 | Lothringentrasse-Brücke frei | 31.10.2027 | 0,80 | 0,40 |
| bo-K10 | bochum-2026-010 | Dreifachsporthalle fertig | 31.12.2027 | 0,80 | 0,35 |
| bo-K11 | bochum-2026-011 | B-Plan Wilhelm-Leithe-Weg Nord | 31.12.2027 | 0,80 | 0,40 |
| bo-K12 | bochum-2026-012 | Haus der Musik in Betrieb | 30.09.2028 | 0,80 | 0,35 |

Mischung: Haushalt/Verwaltung (K01, K11), Schulen/Sport (K08, K10, K12), Verkehr (K04, K06, K09),
Kultur/Bauten/Grün (K02, K05, K07), Energie (K03).

---

## Archivbefund (04.10.2026)

Prüfung mit `werkzeuge/archivsicherung.py` (Stand Zweig `archiv-sicherung`, ohne `--speichern`, Tabelle
nur lokal, nicht committet): **11 von 12 Zitaten stehen wörtlich in einer Wayback-Kopie** (Status `ok`);
seit dem Nachtrag unten **12 von 12**.
Kopien vom 04.10.2026 (01:33–01:44 UTC) für 001–006, 008, 009, 011, 012; für 007 der Schnappschuss
vom 13.05.2026. Ohne Kopie: **bochum-2026-010** (Dreifachsporthalle): Save Page Now antwortete mit
HTTP 520, danach Zeitüberschreitung. Das Zitat steht live wörtlich (zweimal geprüft) und bleibt daher
drin; ein erneuter Sicherungsversuch steht aus. Ebenfalls ohne Kopie (520): die nicht angelegten
Kandidaten K13 (BOGESTRA) und K14 (Bockholtteich).

**Nachtrag 04.10.2026 04:30:** bochum-2026-010 trägt jetzt. Kopie
`https://web.archive.org/web/20261004021426/https://www.bochum.de/Pressemeldungen/22-Juni-2026/Baubeginn-fuer-neue-Dreifachsporthalle-an-der-Markstrasse`
(HTTP 200, 46 619 Byte laut CDX); alle drei Teile des Zitats stehen darin wörtlich (Abruf `id_`, gzip entpackt,
Tags entfernt, Leerraum normalisiert). Damit 12 von 12.

---

## Verworfen

- **Kita Lennershof (85 Plätze, 1. Halbjahr 2027):** Bauherr ist der Bau- und Liegenschaftsbetrieb NRW,
  Träger das AKAFÖ — nicht die Stadt.
- **Kita Dannenbaumstraße (Januar 2027):** freier Träger (Global Education gGmbH), keine Aussage der Stadt.
- **Wellenfreibad Südfeldmark „Ab 2027 wieder für euch da!" (WasserWelten Bochum):** kein prüfbares Datum.
- **Hallenbad Langendreer, Modernisierung „In den nächsten zwei Jahren" (WasserWelten, Bochum Journal
  12.07.2026):** Absicht ohne Datum.
- **Haus des Wissens „2027 soll das Haus des Wissens dann fertig werden" (Radio Bochum 13.01.2026):**
  Zuschreibung unklar (Satz steht nach einem Zitat einer Projektleiterin), ersetzt durch K07.
- **Haus des Wissens, Strategieseite „Angestrebt wird, dass das Haus des Wissens im Jahr 2027 fertiggestellt
  ist":** Dublette zu K07, ohne Monat.
- **OSTPARK „Bis zur IGA 2027 werden … der 4.800 Quadratmeter große Wasserspielplatz … sowie die
  Quartiersgarage" abgeschlossen sein (28.08.2025):** gleiches Projekt wie K05; K05 ist neuer und konkreter.
- **OSTPARK Stadtvillen (BPD, Ende 2026), Mehrgenerationenhaus (Sommer 2027), „Alte Stadtgärtnerei" (VBW,
  Herbst 2027):** private Bauträger, nicht die Stadt.
- **Stadtpark 3. Bauabschnitt „Fertigstellung … für den Sommer 2026 geplant" (10.11.2025):** Termin vor dem
  04.10.2026 verstrichen; ersetzt durch K02.
- **Begegnungsgarten Hamme „Voraussichtlich bis Ende Juni" 2026:** Termin verstrichen.
- **Haltestellen Arnoldschacht (Ende Oktober 2026), Oberstraße (16.10.2026), Rüsingstraße (Ende November),
  Ambergweg (28.09.2026):** Kleinbaustellen, Abschluss praktisch nicht belegbar bzw. Termin vorbei.
- **BOGESTRA Busbetriebshof Essener Straße „bis zum Ende des Jahrzehnts":** zu fern, unscharf.
- **U35-Station Ruhr-Universität, „Rück- und Neubau des Daches im Jahr 2027":** kein Monat, Bauherr Stadt,
  Freigabe hängt an der Aufsichtsbehörde; Ausgang schwer zu fassen.
- **Haushaltssicherungskonzept, 165 Mio. € jährlich bis 2035:** Prüfdatum zu fern.
- **Stadtwerke, Investitionen rund 1 Mrd. € 2024–2030:** Prüfdatum nach 2028, kaum auflösbar.
- **Elftes Gymnasium, endgültiger Neubau 2032 (Radio Bochum 28.05.2026):** zu fern.
- **Strukturelles Defizit „auf über 200 Millionen Euro pro Jahr":** keine Prognose mit Termin, und das
  strukturelle Defizit ist im Haushaltsplan keine eindeutig ablesbare Zahl.
- **Grundsteuer-Hebesatz 2027:** keine Aussage der Stadt zum Hebesatz 2027 im Wortlaut gefunden.
