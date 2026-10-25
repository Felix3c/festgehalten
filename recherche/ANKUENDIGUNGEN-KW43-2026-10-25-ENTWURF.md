# Ankündigungen KW 43 — Kandidaten für neue Wetten (Köln, Bonn, Düsseldorf, Essen, Dortmund)

**Zweck:** Wöchentliche Sammlung datierter, prüfbarer Ankündigungen der fünf Städte aus den eigenen Pressemitteilungen, als Vorrat für neue Wetten.
**Stand:** So 25.10.2026 ~01:50 (Dauerlauf, Wöchentlich KW 43), alle fünf Städte. Dortmund-Vorlauf vom Do 22.10. ~23:55 (Fenster 17.–22.10.), dazu Dortmund 23.10. und Köln, Bonn, Düsseldorf, Essen für etwa 16.–23.10. Neueste Meldungen vom Fr 23.10.
**Status:** ENTWURF. Nichts davon steht im Buch. Übernahme nur nach Felix' „steht“. IDs mit „?“ sind Vorschläge.

**Nächste freie Nummern** (über alle lokalen Zweige, alle Vorschläge KW40–KW43 als belegt): **koeln 094, bonn 041, duesseldorf 044, essen 047, dortmund 032.** koeln-2026-092 (Severinsbrücke, PM 28735) und 093 stehen schon im Buch.

**Methode:** Wie KW42. Dortmund über die Such-Schnittstelle des Newsrooms (`/api/search/proxy/search`, POST, Index `NEW_SITE`): Typ „messagepublication“ mit `releaseDate ≥ 17.10.` (30 Treffer) und Typ „news“ mit `stateDate ≥ 17.10.` (15 Treffer), neueste vom 22.10. 15:02. Die Listenseite `/newsroom/presse-mitteilungen/` gab am 22.10. ~23:45 per curl HTTP 403; Einzelseiten per Python urllib gingen (HTTP 200). robots.txt erlaubt alles.
- Jedes Zitat unten per Skript gegen den abgerufenen Seitentext geprüft (Gleichheit nach Leerzeichen-Normalisierung), 5 von 5 bestanden. Skripte und Rohabrufe: `C:\Users\skyla\allein\tmp\kw43-guard\`.
- SHA-256 = Fingerabdruck der lokalen Rohkopie (Abruf 22.10.2026 ~23:45).
- **Archiv:** Save Page Now am 22.10. ~23:55 für alle vier Seiten HTTP 520 (Archiv drosselt seit dem Abend). Bei Übernahme nachholen.
- **Archiv nachgeholt 23.10. ~02:35 (Dauerlauf):** Save Page Now für die drei Dortmund-Seiten angenommen (CDX Status 200). H-Bahn `20261023003323`, Rohkopie `recherche/belege/2026-10-23-archiv-dortmund-h-bahn-stadion.html`, SHA-256 `bb0f17da758a118ac6c8431b4d6b06cfe0a3a2f7bc14af749af7f401fdff4c81`, Zitat wörtlich. Kiebitzweg `20261023003537`, Rohkopie `recherche/belege/2026-10-23-archiv-dortmund-kiebitzweg.html`, SHA-256 `2244cc424c1ee25b65693fbcba2ba122fdb60fcb684b50f285964096a2e66f61`, Zitat wörtlich. Calvinstraße `20261023003402` liegt laut CDX vor (200), Abruf der Kopie scheiterte (Archiv nahm keine Verbindung an), Zitat gegen die Kopie bei Übernahme prüfen.
- Dublettenprüfung: `git grep` über buecher/ und recherche/ in allen lokalen Zweigen nach Calvin, Kiebitz, Lütgenholthauser, H-Bahn: keine Wette. Die H-Bahn wurde in KW41 und KW42 verworfen („Infoabend, kein Termin“); die Nachricht vom 20.10. nennt jetzt erstmals einen Termin.

---

## Dortmund (3)

### dortmund-2026-029? — H-Bahn bis „Ortsmühle“: Antragsunterlagen Planfeststellung Anfang 2027

- **Zitat:** „Die Antragsunterlagen sollen Anfang 2027 zur Prüfung eingereicht werden.“ Nächster Satz: „Der Planfeststellungsbeschluss könnte 2028 vorliegen, der erste Teilabschnitt 2029 in den Testbetrieb gehen.“
- **Quelle:** https://www.dortmund.de/newsroom/nachrichten-dortmund.de/h-bahn-faehrt-kuenftig-fast-bis-zum-stadion.html — Nachricht der Stadt vom Di 20.10.2026 11:38, Bericht über den Infoabend am 15.10. (DSW21 und Stadt). SHA-256 `07d9a98666e5361699b3be1816ed81ba37a0240044ac85bdca21e82f5d27450a`.
- **Wer sagt es:** Stadt Dortmund auf dortmund.de; der Satz steht im Absatz zu Friedhelm Richter (DSW21, federführend für die Planung). Akteur also DSW21 mit der Stadt, im Text so kennzeichnen.
- **Vorschlag Frage:** Hat DSW21 die Antragsunterlagen für die Planfeststellung des ersten H-Bahn-Abschnitts bis „Ortsmühle“ bis zum 30.04.2027 eingereicht?
- **Übersetzung:** „sollen“ → `voraussichtlich`, 0,80. „Anfang 2027“ als Ende April gelesen (erstes Drittel), Prüfung 01.05.2027. Ja, wenn Stadt, DSW21 (bus-und-bahn.de, dort sollen laut Text Dokumente und Pläne erscheinen) oder die Planfeststellungsbehörde die Einreichung mit Datum melden. Welche Behörde zuständig ist, ist ungeklärt (vermutlich Bezirksregierung Arnsberg, nicht geprüft).
- **Schwäche:** Eine Einreichung wird oft nicht eigens gemeldet; dann bleibt nur die Offenlegung, die später kommt. Die Wette braucht also eine zweite Quelle (DSW21-Projektseite) als Beobachtungsort.
- **Einschätzung:** mittel bis stark. Großes Projekt (rund 13 Mio. €, 95 % Landesförderung), erster fester Termin seit dem Infoabend.

### dortmund-2026-030? — Calvinstraße: Kampfmittel-Untersuchung fertig, Straße frei bis 27.11.

- **Zitat:** „Bis 27. November sollen die Arbeiten abgeschlossen und die Straße wieder freigegeben werden.“
- **Quelle:** https://www.dortmund.de/newsroom/presse-mitteilungen/in-der-calvinstrasse-untersucht-das-tiefbauamt-einen-kampfmittelverdachtspunkt.html — Pressemitteilung vom Mi 21.10.2026 10:00 (Vollsperrung ab Do 22.10., Hausnummern 27 bis 29). SHA-256 `92c45403d5462e497c7239601e7c4cf8f820ba0225a38cf78f575f447eb24795`.
- **Vorschlag Frage:** Ist die Calvinstraße in Höhe der Hausnummern 27 bis 29 bis zum 27.11.2026 wieder für den Verkehr freigegeben?
- **Übersetzung:** „sollen“ → `voraussichtlich`, 0,80. Prüfung 28.11.2026. Ja bei Meldung der Stadt, Eintrag der Baustellenkarte mit Enddatum oder datiertem Foto. Findet die Sondierung ein Kampfmittel, verlängert sich die Sperrung fast sicher; das ist der eigentliche Inhalt der Wette.
- **Einschätzung:** mittel. Kurze Laufzeit (5 Wochen), klare Ja/Nein-Lage, aber Beleg für „wieder frei“ hängt an der Baustellenkarte (bisher kein datierter Abruf geübt).

### dortmund-2026-031? — Kiebitzweg (Hombruch): neue Fahrbahndecke bis 18.11.

- **Zitat:** „Die Arbeiten für eine neue, glatte Fahrbahndecke beginnen am 26. Oktober und dauern voraussichtlich bis 18. November.“
- **Quelle:** https://www.dortmund.de/newsroom/presse-mitteilungen/der-kiebitzweg-in-hombruch-bekommt-eine-neue-fahrbahndecke.html — Pressemitteilung vom Do 22.10.2026 14:00 („Straßenoffensive“, Vollsperrung, ganze Länge). SHA-256 `efe52431e9c78ecbe0535522a16be03f2c61086c4fe6c0ff92f572f2f057ed85`.
- **Vorschlag Frage:** Ist die Sanierung des Kiebitzwegs bis zum 18.11.2026 abgeschlossen und die Vollsperrung aufgehoben?
- **Übersetzung:** „voraussichtlich“ → `voraussichtlich`, 0,80. Prüfung 19.11.2026. Beleg wie oben.
- **Gleiches Muster, gleicher Tag:** Lütgenholthauser Straße 94–100 (PM 21.10. 13:00, „Die Arbeiten zwischen den Häusern 94 bis 100 dauern voraussichtlich vom 26. Oktober bis 18. November.“, SHA-256 `e66b381dcae9cf6b5018a17c84d7daa0e1d0f31cc5f0bd6c892fed0360c989f9`, https://www.dortmund.de/newsroom/presse-mitteilungen/fahrbahnsanierung-strassenoffensive-kommt-in-die-luetgenholthauser-strasse-in-hombruch.html). Vorschlag: nur eine der beiden nehmen (Kiebitzweg, weil ganze Straße), die andere als Vermerk.
- **Einschätzung:** schwach bis mittel. Die „Straßenoffensive“ läuft schon über dortmund-2026-016/021; mehr vom selben Typ macht das Buch nicht stärker. Nur nehmen, wenn Felix kurze Fristen im Dortmund-Buch will.

Geprüft und verworfen (Dortmund): Frohlinder Straße (22.–30.10.), Hallesche Straße (26.–30.10.), Haberlandstraße Fahrbahn (23.–26.10.; Tempo 30 nachts nur „zeitnah“, kein Termin), Kurze Reihe (Sondierung ab 02.11., Dauer ausdrücklich offen), Abwassergebühren +4 % (Satzungsbeschluss, kein prüfbarer Termin in der Meldung), Westfalenpark Zentralplatz (= dortmund-2026-027), A45 Martener Straße zweiter Infoabend 02.11. (KW41/42-Vorschlag 026?, nichts Neues an Terminen), EDG-Laubkörbe (Modellversuch läuft schon), Fahrradstaffel (umgesetzt), Trabzon (Projektbericht), Untere Jagdbehörde 03.–05.11. geschlossen (Kurzfrist), Kultur-/Veranstaltungsmeldungen.

---

## Nachlauf So 25.10. (Köln, Bonn, Düsseldorf, Essen, Dortmund 23.10.)

**Methode:** Python urllib, keine Browser. Köln PM 28730–28740 (16.–23.10.). Bonn: Wayback-CDX für den Ordner `pressemitteilungen/oktober-2026/`; die zwei Seiten mit echter Länge direkt von bonn.de geladen (diesmal ohne Bot-Prüfung), die übrigen CDX-Einträge sind nur Prüfseiten (≈ 4,7 KB). Düsseldorf: Pressedienst-Archiv Seiten 1–5, 38 Meldungen 16.–23.10. einzeln. Essen: „aktuell.de.html“, 40 IDs 16.–23.10. Dortmund: Newsroom-Liste 23.10., 9 neue Seiten. Jedes Zitat unten per Skript gegen die Rohkopie geprüft (Leerzeichen normalisiert), **9 von 9 bestanden**. SHA-256 = Fingerabdruck der Rohkopie (Abruf 25.10. ~01:07–01:16). Rohkopien und Skripte: `C:\Users\skyla\allein\tmp\kw43-guard\`. Archiv (Save Page Now) noch nicht gemacht, bei Übernahme nachholen.
Dublettenprüfung: `git grep` über buecher/ und recherche/ in allen lokalen Zweigen (Zusatzvereinbarung, Theaterplatz, Himmelgeist, Karl-Hohmann, Berty-Albrecht, Quartier der Generationen, Venloer Straße, kick west): keine Wette. Severinsbrücke ist schon koeln-2026-092.

### Bonn (2)

#### bonn-2026-041? — Zusatzvereinbarung Berlin/Bonn-Gesetz am 17.12.2026 unterzeichnet
- **Zitat:** „Am 17. Dezember 2026 soll der lange und anspruchsvolle Verhandlungsprozess durch die Unterzeichnung der Zusatzvereinbarung zum Berlin/Bonn-Gesetz als Auftrag aus dem Koalitionsvertrag erfüllt und vollzogen werden.“
- **Quelle:** https://www.bonn.de/pressemitteilungen/oktober-2026/zusatzvereinbarung-zum-berlin-bonn-gesetz-steht-kurz-vor-der-unterzeichnung.php — PM der Stadt Bonn, Oktober 2026 (Wayback-Kopie `20261017144627` vorhanden). SHA-256 `a79ade626a3c9e81efaa8066059f7e50780cab5b0a2ffa6bb36ad2da566c339c`
- **Wer sagt es:** Bundesministerin Verena Hubertz, zitiert in der PM der Stadt. Akteur ist also der Bund mit Stadt, Land und Kreisen. Gleiche offene Frage wie bei der A45: Gehören Fremdzusagen ins Stadtbuch?
- **Vorschlag Frage:** Ist die Zusatzvereinbarung zum Berlin/Bonn-Gesetz am 17.12.2026 unterzeichnet worden?
- **Übersetzung:** „soll“ → `voraussichtlich`, 0,80. Prüfung 18.12.2026. Ja bei Meldung von Stadt oder Bund mit Datum 17.12. Später unterzeichnet = Nein.
- **Ersetzt:** den KW40-Vorschlag „Zusatzvereinbarung bis Ende 2026 — ZITAT UNGEPRÜFT“. Jetzt mit wörtlichem Zitat und festem Tag.
- **Einschätzung:** stark. Festes Datum, großes Thema für Bonn, kurze Laufzeit (8 Wochen).

#### bonn-2026-042? — Neugestaltung Innenstadt (Theaterplatz): Beginn der Gesamtmaßnahme im Sommer 2027
- **Zitat:** „Der offizielle Beginn der Gesamtmaßnahme ist weiterhin für den Sommer 2027 vorgesehen.“ Dazu: „Die sogenannten archäologischen Sondagearbeiten werden bis voraussichtlich Mitte November 2026 laufen.“
- **Quelle:** https://www.bonn.de/pressemitteilungen/oktober-2026/archaeologische-sondierungen-auf-dem-theaterplatz-ab-19.oktober.php — PM der Stadt Bonn (Wayback `20261015034804`). SHA-256 `d42be465cad93017952a4762304203cd2e92dff017454876b9487c6cd7f520fa`
- **Vorschlag Frage:** Haben die Bauarbeiten der Gesamtmaßnahme zur Neugestaltung der Innenstadt (Theaterplatz) bis 31.08.2027 begonnen?
- **Übersetzung:** „vorgesehen“ → `geplant`, 0,60. „Sommer“ meteorologisch bis 31.08.2027 (wie der Herbst-Stichtag 30.11. im Buch), Prüfung 01.09.2027. Die Sondage bis Mitte November ist zu klein für eine eigene Wette.
- **Einschätzung:** mittel. Das Wort „weiterhin“ zeigt, dass der Termin schon älter ist; gut für den Vergleich, wie lange ein Termin hält.

### Düsseldorf (3)

#### duesseldorf-2026-044? — Hochwasserschutz Himmelgeist: Deichlücke geschlossen bis Ende 2028, rund 43,5 Mio. €
- **Zitat:** „Die Baumaßnahmen werden voraussichtlich Ende 2028 abgeschlossen und kosten rund 43,5 Millionen Euro.“
- **Quelle:** https://www.duesseldorf.de/medienportal/pressedienst-einzelansicht/pld/meilenstein-in-himmelgeist-schliessung-der-deichluecke — PM vom 19.10.2026 (Stadtentwässerungsbetrieb SEBD, städtisch). SHA-256 `53f60cc2b231a2bcab708fb1c4db8a110df08aca16c2a93041062fc6f40fbfca`
- **Vorschlag Frage:** Sind die Baumaßnahmen zur Schließung der Deichlücke in Himmelgeist bis 31.12.2028 abgeschlossen? Wette b (Zahl): Kosten bei Abschluss, Stadt-Prognose 43,5 Mio. €.
- **Übersetzung:** „voraussichtlich“ → `voraussichtlich`, 0,80. Prüfung 01.01.2029.
- **Einschätzung:** stark. Großes Projekt, Betrag und Frist, betrifft rund 13.000 Menschen.

#### duesseldorf-2026-045? — Benrath, Bezirkssportanlage Karl-Hohmann-Straße: Kunstrasen fertig im 3. Quartal 2028
- **Zitat:** „Der Baubeginn ist für das erste Quartal 2028 geplant, die Fertigstellung erfolgt voraussichtlich im dritten Quartal 2028.“
- **Quelle:** https://www.duesseldorf.de/medienportal/pressedienst-einzelansicht/pld/432000-euro-foerdermittel-fuer-den-umbau-des-benrather-tennenspielfeldes — PM vom 22.10.2026. SHA-256 `b0c9171aae566e85886d4dabd175fd228e3fdcf7be28431f659183ff18176b30`
- **Vorschlag Frage:** Ist das Kunstrasenspielfeld an der Karl-Hohmann-Straße bis 30.09.2028 fertig? (Zwischenschritt: Baubeginn bis 31.03.2028.)
- **Übersetzung:** „voraussichtlich“ → `voraussichtlich`, 0,80; Baubeginn „geplant“ → `geplant`, 0,60. Prüfung 01.10.2028.
- **Einschätzung:** mittel. Klar und prüfbar, aber klein; Gegenstück zu duesseldorf-2026-043 (Windscheidstraße).

#### duesseldorf-2026-046? — Berty-Albrecht-Park, 2. Bauabschnitt: fertig bis spätes Frühjahr 2027, rund 450.000 €
- **Zitat:** „Die Arbeiten werden voraussichtlich bis ins späte Frühjahr 2027 andauern.“ (Beginn laut PM Mo 02.11.2026.)
- **Quelle:** https://www.duesseldorf.de/medienportal/pressedienst-einzelansicht/pld/berty-albrecht-park-zweiter-bauabschnitt-zur-sanierung-von-baeumen-und-wegen-startet — PM vom 20.10.2026. SHA-256 `25498306736f05b57d545e60f6253e75f3720acfde161c1ad1bea8b454d7c85c`
- **Vorschlag Frage:** Sind die Arbeiten des zweiten Bauabschnitts im Berty-Albrecht-Park bis 31.05.2027 abgeschlossen und die Wege wieder offen?
- **Übersetzung:** „voraussichtlich“, 0,80. „Spätes Frühjahr“ meteorologisch bis 31.05.2027, Prüfung 01.06.2027.
- **Einschätzung:** schwach bis mittel. Der Beleg für „fertig“ hängt an einer Abschlussmeldung oder einem Foto.

Geprüft und verworfen (Düsseldorf): Baumstandorte Dormagener Straße (166.000 €, kein Termin), Stichstraße Völklinger Straße (bis 04.12., Zufahrt eines Privatprojekts), Schubertstraße (Baustelle), Nahverkehrsplan („bis voraussichtlich 2028“, zu weich), Bombenfund Mörsenbroich (erledigt), Sanierungssprint, Wochen gegen Rassismus, Ferienprogramme und Sprechstunden (Veranstaltungen).

### Essen (1)

#### essen-2026-047? — Bochold, „Quartier der Generationen“: Zweifach-Sporthalle fertig im Oktober 2027
- **Zitat:** „Die Fertigstellung ist für Oktober 2027 vorgesehen.“ (Satz steht direkt hinter der Beschreibung der neuen Zweifach-Sporthalle.)
- **Quelle:** https://www.essen.de/meldungen/pressemeldung_1607023.de.html — PM vom 19.10.2026 („Quartier der Generationen“ in Bochold: Spatenstich für die nächste Bauphase). SHA-256 `733f577f63686f3bd0508b828cbeac542242a5e1f1fd9d1d9d8c354712cc727a`
- **Vorschlag Frage:** Ist die Zweifach-Sporthalle im „Quartier der Generationen“ in Bochold bis 31.10.2027 fertiggestellt?
- **Übersetzung:** „vorgesehen“ → `geplant`, 0,60. Prüfung 01.11.2027. Ja bei Eröffnungs- oder Übergabemeldung der Stadt oder erstem Schulsport in der Halle.
- **Einschätzung:** mittel bis stark. Klare Sache (Halle steht oder nicht), Monat als Frist.

Geprüft und verworfen (Essen): Café am Bauernhof im Grugapark (kein Termin genannt), Kreuzung Bochumer Landstraße/Sachsenring („bis voraussichtlich Anfang Dezember“, Baustelle), Tunnel Schützenbahn, Prosperstraße, Langenberger Straße, Lehmanns Brink, Stolbergstraße (Kurzbaustellen), Forschungszentrum Nano/Material „Sommer 2028“ (steht in einer Straßennamen-PM, Akteur ist die Universität), Bürgerumfrage bis 31.10. (Frist für Bürger, keine Zusage).

### Köln (1)

#### koeln-2026-094? — Venloer Straße, Tunnelportal Bickendorf: Hauptbaumaßnahme 2027 in drei KVB-Sperrfenstern
- **Zitat:** „Die Hauptbaumaßnahme wird in den Zeiten der Vollsperrungen der KVB -Strecke im Jahr 2027 wie folgt durchgeführt:“ Danach: Osterferien 22. März bis 3. April 2027, Sommerferien 19. Juli bis 31. August 2027, Herbstferien 23. Oktober bis 6. November 2027.
- **Quelle:** https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28740/index.html — PM vom 23.10.2026 („Köln-Bickendorf: Fahrbahnsanierung Venloer Straße …“). SHA-256 `fcf47c0a5392eda667f7d444afb2e1c9efd57fac390c473a2517f60251b8aa69`
- **Vorschlag Frage:** Laufen die Arbeiten am Tunnelportal Venloer Straße in den Osterferien 2027 (22.03.–03.04.2027) mit Vollsperrung der KVB-Strecke wie angekündigt?
- **Übersetzung:** „wird … durchgeführt“ → `angekuendigt`, 0,90. Prüfung 04.04.2027.
- **Einschätzung:** schwach bis mittel. Drei feste Fenster, aber der Beleg hängt an KVB-Meldungen; die Stadt ist nur ein Teil des Projekts.

Geprüft und verworfen (Köln): Severinsbrücke (steht als koeln-2026-092 im Buch), Baumpflege Kerpener Straße (bis 13.11., zu klein), Testkäufe Jugendschutz (Bilanz), Unwetterwarnung, stille Feiertage (Regeln, keine Zusage), Ausstellungen und Veranstaltungen.

### Dortmund, Nachtrag 23.10.

- **Vermerk zu dortmund-2026-026? (A45-Brücke Martener Straße):** Die Einladung zum zweiten Infoabend (22.10.) sagt: „Für den Neubau der Autobahnbrücke wird die A45 ab Frühjahr 2027 für voraussichtlich acht Monate voll gesperrt.“ Das passt zum Datum 28.04.2027 aus KW42 und gibt eine zweite Messgröße: A45 wieder frei bis Ende Dezember 2027. Bauherr bleibt die Autobahn GmbH.
- Geprüft und verworfen: „kick west“ (Drogenhilfe Rheinische Straße 111 öffnet Mo 26.10., vor einer Übernahme schon vorbei), Mengeder Straße, Siegenstraße, Herder-/Erwinstraße (bis 30.10.), Kanal Kaiserstraße (vier Tage), A40/B1 (Autobahn GmbH, bis 26.10.), YU-Festival und Ehrenamt (Veranstaltungen).

---

## Kurzbilanz KW 43

| Stadt | Kandidaten | davon Zitat geprüft |
|---|---|---|
| Köln | 1 | 1 |
| Bonn | 2 | 2 |
| Düsseldorf | 3 | 3 |
| Essen | 1 | 1 |
| Dortmund | 3 (Vorlauf 22.10.) + 1 Vermerk | 3 + 1 |

Stärkste Kandidaten: **bonn-2026-041?** (Zusatzvereinbarung am 17.12.2026 unterzeichnet, fester Tag), **duesseldorf-2026-044?** (Deichlücke Himmelgeist bis Ende 2028, 43,5 Mio. €) und **dortmund-2026-029?** (H-Bahn-Antrag Anfang 2027). Bonn hat zum ersten Mal seit KW41 wieder Kandidaten.
