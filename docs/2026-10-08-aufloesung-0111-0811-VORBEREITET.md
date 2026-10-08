# Auflösung vorbereitet: Prüftage 01.11. bis 08.11.2026 (master)

Stand 08.10.2026 08:30, Dauerlauf (Claude). Betrifft die Wetten auf master mit Prüftag 01.–08.11., für die es noch
keine Vorlage gab: essen-2026-039, wuppertal-2026-003, wuppertal-2026-004 (01.11.), bonn-2026-033 (02.11.),
bochum-2026-002 (07.11.), koeln-2026-076 (08.11.). koeln-2026-077 steht schon in
`2026-10-08-aufloesung-koeln-073-und-ueberfaellige-VORBEREITET.md`. Wettdateien unverändert, nichts aufgelöst.
Wetten nur auf Zweigen (aachen-001, gelsenkirchen-001/-002, krefeld-001, muenster-002 bis -004, london-001) sind
hier nicht dabei; sie hängen an Merge und Push (Fristen in ALLEIN.md 6a/7c und H5c).

Alle Quellen am 08.10.2026 zwischen 08:24 und 08:28 abgerufen (curl, Browser-Kopfzeilen). Prüfsummen (SHA-256,
erste 16 Zeichen) nur zum Wiedererkennen, keine Kopie im Repo.

## 01.11. essen-2026-039 — 50. Steeler Weihnachtsmarkt, Start 30./31.10.

- Quelle (WAZ, 24.08.) heute abrufbar, Satz unverändert: „Der Weihnachtsmarkt in Steele startet mit einem
  Jubiläumswochenende am 30. und 31. Oktober.“ (`0b69ed637a1d5288`). Websuche 08.10.: Veranstaltungsportale nennen
  30.10.2026 bis 03.01.2027, keine Absage oder Verschiebung gefunden.
- **Am 01.11. prüfen:** WAZ Essen und Radio Essen auf einen Bericht vom Eröffnungswochenende, dazu
  essen.de-Pressemitteilungen. Die eigene Seite des Marktes antwortete heute nicht (weder steeler-weihnachtsmarkt.de
  noch weihnachtsmarkt-steele.de, curl Code 6); die Adresse ist ungeklärt.
- **Regel:** JA, wenn ein Bericht belegt, dass der Markt am 30. oder 31.10. geöffnet war. Eine Vorschau reicht nicht.
- Aus dem Kontext der Wette: Veranstalter ist ein Verein, nicht die Stadt; die Zuordnung bleibt schwach.

## 01.11. wuppertal-2026-003 — Brücke Fischertal fertig bis 31.10.

- Quelle (wuppertal.de, 10.09.) unverändert: „verzögert sich die Fertigstellung der Gesamtmaßnahme voraussichtlich
  bis Ende Oktober 2026“ (`a81eb7bc3a93e00c`). Liste „Aktuelle Meldungen“ (`2c63dedaa7d1ce3d`) und Oktober-Archiv
  (`3f4b6fadadc2ebb1`): kein Treffer für „Fischertal“. Websuche ohne Ergebnis.
- **Am 01.11. prüfen:** Liste und Archiv Oktober/November, WSW-Meldungen zur Linie 644 (Rückkehr auf den Linienweg),
  WZ Wuppertal, Wuppertaler Rundschau.
- **Regel:** JA nur mit öffentlichem Beleg „freigegeben“ oder „abgeschlossen“ bis einschließlich 31.10. Ohne Beleg
  bis zum Prüftag: Frage an Felix mit Vorschlag NEIN mangels Beleg (wie bei wuppertal-2026-001).
- Abruf: wuppertal.de braucht die `Sec-Fetch-*`-Kopfzeilen, sonst 403. Save Page Now hat die Stadt bisher dreimal mit
  HTTP 520 abgewiesen; Beleg dann als lokale Kopie mit SHA-256 nach `recherche/belege/`.

## 01.11. wuppertal-2026-004 — Gemeinsame Gesellschaft der Stadtwerke, notarielle Gründung bis 31.10.

- Quelle (WSW, 20.07.) unverändert: „vorbehaltlich der Genehmigung durch die Kommunalaufsicht ist die notarielle
  Gründung zum Oktober 2026 vorgesehen“ (`510302a1e42f82d2`). WSW-Pressemitteilungen bis 06.10. (`3c5e9d7fd3d0af8e`):
  keine Meldung zur Gründung oder zur Genehmigung. Websuche ohne Ergebnis. Name der Gesellschaft weiter ungeklärt.
- **Am 01.11. prüfen:** WSW-Pressemitteilungen, Stadtwerke Solingen, EWR Remscheid, Solinger Tageblatt,
  Remscheider General-Anzeiger, Handelsregister-Bekanntmachungen (nur, wenn der Name bis dahin bekannt ist).
- **Regel:** JA, wenn eine Meldung oder Registerbekanntmachung die notarielle Gründung bis einschließlich 31.10.
  belegt. Die Eintragung kann später kommen; gefragt ist die Gründung. Ohne Beleg: Frage an Felix, Vorschlag NEIN
  mangels Beleg. Risiko: eine Gründung, die niemand meldet, sieht hier aus wie keine Gründung.

## 02.11. bonn-2026-033 — Neue Verwaltungsstruktur in Kraft zum 01.11.

- Offen ist Frage 197 (seit 08.10. 07:35): das `zitat` ist eine Zusammenfassung, die Pressemitteilung sagt „mit
  Ausnahme der Einrichtung des neuen Dezernates vorbehaltlich der formellen Beteiligung des Personalrates zum
  1. November“. Diese Vorlage ändert daran nichts.
- **Am 02.11. prüfen:** bonn.de-Pressemitteilungen Oktober/November, Dezernatsverteilung auf bonn.de,
  General-Anzeiger, Radio Bonn. Das Ratsinformationssystem steht hinter einer Bot-Sperre (nur im eigenen Browser).
- **Regel:** hängt an der Antwort auf 197. Bei 197 a: JA, wenn die Neuordnung (ohne das neue Dezernat) zum 01.11.
  belegt in Kraft ist.

## 07.11. bochum-2026-002 — Stadtpark wieder freigegeben spätestens 06.11.

- Quelle (Radio Bochum, 14.08.) unverändert: „soll der neugestaltete Stadtpark am 6. November im Rahmen einer
  kleinen Eröffnungsfeier wieder für die Öffentlichkeit freigegeben werden“ (`67c34b83eaf30fde`). Websuche 08.10.:
  nichts Neueres zur Eröffnung; das Kunstmuseum zeigt zum 150. Geburtstag des Parks „Das öffentliche Grün“ bis 01.11.
  Die Radio-Bochum-Seite `/nachrichten/bochum` gibt 404; eine andere Nachrichtenliste wurde nicht gesucht.
- **Am 07.11. prüfen:** bochum.de-Pressemitteilungen, Bochum Marketing (plant laut Quelle die Feier), Radio Bochum,
  WAZ Bochum. Ende Oktober lohnt ein Blick, ob eine Einladung zur Feier erschienen ist.
- **Regel:** JA, wenn der Park bis einschließlich 06.11. offiziell freigegeben ist (Feier oder Freigabemeldung);
  gesperrte Teilflächen ändern daran nichts, solange die Stadt ihn als freigegeben meldet.

## 08.11. koeln-2026-076 — ZettEmm Open 2026, Aufführung am 07.11. in der Alten Feuerwache

- Quelle (stadt-koeln.de, „Aus Ämtern und Stadtbezirken 458“) abrufbar (`11f45ae3c8a17603`). **Das `zitat` steht so
  nicht in der Quelle** (gleiche Art wie Frage 197). Wortlaut: „Sieben Teilnehmer*innen wurden mit einem Preis
  ausgezeichnet: […] Die (Ur)aufführungen der preisgekrönten Werke sind beim 14. Jugendfestival für zeitgenössische
  Musik ZettEmm_20_26 am 7. November 2026 in der Alten Feuerwache zu erleben.“ Die Zahl sieben steht bei den
  Preisträgern, nicht bei den Werken; Ort und Datum stimmen.
- Vorschlag: nach Felix' Antwort zu 197 hier gleich verfahren (bei 197 a: Vermerk mit dem Wortlaut an die Wette,
  aufgelöst wird, ob die Aufführung der preisgekrönten Werke am 07.11. in der Alten Feuerwache stattfand).
- **Am 08.11. prüfen:** Programm des Festivals ZettEmm_20_26 (Rheinische Musikschule), Veranstaltungskalender der
  Alten Feuerwache, stadt-koeln.de-Presse, Kölner Stadt-Anzeiger.
- **Regel:** JA, wenn die Aufführung am 07.11. dort belegt stattfand (Nachbericht oder Programm mit Hinweis auf
  den Abend). Eine Ankündigung allein reicht nicht; ohne Nachbericht: Frage an Felix.
