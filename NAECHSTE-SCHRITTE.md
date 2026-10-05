# festgehalten — Nächste Schritte

**Stand:** 05.10.2026 15:10 (Dauerlauf: **acht freigegebene Zweige in master und gepusht** (Freigabe Felix 05.10. 14:55): Münster, Bielefeld, Gelsenkirchen, Mönchengladbach, Aachen, Krefeld, Mülheim und `koeln-anzeige-github`; Prüfung 24 Bücher/418 Wetten ohne Fehler, 99 + 78 Tests grün, origin/master = `dc5742a`, keine Konflikte, nichts verworfen; Fristen: `muenster-2026-001` Mo 12.10. auflösen, `bielefeld-2026-001` Mi 14.10.; Abschnitt „Acht Zweige gemergt“ unten) · 05.10.2026 14:05 (Dauerlauf: **Köln, erster gezählter Abruf an der Anzeige** Mo 05.10. 14:00, neun Zentren, Mittel 20,3, Maximum Innenstadt 68 Minuten, Rohkopie mit geprüfter Prüfsumme, keine Wayback-Kopie (HTTP 523); lokal `6165cae` + `6f215f1`, master 15 Commits vor origin, nicht gepusht; Abschnitt „Köln-Messung an der Anzeige“ unten) · 05.10.2026 12:35 (Dauerlauf: **Buch Mülheim an der Ruhr liegt lokal**, Zweig `buch-muelheim` `5561c28` in `~/wettbuch-muelheim`, 9 Wetten, Archiv 8 von 9, 18 Bücher/338 Wetten ohne Fehler, 99 Tests grün; nicht gemergt, nicht gepusht; wartet auf Felix' Antwort zu Frage 133, Abschnitt unten) · 05.10.2026 11:10 (Dauerlauf: Felix „Alles steht“ 10:53 zu 126 und 127 und Freigabe 124 → **`buch-hagen` (`8168c43`) und `buch-hamm` (`b821395`) lokal in master gemergt**; auf master 17 Bücher/329 Wetten ohne Fehler, 99 + 68 Tests grün, alle 14 Prüfsummen der neuen Belege nachgerechnet; master liegt 13 Commits vor origin. **Push macht Felix: `cd ~/wettbuch && git push origin master`, wegen hamm-2026-001 (Ratsbeschluss 13.10.) spätestens Mo 12.10.**; wird bis dahin nicht gepusht, muss 001 vor dem Push verworfen werden. 126 b: hamm-2026-008 (Wertstoffhof ASH) bleibt drin. 127 a: der Abruf vom 05.10. 08:12 ohne Rohkopie zählt nicht. **127 b vorbereitet, NICHT gemergt: Zweig `koeln-anzeige-github` (`9551b60`, `0943767`) in `~/wettbuch-koeln`** — der Workflow `koeln-wartezeit.yml` misst zusätzlich die Anzeige in eine eigene Datei `messwerte-anzeige-github.csv` (Rohkopie nach `belege-anzeige/`), `auswerten.py --quelle anzeige` liest beide Dateien, je Slot zählt der früheste Abruf mit Beleg, der Wächter prüft die neue Datei, `.gitattributes` schützt `belege-anzeige/` vor Zeilenenden-Umwandlung; 78 Tests im Ordner + 99 Projekt-Tests grün, unabhängige Durchsicht per Unteragent (ein Fehler bei `--alle` behoben). Wartet auf Felix' Antwort zu Frage 128 (Slot-Regel), dann Merge; ungeklärt bleibt bis zum ersten Lauf, ob stadt-koeln.de Abrufe von GitHub durchlässt) · 05.10.2026 11:00 (Dauerlauf: Felix „Alles steht“ 10:21 zu Frage 114 und 124 → **Köln wird ab 05.10. an der Anzeige gemessen: Vermerk in koeln-2026-077 bis -082, `auswerten.py --quelle anzeige`, `koeln-rueckfall` lokal in master gemergt (`a18020f`), drei Windows-Aufgaben eingeschaltet**; auf master 99 + 68 Tests grün, 15 Bücher/315 Wetten ohne Fehler; **Push macht Felix: `cd ~/wettbuch && git push origin master`**; Buch Hagen freigegeben, Merge steht noch aus; Fragen 126 Hamm und 127 Köln offen) · 05.10.2026 10:40 (Dauerlauf: neues Buch **„Hamm gegen Hamm“** auf lokalem Zweig `buch-hamm` (`658516c`), 10 Wetten, Archiv 10 von 10, Frage 126) · 05.10.2026 08:35 (Dauerlauf: Felix „Alles steht“ 08:23 zu Frage 112 → **`buch-oberhausen` lokal in master gemergt (`41315cb`)**, auf master 15 Bücher/315 Wetten ohne Fehler, 99 Tests grün; **Push vom Rechte-Filter des Dauerlaufs gesperrt → Felix pusht selbst: `cd ~/wettbuch && git push origin master`** (vor So 29.11., sonst wird oberhausen-2026-001 verworfen; ein `git merge` ist nicht mehr nötig)) · 05.10.2026 08:15 (Dauerlauf: `messen.py --quelle anzeige` gebaut, lokal auf `koeln-rueckfall` in `~/wettbuch-koeln`, erste Messung 08:12 ohne Beleg; Frage 114 weiter offen) · 05.10.2026 08:05 (Dauerlauf: **Köln-Feed am offenen Montag weiter eingefroren, aber die Stadt zeigt frische Wartezeiten über eine zweite Datei** `wartezeiten.json`; Messquelle der Wetten 077–082 = Frage 114) · 05.10.2026 07:35 (Dauerlauf: neues Buch **„Oberhausen gegen Oberhausen“** auf lokalem Zweig `buch-oberhausen` (`4657b15`), 12 Wetten, Archiv 12 von 12, Frage 112) · 05.10.2026 06:10 (Dauerlauf: neues Buch **„Krefeld gegen Krefeld“** auf lokalem Zweig `buch-krefeld` (`d4c97cc`), 15 Wetten, Archiv 12 von 13, Frage 110) · 05.10.2026 04:45 (Dauerlauf: neues Buch **„Aachen gegen Aachen“** auf lokalem Zweig `buch-aachen` (`f41d255`), 13 Wetten, Archiv 13 von 13, Frage 108; Einwohnerzahl Aachen berichtigt) · 05.10.2026 03:25 (Dauerlauf: neues Buch **„Mönchengladbach gegen Mönchengladbach“** auf lokalem Zweig `buch-moenchengladbach`, 11 Wetten, Archiv 11 von 11, Frage 105) · 05.10.2026 01:55 (Dauerlauf: Archiv nachgezogen, Münster 14 von 14 `0f15896`, Gelsenkirchen 13 von 13 `812b4ba`, beide lokal) · 05.10.2026 01:25 (Dauerlauf: neues Buch **„Gelsenkirchen gegen Gelsenkirchen“** auf lokalem Zweig `buch-gelsenkirchen` (`abcafa1`), 14 Wetten, Frage 102) · 05.10.2026 00:30 (Dauerlauf: Buch **„Bielefeld gegen Bielefeld“** fertig auf lokalem Zweig `buch-bielefeld` (`1f9d472`), 12 Wetten, Frage 99) · 05.10.2026 00:20 (Dauerlauf, Tagesprüfung: keine Wette neu fällig seit 04.10., nächste Fristen bonn-2026-034 und wuppertal-2026-001 am 09.10.; koeln-2026-073 und duesseldorf-2026-034 neu gesucht, keine neuen Belege (nur die bekannten Vorberichte), bonn-2026-035/036 weiter Nur Felix (Bot-Sperre); keine Antwort von Presseamt (Thread 1a1032ae28c82b4f), FDP/KSG, KStA; Münster-Archiv-Nachzug nicht möglich, archive.org antwortet auf alle sechs Abfragen mit 429; Feed-Abruf für das D1-Blatt folgt heute nach 8 Uhr; nichts committet) · 04.10.2026 19:20 (Dauerlauf: neues Buch **„Münster gegen Münster“** auf lokalem Zweig `buch-muenster` (`837e023`), 15 Wetten, Frage 98) · 04.10.2026 18:40 (Dauerlauf: Buch Bielefeld begonnen, Stufe 1: Kandidaten-Datei auf lokalem Zweig `buch-bielefeld` (`9bed44c`), keine Wetten, bielefeld.de und Wayback sperren) · 04.10.2026 11:20 (Dauerlauf: Auflösung wuppertal-2026-001 (09.10.) und -002 (11.10.) vorbereitet, `docs/2026-10-04-aufloesung-wuppertal-0910-1110-VORBEREITET.md`, unversioniert; Zeitfenster-Befund Frage 85) · 04.10.2026 07:50 (Dauerlauf: Köln-Belegkopie auf `wortlaut-vorschlag` byte-gleich neu eingecheckt, `.gitattributes` wie `buch-wuppertal`, SHA-256 `c8534af3…`, `930f0c6`) · 04.10.2026 07:35 (Dauerlauf: neues Buch **„Wuppertal gegen Wuppertal“** auf lokalem Zweig `buch-wuppertal` (`8250c39`, Fix Belegkopien), 15 Wetten, Frage 83) · 04.10.2026 06:50 (Dauerlauf: Bonn „kein Treffer“ 18/18 nachgeprüft, 12 gedeckt, 012/013 Stadtverwaltung statt Konzern, 018 300 zu prüfende statt geeignete Dächer, Kita-Frist aus Planlaufzeit, 023 Sprecher, `cc17694` auf `wortlaut-vorschlag`, Frage 80; alle fünf Städte durch) · 04.10.2026 06:30 (Dauerlauf: Essen „kein Treffer“ 13/13 nachgeprüft, 10 gedeckt, 013 Moltkestraße-Satz auf Projektseite + erste Ankündigung 2026/27 (gebrochen), 024 Grundsatz- statt Standortentscheidung, 023 bedingt, `7e444de` auf `wortlaut-vorschlag`, Frage 78) · 04.10.2026 06:06 (Dauerlauf: Dortmund „kein Treffer“ 6/6 nachgeprüft, Kita 005–007 Quelle eigentlich 07.07.2025, Dieselbus 013/014 keine Ankündigung, `4a1e621` auf `wortlaut-vorschlag`, Frage 76) · 04.10.2026 05:51 (Dauerlauf: Düsseldorf „kein Treffer“ 8/8 nachgeprüft, 022 Ausgang beim Sagen schon bekannt, Köln 070–072 Wayback trägt, `a58dcd2` auf `wortlaut-vorschlag`, Frage 75) · 04.10.2026 05:50 (Dauerlauf: Köln „kein Treffer“ 6/6 nachgeprüft, 070–072 Archiv trägt nicht, `fdf98cd` auf `wortlaut-vorschlag`, Frage 73) · 04.10.2026 05:40 (Dauerlauf: Auflösung bonn-2026-034 (09.10.) und essen-2026-035–038 (15.10.) vorbereitet, `docs/2026-10-04-aufloesung-0910-1510-VORBEREITET.md`, unversioniert) · 04.10.2026 04:50 (Dauerlauf: drei KW40-Wetten essen-2026-040, koeln-2026-084, duesseldorf-2026-036 auf lokalem Zweig `kw40-kandidaten` (`080ac84`), Frage 60) · 04.10.2026 04:32 (Dauerlauf: bochum-2026-010 Archivkopie 20261004021426 trägt wörtlich, Bochum jetzt 12 von 12, `607b923` auf `buch-bochum`) · 04.10.2026 04:30 (Dauerlauf: Inhaltsprüfung der vier verdächtigen Zitate, 3 gedeckt, Bonn-031 Frage 67, `fd403d2` auf `wortlaut-vorschlag`) · 04.10.2026 04:05 (Dauerlauf: Probe-Sammelmerge aller fünf wartenden Zweige konfliktfrei, Frage 66) · 04.10.2026 03:50 (Dauerlauf: neues Buch **„Bochum gegen Bochum“** auf lokalem Zweig `buch-bochum` (`29f2067`), Frage 64) · 04.10.2026 02:58 (Dauerlauf: Düsseldorf 004–008 nachgesichert, neue Wayback-Kopie trägt, `fe072ee` auf `wortlaut-vorschlag`) · 04.10.2026 03:20 (Dauerlauf: Wortlaut-Vorschläge für 164 nicht wörtliche Zitate, Zweig `wortlaut-vorschlag` `6379f45`) · 04.10.2026 02:25 (Dauerlauf: die 19 „live wörtlich“ archiviert, jetzt 80 von 273 tragend, Zweig `archiv-sicherung` bis `fda900e`) · 04.10.2026 01:55 (Dauerlauf: Archivsicherung, 156 von 273 Zitaten nicht wörtlich, Zweig `archiv-sicherung`, Frage 61) · 04.10.2026 00:35 (Dauerlauf, Tagesprüfung: keine Wette neu fällig seit 03.10.; die vier ungeklärten Ereignis-Wetten bonn-2026-036, bonn-2026-035, koeln-2026-073 (Indiz JA), duesseldorf-2026-034 (Indiz NEIN) neu recherchiert, keine neuen Belege, Bonn-Ratsinfo hinter Bot-Prüfung; nächste Frist bonn-2026-034 am 09.10.; keine Antworten von Köln/KStA/FDP/Presseamt/LDI; nichts committet) · 03.10.2026 22:45 (Dauerlauf: neues Buch **„Duisburg gegen Duisburg“** auf lokalem Zweig `buch-duisburg` (`ecfb90a`), Frage 54) · 03.10.2026 22:20 (Dauerlauf: Felix hat 22:01–22:03 die beiden 083-NEIN-Nachfass-Mails (FDP/KSG, KStA) und die Presseamt-Mail (49) gesendet; Push wettbuch steht weiter aus, master 10 Commits vor origin) · 03.10.2026 22:10 (Dauerlauf: Felix „Alles steht“ 21:58 zu 48–50 → **`koeln-rueckfall` (`dd9ddc5`) und `buch-ki` (`7aa4232`, Claude-Zahlen mit Offenlegung) lokal in master gemergt**, 99 + 43 Tests grün; **Push macht Felix: `cd ~/wettbuch && git push origin master`** (bringt 848e48b, NRW, Köln-Rückfall, KI live; ein `git merge` ist nicht mehr nötig). Presseamt-Entwurf (49) sendet Felix. Bund (44) und Gatekeeper (46) weiter offen) · 03.10.2026 21:55 (Dauerlauf: neues Buch **„KI gegen KI“** auf lokalem Zweig `buch-ki` (`7542338`), Frage 50) · 03.10.2026 21:15 (Dauerlauf: **Köln-Feed seit 16.09. 07:45 eingefroren**, http 403; Fix auf lokalem Zweig `koeln-rueckfall`, Frage 48/49, Entwurf ans Presseamt) · 03.10.2026 20:50 (Dauerlauf: neues Buch **„Gatekeeper gegen Gatekeeper“** auf lokalem Zweig `buch-gatekeeper` (`9db3728`): 10 Wetten zu Alphabet, Amazon, Apple, Booking, Meta, Microsoft aus eigenen Firmenquellen, Zitate wörtlich geprüft; Auswahl = DMA-Gatekeeper-Liste der Kommission; GPAI-Liste Art. 52 Abs. 6 AI Act nicht veröffentlicht (ungeklärt), ByteDance ohne Kandidaten; Kandidaten/Verworfene in `docs/2026-10-03-buch-gatekeeper-KANDIDATEN.md`; Prüfung 9 Bücher/245 Wetten OK, 99 Tests grün; Merge+Push erst nach „steht“ (Frage 46)) · 03.10.2026 18:55 (Dauerlauf: Felix „Alles steht“ 18:42 → Frage 27 Köln-Fix und 30 Buch NRW freigegeben; **buch-nrw lokal in master gemergt (`ec5dd7e`), 99 Tests grün; Push vom Rechte-Filter des Dauerlaufs gesperrt → Felix pusht selbst: `cd ~/wettbuch && git push origin master`** (bringt 848e48b + NRW live, eilig vor Mo 05.10.). Frage 32: für Wette 16 zählen nur Plan-Foren, Stand 0 von 3, Frist 08.10.) · 03.10.2026 15:25 (Dauerlauf: Datei auf git-Stand gebracht; **Befund Köln-Messung: seit 16.09. keine einzige Messung**, Fix `848e48b` lokal, Push wartet auf Felix) · 03.10.2026 15:00 (Dauerlauf: bonn-2026-032 JA, dortmund-2026-019 JA, duesseldorf-2026-033 JA, essen-2025-030 NEIN aufgelöst und gepusht, `7560373`; 99 Tests grün, alle Bücher OK) · 03.10.2026 14:50 (Entschieden Felix per Mail, Fragen 14/15 „steht“ = Empfehlung: bonn-2026-032 JA, dortmund-2026-019 JA, duesseldorf-2026-033 JA, essen-2025-030 NEIN übernehmen, committen, pushen; dortmund-2026-020 erst mit Bericht vom 21.09., koeln-2026-073 offen lassen. Umsetzung als Aufgabe in ~/allein/ALLEIN.md) · 03.10.2026 14:30 (Dauerlauf: 072/083 gepusht) · 03.10.2026 (Dauerlauf, Tagesprüfung Guard: zehn fällige Ereignis-Wetten recherchiert, zwei Auflösungs-Dateien vorbereitet, nichts committet) · 11.09.2026 nachts (Weitsicht-Buch mit allen sechzehn Zahlen committet, in master gemergt und öffentlich)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte, Beschluss 08.09. „Partei oder Siegel, nie beides") · ~/weitsicht/STAND.md (Herkunft des neuen Buches)
**Phase:** v1 live, 24 Bücher/418 Wetten öffentlich; origin/master = `dc5742a` (05.10. 15:10) plus der Doku-Commit zu diesem Stand, lokal nichts voraus.

## Neu 05.10.2026 15:10 (Dauerlauf): Acht Zweige gemergt und gepusht (Fragen 98, 99, 102, 105, 108, 110, 133, 128)

- **Vorbedingung Münster (6a):** Absatz „Warum Münster“ in `buecher/muenster/BUCH.md` berichtigt (Bielefeld ist seit
  05.10. fertig), `4c109cb` auf `buch-muenster`. Alle an ein Push-Datum geknüpften Wetten bleiben drin (Push am 05.10.,
  früheste Grenze war Sa 10.10.); nichts verworfen, nichts aufgelöst.
- **Merges** (je `merge --no-ff`, ohne Konflikt; nach jedem Prüfung aller Bücher und `python -m pytest`, dann Push):
  `095a404` buch-muenster (18 Bücher/344 Wetten) · `04448e7` buch-bielefeld (19/356) · `5515429` buch-gelsenkirchen
  (20/370) · `d00c121` buch-moenchengladbach (21/381) · `8465d65` buch-aachen (22/394) · `5ddacd0` buch-krefeld (23/409) ·
  `7903419` buch-muelheim (24/418) · `dc5742a` koeln-anzeige-github (24/418).
- **Prüfung nach dem letzten Merge:** „OK: 24 Bücher, 418 Wetten, keine Fehler“, 99 Tests im Wurzelordner und 78 in
  `recherche/koeln-wartezeit` grün.
- **Gepusht:** ja, nach jedem Merge `git push origin master`; nach `git fetch` ist `origin/master..master` = 0 (Stand
  `dc5742a`). Mit dem Köln-Zweig sind auch die geänderten Workflows `koeln-wartezeit.yml` und `koeln-waechter.yml` auf
  GitHub; ob dort ein Lauf durchgeht (lässt stadt-koeln.de Abrufe von GitHub zu?), ist nicht angesehen.
- **Fristen:** Mo 12.10.2026 `muenster-2026-001` auflösen · Mi 14.10.2026 `bielefeld-2026-001` auflösen (Infostand
  13.10.; der 14.10. ist ein Mittwoch, in ALLEIN.md steht „Di“) · Mo 26.10. `muelheim-2026-001` · So 01.11.
  `gelsenkirchen-2026-001`/`-002`, `aachen-2026-001`, `krefeld-2026-001`.
- **Nicht gemacht:** veröffentlichte Seite (GitHub Pages) nicht aufgerufen; Mülheim-Aufnahme `20261005102106` nicht
  erneut geprüft (7h (1), beiläufig); Worktrees und Zweige bleiben stehen. Die älteren Abschnitte unten nennen die Bücher
  noch als „lokal, nicht gemergt“; das gilt für die acht nicht mehr. Offen bleibt `buch-oberhausen` (Frage 112).

## Neu 05.10.2026 12:35 (Dauerlauf): Buch Mülheim an der Ruhr liegt lokal (9 Wetten, Frage 133)

- **Stand:** Zweig `buch-muelheim` `5561c28`, Arbeitsverzeichnis `~/wettbuch-muelheim`, von master `b821395`; nicht gemergt,
  nicht gepusht. Prüfung 18 Bücher/338 Wetten ohne Fehler, 99 Tests grün. Regel: Mülheim an der Ruhr 172 031 Einwohner
  (IT.NRW-PDF, drei Stellen gleich).
- **Quelle:** `https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen` listet 191 Meldungen auf einer Seite
  (06.01. bis 01.10.2026, mit Datum); `www.muelheim-ruhr.de` antwortet für Unterseiten mit 404. Alle 191 einzeln abgerufen,
  zwei Suchläufe über alle Sätze (36 + 40 Meldungen mit Treffer, alle Treffersätze gelesen). **Die Liste ist nicht
  vollständig:** zwei Meldungen der Startseite fehlen in ihr (Hauskampbrücke, ADFC-Umfrage), Ursache ungeklärt.
- **Wetten** (Stadt je 0,80, Heimatpreis 1,00; Prüfung, Computer): 001 Belag Brücke Saarner Straße, neun Wochen ab 24.08.
  (26.10.2026, 0,50) · 002 Heimatpreis im Dezember 2026 prämiert (01.01.2027, 0,85) · 003 Grundwasservorerkundung im
  Herbst/Winter 2026 (01.03.2027, 0,55) · 004 dauerhafte Messstellen im Frühjahr 2027 (01.06.2027, 0,35) · 005 Hallenbad
  Heißen im Frühjahr 2027 fertig (01.06.2027, 0,40) · 006 Erweiterungsbau Barbaraschule zum Schuljahr 2027/2028
  (01.10.2027, 0,50) · 007 Hauskampbrücke, rund 15 Monate ab 21.09.2026 (01.01.2028, 0,30) · 008 Baubeginn Sporthalle
  Luisenschule Anfang 2028 (01.04.2028, 0,45) · 009 Sporthalle zum Schuljahr 2029/2030 fertig (01.10.2029, 0,30).
- **Archiv 8 von 9:** fünf Aufnahmen vom 05.10.2026, die Sporthallen-Meldung (008, 009) aus einer Aufnahme vom 12.04.2026
  (Save Page Now heute HTTP 520); jede Kopie enthält das Zitat, byte-gleich ist keine. Für 001 antwortete Save Page Now mit
  HTTP 404 und nannte danach die Aufnahme `20261005102106`, die sich um 12:30 nicht abspielen ließ; dort trägt nur die
  lokale Kopie mit SHA-256 (`recherche/belege/2026-10-05-muelheim-*.html`, nach dem Commit nachgerechnet, 7 von 7 gleich).
- **Lesarten für Felix** (Kandidaten-Datei `docs/2026-10-05-buch-muelheim-KANDIDATEN.md` auf dem Zweig): 001 und 007 nennen
  eine Dauer statt eines Datums (gerechnet bis 25.10.2026 bzw. wegen „rund“ bis 31.12.2027); bei 007 nennt die Seite als
  Veröffentlichung den 15.09., der Text spricht schon vom Baubeginn am 21.09., `gesagt_am` ist der 21.09.2026; 005 zitiert
  eine Zeile der Eckdaten; 003/004 und 008/009 kommen je aus einer Meldung.
- **Vor dem Merge (erst nach „steht“ zu 133):** kommt der Push nach Sa 24.10.2026, `muelheim-2026-001` vorher verwerfen;
  nach Mi 30.12.2026 auch `-002`; Probe-Merge wie bei den anderen Zweigen. Mo 26.10.2026: 001 auflösen (nur wenn das Buch
  vorher öffentlich war). Vorher beiläufig prüfen, ob die Aufnahme `20261005102106` abspielbar geworden ist.
- **Nächstes Buch nach der Regel:** Leverkusen (168 262), danach Solingen (165 193); beide Zahlen in der PDF an drei
  Stellen gleich gelesen (`%TEMP%/bi/a123r.txt`). Skripte des Mülheim-Laufs in `%TEMP%/mh`. Nicht angesehen in Mülheim:
  Ratsinformationssystem, Haushaltsplan, Amtsblatt, Seiten der Beteiligungen (MST, medl, Ruhrbahn), Projektseiten zur IGA 2027.

## Neu 05.10.2026 10:40 (Dauerlauf): Buch Hamm liegt lokal (10 Wetten, Frage 126)

- **Stand:** Zweig `buch-hamm` `658516c`, Arbeitsverzeichnis `~/wettbuch-hamm`, von master `41315cb`; nicht gemergt, nicht
  gepusht. Prüfung 16 Bücher/325 Wetten ohne Fehler, 99 Tests grün. Regel: Hamm 179 272 Einwohner (IT.NRW-PDF, drei Stellen gleich).
- **Quelle:** `https://www.hamm.de/aktuelles` listet 231 Meldungen auf einer Seite (2017 bis 2026, davon 94 aus 2026), ohne
  Datum in der Liste; alle 231 einzeln abgerufen, eine Suche über alle Sätze, 64 Meldungen mit Treffer gelesen. Eine eigene
  Pressestellen-Seite mit Archiv habe ich nicht gefunden.
- **Wetten** (Stadt je 0,80; Prüfung, Computer): 001 Rat beschließt am 13.10.2026 das ISEK Innenstadt (14.10.2026, 0,90) ·
  002 Schneckenweg im Dezember fertig (01.01.2027, 0,50) · 003 Spielplatz Am Pelkumer Bach nach Jahresende wieder offen
  (01.02.2027, 0,35) · 004 Anliegerstraße Am Maximilianpark im ersten Quartal 2027 (01.04.2027, 0,60) · 005 Baubeginn zweiter
  Abschnitt Umweltachse Werries Anfang 2027 (01.04.2027, 0,45) · 006 Workshop-Gebäude Maxipark zur IGA-Eröffnung 23.04.2027
  (24.04.2027, 0,65) · 007 Mietspiegel 2027 spätestens Juli 2027 (01.08.2027, 0,80) · 008 Wertstoffhof spätestens Herbst 2027
  (01.12.2027, 0,55) · 009 Einzug Respekthaus Herbst 2027 (01.12.2027, 0,35) · 010 Hammer Straße zur Jahresmitte 2028
  (01.08.2028, 0,30).
- **Archiv 10 von 10:** Save Page Now hat alle Adressen angenommen, jede Kopie enthält das Zitat und ist byte-gleich mit der
  lokalen Kopie (`recherche/belege/2026-10-05-hamm-*.html`).
- **Lesarten für Felix** (Kandidaten-Datei `docs/2026-10-05-buch-hamm-KANDIDATEN.md` auf dem Zweig): 008 ist ein Vorhaben des
  Betriebs ASH (Rechtsform nicht nachgeschlagen), anders als in Hagen/Oberhausen aufgenommen, weil der Satz im Mitteilungstext
  auf hamm.de steht; 006 Bauherr ungeklärt, 010 drei Träger; 003 liest aus „bis zum Jahresende gesperrt“ die Wiederöffnung bis
  31.01.2027.
- **Vor dem Merge (erst nach „steht“ zu 126):** kommt der Push nach Mo 12.10.2026, `hamm-2026-001` vorher verwerfen; nach Mi
  30.12.2026 auch `-002`; Probe-Merge wie bei den anderen Zweigen. Mi 14.10.2026: 001 auflösen (nur wenn das Buch vorher
  öffentlich war; Beleg: Ratsinformationssystem Hamm, Sitzung vom 13.10.).
- **Nächstes Buch nach der Regel:** Mülheim an der Ruhr (172 031; Zahl vorher an einer zweiten Stelle der PDF gegenlesen,
  `%TEMP%/bi/a123r.txt`). Skripte des Hamm-Laufs in `%TEMP%/hm` (`hol.py`, `scan.py`, `wetten.py`, `abruf2.py`, `archiv.py`,
  `daten.py`, `bau.py`). Nicht angesehen in Hamm: Ratsinformationssystem, Haushaltsplan, Amtsblatt, Projektseiten außerhalb von
  `/aktuelles`; Kandidaten für später: Feuerwehrgerätehäuser (Baubeginn Heessen 2026), neue Hauptschule bis 2030.

## Neu 05.10.2026 09:30 (Dauerlauf): Buch Hagen liegt lokal, dünn (4 Wetten, Frage 124)

- **Stand:** Zweig `buch-hagen` `92c689d`, Arbeitsverzeichnis `~/wettbuch-hagen`, von master `41315cb`; nicht gemergt, nicht
  gepusht. Prüfung 16 Bücher/319 Wetten ohne Fehler, 99 Tests grün. Regel: Hagen 189 704 Einwohner (IT.NRW-PDF, drei Stellen gleich).
- **Quelle:** hagen.de baut die Meldungsliste aus einer JSON-Datei mit vollem Text
  (`/hagen-aktuell/aktuelle-meldungen/aktuelles-json.json`, 656 Meldungen, fast alle April bis 02.10.2026). Drei Suchläufe, 45
  Meldungen mit Treffer gelesen: nur vier Sätze verbinden ein Vorhaben der Stadt mit einem Datum.
- **Wetten:** 001 Klimaschutzkonzept im Herbst 2026 veröffentlicht (Prüfung 01.12.2026, Computer 0,35) · 002 gemeinsame
  IGA-Auftaktveranstaltung der fünf Ruhrtal-Städte im Frühjahr 2027 (01.06.2027, 0,75) · 003 Rundturnhalle Hohenlimburg nach Ende
  2027 wieder offen (01.02.2028, 0,25) · 004 neuer Kunstrasenplatz Hohenlimburg bis 2029/2030 (01.01.2031, 0,50). Stadt je 0,80.
- **Archiv 0 von 4:** Save Page Now antwortete viermal HTTP 523, ältere Kopien gibt es nicht (404); Ursache ungeklärt. Es tragen
  nur die lokalen Kopien mit SHA-256 (wie Wuppertal). **Neuversuch 05.10. 09:50: wieder 0 von 4** (HTTP 520/523/520/520, auch
  die Startseite 523; hagen.de selbst antwortet mit 200). Nichts am Buch geändert. Die Ursache bleibt ungeklärt; die Codes kommen
  vom Archiv, nicht von der Stadt. Vor dem Merge beiläufig noch einmal `python archiv.py` in `%TEMP%/ha` (nichts löschen), bei
  Erfolg `python bau.py`, Kandidaten-Datei anpassen, neuer Commit.
- **Draußen:** alles, wo der Wirtschaftsbetrieb Hagen (WBH) spricht (Brücke Rehbecke, Ruhrtalradweg, Bahnhofstraße), der
  Hagen-Pakt (Text des Ministeriums), Haushalt 2027 (gerundete Zahlen). Wem der WBH gehört, ist nicht nachgeschlagen.
- **Lesarten für Felix** (Kandidaten-Datei `docs/2026-10-05-buch-hagen-KANDIDATEN.md` auf dem Zweig): vor allem 003, der Satz
  nennt nur die Sperrung „bis Ende 2027“, die Wiederöffnung bis 31.01.2028 ist herausgelesen.
- **Vor dem Merge (erst nach „steht“ zu 124):** kommt der Push nach So 29.11.2026, `hagen-2026-001` vorher verwerfen; Probe-Merge
  wie bei den anderen Zweigen. Di 01.12.2026: 001 auflösen (nur wenn das Buch vorher öffentlich war).
- **Nächstes Buch nach der Regel:** Hamm (179 272; Zahl vorher an einer zweiten Stelle der PDF gegenlesen, `%TEMP%/bi/a123r.txt`).
  Nicht angesehen in Hagen: Ratsinformationssystem, Haushaltsplan, Amtsblatt, Meldungen vor April 2026.

## Neu 05.10.2026 11:00 (Dauerlauf): Köln-Messung an der Anzeige (Frage 114 entschieden)

- **Entschieden Felix 05.10. 10:21 („Alles steht“):** 114 a ab sofort an `wartezeiten.json` messen und das in jeder der sechs
  Wetten als datierten Vermerk festhalten, Frage und Kopf unverändert; 114 b Windows-Aufgaben wieder einschalten; 114 c zweite
  Mail ans Presseamt als Entwurf, erst ab Mi 07.10., wenn bis dahin keine Antwort da ist. 124 a Buch Hagen mit vier Wetten
  mergen und pushen, 124 b Lesart der Wette 003 bleibt.
- **Umgesetzt (lokal, master `a18020f`, nicht gepusht):** Vermerk vom 05.10.2026 in koeln-2026-077 bis -082 (`c8a048a`);
  `auswerten.py --quelle anzeige --monat JJJJ-MM` liest `messwerte-anzeige.csv` und zählt nur Zeilen im Messfenster, deren
  `beleg_sha256` zu einer Rohkopie in `belege-anzeige/` passt (Hash aus dem Dateiinhalt nachgerechnet; `d005281`, `af1d294`);
  `messen.cmd` ruft nach dem Feed auch `messen.py --quelle anzeige` auf; README angepasst. Acht neue Tests (68 im Ordner,
  99 im Projekt), Prüfung 15 Bücher/315 Wetten ohne Fehler. Unabhängige Durchsicht per Unteragent: nichts Ernstes, zwei
  Punkte übernommen (Rohkopie wirklich prüfen statt nur „Spalte gefüllt“; überholte Texte in `messen.py`).
- **Zeitplan:** Aufgaben `koeln-wartezeit-mo-1000`, `-mo-1400`, `-mi-1000` sind seit 05.10. eingeschaltet (Anmeldemodus „nur
  interaktiv“: laufen nur, wenn der Laptop an und Felix angemeldet ist). Sie schreiben direkt in das Arbeitsverzeichnis von
  master (`messwerte-anzeige.csv`, `belege-anzeige/`, Log `messen.log`); committet wird nach jedem Messtag von Hand (lokal).
  Nächste Läufe: Mo 05.10. 14:00, Mi 07.10. 10:00. Der Actions-Workflow misst weiter nur den Feed (Frage 127 b).
- **Stand der Messreihe (05.10. 14:05):** neun Zeilen vom Mo 05.10. 08:12 ohne Rohkopie; sie zählen nicht (Frage 127 a).
  **Erster gezählter Abruf: Mo 05.10. 14:00:09** über die Windows-Aufgabe `koeln-wartezeit-mo-1400` (`messen.log`:
  `exit-anzeige=0`; der Feed-Teil endete wie erwartet mit `exit=1`, Feed weiter auf 16.09. 07:45). Stand der Datei 14:00:03,
  alle neun Zentren Status 1: Kalk 0, Lindenthal 0, Chorweiler 3, Mülheim 3, Ehrenfeld 4, Nippes 33, Porz 35,
  Rodenkirchen 37, Innenstadt 68 Minuten. Rohkopie `belege-anzeige/wartezeiten-20261005-140009-43fc412b.json`, SHA-256
  `43fc412b…8bf891` aus der Datei und aus dem Commit nachgerechnet, beide gleich. **Keine Wayback-Kopie** (Save Page Now:
  HTTP 523), die Spalte `wayback_url` ist leer; der Beleg ist allein die lokale Rohkopie. `auswerten.py --quelle anzeige
  --monat 2026-10`: 1 Messtag, 9 Zeilen gezählt, 9 ohne Beleg nicht gezählt, Mittel über alle Zentren 20,3, Maximum 68
  (Innenstadt). Ein Abruf ist kein Monatsmittel. Lokal `6165cae` (Daten) und `6f215f1` (`.gitattributes`: `belege-anzeige/**
  -text`, dieselbe Zeile wie auf `koeln-anzeige-github`, damit die Rohkopie beim Auschecken byte-gleich bleibt; Probe-Merge
  des Zweigs weiter konfliktfrei). 99 + 68 Tests grün. Nicht gepusht. Nächster Lauf Mi 07.10. 10:00, danach wieder
  committen und auswerten.
- **Ungeklärt wie zuvor:** ob Feed und Anzeige dieselbe Messung zeigen; was gilt, wenn der Feed zurückkommt (dann neu
  entscheiden, die Dateien bleiben getrennt).

## Neu 05.10.2026 08:05 (Dauerlauf): Köln-Feed weiter eingefroren, zweite frische Quelle gefunden (Frage 114)

- **Feed:** `waiting-od.php` am Mo 05.10. um 07:49, 08:03 und 08:03:59 abgerufen, alle byte-gleich (SHA-256 `7a84410a…`): neun
  Kundenzentren weiter `timestamp 2026-09-16 07:45:03`, Status 1, dieselben Minuten. Die Kundenzentren haben montags 7:30–15 Uhr
  ohne Termin offen (Seiten Innenstadt und Chorweiler, Abruf 07:49). Wayback-Kopie byte-gleich:
  https://web.archive.org/web/20261005060400/https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php
- **Zweite Quelle (neu):** Die Seite „Wartezeiten in unseren Kundenzentren“
  (https://www.stadt-koeln.de/service/alle-adressen/kundenzentren/wartezeiten-unseren-kundenzentren, auch `/artikel/72776/index.html`)
  lädt ihre Werte aus `https://www.stadt-koeln.de/interne-dienste/wartezeiten/wartezeiten.json`. Die Datei ist frisch: `stand_iso`
  `2026-10-05T07:50:02+02:00` und `2026-10-05T08:00:04+02:00`, je neun Kundenzentren (Bereich `meldeangelegenheiten`, Felder `name`,
  `wartezeit`, gruppiert nach unter 30 / unter 60 / über 60 Minuten) und acht Führerscheinstellen. Werte 08:00: Ehrenfeld 19,
  Chorweiler 22, Kalk 28, Mülheim 34, Porz 53, Innenstadt 54, Nippes 68, Lindenthal 70, Rodenkirchen 94 (Mittel 49,1; ein
  Augenblick, kein Monatswert).
- **Einordnung:** Im Quelltext steht der Baustein „wartezeiten 2026“ und der Kommentar „In der PHP-Variante …“; die Wayback-Kopie
  der Seite vom 14.05.2026 hat die Zeiten noch im Seitentext. Umbau also zwischen 14.05. und 05.10.2026. **Ungeklärt:** ob am
  16.09. und ob er den Feed abgehängt hat; ob beide Stellen dieselbe Messung zeigen; wie oft die Datei neu geschrieben wird (zwei
  Stände im Abstand von zehn Minuten gesehen).
- **Belege:** `recherche/koeln-wartezeit/belege-2026-10-05/` (fünf Dateien, unversioniert): Feed 07:49 und 08:03, Datei 07:50 und
  08:05, Seite 07:50. Wayback der Seite `20261005055321` geprüft (enthält den Verweis auf die Datei); Wayback der Datei
  `20261005055233` angestoßen, um 08:05 beim Abspielen 404, **nicht geprüft**.
- **Presseamt:** Thread `1a1032ae28c82b4f` bis 05.10. 08:05 ohne Antwort.
- **Folge für koeln-2026-077–082:** Der Wortlaut der Wetten nennt den Open-Data-Feed. An der neuen Datei könnte ab sofort gemessen
  werden; das ändert die Messquelle veröffentlichter Wetten und ist Felix' Entscheidung (**Frage 114**). Bis dahin: 0 gültige
  Oktober-Messungen, und jeder Montag/Mittwoch ohne Messung fehlt im Monatsmittel (nächste: Mi 07.10., Mo 12.10.).
- **Vorbereitung ohne Entscheidung: ERLEDIGT 05.10. 08:15 (Dauerlauf, ALLEIN Jetzt 0d).** Lokaler Zweig `koeln-rueckfall`
  im eigenen Arbeitsverzeichnis `~/wettbuch-koeln` (master nicht umgeschaltet, nichts gemergt, nichts gepusht), drei Commits auf
  `0d22085`: `36e7914` (Code + Tests), `8497b2e` (erste Messung, eigener Commit zum Verwerfen), `8f25018` (README).
  `python recherche/koeln-wartezeit/messen.py --quelle anzeige` misst `wartezeiten.json` mit demselben Messfenster und schreibt nach
  `messwerte-anzeige.csv` (Spalten `abgerufen_am, kundenzentrum, wartezeit_minuten, stand_iso, status, quelle, wayback_url,
  beleg_sha256`), Rohkopie je Abruf in `belege-anzeige/`. Sperre in beide Richtungen: Die Anzeige schreibt nie in eine Feed-Datei,
  der Feed nie in eine Anzeige-Datei. Standardweg ohne `--quelle` unverändert. 60 Tests im Ordner (17 neu), 99 im Projekt grün;
  unabhängige Durchsicht per Unteragent: nichts Ernstes, vier Punkte übernommen.
- **Erste Messung an der Anzeige:** Mo 05.10. 08:12, Stand der Datei 08:10:03: Ehrenfeld 13, Chorweiler 23, Kalk 30, Mülheim 45,
  Innenstadt 48, Lindenthal 58, Nippes 62, Porz 68, Rodenkirchen 94 Minuten (Mittel 49,0; ein Augenblick, kein Monatswert).
  **Ohne Beleg:** Der Abruf lief vor dem Einbau der Rohkopie, und Wayback gab 404. Zählt für keine Wette (Frage 114).
- **Wayback bei dieser Datei:** Save Page Now lehnt nicht ab, sondern leitete um 08:12 auf die Aufnahme von 07:52
  (`20261005055233`) um; deren Abspielen gab 404, der Index von archive.org meldete „Temporarily Offline“. Weil die Stadt die
  Datei alle zehn Minuten neu schreibt (07:50, 08:00, 08:10 gesehen, `Last-Modified` passt), zeigt eine umgeleitete Aufnahme
  nicht den gemessenen Stand. Deshalb die Rohkopie mit SHA-256. **Nicht geprüft:** ob die Aufnahme `20261005055233` später
  abspielbar wird.
- **Offen ohne Entscheidung:** heute nach 12 Uhr ein zweiter Abruf (Nachmittags-Slot, dann mit Rohkopie); Mi 07.10. 7:30–12 Uhr
  der nächste. Kein Zeitplan, keine Windows-Aufgabe, `auswerten.py` liest die Datei nicht.
- D1-Blatt `~/kybernokratie/mails/2026-10-04-d1-cologne-stichworte.md` hat den Befund oben; Stichworte 1, 3, 4 angepasst
  („geht gerade nicht“ stimmt nicht mehr).

## Neu 05.10.2026 07:35 (Dauerlauf): Buch „Oberhausen gegen Oberhausen“, lokal (Frage 112)

- Lokaler Zweig `buch-oberhausen`, Commit `4657b15` (Arbeitsverzeichnis `~/wettbuch-oberhausen`, von master `f641a19`,
  nicht gemergt, nicht gepusht): `buecher/oberhausen/` mit BUCH.md und 12 Wetten `oberhausen-2026-001` bis `-012`.
- Auswahlregel: IT.NRW A123 2025 21, nach Krefeld (231 116) folgt Oberhausen (213 349, in der PDF an drei Stellen
  gleich); danach Hagen (189 704), Hamm (179 272), Mülheim an der Ruhr (172 031).
- Quelle: blätterbare Presseliste `oberhausen.de/de/index/rathaus/aktuelle-pressemeldungen.php?pagePresse=N&aktYear=`:
  385 Meldungen 2026, 383 im Volltext (zwei Friedhofs-Bekanntmachungen nicht abrufbar), 61 mit Terminsatz gelesen,
  dazu eine zweite Suche nach Terminen ohne Jahreszahl. Oberhausen nennt deutlich weniger Termine als die bisherigen Städte.
- Wetten: Steganlage Hans-Sachs-Berufskolleg (Herbst 2026), Vollsperrung Kewerstraße/Bebelstraße (Ende Dezember 2026),
  Jahrbuch 2027 (Ende 2026, Eichwette 0,85), Hessenstraße (Ende März 2027; im März hieß es noch 31.07.2026),
  Ruhrpark fertig zur IGA 2027 (Computer 0,15: Gesamtbaustart laut Stadt erst zum Jahresende), Vorentwürfe Pocket-Park
  Marktstraße (Frühjahr 2027), Containerkonzept (Sommerpause 2027), rund 130 Nachwuchskräfte 2027, neue Gesamtschule
  Eschenstraße (Schuljahr 2027/28), Ebertbad-Gastronomie (Dezember 2027), NEWAG-Beteiligung (Anfang 2028),
  Erweiterungsneubau Sophie-Scholl-Gymnasium (Frühjahr 2029).
- Belege: jedes Zitat in zwei Abrufen wörtlich (12 von 12); 12 von 12 Quellen mit Wayback-Kopie vom 05.10.2026, Zitat
  darin geprüft (keine byte-gleich, die Seiten werden je Abruf neu erzeugt); 12 lokale Kopien mit SHA-256 (rund 3,4 MB).
- Prüfung 12 Wetten bzw. 15 Bücher/315 Wetten ohne Fehler, 99 Tests grün. Kandidaten, Verworfene, Lesarten und Grenzen
  in `docs/2026-10-05-buch-oberhausen-KANDIDATEN.md` (auf dem Zweig).
- **Halter-Lesarten (vor dem Livegang ansehen):** 002/004 Straßenausbau ohne genannten Bauherrn als Vorhaben der Stadt;
  010 Ebertbad (für den Bau spricht die GVO); 005 Stichtag 23.04.2027; 007 Sommerpause = 31.07.2027; 008 „rund 130“ =
  mindestens 120; 009 Start zählt, nicht die vier Klassen; 011 „Anfang 2028“ = erstes Quartal. Wem WBO und GVO gehören: ungeklärt.
- **Zeitfenster:** 001 nur ehrlich bei Push vor dem 30.11.2026, 002/003 vor dem 31.12.2026; sonst vor dem Merge verwerfen.
- Nächste Stadt nach der Regel: Hagen (189 704; vor dem Buch an einer zweiten Stelle der PDF gegenlesen). Skripte des Laufs
  in `%TEMP%/ob` (`liste.py`, `hol.py`, `scan.py`, `wetten.py`, `abruf2.py`, `archiv.py`, `daten.py`, `bau.py`).
- **Wartet auf Felix:** Frage 112 (mergen und pushen), gemailt 05.10. 07:40.

## Neu 05.10.2026 06:10 (Dauerlauf): Buch „Krefeld gegen Krefeld“, lokal (Frage 110)

- Lokaler Zweig `buch-krefeld`, Commit `d4c97cc` (Arbeitsverzeichnis `~/wettbuch-krefeld`, nicht in master, nicht gepusht):
  `buecher/krefeld/` mit BUCH.md und 15 Wetten `krefeld-2026-001` bis `-015`. Auswahl nach der Einwohner-Regel
  (IT.NRW 30.06.2025: Krefeld 231 116). Alle 718 Pressemeldungen 2026 der Stadt (blätterbare Liste
  `krefeld.de/press-releases?page=N`) im Volltext, 58 mit Terminsatz gelesen.
- Wetten: Vereinstreffpunkt am Elfrather See Ende Oktober 2026, Schinkenplatz und Umbaubeginn Notschlafstelle
  Feldstraße bis Jahresende, Inklusionsplan erste Jahreshälfte 2027, Rheinlandhallen Sommer 2027, Sanierungsbeginn
  Glockenspitzhalle Mitte 2027, Feuerwache Gellep-Stratum Oktober 2027, Stadtbad Neusser Straße Ende 2027,
  Promenade Trift/Weiden Baubeginn 2027, Bettensteuer ab 2027, Offener Ganztag 68 Prozent bis 2027, Stadtwaldhaus
  geschlossen ab 01.01.2028 (Eichwette, 0,80) und Grundsanierung April 2028, Fabrik Heeder Studiobühne I März 2028,
  Badesee-Areal Winter 2028/2029 (Computer 0,25).
- Jedes Zitat in zwei Abrufen wörtlich (15 von 15); 12 von 13 Quellen mit Wayback-Kopie, Zitat darin geprüft
  (zehn vom 05.10.2026, 006 vom 04.10.2026, 007 vom 06.05.2026); **011 (OGS-Bericht) ohne Archivkopie**, die
  Sicherung antwortet HTTP 404, nachziehen. 13 lokale Kopien mit SHA-256 (rund 2,0 MB).
  **Nachtrag 05.10. 06:25:** Die Aufnahme gibt es (Save Page Now meldet „success“, HTTP 200, Zeitstempel
  20261005040152), sie war aber bis 06:25 nicht abspielbar (404, Index leer); am Buch nichts geändert,
  nächster Versuch ab 08:30 (Schritte in `~/allein/ALLEIN.md`, Jetzt 7d).
  **Erledigt 05.10. 11:15: jetzt 13 von 13.** Die Aufnahme 20261005040152 war auch um 11:13 nicht abspielbar und
  steht nicht im Index (der Index antwortet wieder und kennt die Nachbar-Aufnahmen von 03:59), also neu gesichert:
  `https://web.archive.org/web/20261005091417/https://www.krefeld.de/ogs-bericht`, Zitat wörtlich darin, gleich
  lang wie die lokale Kopie, zwei Zeilen anders (zufällige Seiten-Kennung), deshalb nicht byte-gleich. Wette 011
  und Kandidaten-Datei angepasst, Commit `99ed4b4` auf `buch-krefeld` (Zweigspitze, lokal); Prüfung 15 Bücher/318
  Wetten ohne Fehler, 99 Tests grün.
- Prüfung 15 Bücher/318 Wetten ohne Fehler, 99 Tests grün. Kandidaten, Verworfene, Lesarten und Grenzen der Suche
  in `docs/2026-10-05-buch-krefeld-KANDIDATEN.md` (auf dem Zweig).
- **Zeitfenster:** 001 nur ehrlich bei Push vor dem 31.10.2026, 002/003 vor dem 31.12.2026; sonst vor dem Merge verwerfen.
- Nächste Stadt nach der Regel: am 05.10. nicht nachgeschlagen (in der IT.NRW-PDF nachlesen).
- **Wartet auf Felix:** Frage 110 (mergen und pushen), gemailt 05.10. 06:15.

## Neu 05.10.2026 04:45 (Dauerlauf): Buch „Aachen gegen Aachen“, lokal (Frage 108)

- Lokaler Zweig `buch-aachen`, Commit `f41d255`, Arbeitsverzeichnis `~/wettbuch-aachen` (von master `f641a19`, nicht gemergt, nicht gepusht):
  `buecher/aachen/` mit BUCH.md und 13 Wetten `aachen-2026-001` bis `-013`.
- Auswahlregel: IT.NRW A123 2025 21, nach Mönchengladbach (266 840) folgt Aachen (262 211); danach Krefeld (231 116).
  **Berichtigt:** In BUCH.md und Kandidaten-Dokument von Gelsenkirchen und Mönchengladbach stand für Aachen 263 948 (Kreis Heinsberg);
  lokal berichtigt auf `buch-gelsenkirchen` `bc037b0` und `buch-moenchengladbach` `7cadf14`. Reihenfolge unverändert, nie veröffentlicht.
- Quelle: Pressemitteilungen der Stadt, aufgezählt über die Sitemap der Stadt (die Presseliste wird per Skript nachgeladen): 664 Meldungen
  2026 im Volltext, 72 mit Terminsatz gelesen. Vollständigkeit der Sitemap nicht geprüft; steht so im Kandidaten-Dokument.
- Zugriff: aachen.de hat keine robots.txt; der Vermerk „noai, noindex, noarchive“ steht nur auf der Fehlerseite, nicht auf den Presseseiten.
- Wetten: Skateanlage Schagenstraße (Ende Oktober 2026), Info-Tafeln Premiumfußwege (Herbst 2026), Brücke Münsterstraße (Dezember 2026),
  Ulla-Klinger-Halle (Ende Februar 2027), Freibad Hangeweiher (01.05.2027, Eichwette), AR-Führung Krönungssaal (Mitte 2027), Rückbau altes
  Polizeipräsidium und Bismarckstraße (Sommer 2027), Baubeginn Klappergasse/Rennbahn (Herbst 2027), Theaterstraße und Indestützmauer
  Hahner Straße (Ende 2027), Theaterplatz (Ende 2028), Haus der Neugier (bis 2029).
- Belege: jedes Zitat in zwei Abrufen wörtlich; 13 von 13 Quellen mit Wayback-Kopie vom 05.10.2026, Zitat darin geprüft; 13 lokale Kopien mit
  SHA-256 in `recherche/belege/` (zusammen rund 2,3 MB).
- Prüfung 15 Bücher/316 Wetten OK (Zweig gegen master), 99 Tests grün. Verworfene mit Gründen: `docs/2026-10-05-buch-aachen-KANDIDATEN.md`.
- Zeitfenster: 001 (Stichtag 31.10.2026) vor dem Merge verwerfen, wenn der Push nach dem 30.10. kommt; 002 nach dem 29.11., 003 nach dem 30.12.
- **Wartet auf Felix:** Frage 108 (mergen + pushen).

## Neu 05.10.2026 03:25 (Dauerlauf): Buch „Mönchengladbach gegen Mönchengladbach“, lokal (Frage 105)

- Lokaler Zweig `buch-moenchengladbach`, Commit `02755d8` (+ ein Doku-Commit), Arbeitsverzeichnis `~/wettbuch-moenchengladbach` (nicht in master, nicht gepusht):
  `buecher/moenchengladbach/` mit BUCH.md und 11 Wetten `moenchengladbach-2026-001` bis `-011`.
- Auswahlregel: IT.NRW A123 2025 21, nach Gelsenkirchen (267 733) folgt Mönchengladbach (266 840); danach Aachen (262 211; hier stand bis 05.10. 04:10 irrtümlich 263 948, die Zahl des Kreises Heinsberg, auf dem Zweig berichtigt mit `7cadf14`).
- Quelle: Newsroom der Stadt, aufgezählt über die Suche der Stadt (keine blätterbare Liste; 17 Suchwörter, 553 Meldungen 2026 im Volltext,
  129 mit Terminsatz gelesen). Die Liste ist nicht nachweislich vollständig; steht so im Kandidaten-Dokument.
- Wetten: Viersener Straße Großheide (Ende November 2026), Turmstraße, Stadtplatz Durchstich Museum Abteiberg, Spielplatz Bunter Garten
  (alle Jahresende), Rathaus-Neubau Rheydt Rückbau (1. Quartal 2027) und Übergabe (März 2030), Heinz Sielmann Biotop (02.06.2027, Eichwette),
  Bettrather Brücke (2. Quartal 2027), Nahverkehrsplan (Sommer 2027), Hockey-Trainingszentrum (Ende 2027), siebte Gesamtschule (2029).
- Belege: jedes Zitat in zwei Abrufen wörtlich; 11 von 11 Quellen mit Wayback-Kopie vom 05.10.2026, Zitat darin geprüft; 11 lokale Kopien mit
  SHA-256 in `recherche/belege/` (zusammen rund 9,6 MB).
- Prüfung 15 Bücher/314 Wetten OK (Zweig gegen master), 99 Tests grün. Verworfene mit Gründen: `docs/2026-10-05-buch-moenchengladbach-KANDIDATEN.md`.
- Zeitfenster: 001 (Stichtag 30.11.2026) vor dem Merge verwerfen, wenn der Push nach dem 29.11. kommt; 002–004 entsprechend nach dem 30.12.
- **Wartet auf Felix:** Frage 105 (mergen + pushen).

## Neu 05.10.2026 01:25 (Dauerlauf): Buch „Gelsenkirchen gegen Gelsenkirchen“, lokal (Frage 102)

- Zweig `buch-gelsenkirchen` (Arbeitsverzeichnis `~/wettbuch-gelsenkirchen`, von master `f641a19`, `abcafa1`), nicht gemergt, nicht gepusht:
  `buecher/gelsenkirchen/` mit BUCH.md und 14 Wetten `gelsenkirchen-2026-001` bis `-014`; Kandidaten und Verworfene in
  `docs/2026-10-05-buch-gelsenkirchen-KANDIDATEN.md`.
- Auswahlregel: IT.NRW A123 2025 21, nach Münster (307 979) folgt Gelsenkirchen (267 733); danach Mönchengladbach (266 840).
- Quelle: Listenansicht `https://www.gelsenkirchen.de/de/_meta/aktuelles/artikel/seite/N` (67 Seiten), 655 Meldungen 2026,
  536 der Stadt/Gelsendienste im Volltext (2 s Abstand, keine Sperre), 65 mit Terminsatz gelesen. Nur Meldungen mit Quellenangabe
  „Stadt Gelsenkirchen“ im Buch.
- Zitate 14/14 wörtlich im ersten und zweiten Abruf. **Archiv (Nachzug 05.10. 01:55):** 13 von 13 Quellen mit Wayback-Kopie,
  Zitat in jeder wörtlich (12 Kopien vom 04.10. UTC, IGA 2027 ältere Kopie vom 20.05.2026); dazu 13 lokale Kopien
  `recherche/belege/2026-10-05-gelsenkirchen-artikel-*.html`, SHA-256 im Vermerk. Auf `buch-gelsenkirchen` committet.
- Früheste Prüfungen: 001 Liboriusstraße und 002 Gasleitung Kurt-Schumacher-Straße am 01.11.2026 (Stichtag 31.10.), 003 metropolradruhr
  01.12.2026, 004–006 am 01.01.2027.
- **Zeitfenster:** 001/002 sind nur ehrlich, wenn das Buch vor dem 31.10. öffentlich ist; sonst vor dem Merge verwerfen.
- `--pruefen` 15 Bücher / 317 Wetten ohne Fehler, 99 Tests grün. Nur neue Dateien.
- Nicht angesehen: Ratsinformationssystem, Haushaltsplan-Entwurf 2027.
- **Wartet auf Felix:** Frage 102 (mergen und pushen; der Archiv-Nachzug ist seit 05.10. 01:55 erledigt: `cd ~/wettbuch && git merge buch-gelsenkirchen && git push origin master`).

## Neu 05.10.2026 00:30 (Dauerlauf): Buch „Bielefeld gegen Bielefeld“ fertig, lokal (Frage 99)

- Zweig `buch-bielefeld` (Arbeitsverzeichnis `~/wettbuch-bielefeld`, `1f9d472`), nicht gemergt, nicht gepusht:
  `buecher/bielefeld/` mit BUCH.md und 12 Wetten `bielefeld-2026-001` bis `-012` (4 Baustellen: 002, 003, 006, 011; Eichwette 001).
  Herleitung und Verworfene in `docs/2026-10-04-buch-bielefeld-KANDIDATEN.md`, Abschnitt „Stufe 2“.
- bielefeld.de sperrte nicht mehr (29 Abrufe, je 6 s Abstand). Jedes Zitat in zwei Abrufen wörtlich; 9 von 10 Quellen in der
  Wayback Machine, Zitat in der Kopie geprüft (node 34713 zweimal HTTP 520, dort lokale Kopie); alle 10 Quellen als Kopie mit SHA-256
  in `recherche/belege/` (Blob = Prüfsumme, drei Stichproben). Zehnte Quelle: Stadtwerke Bielefeld, Mitteilung 19.06.2026.
- Prüfung: 12 Wetten ohne Fehler; `alle`: 15 Bücher, 315 Wetten; 99 Tests grün.
- Nächste Fristen: 001 am 14.10. (Infostand 13.10.; nur ehrlich, wenn das Buch vorher öffentlich ist, sonst vor dem Merge verwerfen),
  002 am 18.11., 003 und 004 am 01.12.2026.
- Vor dem Merge beider Stadt-Zweige: Absatz „Warum Münster“ in `buecher/muenster/BUCH.md` berichtigen (nennt Bielefeld noch „nicht fertig“).
- Nicht angesehen: Ratsinformationssystem Bielefeld, Haushalt 2027 (spätere Ergänzung).
- **Wartet auf Felix:** Frage 99 (mergen und pushen: `cd ~/wettbuch && git merge buch-bielefeld && git push origin master`).

## Neu 04.10.2026 19:20 (Dauerlauf): Buch „Münster gegen Münster“, lokal (Frage 98)

- Zweig `buch-muenster` (Arbeitsverzeichnis `~/wettbuch-muenster`, von master `f641a19`, `837e023`), nicht gemergt, nicht gepusht:
  `buecher/muenster/` mit BUCH.md und 15 Wetten `muenster-2026-001` bis `-015`; Kandidaten und Verworfene in
  `docs/2026-10-04-buch-muenster-KANDIDATEN.md`.
- **Vorgezogen vor Bielefeld** (IT.NRW: Bielefeld 330 825, Bonn 323 245 mit Buch, Münster 307 979), weil bielefeld.de weiter sperrt;
  steht so in BUCH.md.
- Quelle: Schnittstelle des Presseportals (`https://pressemitteilungen.stadt-muenster.de/api/items?page=N`, Einzelabruf
  `…/api/item/<Nummer>`, Feld `plain_article`); 792 Mitteilungen seit 01.01.2026, 89 mit Terminsatz. Die Wetten nennen die
  Schnittstelle als `quelle`, die Leseansicht im Vermerk (Abweichung von den anderen Stadtbüchern).
- Zitate 15/15 wörtlich im zweiten Abruf. **Archiv (Nachzug 05.10. 01:50, `0f15896`):** 14 von 14 Quellen mit geprüfter Wayback-Kopie; die 6 fehlenden hatten
  schon eine Kopie vom 04.10. (nur die Anzeige hing nach), jede byte-gleich mit der lokalen Kopie, Zitate wörtlich. Alle 14 als lokale Kopie
  `recherche/belege/2026-10-04-muenster-item-*.json`, SHA-256 im Vermerk (Blob = Prüfsumme, zwei Stichproben).
- Früheste Prüfungen: 001 Blindgänger-Überprüfung Lamberti-Kirchplatz 12.10. (Ereignis So 11.10.), 002–004 Schul-Einzüge 07.11.,
  005 Hallenbad Wolbeck 09.11., 006–009 am 01.01.2027.
- **Zeitfenster:** 001 ist nur ehrlich, wenn das Buch bis Sa 10.10. öffentlich ist; sonst vor dem Merge verwerfen.
- `--pruefen` 15 Bücher / 318 Wetten ohne Fehler, 99 Tests grün. Nur neue Dateien.
- **Wartet auf Felix:** Frage 98 (mergen und pushen: `cd ~/wettbuch && git merge buch-muenster && git push origin master`).

## Neu 04.10.2026 18:40 (Dauerlauf): Buch „Bielefeld gegen Bielefeld“ begonnen, Stufe 1 (keine Wetten)

- Zweig `buch-bielefeld` (Arbeitsverzeichnis `~/wettbuch-bielefeld`, auf master `f641a19` vorgespult, `9bed44c`), nicht gemergt, nicht gepusht.
- `docs/2026-10-04-buch-bielefeld-KANDIDATEN.md`: 728 Mitteilungen in der Liste (Jan.–Okt. 2026), Volltext der 49 jüngsten,
  24 mit Terminsatz (7 brauchbar, 17 schwache Kurzsperrungen), Kopien mit SHA-256 in `recherche/belege/2026-10-04-bielefeld-node-*.html`;
  17 größere Vorhaben nur als Titel (Volltext fehlt).
- **Nicht fertig, weil:** bielefeld.de sperrt den Rechner nach ~65 Abrufen (503, dann keine Verbindung), Wayback Save antwortet 429.
  Zweiter Abruf und Archivkopie fehlen → keine Wetten angelegt. Nächster Lauf: höchstens ein Abruf je 5 s, höchstens 40 je Lauf;
  Schritte 1–5 stehen am Ende der Kandidaten-Datei.
- Nebenbefund: master ist seit Felix' Merges vom 04.10. gleich origin (`f641a19`); die Zeile „Phase“ oben ist überholt.

## Neu 04.10.2026 11:20 (Dauerlauf): Wuppertal-Fristen 09./11.10. vorbereitet (Frage 85)

- `docs/2026-10-04-aufloesung-wuppertal-0910-1110-VORBEREITET.md` (unversioniert): 001 Spielplatz Werther Hof, Termin 08.10.
  unverändert in „Aktuelle Meldungen“; 002 Brunnen Alte Freiheit: seit 07.08. keine Meldung, Quelle unverändert, Prognose 0,35 plausibel.
- **Befund:** Beide Wetten sind nur ehrlich, wenn `buch-wuppertal` vor dem Ereignis öffentlich ist (Push bis Mi 07.10.). Später
  gepusht → 001/002 vor dem Merge verwerfen („Ereignis vor Veröffentlichung“), 13 Wetten bleiben. **Wartet auf Felix: Frage 85.**

## Neu 04.10.2026 07:35 (Dauerlauf): Buch „Wuppertal gegen Wuppertal“ (8. Stadtbuch), lokal (Frage 83)

- Lokaler Zweig `buch-wuppertal` (von master `580b504`; `8250c39` + Fix), nicht gemergt, nicht gepusht: `buecher/wuppertal/`
  mit BUCH.md und 15 Wetten `wuppertal-2026-001` bis `-015`. Auswahlregel wie Bochum (IT.NRW A123 2025 21: Wuppertal 357 900).
- Quellen: 12 Pressemitteilungen wuppertal.de (alle 589 Mitteilungen Jan.–Sep. 2026 durchsucht), 2 WSW, 1 talzeit (Pina Bausch
  Zentrum: Kulturdezernent kündigte im Rat 28.09. drei Bauvarianten bis Jahresende an; 228 statt 161 Mio €).
- Zitate: 15/15 live wörtlich, beim Anlegen in einem dritten Abruf erneut bestätigt.
- **Archiv:** wuppertal.de weist Wayback ab (HTTP 520). Nur 4 von 15 im Archiv (WSW ×2, talzeit, Deweerth 14.04.). Für die
  11 übrigen lokale Kopie `recherche/belege/2026-10-04-wuppertal-*.html`, SHA-256 als Vermerk in der Wette;
  `.gitattributes` `recherche/belege/** -text`, damit der gespeicherte Blob byte-gleich zur Prüfsumme ist (11/11 geprüft).
- **Befund nebenbei (erledigt 04.10. 07:50, `930f0c6`):** Auf `wortlaut-vorschlag` hatte git (autocrlf) die Köln-Belegkopie
  umgeschrieben (114 CR weg, Original nicht rekonstruierbar). Neu abgerufen 07:45 (Last-Modified unverändert, Unterschied nur
  Cache-Zeitstempel), mit identischer `.gitattributes` byte-gleich eingecheckt, Bericht nennt jetzt `c8534af3…` + Wayback
  `20261004033133` (per CDX bestätigt). Alle drei Belegkopien Blob = Prüfsumme; Merge mit `buch-wuppertal` konfliktfrei, 99 Tests grün.
  Reihenfolge im Sammelmerge damit egal.
- Früheste Prüfungen: 001 Spielplatz Werther Hof 09.10., 002 Brunnen Alte Freiheit 11.10., 003 Brücke Fischertal und
  004 WSW-Gesellschaft 01.11., 005 Gartenhallenbad Cronenberg 17.11.
- Kein Haushalt 2027 möglich (Doppelhaushalt 2026/27 genehmigt, Mitteilung 28.07.2026) → verworfen; Liste der Verworfenen in
  `docs/2026-10-04-buch-wuppertal-KANDIDATEN.md`.
- `--pruefen` 10 Bücher / 259 Wetten ohne Fehler, 99 Tests grün. Nur neue Dateien + `.gitattributes`.
- **Wartet auf Felix:** Frage 83 (Zweig mergen und pushen = Buch geht live; bei Freigabe in den Sammelmerge-Befehl aus Frage 66
  `buch-wuppertal` vorne mit aufnehmen).

## Neu 04.10.2026 06:50 (Dauerlauf): Bonn „kein Treffer“ nachgeprüft (Frage 80)

- Bericht `recherche/BONN-KEIN-TREFFER-2026-10-04.md` auf Zweig `wortlaut-vorschlag` (`cc17694`), Wettdateien unverändert.
- **gedeckt (12):** 001, 003–006, 009, 014, 016, 019, 022, 023, 031 (Haushalt: Quelle schreibt „97“, Wetten „97,0“ → darum kein Treffer).
- **012/013:** Quelle „Stadtverwaltung“, Wette „Konzern Stadt Bonn“; 013 „knapp 67“ statt „rund 67“.
- **018:** rund 300 Gebäude werden auf PV-Tauglichkeit GEPRÜFT; Ziel 2028 = alle baulich geeigneten. Frage so nicht auflösbar → Vorschlag neue Frage.
- **014–017:** Frist 2027 nur aus Planlaufzeit „2023 bis 2027“; 015/017 nennen kein Jahr → Kontextsatz.
- **023:** Satz stammt aus dem Text der Stadt über die VEBOWAG („konkrete Planungen … bis einschließlich 2028“), nicht von OB/Hermes.
- Damit alle fünf Städte durch (Köln 73, Düsseldorf 75, Dortmund 76, Essen 78, Bonn 80).

## Neu 04.10.2026 06:30 (Dauerlauf): Essen „kein Treffer“ nachgeprüft (Frage 78)

- Bericht `recherche/ESSEN-KEIN-TREFFER-2026-10-04.md` + lokale Kopie der Projektseite Moltkestraße (SHA-256 `4b5954f9…d8c0`)
  auf Zweig `wortlaut-vorschlag` (`7e444de`), Wettdateien unverändert.
- **gedeckt (10):** 002–005, 014–017, 020, 033 (Umschreibungen, Zahlen/Termine wörtlich in der Archivkopie).
- **013:** „Spätestens zum Schuljahr 2027/2028“ steht auf der Projektseite (Wayback 20261004041946), nicht in der PM 02.05.2025.
  PM 20.11.2024 nannte noch „möglichst schon zum Schuljahr 2026/2027“ → Kandidat für neue Wette mit Ausgang NEIN.
- **024:** Quelle kündigt „Grundsatzentscheidung für den Neubau“ an, nicht den Standort → Vorbehalt im Vermerk 30.08. entfällt, JA bleibt.
- **023:** „Vorbehaltlich des Ratbeschlusses zum Bebauungsplan … könnten“ → Bedingung als Vermerk.
- Verbleibend „kein Treffer“: Bonn 17.

## Neu 04.10.2026 06:06 (Dauerlauf): Dortmund „kein Treffer“ nachgeprüft (Frage 76)

- Bericht `recherche/DORTMUND-KEIN-TREFFER-2026-10-04.md` + lokale Seitenkopie `recherche/belege/2026-10-04-dortmund-fabido-…-2025-07-07.html`
  (SHA-256 `d1c4a1fd…a674`) auf Zweig `wortlaut-vorschlag` (`0dbea27`, `4a1e621`), Wettdateien unverändert.
- **gedeckt:** 012 (van Bebber: „sehr ambitioniertes Ziel“, „3,1 Millionen Reisenden“).
- **005–007 (FABIDO-Kitas):** Platzzahlen/Gruppen/Termine stehen nicht in der zitierten RN-Quelle vom 12.11.2024 (nur „vier
  Einrichtungen … 491 Plätze bis Ende 2025“), sondern in der Stadtmeldung **07.07.2025** (dortmund.de, Wayback 20261004040434).
  `gesagt_am`/`hinterlegt_am` falsch, Ausgänge bleiben (JA/JA/NEIN). Vorschlag: Quelle, Datum, Zitat korrigieren.
- **013/014 (DSW21-Diesel):** „155 Busse / 55 Mio €“ ist eine Kostenrechnung der Presse, kein Plan; angekündigt waren vier
  Diesel pro Jahr. Beide offen (null). Vorschlag: nicht werten, schließen mit Vermerk.
- Verbleibend „kein Treffer“: Bonn 17, Essen 13.

## Neu 04.10.2026 05:51 (Dauerlauf): Düsseldorf „kein Treffer“ nachgeprüft (Frage 75)

- Bericht `recherche/DUESSELDORF-KEIN-TREFFER-2026-10-04.md` auf Zweig `wortlaut-vorschlag` (`a58dcd2`), Wettdateien unverändert.
- **gedeckt:** 006, 010, 019, 020, 024, 025. **021** gedeckt mit Unschärfe (5,4 Mio gelten laut PM „von der Hansaallee bis
  zum Luegplatz“, der 1. BA beginnt am Areal Böhler).
- **022 (Luegallee–Luegplatz, aufgelöst JA):** Quelle sagt am 11.07.2025 „ist bereits fertiggestellt“, für „dieses Jahr“
  war nur der Rest angekündigt → Prognose gegen ein schon eingetretenes Ereignis gewertet. Vorschlag: neu fassen (ganzer
  1. BA bis 31.12.2025, Indiz NEIN) oder aus der Wertung nehmen → Frage 75.
- **Köln 070–072:** Wayback-Save gelungen, Kopie 20261004033133 enthält alle drei Stellen wörtlich (Frage 73 zu `gesagt_am` bleibt).
- Verbleibend „kein Treffer“: Bonn 17, Essen 13, Dortmund 6.

## Neu 04.10.2026 05:50 (Dauerlauf): Köln „kein Treffer“ nachgeprüft (Frage 73)

- Bericht `recherche/KOELN-KEIN-TREFFER-2026-10-04.md` + lokale Seitenkopie `recherche/belege/…kulturtermine-september-2026.html`
  (SHA-256 `a7c61c3d…c424`) auf Zweig `wortlaut-vorschlag` (`fdf98cd`), Wettdateien unverändert.
- **gedeckt:** koeln-2025-043 (GU im 3. Quartal 2025), koeln-2025-064 (19.579 m² BGF), koeln-2026-073 (r e t u r n, 16.09. 19 Uhr).
- **koeln-2026-070/-071/-072 (Bühnen):** Absatz fehlt in der einzigen Wayback-Kopie (19.08. 00:08 UTC); Live-Seite
  Last-Modified 20.08. 16:33 → `gesagt_am` 18.08. vermutlich falsch (eher 20.08.). Ausgang unverändert. Wayback-Save
  scheitert (520 / job-failed) → im nächsten Guard-Lauf erneut versuchen.
- Verbleibend „kein Treffer“: Bonn 17, Essen 13, Düsseldorf 8, Dortmund 6 (Dortmund 005–007 ungeklärt, Bezahlschranke).

## Neu 04.10.2026 05:40 (Dauerlauf): nächste Fristen vorbereitet

- `docs/2026-10-04-aufloesung-0910-1510-VORBEREITET.md` (unversioniert wie die anderen VORBEREITET-Dateien).
- **bonn-2026-034** (Prüfung 09.10.): SWB-Meldung 28.09. „Nach erfolgreichen Sanierungsarbeiten an Gleis 1 …“, Gleis 2
  gesperrt ab 09.10. 02:00; wörtlich und archiviert (Wayback 20261004031422). Starkes Indiz JA; am 09.10. nur auf
  Verlängerung prüfen und neu archivieren.
- **essen-2026-035 bis -038** (Prüfung 15.10.): Rat 9. Sitzung 14.10. 15:00 per OParl bestätigt (meeting/33118), Tagesordnung
  am 04.10. noch leer → ab ~07.10. prüfen, ob die vier Vorlagen draufstehen. Prüfregeln je Wette in der Datei.

## Neu 04.10.2026 04:50 (Dauerlauf): KW40-Kandidaten als fertige Wetten (Frage 60)

- Zweig `kw40-kandidaten` (`080ac84`, von master, lokal): **essen-2026-040** Zentralbibliothek öffnet 24.10.2026
  (Stadt 1,00 angekündigt, Computer 0,92; Prüfung 25.10. — eilig), **koeln-2026-084** Einzug Bezirksrathaus Rodenkirchen
  bis 30.09.2028 (0,80 / 0,30), **duesseldorf-2026-036** Baubeginn Tonhalle-Gesamtfassade bis 30.06.2027 (0,80 / 0,50;
  im Entwurf als „037?“ geführt, nächste freie Nummer ist 036).
- Zitate am 04.10. live wörtlich, alle drei Quellen im Wayback (20261004024530, 20261004024425, 20261004024206); Essener
  Termin am 04.10. zusätzlich auf der Startseite der Stadtbibliothek bestätigt (archiviert 20261004024732).
- `--pruefen` 9 Bücher / 247 Wetten ohne Fehler, 99 Tests grün. Nur neue Dateien → kein Konflikt mit den anderen Zweigen.
- Bei „steht“ zu 60: `git merge kw40-kandidaten`, dann Push durch Felix (mit den anderen).

## Neu 04.10.2026 04:30 (Dauerlauf): Inhaltsprüfung der vier verdächtigen Zitate

- Bericht `recherche/INHALTSPRUEFUNG-2026-10-04.md` auf Zweig `wortlaut-vorschlag` (`fd403d2`), Wettdateien unverändert.
- **gedeckt:** bonn-2025-022 (Quelle schreibt „sechs Millionen Euro“), koeln-2025-023 (Fließtext „bis zum Ende des zweiten
  Halbjahres 2025“), duesseldorf-2025-016 („bis 2030“ nicht in der PM 06.12.2024, aber OB Keller 21.07.2023 laut
  Stadtplanungsamt 26.07.2023, neu archiviert 20261004021436).
- **bonn-2026-031:** Totensonntag gedeckt, „ab 12 Uhr“ mehrdeutig (Satz steht nach dem Dreikönigsmarkt-Absatz) →
  **Frage 67**, eilig vor Prüfung 19.11.: 12 Uhr aus der Bedingung nehmen.
- bochum-2026-010: ~~Wayback-Save wieder 520~~ **erledigt 04:32:** Kopie 20261004021426 (HTTP 200), Zitat in allen drei Teilen
  wörtlich; Nachtrag im Archivbefund der KANDIDATEN-Datei, `607b923` auf `buch-bochum` (lokal). Bochum: 12 von 12 tragen.

## Neu 04.10.2026 04:05 (Dauerlauf): Probe-Sammelmerge der wartenden Zweige

- Auf einem Wegwerf-Zweig von master (`580b504`) nacheinander gemergt: `buch-gatekeeper`, `buch-bund`, `buch-duisburg`,
  `buch-bochum`, `wortlaut-vorschlag` (enthält `archiv-sicherung`). **Keine Konflikte.** Danach: 99 + 26 Tests grün,
  `--pruefen` 13 Bücher / 285 Wetten ohne Fehler, voller Site-Bau wie `pages.yml` grün (323 HTML-Seiten, neue Ordner
  bochum, bund, duisburg, gatekeeper). Wegwerf-Zweig wieder gelöscht, master unverändert (11 Commits vor origin).
- `wortlaut-vorschlag`/`archiv-sicherung` ändern keine Wettdatei (nur Werkzeuge + Berichte), können also unabhängig von
  Frage 61 mit.
- **Wartet auf Felix:** Frage 66 (alles auf einmal, Befehl unten) — oder einzeln über 44/46/54/64.
  Befehl, falls „steht“: `cd ~/wettbuch && for b in buch-gatekeeper buch-bund buch-duisburg buch-bochum wortlaut-vorschlag; do git merge --no-edit $b; done && python -m pytest -q && git push origin master`

## Neu 04.10.2026 03:50 (Dauerlauf): Buch „Bochum gegen Bochum“ (7. Stadtbuch), lokal

- Lokaler Zweig `buch-bochum`, Commit `29f2067` (von master `580b504`, nicht gemergt, nicht gepusht): `buecher/bochum/` mit
  BUCH.md und 12 Wetten `bochum-2026-001` bis `-012`. Auswahl ohne Ermessen = einwohnerstärkste NRW-Stadt ohne Buch:
  IT.NRW A123 2025 21 (Stand 30.06.2025) Bochum 358 426 vor Wuppertal 357 900 (knapp; nächste nach dieser Regel: Wuppertal).
- Themen: Haushaltssatzung 2027, Stadtpark-Freigabe 06.11.2026, Windpark Sundern (Stadtwerke), SB33-Einstellung, Wasserspielplatz
  Ostpark, Einbahnstraße Alleestraße bis März 2027, Haus des Wissens, 11. Gymnasium, Lothringentrasse-Brücke A 43,
  Dreifachsporthalle Markstraße, B-Plan Wilhelm-Leithe-Weg Nord, Haus der Musik 2028.
- Zitate: alle 12 gegen frischen Live-Abruf wörtlich geprüft (Unteragent); Archivkopien für 11 von 12 tragend (010 Sporthalle:
  Wayback 520, neuer Versuch offen). Stichprobe 006 von mir in der Wayback-Kopie 20261004013939 wörtlich gefunden.
- Schwächen: 002/004 (Radio Bochum) und 008 (Bochum Journal) sind Pressewiedergaben „laut Stadt“; 007 Projektseite ohne Datum
  (gesagt_am = Schnappschuss 13.05.2026); 003 Windpark liegt im Hochsauerland (Aussage der städt. Tochter). Stadt-Prognosen
  nach FORMAT §1.2: angekündigt 1,00, voraussichtlich 0,80.
- Kandidaten (17) und Verworfene (~20) mit Grund: `docs/2026-10-04-buch-bochum-KANDIDATEN.md`.
- Prüfung: `alle buecher … --pruefen` 10 Bücher, 256 Wetten, keine Fehler; 99 Tests grün.
- Erste Frist: bochum-2026-002 Stadtpark (Prüfung 07.11.2026).
- **Wartet auf Felix:** Frage 64 (Zweig mergen und pushen = Buch geht live).

## Neu 04.10.2026 03:20 (Dauerlauf): Wortlaut-Vorschläge (Vorarbeit Frage 61), lokal

- Zweig `wortlaut-vorschlag` (`6379f45`, von `archiv-sicherung` abgezweigt, nicht in master): `werkzeuge/wortlaut_vorschlag.py`
  (26 Tests mit archivsicherung) sucht je `zitat_fehlt`-Wette die Stelle in der Archivkopie, die das Zitat am besten deckt.
  Wettdateien unverändert. Bericht `recherche/WORTLAUT-VORSCHLAEGE-2026-10-04.md`, Tabelle `recherche/wortlaut-vorschlaege.csv`.
- 164 Wetten: **88 Vorschlag, 22 Zahl abweichend (meist Datumsschreibweise), 49 kein Treffer, 5 Archiv leer**
  (duesseldorf-2025-004…008: Archivkopie ist Bot-Schutzseite → neue Kopie oder Ratsdokument nötig).
- Bonner Haushaltszahlen stehen als Liste in der Quelle („2025 97 Millionen Euro, 2026 123 …“) → Formfehler, nicht erfunden.
- **Inhaltlich zu prüfen:** duesseldorf-2025-016 („bis 2030“ nicht in Quelle), koeln-2025-023 („Ende 2. Halbjahr 2025“ vs.
  „bis Ende 2025“), bonn-2026-031 (Totensonntag-Zusatz), bonn-2025-022 („6 Mio Bundesförderung“), dortmund-2025-005…007
  (Platzzahlen je Kita nicht auf der Seite, Ruhr-Nachrichten hinter Bezahlschranke → ungeklärt).
- **Nachtrag 02:58 (`fe072ee`):** Düsseldorf 004–008 nachgesichert — Live-Seite liefert mit Browser-Kennung den
  vollen Text, neue Wayback-Kopie 20261004005146 enthält alle fünf Zahlen wörtlich; Zitate sind Umschreibungen, Inhalt
  gedeckt. Zählung jetzt 92 vorschlag / 22 zahl_abweichend / 50 kein_treffer / 0 archiv_leer.
- Vorschläge sind Fundorte, keine fertigen Vermerke (Wortzählung; Stichprobe: koeln-2025-012 falscher Satz). Vermerke erst nach
  „steht“ zu Frage 61, je Stelle von Hand nachsehen.

## Neu 04.10.2026 01:55 (Dauerlauf): Archivsicherung + Wörtlichkeits-Prüfung aller 273 Wetten, lokal

- Lokaler Zweig `archiv-sicherung` (`ba26546`…`6349fbb`, nicht in master): `werkzeuge/archivsicherung.py` (15 Tests,
  ohne Netz) sucht je Wette die jüngste Wayback-Kopie, prüft das Zitat darin und sonst auf der Live-Seite; mit
  `--speichern` stößt es fehlende Kopien an (Save Page Now, langsam; bei bonn.de Minuten je Seite). Wettdateien bleiben unverändert.
- **Befund** (`recherche/ARCHIVSICHERUNG-2026-10-04.md`, Tabelle `recherche/archiv-quellen.csv`): von 273 Wetten tragen
  **61** (Archiv + Zitat wörtlich), bei **19** steht das Zitat live wörtlich, aber eine Archivkopie fehlt, **156 sind nicht
  wörtlich** (weder im Archiv noch live; 130 davon Alt-Wetten 2025: Stichworte, „Mio“ statt „Millionen Euro“, eingefügte
  Wörter ohne Klammer, Sätze ohne „…“ zusammengezogen), 37 nicht erreichbar (Bonn komplett hinter Bot-Prüfung).
  Inhaltlich erfunden war in keiner Stichprobe etwas, verletzt ist FORMAT.md Z. 74/261. Die Bücher vom 03.10. sind fast sauber.
- **Wartet auf Felix:** Frage 61 (Vermerk mit Wortlaut je Wette, Kopf bleibt eingefroren; Prüfwarnung im Generator).
- **Erledigt 04.10. 02:25:** die 19 „live wörtlich“ mit neuer Option `--nur-live --speichern` archiviert (`6ca0034`…`fda900e`,
  16 Tests); alle 19 tragen → **80 tragen, 156 nicht wörtlich, 37 nicht erreichbar**. Save Page Now meldet manchmal Fehler,
  obwohl die Kopie entsteht → nach dem Speicherlauf einmal ohne `--speichern` nachprüfen. Rest wartet auf Frage 61.

## Neu 04.10.2026 00:40 (Dauerlauf): Wochenprüfung KW 40 — Ankündigungen und Ausbau-Vorschlag

- `recherche/ANKUENDIGUNGEN-KW40-2026-10-04-ENTWURF.md` (unversioniert, nichts im Buch): 17 Kandidaten (Köln 4,
  Bonn 2 ungeprüft, Düsseldorf 4, Essen 3, Dortmund 4), Zitate wörtlich aus Pressemitteilungen, IDs mit „?“.
  Stärkste: essen-2026-040? Zentralbibliothek eröffnet 24.10.2026; koeln-2026-084? Bezirksrathaus Rodenkirchen bis
  Ende Q3 2028 / 85,1 Mio.; duesseldorf-2026-037? Tonhalle-Fassade Baubeginn Q2 2027. bonn.de-Presse jetzt ganz hinter
  Bot-Prüfung; Ratsinfo in keiner Stadt durchsucht. Offen: dortmund-024? evtl. Dublette zu 016. → Frage 60.
- Ausbau-Vorschlag „Auskunft gegen Frist“ (Fristquote IFG-Anfragen aus der offenen FragDenStaat-API je Buch-Stadt,
  zuerst lokale Probe 2025, keine Wette) → Frage 58. API-Lizenz ungeklärt; Eingangsbestätigungen herausfiltern.

## Neu 03.10.2026 22:45 (Dauerlauf): Buch „Duisburg gegen Duisburg“ (6. Stadt), lokal

- Lokaler Zweig `buch-duisburg`, Commit `ecfb90a` (nicht in master, nicht gepusht): `buecher/duisburg/` mit BUCH.md und
  11 Wetten `duisburg-2026-001` bis `-011`. Auswahl ohne Ermessen = einwohnerstärkste NRW-Stadt ohne Buch (nach Köln,
  Düsseldorf, Dortmund, Essen). Themen: drei Schulbauten (Heine, Leibniz, Mitte-Süd), Feuerwache 1A (zweimal verschoben),
  Feuerwehr Hamborn, RheinPark zum IGA-Start 23.04.2027, Linie 903 im 5-Min-Takt (DVG-Seite heute 404, Zitat aus Wayback),
  Sperrtor Marientor Baustart, Bibliothek Ruhrort 2026, Defizit 2027 > 400 Mio (Entwurf 439,8), keine Steuererhöhung 2027.
- Zitate: Unteragent hat jede Seite abgerufen und wörtlich kopiert; Stichprobe (006 RheinPark, 004 Feuerwache) live gegengeprüft.
  Schwächen: 008/010/011 aus Lokalpresse wiedergegeben; Wayback-Links fehlen außer bei 007.
- Kandidaten, Verworfene (14) und Begründungen: `docs/2026-10-03-buch-duisburg-KANDIDATEN.md`.
- Prüfung: `alle buecher … --pruefen` 10 Bücher, 255 Wetten, keine Fehler; 99 Tests grün.
- Erste Fristen: 009 Bibliothek (01.01.2027), 010 Haushalt (01.01.2027).
- **Wartet auf Felix:** Frage 54 (Zweig mergen und pushen = Buch geht live).

## Neu 03.10.2026 22:26 (Dauerlauf): 5. Auflösungslauf, lokal committet (`580b504`)

- `recherche/AUFLOESUNG-2026-10-03.md`: 13 überfällige Wetten (koeln-2025-032/-050/-059, Köln JA 2025 -005/-006/-007/-008/-015,
  essen-2025-001/-032/-034, dortmund-2025-001/-014), **keine auflösbar**, Wettdateien unverändert.
- JA 2025 nur Entwurf/vorläufig: Köln vorläufig **650,0 Mio** Fehlbetrag (angekündigt 582 / Plan 399,3), Grundsteuer B 11,0 Mio
  unter Plan; Essen Entwurf **+1,1 Mio** Jahresüberschuss (ordentl. Ergebnis −73,8 Mio); Dortmund Entwurf **−352,7 Mio**.
  Köln hat zuletzt JA **2023** festgestellt (04.09.2025) → Köln-Wetten Wiedervorlage Ende 2027; Essen ~Nov. 2026; Dortmund Dez. 2026.
- dortmund-2025-014 (und vermutlich -013): DSW21 bestreitet die „155 Dieselbusse für 55 Mio“ (Presse-Fehllesung) → Frage 52.
- koeln-2025-059 Kreuzgasse: PM 13.05.2026 „Vergabeverhandlungen … dauern noch an“, danach nichts → offen, Richtung Nein.
- **Wartet auf Felix:** Frage 51 (Messgröße Essen 032/034), Frage 52 (dortmund 013/014 annullieren).

## Neu 03.10.2026 21:55 (Dauerlauf): Buch „KI gegen KI“ (Ebene KI-Anbieter), lokal

- Lokaler Zweig `buch-ki`, Commits `cba4157` + `7542338` (nicht in master, nicht gepusht): `buecher/ki/` mit BUCH.md und 9 Wetten
  `ki-2026-001` bis `-009`. Auswahl ohne Ermessen = Vollunterzeichner des GPAI-Verhaltenskodex laut Kommission
  (https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai, Stand 31.07.2026, 21 Unterzeichner) ohne die DMA-Gatekeeper
  (Amazon, Google, Microsoft haben das Gatekeeper-Buch); xAI nur Teilunterzeichner, Meta kein Unterzeichner; Liste nach Art. 52 Abs. 6
  AI Act am 03.10. weiter nicht auffindbar.
- Wetten: OpenAI Stargate UAE 200 MW live 2026, OpenAI for Germany Start 2026; Anthropic 10.000 Frontier Deployed Engineers bis Ende
  2027, > 1 GW TPU in Betrieb 2026; Cohere/Aleph Alpha Closing 2026 (zwei Wetten, ein Ereignis); IBM B300-Cluster Q1 2027, Quantum
  System Two Schweiz Ende 2026; ServiceNow 240.000 Lernende UK bis 2027. Alle Zitate aus Firmenquellen, per curl wörtlich geprüft.
- **Interessenkonflikt offengelegt:** der Computer ist ein Anthropic-Modell (BUCH.md + Vermerk bei 003/004). Dazu Offenlegung
  GitHub/Microsoft/OpenAI.
- Verworfen (Gründe in `docs/2026-10-03-buch-ki-anbieter-KANDIDATEN.md`): Mistral (nichts Eigenes im Fenster), Stargate 500 Mrd. (bis
  2029), IBM Quantum Advantage (schon gemeldet), kleine Unterzeichner ohne Prüfbares; Reserve Stargate Norway.
- Prüfung 9 Bücher/244 Wetten OK (Zweig gegen master), 99 Tests grün.
- **Wartet auf Felix:** Frage 50 (mergen + pushen; 003/004 mit Claude-Zahl oder qwen3:4b schätzen lassen).

## Neu 03.10.2026 21:15 (Dauerlauf): Köln-Feed eingefroren, Fix lokal

- **Befund:** `waiting-od.php` liefert seit **Mi 16.09.2026 07:45** für alle neun Kundenzentren dieselben Werte (Status
  „geöffnet“, Chorweiler 71 … Innenstadt 6 Min.). Wayback 16.09. 13:27 UTC und 20.09. 08:47 UTC gleicher Digest (`5HSZ6PS2…`),
  03.10. unverändert: https://web.archive.org/web/20261003190545/https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php
  `http://` leitet seit 20.09. per 301 um und liefert am 03.10. **403**; `https://` liefert 200.
- Folge: Auch ein pünktlicher Lauf (Fix `848e48b`) misst nichts Echtes. Der alte Code scheitert an 403, oder er schreibt bei einer Umleitung die Zahlen vom
  16.09. als Oktober-Messung.
- **Fix auf lokalem Zweig `koeln-rueckfall`** (`dfa94cb`, `0d22085`, nicht in master): `FEED_URL` https; `frische_records` /
  `feed_veraltet`: nur Zentren mit `timestamp` von heute (nicht Zukunft), sonst keine Zeile, Exit 1, Wayback-Beleg (Wächter
  mailt). Laptop-Rückfallebene: `messen.cmd` → `messwerte-laptop.csv` (gitignored), `nachtragen.py` übernimmt nur fehlende
  Slots (Probe ohne `--schreiben`). 43 Mess-Tests, 99 Generator-Tests grün; Review: Slot nach Uhrzeit vs. Cron als Grenze in README.
- **Presseamt-Mail gesendet von Felix 03.10. 22:03** (Thread `1a1032ae28c82b4f`, „Open-Data-Feed Wartezeiten Kundenzentren seit 16.09. nicht aktualisiert?“). Antwort wie Schweigen ist ein Beleg; Tagesprüfung sieht nach, Schweigen ab 17.10. (zwei Wochen) als Befund festhalten.
- koeln-2026-077–082 bleiben offen; Windows-Aufgaben bleiben aus, bis der Feed wieder frisch ist.
- **Wartet auf Felix:** Frage 48: vor dem Push `git merge koeln-rueckfall`, dann `git push origin master`.

## Neu 03.10.2026 20:20 (Dauerlauf): Buch „Bund gegen Bund“ (Ebene Bund), lokal

- Lokaler Zweig `buch-bund`, Commit `d36d468` (nicht in master, nicht gepusht): `buecher/bund/` mit BUCH.md und 8 Wetten
  `bund-2026-001` bis `-008`: d-you-Wallet 02.01.2027, Kindergeld 267 € ab 2027, Wohngeld-Absenkung 01.01.2027, Pflege-
  Strukturreform 01.07.2027, Pflegekommission bis 31.01.2027, digitaler Führerschein bis 31.12.2026, Bundeswehr ≥ 187.000
  zum 31.12.2026, 11 GW Kapazitätsausschreibung bis 03.09.2027. Alle Zitate zweimal unabhängig per curl wörtlich geprüft.
- Halter-Festlegungen nach Empfehlung (änderbar vor dem Livegang): Bundeswehr-Schwelle 187.000 („deutlich im Korridor“),
  Kraftwerks-Frist ab Seitendatum 03.09.2026, Führerschein „Ende des Jahres“ = 31.12.2026.
- Nicht übernommen (Gründe in `docs/2026-10-03-buch-bund-KANDIDATEN.md`): Haushalt 2027 ≤ 119 Mrd. (BMF-Bot-Sperre, Zitat nur
  einmal gesehen), zentrale Kfz-Zulassung (Abgrenzung), BIP/Inflation 2027 (Prognosen, Prüfung 2028); keine Bahn-Quelle gefunden.
- `alle buecher … --pruefen`: 9 Bücher, 243 Wetten, keine Fehler; 99 Tests grün.
- **Wartet auf Felix:** Frage 44 (Zweig mergen und pushen = Buch geht live).

## Neu 03.10.2026 17:55 (Dauerlauf): Buch „NRW gegen NRW“ (Ebene Land), lokal

- Lokaler Zweig `buch-nrw`, Commit `d12696f` (nicht in master, nicht gepusht): `buecher/nrw/` mit BUCH.md und 11 Wetten
  `nrw-2026-001` bis `-011`, alle Quellen Pressemitteilungen auf land.nrw, Zitate wörtlich geprüft (Skript + zwei Stichproben
  per curl). Erste Prüftage 01./02.01.2027 (Forensik Lünen fertig, Entlastungsgesetz, Lebensarbeitszeitkonto, Besoldung);
  dazu Radwege 1.000 km bis Ende Legislatur (Stichtag 31.05.2027 gesetzt), 3.000 Kommissaranwärter 01.09.2027 (2026 nur
  ~2.600), Nettoneuverschuldung 2027 (5,0 Mrd), GreenTech-Messe 09.09.2027, Abiture 2027, fünftes Abiturfach BK.
- `python -m wettbuch alle buecher … --pruefen`: 8 Bücher, 235 Wetten, keine Fehler; 99 Tests grün.
- Verworfen (Gründe im Lauf): Windkraft 1.000 Anlagen, RE 13 Eindhoven, Termine ab 2029, Mittelzusagen ohne Auflösbarkeit.
- **Wartet auf Felix:** Frage 30 (Zweig in master mergen und pushen = Buch geht live).

## Tagesprüfung 03.10.2026 (Dauerlauf)

- **43 Wetten fällig und offen** (pruefung_am ≤ 17.10., ohne ausgang, ohne ersetzt_durch). Die alten hängen an Jahresabschlüssen und IFG (`recherche/IFG-2026-09.md`); bearbeitet wurden die zehn Ereignis-Wetten aus September.
- `docs/2026-10-03-aufloesung-bonn-dortmund-VORBEREITET.md`: bonn-2026-032 **JA** (WDR 25.09., 36:27), dortmund-2026-019 **JA** (DOSB, amtlich), dortmund-2026-020 **JA mit Vorbehalt** (Start amtlich, Ende 21.09. nur Programm), bonn-2026-036 und -035 ungeklärt (bonn.de und Ratsinfo hinter Bot-Sperre, Felix kann im Browser nachsehen, Stellen in der Datei).
- `docs/2026-10-03-aufloesung-koeln-duesseldorf-essen-VORBEREITET.md`: duesseldorf-2026-033 **JA**, essen-2025-030 **NEIN** (Eröffnung Hallenbad Borbeck auf Frühjahr 2027 verschoben, radioessen.de 09.07. mit Stadt-Zitat), koeln-2026-073 ungeklärt (nur WZ-Bericht ohne Uhrzeit, Option JA in der Datei), duesseldorf-2026-034 ungeklärt (Indiz für NEIN), essen-2025-031 bleibt offen bis Verfall 2028.
- **032/019/033 JA, 030 NEIN aufgelöst und gepusht 03.10. 15:00 (`7560373`, Freigabe Felix Fragen 14/15).** Weiter offen: dortmund-2026-020 (wartet auf Bericht zum 21.09.), koeln-2026-073 (offen gelassen), bonn-2026-035/036 (Felix im Browser), duesseldorf-2026-034 (ungeklärt, Indiz NEIN). Die vorbereiteten „Beleg gesucht“-Vermerke für 073/034/031 sind nicht übernommen (nicht freigegeben).
- **072 JA / 083 NEIN aufgelöst und gepusht 03.10. 14:28 (`3734488`, Freigabe Felix per Mail „1-10 steht").** Köln jetzt: 21 aufgelöste Ja/Nein, 11 nicht eingetreten, 10 eingetreten. Nachfass-Entwürfe mit 083-NEIN liegen in Gmail (FDP/KSG mit CC Schöppen, Meifert/KStA), Felix sendet; alter Festakt-Entwurf an Meifert muss Felix noch löschen (Löschen war für den Dauerlauf gesperrt), der an FDP ist gelöscht.
- Köln-Messung: **korrigiert 15:25** — die Zeile hier vorher („am Nachmittag gemessen“, „Remote ist weiter“) war falsch. Siehe Abschnitt „Köln-Messung steht still“ unten.
- Postfach: keine Antwort von Köln, Podcasts oder Redaktionen.

## Köln-Messung steht still (Befund 03.10.2026, 15:20)

- `messwerte.csv` auf origin/master endet am **16.09.2026** (letzter „data:“-Commit `5638a62`). Seitdem: null Zeilen.
- Ursache (GitHub-API, öffentliche Run-Liste, abgerufen 03.10.): jeder geplante Lauf startete 5–7 h zu spät, frühester Start je Tag
  21.09. 13:16, 23.09. 12:03, 28.09. 14:24, 30.09. 12:57 UTC. Das Fenster endet Mo 13:00 UTC, Mi 10:00 UTC (MESZ).
  `messen.py` verwirft Läufe außerhalb korrekt („keine Messung“, Lauf trotzdem „success“); der Wächter schlug fehl und stieß per
  Dispatch nach, aber ebenfalls nach Schließung. Die Härtung `0f305db` funktioniert also, nur kommt kein Lauf rechtzeitig an.
- **Folge:** koeln-2026-077 (Oktober) braucht Oktober-Messungen; Wette 9 (privat) braucht ≥ 6 Monate mit Messwerten. Der September
  hat nur den 16.09. (ein Abruf, 15:27, außerhalb der Wertung).
- **Fix lokal, `848e48b`:** acht zusätzliche Startversuche Mo+Mi 00:07–04:03 UTC (Slot „vormittag“). Kommen sie pünktlich, enden sie
  vor 7:30 ohne Zeile; kommen sie 5–7 h zu spät, landen sie im Fenster. Neuer Test, 30 Mess-Tests + 99 Generator-Tests grün.
  **Nicht gepusht** (öffentliches Repo, Frage an Felix). Wirkt erst nach Push; nächster Messtag Mo 05.10.
- Rückfallebene, falls auch das nicht greift: die drei Windows-Aufgaben auf dem Laptop (deaktiviert seit 11.09., README im Ordner)
  oder ein externer Auslöser für `workflow_dispatch` (braucht Konto/Token = Felix).

## Wo wir stehen (03.10.2026)

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten. Pages-Build zuletzt grün 03.10. 12:46 UTC.
- Zweige `weitsicht` und `hinterlegt-sammelbuch` sind in master gemergt (lokal und auf origin noch vorhanden, löschbar).
- Bücher (Stand Dateien 03.10.): Köln 86 (29 aufgelöst, 54 offen, 3 ersetzt), Essen 39 (11/28), Düsseldorf 35 (16/19),
  Bonn 36 (5/31), Dortmund 20 (5/15), Weitsicht 8 (0/8). `buecher/hinterlegt/` leer.
- Fällig und offen (pruefung_am ≤ 03.10.): **32**, bis 17.10.: 37. Davon
  - 25 Alt-Wetten 2025 (Jahresabschlüsse, Baukosten, Bäume, Brücken) mit 1–4 Suchvermerken: warten auf Jahresabschlüsse
    (Köln festgestellt zuletzt 2023, Muster ~20 Monate) bzw. auf IFG (`recherche/IFG-2026-09.md`, sieben Anfragen nicht gesendet).
  - Ereignis-Wetten September: 073 (offen gelassen, Felix 03.10.), bonn-2026-035/-036 (Felix im Browser), dortmund-2026-020
    (wartet auf Bericht 21.09.), duesseldorf-2026-034 (Indiz NEIN), essen-2025-031 (bis Verfall 2028).
  - neu fällig: bonn-2025-001 (Defizit 2025, seit 01.10.).
  - nächste Stichtage: bonn-2026-034 (09.10., Heussallee), essen-2026-035 bis -038 (Rat 14.10., Prüfung 15.10.).
- Weitsicht-Buch: acht Einträge mit Felix- und Computer-Zahl, live seit 11.09. (`1d714bc`), Zahlen-Tabelle in der Git-Historie
  dieser Datei (Stand 11.09.).
- Seit 11.09. hinzugekommen (git log): Atom-Feed je Buch (`e666b96`), Impressum/Datenschutz (`d616c0f`), Köln sieben neue Wetten
  077–083 (`de299e8`), Auflösungen koeln-2025-003 (`4b0957c`), 070/071 (`5eb1a16`), 072/083 (`3734488`), Bonn/Dortmund/
  Düsseldorf/Essen (`7560373`).
- Ungetrackt in `docs/`: vier `*-VORBEREITET.md` (Arbeitsdateien der Auflösungen; 25.09., 01.10., zweimal 03.10.).
- Privates Wettbuch `~/kybernokratie/WETTBUCH.md`: offene private Fristen bis 31.10.: Wette 16 (Foren, 15.10., Bedingung drei
  Beiträge bis 08.10.), Wette 20 (Sprint, 31.10.). Wette 19 war in der Tabelle noch „offen“, obwohl der Eintrag sie am 27.09.
  zurückzieht → Tabellenzelle am 03.10. nachgezogen (Wettstand zeigt sie nicht mehr).
- Rechtsform: gUG nicht jetzt. Köln: 21 aufgelöste Ja/Nein (11 nicht eingetreten, 10 eingetreten).

## Nächster konkreter Schritt

1. **Felix:** erst `git merge koeln-rueckfall` (Frage 48), dann Push von `848e48b` freigeben (Frage in ~/allein/ALLEIN.md), am besten vor Mo 05.10. 02:00 Uhr; danach Di 06.10.
   prüfen, ob ein „data:“-Commit vom Montag da ist.
2. Recherche 03.10. (`docs/2026-10-03-aufloesung-haushalt-bonn-VORBEREITET.md`, Vermerke vorbereitet, nicht übernommen):
   bonn-2025-001 ungeklärt (Entwurf JA 2025 ~96,6 Mio nur aus Suchauszug, Quelle passwortgeschützt; bonn.de/Ratsinfo Bot-Sperre),
   dortmund-2025-001 ungeklärt (weiter nur Entwurf 352,7 Mio, nicht festgestellt), duesseldorf-2026-034 ungeklärt, Indiz NEIN,
   **bonn-2026-034 starkes Indiz JA** (SWB 28.09.: „Nach erfolgreichen Sanierungsarbeiten an Gleis 1 …“) → am Fr 09.10. auflösen.
3. Do 15.10.: essen-2026-035 bis -038 (Rat 14.10.) auflösen vorbereiten.

## Wartet auf Felix

- Frage 50: Buch KI (Zweig `buch-ki`, `7542338`) mergen und pushen.

- Frage 30: Buch NRW (Zweig `buch-nrw`, `d12696f`) mergen und pushen.

- Push `848e48b` (Köln-Messung).
- bonn-2026-035/-036 im Browser nachsehen (Stellen in `docs/2026-10-03-aufloesung-bonn-dortmund-VORBEREITET.md`).
- Sieben IFG-Anfragen absenden (`recherche/IFG-2026-09.md`); Vermögensbindung Satzung; Nachfolger als Hüter (Frist 31.12.2026).
- ~~Zwei Gmail-Entwürfe mit 083-NEIN senden~~ **gesendet von Felix 03.10. 22:01/22:02** (FDP/KSG + CC Schöppen Thread `1a0a5cebb76e922d`; Meifert/KStA Thread `1a0a5ce969b87477`). Offen: alten Festakt-Entwurf an Meifert löschen, falls noch da.
- Zweige `weitsicht` und `hinterlegt-sammelbuch` löschen (gemergt; Löschen nur mit „steht“).

## Blocker

Köln-Messung: ohne Push des Fixes (oder Rückfallebene) bleibt der Oktober leer, koeln-2026-077 und Wette 9 laufen ins Leere.
