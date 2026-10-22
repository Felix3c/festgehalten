# Ankündigungen KW 43 — Kandidaten für neue Wetten (Köln, Bonn, Düsseldorf, Essen, Dortmund)

**Zweck:** Wöchentliche Sammlung datierter, prüfbarer Ankündigungen der fünf Städte aus den eigenen Pressemitteilungen, als Vorrat für neue Wetten.
**Stand:** Vorlauf Do 22.10.2026 ~23:55 (Dauerlauf, Guard Laufend), nur **Dortmund**, Fenster 17.10.–22.10.2026. Köln, Bonn, Düsseldorf, Essen und der Rest von Dortmund (23.–25.10.) folgen im Wochenlauf So 25.10.
**Status:** ENTWURF. Nichts davon steht im Buch. Übernahme nur nach Felix' „steht“. IDs mit „?“ sind Vorschläge.

**Nächste freie Nummer Dortmund:** dortmund-2026-029 (027 im Buch, 028? liegt noch als KW42-Vorschlag).

**Methode:** Wie KW42. Dortmund über die Such-Schnittstelle des Newsrooms (`/api/search/proxy/search`, POST, Index `NEW_SITE`): Typ „messagepublication“ mit `releaseDate ≥ 17.10.` (30 Treffer) und Typ „news“ mit `stateDate ≥ 17.10.` (15 Treffer), neueste vom 22.10. 15:02. Die Listenseite `/newsroom/presse-mitteilungen/` gab am 22.10. ~23:45 per curl HTTP 403; Einzelseiten per Python urllib gingen (HTTP 200). robots.txt erlaubt alles.
- Jedes Zitat unten per Skript gegen den abgerufenen Seitentext geprüft (Gleichheit nach Leerzeichen-Normalisierung), 5 von 5 bestanden. Skripte und Rohabrufe: `C:\Users\skyla\allein\tmp\kw43-guard\`.
- SHA-256 = Fingerabdruck der lokalen Rohkopie (Abruf 22.10.2026 ~23:45).
- **Archiv:** Save Page Now am 22.10. ~23:55 für alle vier Seiten HTTP 520 (Archiv drosselt seit dem Abend). Bei Übernahme nachholen.
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
