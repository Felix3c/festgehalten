# festgehalten — Nächste Schritte

**Stand:** 10.10.2026 21:50 (Kurzfassung). Diese Datei ist öffentlich und enthält seit 07.10. nur noch Stand,
nächste Prüftage und offene Punkte, ohne Namen Dritter und ohne Entwurfstexte (Beschluss 06.10., Frage 140 b).
Die ausführlichen Arbeitsnotizen liegen außerhalb des Repos: `~/wettbuch-notizen/NAECHSTE-SCHRITTE-lang.md`
(dort weiterschreiben; Stand bis 07.10. 10:05 ist byte-gleich mit dem bisherigen Inhalt dieser Datei).
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung)
**Phase:** v1 live, 24 Bücher / 418 Wetten öffentlich.

## Wo wir stehen

- 15.10. ~06:35: bonn-2026-035 (nächtliche Kanalreinigung bis 25.09. abgeschlossen?) erneut geprüft: bonn.de-Pressemitteilungen ohne Folgemeldung (Suche „Kanal“/„Kanalreinigung“ im Chrome-Werkzeug). Ausgang bleibt offen; Rückfrage an die Pressestelle der Stadt liegt als Entwurf, senden = Felix (Behörde).
- 15.10. ~06:10: duesseldorf-2026-034 („Die Brause“ bis 30.09. eröffnet?) erneut gesucht: Stadt und Verein ohne Eröffnungsmeldung, nur Vorberichte. Indiz Nein, kein Beleg, Ausgang bleibt offen; Vermerk + zwei Kopien mit SHA-256, master `6a6390b`, nicht gepusht. Nur eine Antwort der Stadt löst sie auf (offene Frage an den Halter).
- 15.10. ~05:55: **bonn-2026-036 (Hauptausschuss 17.09.) aufgelöst JA, master `771562e`, nicht gepusht.** Neuer Weg: Die
  OParl-Schnittstelle des Bonner Ratsinfo (`www.bonn.sitzung-online.de/oparl/`) ist offen (Open-Data-Lizenz), nur die
  Webseiten haben die Menschen-Prüfung. Sitzung 17.09. 18:00–18:48, TOP 6.1 Vorlage 261626-01 „ohne Votum“ (behandelt,
  keine Empfehlung an den Rat). Wayback-Kopien 20261015035212/035334, lokale JSON-Kopien mit SHA-256. Bonn-36 ohne Fehler,
  109 Tests. Hinweis: Über OParl lassen sich womöglich auch die Bonner Zitat-Warnungen schließen (nächster Guard-Lauf).
- 15.10. ~05:40: **dortmund-2026-020 (FATT 15.–21.09.) aufgelöst JA, master `1027b7c`, nicht gepusht.** Der fehlende Beleg
  für den Schlusstag ist da: Rückblick auf sport-tech-city.de „am 21. September 2026 über 100 Teilnehmende im Salzlager der
  Kokerei Hansa“ (Sport Tech Connect, laut FATT-Tagesprogramm Teil des Festivals). Wayback 20261015033452, lokale Kopie mit
  SHA-256. 109 Tests, 24 Bücher / 424 Wetten ohne Fehler. Push nach Freigabe.
- 15.10. ~04:55: **bonn-2025-025 (E-Busse SWB) 4. Suchlauf, master `ae46118`, nicht gepusht.** Weiter keine abgerechnete
  Summe; neu: Förderanteil Busse 1,76 Mio EUR, Akkus 490 statt 396 kWh geliefert. Nächster Blick Beteiligungsbericht
  Bonn / Jahresabschluss SWB Bus und Bahn 2025 (Bundesanzeiger), Verfall 01.07.2027. 24 Bücher / 424 Wetten ohne Fehler.
- 15.10. ~03:30: **Archivkopien nachgezogen, Zweig `sammel-1010` `d98e5ac`, nicht gepusht.** koeln-2025-032/048/050 und
  ki-2026-013 haben jetzt eine Wayback-Kopie, in der das Zitat wörtlich steht (Status ok). 149 Tests grün, 24 Bücher /
  441 Wetten ohne Fehler, Zitat-Warnungen weiter 21 (Bonn 9, Wuppertal 11, duesseldorf-2026-033).
- 14.10. ~09:32: **london-2026-001 Datumskonflikt** (Zweig `buch-london` `1cf5815`, nicht gepusht): Verordnung sagt weiter
  30.10., die TfL-Lizenzseite inzwischen 27.11.; Vermerk gesetzt, Prognosen unverändert. Push vor Fr 30.10. oder 001 verwerfen (Frage an Felix).
- 14.10. ~08:55: **Trefferquote je Stadt (KR3, Kachel 3.8 Vorstufe), Zweig `trefferquote-stadt` `fd2e0e9` (von
  `methode-nachrechnen`), nicht gepusht.** Neu `werkzeuge/trefferquote.py buecher` (liest nur, wertet mit `bewerten.py`):
  je Buch aufgelöst, eingetreten, Brier Institution/Computer, Rechenschaft, offen; „noch kein Rang“ unter 10. 6 neue
  Tests, 162 grün; METHODE §7 Absatz „Je Stadt“. Stand: 43 aufgelöste Ja/Nein, nur Köln mit Rang (21, davon 10
  eingetreten, Brier 0,495), Essen 6, Bonn/Dortmund/Düsseldorf je 5, Wuppertal 1. Zahlen nur aus diesem Zweig
  (münster-2026-001 JA liegt auf `buch-muenster`, noch nicht drin). Kurve erst, wenn mehrere Städte über 10 sind.
  Push zusammen mit `methode-nachrechnen` nach Felix' Antwort auf Frage 287.
- 14.10. ~08:30: **Methode nachrechenbar (KR2, Kachel 6.6), Zweig `methode-nachrechnen` `d8fe85f` (von `sammel-1010`),
  nicht gepusht.** Neu `werkzeuge/nachrechnen.py` (liest nur, wertet mit `bewerten.py`): Brier Computer/Institution/Münze,
  Kalibrierung in Bändern zu 0,20, Punkt-Bilanz, `--einzeln` mit Rechenweg je Wette; METHODE.md §7 erklärt Formel und
  Befehl, mit Zahlen Stand 14.10.: 13 gewertete Wetten, Computer 0,116, Institution 0,151, Münze 0,250 (30 aufgelöste
  Ja/Nein-Wetten ohne Computer-Zahl, weil vor dem Hinterlegen schon entschieden). 7 neue Tests, 156 grün, 24 Bücher /
  441 Wetten ohne Fehler. Tests im Worktree nur mit `PYTHONPATH=generator`, sonst greift das installierte master-Paket.
  Veröffentlichen = Frage an Felix.
- 14.10. ~08:00: **Wortlaut-Vermerke für die sinngemäßen Zitate gesetzt (KR1b), Zweig `sammel-1010` `819303f`, nicht
  gepusht.** 13 Vermerke (dortmund-2026-017/018, duesseldorf-2025-009, duisburg-2026-003, essen-2025-030/031,
  essen-2026-035–039, koeln-2025-047, koeln-2026-076), jeder Wortlaut vor dem Schreiben automatisch wörtlich gegen die
  Live-Quelle geprüft (Skript `~/allein/tmp/kr1b-skript/vermerke.py`, Gegenprobe mit falschem Satz schlägt an).
  duesseldorf-2026-033: Quelle 404, Wayback-Verzeichnis leer → Vermerk „Wortlaut nicht mehr prüfbar“, Warnung bleibt
  (ehrlich, Ausgang über beleg_ausgang belegt). **Rest 21 Warnungen:** Bonn 9 + Wuppertal 11 (Bot-Sperren, nur Felix im
  eigenen Browser) + duesseldorf-2026-033. 149 Tests grün, 24 Bücher / 441 Wetten ohne Fehler.
- 14.10. 07:30: **Zitat/Archiv-Lücken neu gezählt (KR1, Kachel 3.6), Zweig `sammel-1010`, nicht gepusht.**
  Die alte Zahl „12 offen“ war zu klein: `--zitate` warnte nur bei `zitat_fehlt`; Wetten ohne Archivkopie, deren
  Zitat live nicht bestätigt ist, blieben stumm. Neu `pruefen.wortlaut_offen_lesen` + Warnung „Wortlaut ungeprüft“
  (Test zuerst, `813e70b`, 113 + 36 Tests grün). Geschlossen: aachen-2026-002/-008 (ok), bund-2026-016 (pdf_ok,
  Kopie 01.09. trägt wieder) `f908ab2`; koeln-2025-032/-048/-050 live wörtlich (Fehlalarm) `4f29712`.
  **Rest 34 Warnungen:** Bonn 024/025/027/028/032–036 (302, Bot-Sperre, nur im eigenen Browser), Wuppertal 001–015
  (403, 11 Wetten), 14 sinngemäße Zitate ohne Vermerk (dortmund-2026-017/018, duesseldorf-2025-009, -2026-033 (404),
  duisburg-2026-003, essen-2025-030/031, essen-2026-035–039, koeln-2025-047, koeln-2026-076) → je Wortlaut-Vermerk
  wie am 09.10. (nächste Portion). ki-2026-013 Zitat live ja, Archiv offline (14.10. „Temporarily Offline“) →
  Tagesprüfung; Köln 032/048/050 ebenso Archiv nachziehen. 24 Bücher / 441 Wetten ohne Fehler, 0 Archivlücken.
- 12.10. 01:05: **bund-2026-016 Archivabgleich weiter offen.** Wayback sperrt den Inhaltsabruf (Bot-Sperre), neue Kopie
  anlegen gibt 520; die CDX-Schnittstelle nennt die Kopie vom 01.09. (304.184 Byte). Die Live-PDF ist inzwischen eine
  andere Fassung (286.575 Byte), das Zitat steht dort wörtlich. CSV bleibt `kein_archiv` (Prüfdatum 12.10.), Befund in
  `docs/2026-10-10-buch-bund-NACHTRAG.md` auf `buch-bund-2` (`331d930`). `buch-bund-2` und `buch-nrw-2` neu in
  `sammel-1010` gemergt (`bb9259a`): 109 Tests grün, 24 Bücher / 441 Wetten ohne Fehler mit Zitat-Abgleich, 0 Archivlücken,
  Merge auf master weiter konfliktfrei. Nächster Archivversuch nur in einer Tagesprüfung, kein eigener Lauf. **Nicht gepusht.**

- 10.10. 21:50: **essen-2026-036 vorbereitet:** Antrag 20.1 (1692/2026/CDU/SPD) ist ein Maßgaben-Antrag zur Umsetzung,
  keine Vertagung/Rückverweisung; 036 bleibt JA bei Kenntnisnahme am 14.10. Ratssitzung unverändert, TOPs stehen.
  Archivkopie scheiterte (Wayback 523/429), am Prüftag 15.10. erneut. Nachtrag in
  `docs/2026-10-04-aufloesung-0910-1510-VORBEREITET.md`. Alle acht Wetten mit Prüftag 11.–20.10. sind vorbereitet.

- 10.10. 20:54: **Merge-Probe `sammel-1010` auf heutiges master (`0932b19`)**, das seit dem Sammelzweig vier
  Doku-Commits weiter ist: konfliktfrei, 109 + 36 Tests grün, 24 Bücher / 441 Wetten ohne Fehler, Archivlücken 0.
  `git merge sammel-1010` auf master geht nach „steht“ weiterhin ohne Nacharbeit. Probe in Wegwerf-Arbeitsbaum, master unverändert.

- 10.10. 19:30: **Archivtabelle ohne Lücken.** Neues Werkzeug `python werkzeuge/archivsicherung.py buecher --luecken`
  (ohne Netz, Exit 1 bei Lücken) fand auf master **107 Wetten ohne Zeile** in `recherche/archiv-quellen.csv`
  (Gelsenkirchen, Hagen, Hamm, Krefeld, Mönchengladbach, Mülheim, Münster, Oberhausen, Wuppertal, Dortmund 3, Köln 2,
  Essen 1), dazu 13 auf den Zweigen (Bund 009–016, NRW 012–016). Nachgetragen per vorhandener Wayback-Kopie (nichts neu
  gespeichert): 101 + 12 mit Kopie, in der das Zitat wörtlich steht. Damit ist der Archivabgleich nrw-2026-012/015/016 und
  bund-2026-013 erledigt. Ohne Kopie: 11 Wuppertal-Wetten (wuppertal.de antwortet dem Werkzeug mit 403, auch Save Page Now
  scheitert) und bund-2026-016 (die Kopie vom 01.09. gibt beim Archiv 500; Zitat steht live wörtlich; 11.10. 00:34
  erneut: Archiv 429 Bot-Sperre, nächster Versuch frühestens Mo 12.10.). NACHTRAG-Dateien am 11.10. nachgezogen:
  `buch-nrw-2` `5662129`, `buch-bund-2` `199b119` (seit 12.10. in `sammel-1010`). Zweig `archiv-luecken` (`ab6d994`, von master), `buch-bund-2` `030cd40`, `buch-nrw-2`
  `8161d60`; alle drei in `sammel-1010` gemergt (`22ae09b`, CSV-Konflikt als Vereinigung nach id gelöst). Sammelzweig:
  0 Lücken, 145 Tests grün, 24 Bücher / 441 Wetten ohne Fehler. **Nicht gepusht.**

- 10.10. 18:46: **Sammelzweig `sammel-1010` (`1d18c4c`)** = master + `buch-wuppertal` + `buch-gatekeeper-2` + `buch-nrw-2` +
  `buch-ki-3` + `buch-bund-2`, lokal gemergt. Einziger Konflikt: angehängte Zeilen in `recherche/archiv-quellen.csv`
  (Gatekeeper 011–013 gegen KI 013), beide behalten. Ergebnis: 24 Bücher, 441 Wetten ohne Fehler (mit Zitat-Abgleich),
  109 Tests grün. Wenn alle Fragen zu diesen Zweigen „steht“ sind, reicht `git merge sammel-1010` auf master (ohne Konflikt geprüft),
  dann Push. Sagt eine Frage „nein“, den Sammelzweig verwerfen und einzeln mergen. Die Archivkopien von nrw-2026-012/015/016
  und bund-2026-013/016 kommen am 11.10. dazu (Tagesprüfung).
  Dazu: Für nrw-2026-012 bis -016 und bund-2026-009 bis -016 gibt es noch keine Zeile in `archiv-quellen.csv`. Die Archive
  stehen nur in den Vermerken. Die Formatprüfung meldet das nicht. Nachtragen am 11.10. zusammen mit dem Archivabgleich.

- 10.10. 18:05: Buch „Bund gegen Bund“ +4 Wetten, alle mit Prüftag 02.01.2027 (bisher hatten die Bücher Bund/NRW/KI/
  Gatekeeper fast nichts, das 2026 aufgelöst wird): bund-2026-013 Spritpreisdeckel gilt am 01.01.2027; -014 Bundestag
  beschließt bis 31.12. „kein Grundsicherungsbezug bei Haftbefehl“; -015 Kabinett beschließt bis 31.12. die
  Arbeitszeitgesetz-Reform; -016 neue UVgO bis 31.12. im Bundesanzeiger. Zitate live wörtlich, RegPK auch im Archiv;
  Archivabgleich Spritpreis/UVgO offen (Wayback sperrte) → Tagesprüfung 11.10.; 432 Wetten ohne Fehler, 109 Tests grün;
  Zweig `buch-bund-2` (`f13f564`), **nicht gepusht** (Frage 250).

- 10.10. 17:50: Buch „KI gegen KI“ +1 Wette (ki-2026-013 ServiceNow University 3 Mio. Lernende bis Ende 2027,
  Prüftag 30.06.2028). Zitat live wörtlich, Archivkopie scheiterte (Wayback 520) → Tagesprüfung; 425 Wetten ohne Fehler,
  109 Tests grün; Zweig `buch-ki-3` (`ceb4c7c`), **nicht gepusht** (Frage 249). Cohere, Mistral, Aleph Alpha, Black Forest
  Labs ohne neuen Fund. Prüfweg `docs/2026-10-10-buch-ki-anbieter-NACHTRAG.md` (auf dem Zweig).
- 10.10. 16:50: Buch „NRW gegen NRW“ +5 Wetten (nrw-2026-012 Verbundsatz 23,5 % im GFG 2027; -013 Zentrales Schülerfeedback
  2027/28 an allen Schulen verbindlich; -014 NRW.BANK.Energienetze offen bis 31.03.2027; -015 KI:Inferenzcluster.nrw Hardware
  an der RWTH bis Ende 2027; -016 Landtagswahl im April 2027 ab 16). Zitate live wörtlich, Archiv: 013/014 wörtlich, 012/015/016
  Kopie angelegt, Abgleich offen (Wayback sperrte); 429 Wetten ohne Fehler, 109 Tests grün; Zweig `buch-nrw-2` (`56be378`),
  **nicht gepusht** (Frage 247). Prüfweg `docs/2026-10-10-buch-nrw-NACHTRAG.md` (auf dem Zweig).
- 10.10. 16:35: Buch „Bund gegen Bund“ +4 Wetten (bund-2026-009 GKV-Zusatzbeitrag 2027 ≤ 2,9 %, Prüfung 02.11.2026;
  -010 Beitragsbemessungsgrenze KV 2027 76.500 €; -011 Autobahn GmbH erster eigener Kredit bis Ende 2027; -012 i-Kfz zentral
  beim KBA ab 01.07.2027). Zitate live und im Archiv wörtlich, 428 Wetten ohne Fehler, 109 Tests grün; Zweig `buch-bund-2`
  (`161e981`), **nicht gepusht** (Frage 246). Prüfweg `docs/2026-10-10-buch-bund-NACHTRAG.md` (auf dem Zweig).
- 10.10. 15:05: Buch „Gatekeeper gegen Gatekeeper“ +3 Wetten (gatekeeper-2026-011 Amazon, -012 Meta, -013 Alphabet),
  Zitate live und im Archiv wörtlich, 427 Wetten ohne Fehler, 109 Tests grün; Zweig `buch-gatekeeper-2` (`e6fb0f2`),
  **nicht gepusht** (Frage 238; 239 zu gatekeeper-2026-006). Prüfweg `docs/2026-10-10-buch-gatekeeper-NACHTRAG.md` (auf dem Zweig).
- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten
- 10.10. 11:50: Buch „KI gegen KI“ (Frage 229): ki-2026-010 und -011 stehen, -012 verworfen (gerechnetes Datum
  reicht nicht); `buch-ki-2` lokal nach master gemergt (`4c3df26`), 109 Tests grün, **nicht gepusht** (Push macht Felix).
- 10.10. 11:43: Ruhetage-Regel (Frage 184 a) lokal nach master gemergt (`76b765d`): angekündigte Schließtage gelten als
  Ruhetag und werden nicht gemittelt; 109 + 81 Tests grün, **nicht gepusht** (Push macht Felix).
- Prüfung 08.10. 20:40: 24 Bücher, 418 Wetten, keine Fehler; 99 Tests grün.
- 09.10. 14:45: **Gepusht** (`273dd60` auf master, Home-Tab): enthält bonn-2026-034 JA, Spalte „davon sonstige“,
  Wortlaut-Vermerke und Dortmund 015–017; die drei Rohkopien fremder Stadtseiten sind aus dem Index (nur Wayback-Link
  + SHA-256, Ordner in `.gitignore`). Aus demselben Beschluss seit 10.10. 14:20 lokal in master (`be7f4aa`, **nicht
  gepusht**): essen-2025-011 ersetzt durch essen-2025-035 (Stichtag 31.12.2027, Zitat jetzt wörtlich, Stadt „angekündigt“
  1,00, Computer 0,55), essen-2025-013 verworfen (Datei entfernt, Grund im Commit), dortmund-2025-013/-014 Vermerk
  „offen bis Verfall 01.01.2028“; 109 Tests grün, 24 Bücher / 424 Wetten ohne Fehler. `buch-ki-2` seit 10.10. in master.
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

- Fr 09.10.: bonn-2026-034 **aufgelöst JA** (09.10. 00:20, Beleg SWB-Meldung 28.09. „Nach erfolgreichen Sanierungsarbeiten an Gleis 1“, lokal committet, nicht gepusht); wuppertal-2026-001 **aufgelöst JA am 10.10. ~14:10** (Beleg WZ-Bericht vom 09.10. 12:05: Spielplatz „wurde gestern Nachmittag seiner Bestimmung übergeben“; nur auf dem lokalen Zweig `buch-wuppertal` `72ec5d1`, Arbeitsbaum `~/wettbuch-wuppertal`, nicht gemergt; Wayback-Save lief in eine Zeitüberschreitung, Kopie lokal außerhalb des Repos mit SHA-256; die Stadt hat bis 10.10. keine Nachmeldung). Alter Stand: bis 09.10. 00:20 nur Ankündigungen (Stadt, Rundschau, talzeit vom 07.10.), kein Bericht über die Eröffnung; weiter prüfen bis ~15.10., dann Frage an Felix (Vorschlag NEIN mangels Beleg); Nachprüfung 09.10. 11:55: weiter kein Bericht nach dem Termin (Stadt-Meldungsliste nur die Ankündigung vom 01.10., Rundschau nur Vorbericht 02.10., Talzeit-Artikel erschien 08.10. ~05:00, also vor 15:30, „Seit heute (8. Oktober)“ ist Vorbericht, kein Beleg)
- So 11.10.: wuppertal-2026-002 **am Prüftag ohne Beleg** (11.10. 00:25: Quelle unverändert, Stadt-Liste und Oktober-Archiv ohne „Brunnen“, Websuche nichts nach August; nicht aufgelöst, bis ~15.10. auf Nachbericht warten, dann Frage an Felix, Vorschlag NEIN; lokal `c2f9dac`) (Vorprüfung 10.10. 20:39 am Stichtag-Abend: Quelle unverändert, 19 Oktober-Meldungen ohne Brunnen, Presse nichts nach August → Richtung NEIN mangels Beleg, `8e49aad`; Nachprüfung 10.10. ~14:05: Stadt-Meldungsliste und Oktober-Archiv ohne „Brunnen“/„Alte Freiheit“, Websuche findet nichts nach August; Vorprüfung 09.10. 12:25: Quelle unverändert „Anfang Oktober geplant“, keine Meldung der Stadt, nichts in der Presse nach August, keine Verschiebung; ohne Beleg „fertig“ bis 10.10. gilt NEIN; Notiz in `docs/2026-10-04-aufloesung-wuppertal-0910-1110-VORBEREITET.md`, lokal `0360f4d`)
- Mo 12.10.: muenster-2026-001 **aufgelöst JA** (12.10. 00:40, Beleg Stadt-Mitteilung 11.10. 08:37 „Entwarnung: Kein Blindgänger an der Lambertikirche“: Verdachtspunkt freigelegt, nur Eisenrohre; Wayback 20261011223924 byte-gleich, lokal committet, nicht gepusht) (Vorprüfung 09.10. 12:40: Quelle byte-gleich, keine Absage/Verschiebung in den Mitteilungen bis 09.10. 10:03, lokal `5dcbf4a`); Köln-Messung 10:00 und 14:00 — Achtung: alle Kundenzentren an dem Tag geschlossen (Personalversammlung, Hinweis der Stadt, abgerufen 08.10.); Umgang mit Nullen entschieden 10.10. (Variante a): angekündigte Schließtage zählen als Ruhetag, nicht ins Mittel; lokal gemergt `76b765d`, nicht gepusht
- Mi 14.10.: bielefeld-2026-001, hamm-2026-001 **am Prüftag ohne Beleg** (14.10. ~09:35, Vermerke lokal `f7a481c`: Hamm Ratsinfo noch Status „Einladung“, kein Ergebnis für HPFA 12.10./Rat 13.10., aber 1. Ergänzung BV-183/26: HPFA empfahl einstimmig bei 1 Enthaltung, Punkt 6 Tiefgaragen-Studie dazu; Bielefeld Projektseite „Der Termin findet statt (Stand: 12. Oktober 2026, 15:25 Uhr)“, kein Bericht danach; beide bis ~20.10. auf Beschlussauszug/Bericht warten, dann Frage) (Hamm: Punkt steht als TOP 2.15 auf der Ratssitzung 13.10., geprüft 08.10.; Vorberatung 07.10. mehrheitlich empfohlen 34/3/2, geprüft 09.10.)
- Do 15.10.: essen-2026-035 bis -038 und essen-2025-001 (Rat 14.10., Feststellung Jahresabschluss 2025); alle vier Vorlagen 035–038 stehen auf der Tagesordnung (TOP 6, 19, 20, 25; zu 19/20 Änderungsanträge), geprüft 08.10.; TOP 7/8 Jahresabschluss erneut geprüft 09.10., unverändert; essen-2025-001 misst an 1,07 Mio (Ergebnisrechnung), Vermerk mit beiden Zahlen seit 10.10. lokal `0833691`, nicht gepusht
- Do 15.10.: **Kill-Check Köln BESTANDEN** (15.10. ~03:45 abgeschlossen, Lesart Felix 14.10.: eine inhaltliche Antwort aus der Presse zählt; Kölner Fraktionen und Lokalredaktionen haben bis 15.10. nicht geantwortet, Befund bleibt; Ergebnisblock in der Vorlage). Alter Text: **Kill-Check Köln** (Plan „Köln zuerst“), Vorlage `docs/2026-10-15-killcheck-koeln-VORBEREITET.md`. Neu 14.10. 10:09: erste menschliche Antwort (Winterhager/BauNetz, Bonn, kein Kölner Lokalmedium; weiß keinen Termin für die Schlussrechnung, Nachträge laufen). Ob das zählt, entscheidet Felix (ALLEIN Frage 305, Empfehlung NEIN mit Vermerk). Am 15.10. nur noch Gmail-Schritt 1 und Felix' Search Console.
- So 25.10.: essen-2026-040 (Zentralbibliothek, Eröffnung 24.10. am 15.10. weiter angekündigt); Mo 26.10.:
  muelheim-2026-001 (Brücke Saarner Straße, am 15.10. keine Fertig- oder Verlängerungsmeldung). Vorlage
  `docs/2026-10-08-aufloesung-2510-2610-VORBEREITET.md`, Nachtrag 15.10.
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
