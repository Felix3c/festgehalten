# Buch „Bielefeld gegen Bielefeld" — Kandidaten, Stufe 1, recherchiert am 04.10.2026

Status: **noch keine Wette angelegt, kein BUCH.md.** Zweig `buch-bielefeld` (Arbeitsverzeichnis
`~/wettbuch-bielefeld`, auf master `f641a19` vorgespult), nicht gemergt, nicht gepusht. Recherche: Claude,
Sonntag 04.10.2026, 18:23–18:38, im Dauerlauf (Auftrag Guard weiterbauen, Felix 03.10.2026).

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl (IT.NRW, A123 2025 21, Zahlen übernommen aus
`buecher/wuppertal/BUCH.md`, hier nicht neu abgerufen): Wuppertal 357 900 (Buch seit 04.10.), **Bielefeld 330 825**.
Bonn hat schon ein Buch. Ob zwischen Bielefeld und der nächsten Stadt eine weitere ohne Buch liegt, ist für
dieses Buch unerheblich; für das danach: ungeklärt, in der IT.NRW-Tabelle nachsehen.

## Warum das Buch heute nicht fertig wurde

bielefeld.de hat den Rechner nach rund 65 Abrufen in zehn Minuten ausgesperrt (erst HTTP 503, dann keine
Verbindung mehr, Stand 18:38). Die Wayback Machine antwortet auf Save Page Now mit HTTP 429 (zu viele Anfragen
heute). Damit fehlen die zwei Dinge, die jedes Buch bisher hatte: der **zweite, frische Abruf** jedes Zitats
und die **Archivkopie**. Ohne beides lege ich keine Wetten an.

Vermutlich hing der abgebrochene Lauf von heute 07:58–10:58 (drei Stunden, keine Spuren außer diesem leeren
Zweig) an derselben Sperre.

**Regel für den nächsten Lauf:** bielefeld.de höchstens ein Abruf alle 5 Sekunden, höchstens 40 je Lauf,
bei der ersten 503 aufhören. Erst prüfen, ob die Sperre weg ist (`curl -m 25 https://www.bielefeld.de/node/35886`).

## Was vorliegt

- Listenansicht `https://www.bielefeld.de/pressemeldungen` Seiten 0–14 vollständig: **728 Mitteilungen**
  (Titel, Datum, Anriss), zurück bis Januar 2026. Die Seite ist ein Drupal, jede Mitteilung `/node/<Nummer>`.
- Volltext der **49 jüngsten** Mitteilungen (24.09.–02.10.2026), einmal abgerufen 18:23–18:33.
- Darin **24 Mitteilungen mit Terminsatz**. Kopie je Seite in `recherche/belege/2026-10-04-bielefeld-node-<Nummer>.html`,
  byte-gleich zum Abruf (`.gitattributes` `recherche/belege/** -text`), SHA-256 unten.
- Die Zitate unten hat ein Skript aus dem Seitentext geschnitten (Tags entfernt, Leerraum vereinheitlicht),
  nicht abgetippt. Sie sind **einmal** abgerufen, nicht ein zweites Mal bestätigt.

## A. Brauchbar (sieben Mitteilungen, neun Sätze)

Kriterium: Termin mit Monat oder Tag, und das Ende lässt sich später belegen (Folgemeldung der Stadt oder
der Stadtwerke, Lokalpresse, bielefeld-baut.de). „gesagt_von“: Mitteilungstext, keine Person zitiert.

### node 37384 — Windfang: Arbeiten verlängern sich

- **URL:** https://www.bielefeld.de/node/37384
- **gesagt_am:** 02.10.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Straße Windfang bleibt in Höhe des Wasserwerkes aufgrund von Arbeiten an den Wasserleitungen noch bis Ende November voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37384.html`, SHA-256 `c67be407c3bd314ff397e60a9f8f799445368c5b98bcb780ab898148d91e3f10`

### node 37364 — Straßenbauarbeiten: Abschnittsweise Sperrungen im Alten Postweg

- **URL:** https://www.bielefeld.de/node/37364
- **gesagt_am:** 01.10.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten beginnen am Montag, 5. Oktober, und werden bis Ende November andauern.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37364.html`, SHA-256 `3f34ef64481793b448b7a52485a3977347848b47ee83f77df81025f92bf4021b`

### node 37353 — Arbeiten in der Ravensberger Straße dauern an

- **URL:** https://www.bielefeld.de/node/37353
- **gesagt_am:** 30.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Vollsperrung in Höhe des Baugrundstücks bleibt bis voraussichtlich Ende Februar 2027 bestehen.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37353.html`, SHA-256 `7224570a6aee151a5c1d4327fc3351b052c45847458b601d8e58099702baec47`

### node 37305 — Herforder Straße: Arbeiten der Stadtwerke Bielefeld in neuem Teilstück führen zu neuem Verkehrsfluss Strom-Projekt: Stadtwerke arbeiten ab 30. September im Kreuzungsbereich Am Stadtholz

- **URL:** https://www.bielefeld.de/node/37305
- **gesagt_am:** 28.09.2026 · **Wer:** Stadtwerke Bielefeld (Pressemeldung, von der Stadt verbreitet)
- **Zitat:** „Die Arbeiten im Kreuzungsbereich dauern voraussichtlich bis Ende Oktober.“
- **Zitat:** „Sowohl dieser Bauabschnitt als auch der Anfang September zwischen Schildescher Straße und Beckhausstraße gestartete Abschnitt werden voraussichtlich Ende Oktober abgeschlossen.“
- **Zitat:** „Voraussichtlich soll die gesamte Maßnahme bis zum Jahreswechsel 2027 abgeschlossen werden.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37305.html`, SHA-256 `892f67cc80526380d29fec5e52101c56dbe703294e9e988ac000363b3ebda394`

### node 37295 — Eingezogene Spur in der Artur-Ladebeck-Straße

- **URL:** https://www.bielefeld.de/node/37295
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Baumaßnahme soll bis Dienstag, 17. November, abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37295.html`, SHA-256 `3aee7a849bebdc67357fbffd820ff4413d9dd2d398ef0e8f49e00436ec16f65e`

### node 37208 — Kanalarbeiten in Gadderbaum

- **URL:** https://www.bielefeld.de/node/37208
- **gesagt_am:** 25.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die gesamte Baumaßnahme soll im Frühjahr 2028 abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37208.html`, SHA-256 `62ea0af47e6236dfe1126fb30f3b6cb2a3838067e9cd8eef87ed256145a7ad36`

### node 37207 — Abschnittsweise Sperrung der Wüstenrotstraße

- **URL:** https://www.bielefeld.de/node/37207
- **gesagt_am:** 25.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Kanalarbeiten auf Höhe der Wüstenrotstraße 1 und Alter Postweg sind für die Osterferien 2027 vorgesehen.“
- **Zitat:** „Der Umweltbetrieb geht davon aus, dass das Gesamtprojekt Wüstenrotstraße voraussichtlich im Juli 2027 abgeschlossen sein wird.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37207.html`, SHA-256 `ea3d848924880da5712cd77d6839484de767dce95a28a8dc3348a230d9a66604`

## B. Schwach (17 Mitteilungen)

Kurze Sperrungen (Kran, Baumpflege, Leitung, eine bis sechs Wochen). Termin steht drin, aber das Ende meldet
später niemand; ohne Beleg wäre jede Auflösung „Nein mangels Beleg“ und damit unfair gegenüber der Stadt.
Empfehlung: nicht aufnehmen, höchstens zwei oder drei als Eichwetten, wenn bielefeld-baut.de das Ende zeigt
(ungeklärt, Seite nicht abgerufen).

### node 37382 — Ramsbrockring wegen Kanalarbeiten gesperrt

- **URL:** https://www.bielefeld.de/node/37382
- **gesagt_am:** 02.10.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Der Ramsbrockring wird von Montag bis voraussichtlich Freitag, 5. bis 16. Oktober, zwischen den Einmündungen Donauallee und Sprungbachstraße halbseitig gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37382.html`, SHA-256 `3c4b6d8bb38c803c7cccf610db93c39d70568c268f19fa1f43dea3afc86a72af`

### node 37381 — Literaturtage: Absage der Lesung mit András Visky

- **URL:** https://www.bielefeld.de/node/37381
- **gesagt_am:** 01.10.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Ein Ersatztermin ist für März 2027 geplant; das genaue Datum wird zeitnah mitgeteilt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37381.html`, SHA-256 `0fa3b3fa38074bdc75bd220ebc4fe92ab5504c6d2ace7d32afc10ff60c85ad1a`

### node 37354 — Baumpflege: Vollsperrung in der Furtwänglerstraße

- **URL:** https://www.bielefeld.de/node/37354
- **gesagt_am:** 30.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten sollen Mitte Oktober abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37354.html`, SHA-256 `dfebdffc744c34a45f9c18460f83ebafd3e40f3fae43b3b75ab5306bd6a63dbe`

### node 37328 — Vollsperrung der Neustädter Straße

- **URL:** https://www.bielefeld.de/node/37328
- **gesagt_am:** 29.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten sollen Anfang November abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37328.html`, SHA-256 `27378180496dc8fa20aa99ceff6de7a6150ec43f0394fe65f36dd39e25a84e73`

### node 37324 — Kanalarbeiten: Idunastraße halbseitig gesperrt

- **URL:** https://www.bielefeld.de/node/37324
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Idunastraße wird im Einmündungsbereich zur Osnabrücker Straße von Montag, 5. Oktober, bis Freitag, 16. Oktober, halbseitig gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37324.html`, SHA-256 `d152708d7875e79cb15df36a7b5badc9b2c113b89626d0e20e5f880e28741e6e`

### node 37319 — Fernmeldeleitungen: Altmühlstraße wird zur Einbahnstraße

- **URL:** https://www.bielefeld.de/node/37319
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Altmühlstraße wird von Montag bis Freitag, 5. bis 9. Oktober, halbseitig unter Einbahnstraßenregelung gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37319.html`, SHA-256 `cd27f64ac77575c615c7344239b9d110ca526fe9baaf71af1358534d47958b0d`

### node 37308 — Abschnittsweise Sperrung der Körnerstraße

- **URL:** https://www.bielefeld.de/node/37308
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten sollen Mitte November abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37308.html`, SHA-256 `2adeac88f83996674d66089616abcbad2f01ecaf7272a13fab55432ff7fc8895`

### node 37300 — Straßenbauarbeiten in der Wilbrandstraße

- **URL:** https://www.bielefeld.de/node/37300
- **gesagt_am:** 02.10.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten sollen Anfang November abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37300.html`, SHA-256 `4777cee334c7bd825883ae25ed9b04d1b95e0d85c0bc25596d1fb80fc12ab6a0`

### node 37299 — Arbeiten in der Graf-Bernadotte-Straße dauern an

- **URL:** https://www.bielefeld.de/node/37299
- **gesagt_am:** 25.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Aufgrund von Arbeiten an den Versorgungsleitungen der Stadtwerke Bielefeld bleibt die Graf-Bernadotte-Straße in Höhe der Hausnummer 43 noch bis voraussichtlich Mitte Oktober voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37299.html`, SHA-256 `d64367283af9255b4c7680d63291ba0e0fb8a4bd2936db0a18823341f60f7310`

### node 37298 — Versorgungsnetz: Vollsperrung in der Bechterdisser Straße

- **URL:** https://www.bielefeld.de/node/37298
- **gesagt_am:** 25.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Bechterdisser Straße wird zwischen der Evenhausener Straße und dem Schmetterlingsweg von Montag, 28. September, bis voraussichtlich Mitte November voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37298.html`, SHA-256 `75c39cfc0aa645a345808537fa2a6c110019b873e38ddccb1a19d2f20beacd24`

### node 37294 — Kranarbeiten: Vollsperrung in der Furtwänglerstraße

- **URL:** https://www.bielefeld.de/node/37294
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Arbeiten sollen Mitte Oktober abgeschlossen sein.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37294.html`, SHA-256 `adc5f88bbf6b28a51a1e51bbbbf28964e973d3c70214d6664753846841a216ba`

### node 37293 — Vollsperrung in der Buddestraße dauert an

- **URL:** https://www.bielefeld.de/node/37293
- **gesagt_am:** 25.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Bauarbeiten auf den Grundstücken Buddestraße 5 bis 7 dauern an, daher bleibt die Buddestraße in Höhe der Baumaßnahme noch bis voraussichtlich Anfang Dezember voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37293.html`, SHA-256 `48f5782daff5dc506d7ca07c82748aeeacfe08f447501f2757c6ba97fe8619f9`

### node 37265 — Kranarbeiten in der Kiskerstraße

- **URL:** https://www.bielefeld.de/node/37265
- **gesagt_am:** 30.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Kiskerstraße wird von Montag bis voraussichtlich Donnerstag, 5. bis 8. Oktober, in Höhe der Hausnummer 26 voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37265.html`, SHA-256 `0eac6270229e1c78eba67e5368b0fe03f729b67bc6522a5cc4a5afd29170db4a`

### node 37241 — Leitungsarbeiten: Halbseitige Sperrung und Einbahnstraßenregelung in der Leipziger Straße

- **URL:** https://www.bielefeld.de/node/37241
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Aufgrund von Leitungsarbeiten der Stadtwerke Bielefeld wird die Leipziger Straße in der Zeit von Mittwoch, 7. Oktober, bis voraussichtlich Ende des Jahres im Bereich zwischen der Jenaer Straße und der Dresdener Straße halbseitig gesperrt und in eine Einbahnstraße verwandelt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37241.html`, SHA-256 `b0f19b33b25b6934fe74a40b5c8696d4ebeb8c1a48e6f996522e1fdab198288c`

### node 37179 — Kanalarbeiten: Kölner Straße voll gesperrt

- **URL:** https://www.bielefeld.de/node/37179
- **gesagt_am:** 28.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Kölner Straße wird von Montag bis voraussichtlich Freitag, 5. bis 16. Oktober, in Höhe der Hausnummer 30 voll gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37179.html`, SHA-256 `ff2aee07355d9cdba833cb747a1c3a965118eb12dbefe565ae719b96437dfdf9`

### node 37177 — Leitungsarbeiten: Ampelregelung auf der Bodelschwinghstraße

- **URL:** https://www.bielefeld.de/node/37177
- **gesagt_am:** 24.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Die Regelung besteht bis voraussichtlich Ende Oktober.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37177.html`, SHA-256 `db16eb069bc2c5cd06f1267c5618301c7c134d0d1aa96ebc771c332940d9fc98`

### node 37137 — Kanalarbeiten: Huberstraße wird nachts zur Einbahnstraße

- **URL:** https://www.bielefeld.de/node/37137
- **gesagt_am:** 30.09.2026 · **Wer:** Stadt Bielefeld (Pressemeldung)
- **Zitat:** „Aufgrund von Kanalarbeiten des Umweltbetriebes wird die Huberstraße im Kreuzungsbereich Am Stadtholz, Bleichstraße, Huberstraße vom Donnerstag bis Samstag, 8. und 10. Oktober, nachts von 22 bis 6 Uhr halbseitig unter Einbahnstraßenregelung gesperrt.“
- **Kopie:** `recherche/belege/2026-10-04-bielefeld-node-37137.html`, SHA-256 `6e064ef44f16cce48fa4e7032e0afcf368019949130749eb4bd2e7da3db6639f`

## C. Größere Vorhaben aus der Liste, Volltext noch nicht abgerufen

Nur Titel und Anriss aus der Listenansicht. Ob ein Terminsatz drinsteht, ist ungeklärt. Diese zuerst abrufen,
sie tragen ein Buch eher als Baustellen.

- node 35886: Gymnasium am Seidensticker-Campus – Errichtung des Interimsgebäudes 01.06.2026 | Zum Schuljahr 2026/27 eröffnet das neue Gymnasium am Seidensticker-Campus (GSC). Seit Mai wird…
- node 35335: Das neue Gymnasium am Seidensticker-Campus kommt 14.04.2026 | Zum neuen Schuljahr im Sommer eröffnet das neue Gymnasium am Seidensticker-Campus. Diese Nachricht…
- node 36943: Ein besonderer erster Schultag: Das Gymnasium am Seidensticker-Campus startet gemeinsam mit seinen ersten Schülerinnen und Schülern 03.09.2026 | Es gibt Tage und Momente, die lange in Erinnerung bleiben: der erste Schultag mit Schultüte in der…
- node 34886: Richtfest für das neue Begegnungshaus 05.03.2026 | Am Dienstag, 3. März, konnte für das neue Begegnungshaus Olderdissen – Tier, Wald, Umwelt Richtfest…
- node 34847: Hochwasserschutz und naturnaher Ausbau der Weser-Lutter: Start der Baumaßnahmen 05.03.2026 | Die Baumaßnahmen zum hochwassersicheren Ausbau der Weser-Lutter zwischen der Straße am Venn und der…
- node 35531: Stadt Bielefeld, BBVG und Goldbeck legen Grundstein in Vilsendorf: Startschuss für 16 Erweiterungsbauten an Grundschulen 04.05.2026 | Mit der Grundsteinlegung an der Grundschule Vilsendorf startete am Donnerstag, 30. April, offiziell…
- node 34713: Erste Konzeptvergabe für das Wohnquartier Amerkamp startet 23.02.2026 | Die Stadt Bielefeld startet gemeinsam mit der städtischen Tochtergesellschaft BBVG die erste…
- node 34674: altstadt.raum: Kernteam empfiehlt Vorzugsvariante für Umgestaltung des Klosterplatzes 20.02.2026 | Der Klosterplatz soll im Zuge des Großprojekts altstadt.raum umgestaltet werden. Grundlage für die…
- node 34367: altstadt.raum: Klosterplatz-Umgestaltung startet 16.01.2026 | Der Klosterplatz soll im Zuge des Großprojekts altstadt.raum umgestaltet werden. Dafür starten die…
- node 36860: Online-Befragung zum Pilotprojekt am Jöllenbecker Marktplatz startet 31.08.2026 | Der Jöllenbecker Marktplatz und die Amtsstraße werden für einen Testzeitraum umgestaltet. Seit…
- node 37043: Neue Zweirad-Parkplätze für die Innenstadt geplant Fünf Standorte im Altstadtbereich sollen das Parken für Motorräder und Roller einfacher machen 03.09.2026 | Wer mit dem Motorrad, Roller oder Moped in die Bielefelder Innenstadt fährt, soll künftig wieder…
- node 35518: Am Mühlenberg bis Ende Oktober voll gesperrt 06.05.2026 | Die Straße Am Mühlenberg wird zwischen den Hausnummern 1 bis 42 ab Mittwoch, 27. Mai, voll gesperrt…
- node 35697: Freilufthalle Rußheide erweitert das Sportangebot der Stadt Bielefeld 15.05.2026 | Ein neues Sportangebot geht an den Start. Die Freilufthalle auf der Bezirkssportanlage Rußheide…
- node 36886: Baubeginn der Kanalarbeiten in der Senner Straße 01.09.2026 | In der Senner Straße wird der Umweltbetrieb der Stadt Bielefeld zwischen der Südstraße und der…
- node 36621: Kanalarbeiten am Ehlentruper Weg 04.08.2026 | Mit dem Start in den September beginnen auch die Kanal- und Straßenbauarbeiten am Ehlentruper Weg…
- node 37317: Am Pfarrholz/Tiesloh: Neue Befestigung und Beleuchtung für sicherere Geh- und Radwege Infostand für Anwohnende zur geplanten Umplanung 29.09.2026 | Die Straßen „Am Pfarrholz“ und „Tiesloh“ sollen umgestaltet werden. Die Untergrundqualität ist dort…
- node 37015: Detmolder Straße: Letzter Bauabschnitt wird am 4. September freigegeben Wetterbedingte Verzögerung bei Markierungsarbeiten 02.09.2026 | Die umfangreichen Arbeiten im letzten Bauabschnitt der Detmolder Straße befinden sich auf der…

## Nächste Schritte (ein Durchlauf, sobald die Sperre weg ist)

1. Die 17 Seiten aus C abrufen (langsam), Terminsätze schneiden.
2. Die neun Sätze aus A und die Treffer aus C ein zweites Mal abrufen und wörtlich prüfen.
3. Je Quelle einmal Save Page Now; trägt die Archivkopie nicht, bleibt die lokale Kopie mit Prüfsumme (wie Wuppertal).
4. Zusätzlich prüfen: Ratsinformationssystem Bielefeld (Vorlagen mit Zeitplan), moBiel/Stadtwerke-Presse,
   Haushalt 2027 (Einbringung, Beschluss). Heute nicht angesehen.
5. `buecher/bielefeld/BUCH.md` und Wetten `bielefeld-2026-001…` nach Vorlage Wuppertal, Prüfung und Tests,
   dann Frage an Felix (Merge und Push).

Ziel wie bei Bochum und Wuppertal: 10–15 Wetten, davon höchstens ein Drittel Baustellen.
