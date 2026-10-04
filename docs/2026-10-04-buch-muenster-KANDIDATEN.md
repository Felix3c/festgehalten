# Buch „Münster gegen Münster" — Kandidaten, recherchiert am 04.10.2026

Status: **15 Wetten angelegt** (`buecher/muenster/wetten/muenster-2026-001` bis `-015`), Zweig `buch-muenster`
(Arbeitsverzeichnis `~/wettbuch-muenster`), nicht gemergt, nicht gepusht. Recherche, Abruf und Wortlautprüfung:
Claude, Sonntag 04.10.2026, im Dauerlauf (Auftrag Guard weiterbauen, Felix 03.10.2026). Die Freigabe (Merge,
Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl (IT.NRW, A123 2025 21, am 04.10.2026 neu
abgerufen und per `pdftotext` gelesen): Wuppertal 357 900, Bielefeld 330 825, Bonn 323 245, **Münster 307 979**.
Nach der Regel ist Bielefeld dran. Das Buch Bielefeld ist begonnen (Zweig `buch-bielefeld`, nur Kandidaten),
aber bielefeld.de antwortete am 04.10. um 18:57 weiter nicht (Zeitüberschreitung nach 21 s). Münster wurde
deshalb vorgezogen; das steht so in `BUCH.md`. Bonn hat ein Buch. Im selben Heft stehen danach Gelsenkirchen
(267 733) und Mönchengladbach (266 840); ob dazwischen noch eine Stadt liegt, vor dem nächsten Buch prüfen.

**Methode:** Die Leseansicht `stadt-muenster.de/aktuelles/pressemitteilungen` lädt den Text über eine
Schnittstelle nach (`https://pressemitteilungen.stadt-muenster.de/api/items?page=N`, 20 Mitteilungen je Seite,
Feld `plain_article`; Einzelabruf `…/api/item/<Nummer>`). Am 04.10.2026 Seiten 1–40 abgerufen (eine Seite je
2 s): **792 Mitteilungen** mit Veröffentlichung seit 01.01.2026. Sätze mit Zukunftstermin und Ankündigungsverb
herausgefiltert (89 Mitteilungen mit Treffer), von Hand gelesen, 15 ausgewählt. Jedes Zitat wurde gegen einen
**zweiten, frischen Einzelabruf** geprüft (Leerraum vereinheitlicht): **15 von 15 stehen wörtlich im Text**;
Titel und Veröffentlichungsdatum stimmen mit dem Abruf überein.

**Quelle in der Wette:** die Adresse der Schnittstelle (`…/api/item/<Nummer>`), weil die Leseansicht
(`…/pressemitteilungen#/item/<Nummer>`) ohne Browser keinen Text liefert und sich nicht archivieren lässt.
Die Leseansicht steht im Vermerk. Das weicht von den anderen Stadtbüchern ab (dort HTML-Seiten).

**Vorbehalt:** „voraussichtlich" (0,80) bei „soll", „geplant", „plant", „vorgesehen", „voraussichtlich",
„nach jetzigem Stand", „nach aktueller Planung"; sonst „angekuendigt" (1,00), wie FORMAT.md §1.2.

**Archivbefund:** Für alle 14 Quell-Adressen Save Page Now ausgelöst (alle ohne Fehler angenommen). Die
Availability-Abfrage zeigte danach für **8 von 14** eine Kopie vom 04.10.2026; in allen 8 steht das Zitat
wörtlich. Für 6 (Nummern 1211114, 1218090, 1219879, 1226457, 1227721, 1227865; Wetten 001, 003, 007, 009, 010,
013, 014) war bei zwei Abfragen noch keine Kopie sichtbar (ungeklärt, ob nur die Anzeige nachhängt). Für alle
14 liegt die Rohantwort als lokale Kopie in `recherche/belege/2026-10-04-muenster-item-<Nummer>.json`, SHA-256
im Vermerk. **Nächster Schritt:** die 6 erneut abfragen und den Vermerk ergänzen.

## Die 15 Wetten

| Nr. | Mitteilung (Nummer, Datum) | Aussage | Stichtag | Stadt | Computer |
|---|---|---|---|---|---|
| 001 | 1227865, 24.09.2026 | Blindgängerverdacht Lamberti-Kirchplatz wird am 11.10. überprüft | 11.10.2026 | 1,00 | 0,93 |
| 002 | 1219431, 12.06.2026 | Ratsgymnasium startet nach den Herbstferien im Erweiterungsbau | 06.11.2026 | 1,00 | 0,65 |
| 003 | 1211114, 05.03.2026 | Freiherr-vom-Stein-Gymnasium: Einzug in den Herbstferien | 06.11.2026 | 0,80 | 0,60 |
| 004 | 1211274, 06.03.2026 | Margaretenschule: Umzug an den Brentanoweg in den Herbstferien | 06.11.2026 | 0,80 | 0,60 |
| 005 | 1227091, 16.09.2026 | Hallenbad Wolbeck: öffentliches Schwimmen ab 07./08.11. | 08.11.2026 | 1,00 | 0,80 |
| 006 | 1228107, 28.09.2026 | Funktionsgebäude Sportanlage Arnheimweg im Dezember fertig | 31.12.2026 | 0,80 | 0,45 |
| 007 | 1226457, 09.09.2026 | Rotkehlchenweg/Zaunkönigweg bis Ende 2026 eingeführt | 31.12.2026 | 0,80 | 0,60 |
| 008 | 1218791, 05.06.2026 | Regenwasserrückhaltebecken Hiltrup Ende des Jahres fertig | 31.12.2026 | 0,80 | 0,35 |
| 009 | 1218090, 28.05.2026 | Familienzentrum Maria Aparecida: Haustechnik bis Ende des Jahres erneuert | 31.12.2026 | 1,00 | 0,45 |
| 010 | 1227721, 23.09.2026 | Gievenbecker Ortsmitte: Vorbereitungen beginnen im 1. Quartal 2027 | 31.03.2027 | 0,80 | 0,60 |
| 011 | 1228727, 02.10.2026 | Schulzentrum Wolbeck: Baubeginn im 1. Quartal 2027 | 31.03.2027 | 0,80 | 0,50 |
| 012 | 1221009, 01.07.2026 | Schulzentrum Hiltrup: Baustart Anfang 2027 | 31.03.2027 | 0,80 | 0,40 |
| 013 | 1219879, 18.06.2026 | Regenwasserpumpwerk Kanalstraße: Baubeginn März 2027 | 31.03.2027 | 0,80 | 0,50 |
| 014 | 1227865, 24.09.2026 | Lamberti-Brunnen sprudelt voraussichtlich im August 2027 wieder | 31.08.2027 | 0,80 | 0,50 |
| 015 | 1211325, 09.03.2026 | Neue Erstaufnahme Gievenbeck ersetzt im August 2027 die alte | 31.08.2027 | 0,80 | 0,45 |

Festlegungen, die Ermessen enthalten: „nach den Herbstferien" und „in den Herbstferien" (laut Mitteilung
1228574 beginnen sie am 17.10.2026) werden bis Freitag 06.11.2026 gelesen (erste Schulwoche danach, Ferienende
nicht aus einer Primärquelle geprüft); „Anfang 2027" als erstes Quartal; „Ende des Jahres" als 31.12.2026.
001 und 014 stammen aus derselben Mitteilung.

**Zeitfenster:** 001 wird am 12.10. geprüft, das Ereignis ist am So 11.10. Die Wette ist nur ehrlich, wenn
das Buch vorher öffentlich ist (Push bis Sa 10.10.). Sonst 001 vor dem Merge verwerfen („Ereignis vor
Veröffentlichung"), 14 Wetten bleiben.

## Verworfen (Auswahl)

- **Hallenbad Ost** (1228574, 01.10.): „kann am 10. Oktober bis zum Beginn der Herbstferien am 17. Oktober den
  Betrieb wieder aufnehmen" — Satz nicht eindeutig (Termin oder Zeitraum).
- **Hallenbad Roxel** 14./15.11. (1227091): hängt eng an 005, keine eigene Wette.
- **Bodelschwinghschule** (1218260, 29.05.: Umbau bis Ende 2026): laut 1223289 (30.07.) schon „weitgehend
  abgeschlossen", offen nur ein Glasaufzug „im Herbst"; Ausgang kaum belegbar.
- **Beachvolleyball-Halle** Baubeginn 4. Quartal (1212815): Bau hat laut 1224753 (20.08.) schon begonnen.
- **Matthias-Claudius-Schule** vorbereitende Arbeiten Anfang Oktober (1227085): Beginn kaum belegbar.
- **Trinkwasserbrunnen** Förderentscheidung bis Jahresende (1221209): Entscheidung eines Dritten.
- **Umweltspur Warendorfer Straße** „bis zum Frühjahr 2027" (1227874): mehrere Schritte, eine Ausnahme, unscharf.
- **Haushalt:** Doppelhaushalt 2026/2027 beschlossen, Haushaltssperre seit 08.09.2026 (1226358); kein datierter
  nächster Schritt in den Mitteilungen → keine Haushaltswette.
- Fertigstellungen 2028/2029 (Stadthaus 4, Preußenstadion, Oxford-Quartier, Berufskollegs): zu weit weg für
  die erste Runde, als Vorrat für später.

## Prüfung

`festgehalten alle buecher <ausgabe> --pruefen`: OK, 15 Bücher, 318 Wetten, keine Fehler. `pytest` im Ordner
`generator`: 99 bestanden.
