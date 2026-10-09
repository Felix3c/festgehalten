# festgehalten — Nächste Schritte

**Stand:** 08.10.2026 21:00 (Kurzfassung). Diese Datei ist öffentlich und enthält seit 07.10. nur noch Stand,
nächste Prüftage und offene Punkte, ohne Namen Dritter und ohne Entwurfstexte (Beschluss 06.10., Frage 140 b).
Die ausführlichen Arbeitsnotizen liegen außerhalb des Repos: `~/wettbuch-notizen/NAECHSTE-SCHRITTE-lang.md`
(dort weiterschreiben; Stand bis 07.10. 10:05 ist byte-gleich mit dem bisherigen Inhalt dieser Datei).
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung)
**Phase:** v1 live, 24 Bücher / 418 Wetten öffentlich.

## Wo wir stehen

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten
- Prüfung 08.10. 20:40: 24 Bücher, 418 Wetten, keine Fehler; 99 Tests grün.
- 09.10. 14:45: **Gepusht** (`273dd60` auf master, Home-Tab): enthält bonn-2026-034 JA, Spalte „davon sonstige“,
  Wortlaut-Vermerke und Dortmund 015–017; die drei Rohkopien fremder Stadtseiten sind aus dem Index (nur Wayback-Link
  + SHA-256, Ordner in `.gitignore`). Offen aus demselben Beschluss: essen-2025-011 Stichtag 31.12.2027, essen-2025-013
  verwerfen, dortmund-2025-013/-014 Vermerk bis 01.01.2028; `buch-ki-2` wartet auf Frage 229.
- 09.10. 12:05: Wörtliche Zitate fertig: keine Warnung mehr. Dortmund-Kita 005–007 nannten eine Quelle ohne Platzzahl
  und Termin; ersetzt durch 015–017 mit der Stadtmeldung vom 07.07.2025 (Ausgänge unverändert, alte Einträge bleiben
  mit `ersetzt_durch`). Zweig `wortlaut-vermerke` lokal in master gemergt (`04dc9e3`), 421 Wetten, 143 Tests grün,
  **nicht gepusht** (vorher Rohkopien in `recherche/belege/` klären).
- 09.10. 08:30: Startseite zeigt jetzt die Spalte „davon sonstige“ (ersetzt/verfallen/strittig), damit jede Zeile aufgeht
  (Köln vorher 87 gesamt bei 29 + 55); lokal `2c61bfe`, 100 Tests grün, **nicht gepusht** (wartet auf „steht“).
- 32 fällige offene Wetten (Stand 08.10.): 25 Zahl-Wetten, die meisten warten auf festgestellte
  Jahresabschlüsse oder Schlussrechnungen (15 davon ausdrücklich auf einen Jahresabschluss), und 7 Ja/Nein-Wetten.
  Die drei ersetzten Köln-Einträge (koeln-2025-001/-002/-004) zählen nicht mit; die frühere Zahl 35 enthielt sie.
- Köln-Wartezeiten werden seit 05.10. an der Anzeige der Stadt gemessen (Windows-Aufgaben und GitHub als zweite
  Messstelle, je Slot zählt der früheste Abruf mit Rohkopie). Oktober bisher: 2 Messtage, Mittel 18,1 Min.,
  Maximum 68 Min. Der alte Feed ist seit 16.09. eingefroren.

## Nächste Prüftage

- Fr 09.10.: bonn-2026-034 **aufgelöst JA** (09.10. 00:20, Beleg SWB-Meldung 28.09. „Nach erfolgreichen Sanierungsarbeiten an Gleis 1“, lokal committet, nicht gepusht); wuppertal-2026-001 **offen**: bis 09.10. 00:20 nur Ankündigungen (Stadt, Rundschau, talzeit vom 07.10.), kein Bericht über die Eröffnung; weiter prüfen bis ~15.10., dann Frage an Felix (Vorschlag NEIN mangels Beleg); Nachprüfung 09.10. 11:55: weiter kein Bericht nach dem Termin (Stadt-Meldungsliste nur die Ankündigung vom 01.10., Rundschau nur Vorbericht 02.10., Talzeit-Artikel erschien 08.10. ~05:00, also vor 15:30, „Seit heute (8. Oktober)“ ist Vorbericht, kein Beleg)
- So 11.10.: wuppertal-2026-002 (Vorprüfung 09.10. 12:25: Quelle unverändert „Anfang Oktober geplant“, keine Meldung der Stadt, nichts in der Presse nach August, keine Verschiebung; ohne Beleg „fertig“ bis 10.10. gilt NEIN; Notiz in `docs/2026-10-04-aufloesung-wuppertal-0910-1110-VORBEREITET.md`, lokal `0360f4d`)
- Mo 12.10.: muenster-2026-001 (Vorprüfung 09.10. 12:40: Quelle byte-gleich, keine Absage/Verschiebung in den Mitteilungen bis 09.10. 10:03, lokal `5dcbf4a`); Köln-Messung 10:00 und 14:00 — Achtung: alle Kundenzentren an dem Tag geschlossen (Personalversammlung, Hinweis der Stadt, abgerufen 08.10.); Umgang mit Nullen offen (Frage 184)
- Mi 14.10.: bielefeld-2026-001, hamm-2026-001 (Hamm: Punkt steht als TOP 2.15 auf der Ratssitzung 13.10., geprüft 08.10.; Vorberatung 07.10. mehrheitlich empfohlen 34/3/2, geprüft 09.10.)
- Do 15.10.: essen-2026-035 bis -038 und essen-2025-001 (Rat 14.10., Feststellung Jahresabschluss 2025); alle vier Vorlagen 035–038 stehen auf der Tagesordnung (TOP 6, 19, 20, 25; zu 19/20 Änderungsanträge), geprüft 08.10.; TOP 7/8 Jahresabschluss erneut geprüft 09.10., unverändert
- So 01.11.: essen-2026-039, wuppertal-2026-003, wuppertal-2026-004; Mo 02.11.: bonn-2026-033 (hängt an Frage 197);
  Sa 07.11.: bochum-2026-002; So 08.11.: koeln-2026-076 (Zitat ist Zusammenfassung wie bei 197). Vorlage mit Abruf
  08.10.: `docs/2026-10-08-aufloesung-0111-0811-VORBEREITET.md`, alle Quellen unverändert, keine Absage gefunden.
- Dazu seit 08.10. 20:10 (Bücher seit dem Morgen auf master): So 01.11. aachen-2026-001, gelsenkirchen-2026-001
  (Baustellenkarte: bis voraussichtlich 30.10., hält), gelsenkirchen-2026-002 (Richtung NEIN, Karte 30.11.),
  krefeld-2026-001; Sa 07.11. muenster-2026-002 bis -004; Mo 09.11. muenster-2026-005. Vorlage
  `docs/2026-10-08-aufloesung-0111-0911-nachtrag-VORBEREITET.md`, alle acht Zitate wörtlich, keine Absage gefunden.

- Dazu seit 08.10. 20:55: 17.11. wuppertal-2026-005, 18.11. bielefeld-2026-002, 19.11. bonn-2026-031, 20.11.
  duesseldorf-2026-035 und koeln-2026-075, 24.11. koeln-2026-074, 28.11. duesseldorf-2026-032. Vorlage
  `docs/2026-10-08-aufloesung-1711-2811-VORBEREITET.md`, alle sieben Quellen unverändert abrufbar.

## Offene Punkte

- 09.10. 14:10: Buch „KI gegen KI“ um drei Wetten erweitert (ki-2026-010 Mistral, -011 Domyn, -012 Dweve), Zitate live
  und im Archiv wörtlich geprüft, 424 Wetten ohne Fehler, 109 Tests grün; Zweig `buch-ki-2` (`9f3dd08`), **nicht gepusht**
  (wartet auf „steht“). Prüfweg und Verworfenes in `docs/2026-10-09-buch-ki-anbieter-NACHTRAG.md`.

- Wörtliche Zitate (Beschluss 04.10.): Zweig `wortlaut-vermerke` (lokal) enthält die Vorarbeit vom 04.10., eine
  Warnung im Generator (`--zitate recherche/archiv-quellen.csv`, 8 neue Tests, 107 grün) und die ersten Vermerke
  (sieben Wetten, darunter bonn-2026-031 ohne die mehrdeutige 12-Uhr-Bedingung). Stand 08.10.: 161 Wetten ohne
  Vermerk; die seit 04.10. neuen Wetten werden gerade nachgeprüft. Mergen erst, wenn alle Vermerke stehen.
  Stand 09.10. (Dauerlauf, H21): Werkzeugfehler behoben (`a03bb23`): die Prüfung löschte HTML-Entities statt
  sie zu dekodieren, Umlaut-Zitate galten fälschlich als nicht wörtlich (4 von 23 geprüften waren Fehlalarme).
  Neu `--nur-neue`. 19 neue Wetten in der Prüfliste, 19 Vermerke an den fälligen offenen Wetten (`7165ecd`),
  Warnungen 163 → 139, 107 Tests grün. Nächste Portion: erst `archivsicherung.py buecher --max 20` OHNE
  `--nur-neue` (prüft die alten zitat_fehlt mit dem Fix nach, räumt Fehlalarme ab), dann Vermerke nach Prüftag.
  Tests im Worktree nur mit `PYTHONPATH=generator` (sonst lädt Python das Paket aus `~/wettbuch`).
  Stand 09.10. 10:45 (Portion 2): die 20 nächstfälligen offenen Warnungen (Köln Wartezeit 077–082, Essen
  002/020/021/022/026, Dortmund 008/010/011/2026-015, Köln 024/055–058) live mit dem reparierten Abgleich geprüft:
  alle 20 echt nicht wörtlich (kein Fehlalarm), je Vermerk mit Wortlaut + SHA (`275be19`), Warnungen 139 → 119
  (72 offene, 47 aufgelöste), 107 Tests grün. Noch offen: die alten zitat_fehlt-Zeilen in der csv mit dem Fix
  nachprüfen (`archivsicherung.py buecher --max 20` ohne `--nur-neue`), dann nächste 20 nach Prüftag (ab koeln-2025-009).
  Stand 09.10. 10:32 (Portion 3): nächste 20 nach Prüftag (Dortmund 002/003, Düsseldorf 010/011/013–015/029,
  Köln 009/010/016–018/060, Duisburg 2026-008, Essen 011, Bonn 014–017) live geprüft: duisburg-2026-008 Fehlalarm
  (csv → ok), 19 Vermerke (`37c9227`), Warnungen 119 → 99 (52 offen), 107 Tests grün. **Achtung essen-2025-011:** Quelle
  nennt nur „2027“, kein „2. Quartal“; der Stichtag 30.06.2027 ist damit nicht aus der Quelle belegt (Frage an Felix).
  Stand 09.10. 10:40 (Portion 4): nächste 20 ab dortmund-2025-004 live geprüft: zwei Fehlalarme (koeln-2025-063
  nach Entity-Fix ok; gatekeeper-2026-009 ist .docx, das Werkzeug las es als Binärsalat → `archivsicherung.py`
  liest jetzt .docx, Test zuerst, `15bb405`), csv → ok; 18 Vermerke (`08999b5`), Warnungen 99 → 79 (32 offen),
  140 Tests grün (werkzeuge + generator). **Achtung essen-2025-013:** Quelle (live und Archiv 19.05.2026) nennt für
  die Grundschule Moltkestraße gar keinen Termin (Frage an Felix, wie essen-2025-011).
  Stand 09.10. 10:50 (Portion 5): 20 ab bonn-2025-003 live geprüft: ein Fehlalarm (aachen-2026-012, aachen.de
  schreibt Umlaute zerlegt (u + U+0308) → `archivsicherung.py` normalisiert jetzt NFC, Test zuerst, `5d7b539`, csv → ok);
  19 Vermerke (`07b9821`), jeder vermerkte Wortlaut gegen die Live-Quelle nachgeprüft, Warnungen 79 → 59 (12 offen),
  141 Tests grün. Inhaltlich auffällig (nur Vermerk, keine Frage): bonn-2025-012/013 Quelle sagt Stadtverwaltung statt
  Konzern, bonn-2025-018 nur 300 *zu prüfende* Gebäude, bonn-2025-023 nur Planungen bis 2028.
  Stand 09.10. 11:05 (Portion 6): die letzten 12 offenen Warnungen (koeln-2025-013 bis bonn-2025-030) live
  geprüft, kein Fehlalarm, 12 Vermerke (`a72affe`), Warnungen 59 → 47, **keine offene Wette mehr ohne Vermerk**;
  107 Tests grün. Auffällig (nur Vermerk): bonn-2025-011 Quelle sagt Einsparungen im beschlossenen Haushalt statt
  Konsolidierungsvolumen, duesseldorf-2025-023 „städtische Schulen“ statt Schulbauoffensive. Rest: 47 Warnungen an
  aufgelösten Wetten, danach csv-Nachprüfung der alten zitat_fehlt ohne `--nur-neue`, dann Merge in master (lokal).
  Stand 09.10. 11:25 (Portion 7, aufgelöste Wetten): 20 live geprüft (Dortmund 005–007 ausgelassen, Frage 76),
  sechs Köln-Fehlalarme (Entities) in der csv auf ok, 14 Vermerke (`beb6a16`), Warnungen 47 → 27; 107 + 34 Tests grün.
  Auffällig (nur Vermerk): duesseldorf-2025-020/-022 die 5,4 Mio. gelten Hansaallee–Luegplatz, nicht „1. Bauabschnitt“;
  dortmund-2025-012 die 3,1 Mio. sind die Erwartung für 2024; duesseldorf-2025-024 Erweiterungsbau statt Neubau.
  Stand 09.10. 11:28 (Portion 8, letzte aufgelöste): 24 nachgeprüft, drei Fehlalarme (koeln-2025-044/-069,
  essen-2025-007) in der csv auf ok, 21 Vermerke (`a95ec0c`), jeder Wortlaut vor dem Schreiben automatisch wörtlich
  gegen die Live-Quelle geprüft (`tmp/h21/vermerke8.py`), Warnungen 27 → 3; 107 Tests grün. Auffällig (nur Vermerk):
  essen-2025-033 Quelle sagt „(Nach-)Besetzungssperre“ statt Einstellungsstopp, essen-2025-006 die 24.482 Plätze
  gelten zum Ende des Kita-Jahres, essen-2025-027 „Bahnhofstangente“ statt „Stufe 1“.
  **Rest: nur dortmund-2025-005/-006/-007, warten auf Frage 76** (Quelle/Zitat tauschen statt Vermerk). Danach Merge
  `wortlaut-vermerke` in master (lokal), Push erst nach „steht“.

- Bonn: Ratsinformationssystem hinter einer Bot-Sperre; bonn-2026-035/-036 nur im eigenen Browser prüfbar. bonn.de-Pressemitteilungen am 08.10. im Chrome-Werkzeug geprüft: keine Folge-Meldung zu 035, zu 036 nur der Ratsbeschluss 24.09. (Hauptausschuss nicht erwähnt); beide weiter ungeklärt.
- Großstädte statt weiterer NRW-Städte: zuerst London. Aufwand und Rechtslage geprüft 07.10.
  (`recherche/LONDON-AUFWAND-2026-10-07.md`): Sprach-Schalter nötig, Rohkopien nur lokal. Eigener Zweig erst
  nach Entscheidung; veröffentlicht wird erst nach Freigabe.
- London, Oxford Street (geprüft 08.10.): Primärquelle gefunden, TfL „Oxford Street area works“ nennt Mo 26.10.2026
  als Start (Wayback 20261008040024). Kandidat T-OX in `~/wettbuch-notizen/london-gla/KANDIDATEN-GLA-2026-10-08.md`;
  nur ehrlich, wenn er vor So 25.10. öffentlich steht (Frage 196).
- gelsenkirchen-2026-002 (Gasleitung Kurt-Schumacher-Straße, Prüftag 01.11.): Die Baustellenkarte der Stadt nennt
  seit 04.10. „bis voraussichtlich 30.11.2026“ (Hinweis einer Lokalredaktion 08.10.). Vermerk mit Archivkopie
  20261008080928 und lokaler Kopie eingetragen (`7593025`, lokal); Prognosen unverändert, ob die Richtung Buer bis
  31.10. fertig ist, bleibt ungeklärt.
- Zweige `archiv-sicherung` und `wortlaut-vorschlag` sind nicht gemergt (Archivkopien, Wortlaut-Vorschläge).
- Sieben IFG-Anfragen (`recherche/IFG-2026-09.md`) nicht gesendet; Nachfolge als Hüter bis 31.12.2026 offen.
- Ungeklärt (geprüft 08.10.): Innenstadt Köln zeigte am 07.10. zweimal 0 Min.; die Datei trennt „niemand wartet“ nicht von „kein Wert“, die Stadt meldet für Innenstadt Kasse geschlossen 07.–08.10. Oktobermittel 18,1 Min. mit, 19,2 ohne die 0. Vermerk `recherche/koeln-wartezeit/VERMERK-INNENSTADT-0-MIN-2026-10-07.md`.

## Wartet auf Felix

- Push von master (lokal voraus: Köln-Messung 07.10., diese Kurzfassung und seit 08.10. die nachgetragene Archivkopie für muelheim-2026-001).
- IFG-Anfragen, Hüter-Nachfolge, gemergte Zweige `weitsicht` und `hinterlegt-sammelbuch` löschen.

- 08.10.2026 18:59 (Dauerlauf H18): Fachfragen an Matthieß (Göttingen), U. Krüger (Leipzig), Birch (Laval) gesendet. Sprachregel für Mails: „418 Einträge“ (nicht Ankündigungen), Prognose „zu den meisten Einträgen“ (331 von 418 laut öffentlichem Stand 05.10.).
