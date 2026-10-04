# Buch „Wuppertal gegen Wuppertal" — Kandidaten, recherchiert am 04.10.2026

Status: **15 Wetten angelegt** (`buecher/wuppertal/wetten/wuppertal-2026-001` bis `-015`, in der Reihenfolge
wu-K01 bis wu-K15), Zweig `buch-wuppertal`, nicht gepusht. Recherche, Abruf und Wortlautprüfung: Claude,
Sonntag 04.10.2026, im Dauerlauf (Auftrag Guard weiterbauen, Felix 03.10.2026). Beim Anlegen (07:40) alle
15 Zitate in einem dritten Abruf erneut wörtlich gefunden. Für die 11 Stadt-Seiten ohne Archivkopie liegt
die Seite als lokale Kopie in `recherche/belege/2026-10-04-wuppertal-*.html`, SHA-256 als Vermerk in der
Wette. Die Freigabe (Merge, Push) trifft Felix.

**Auswahlregel:** größte NRW-Stadt ohne Buch nach Einwohnerzahl (IT.NRW). Vorhandene Bücher:
Köln, Düsseldorf, Dortmund, Essen, Duisburg, Bochum (Zweige), Bonn. Nächste Stadt: **Wuppertal**.
Quelle (übernommen aus `docs/2026-10-04-buch-bochum-KANDIDATEN.md`, Zweig `buch-bochum`): IT.NRW,
Statistische Berichte „Bevölkerung der Gemeinden Nordrhein-Westfalens am 30. Juni 2025"
(Artikel-Nr. A123 2025 21), https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/NWHeft_derivate_00022899/a123202521.pdf:
Bochum 358 426, **Wuppertal 357 900**, Bielefeld 330 825. Die Bochum-Datei hält schon fest: „Beim
nächsten Buch nach dieser Regel ist Wuppertal dran." Hier nicht neu abgerufen.

**Methode:** Die Pressemitteilungen der Stadt wurden am 04.10.2026 über die Listenansicht
(`/presse/aktuelle-meldungen.php`) und die Monatsarchive Januar–September 2026
(`/rathaus-buergerservice/verwaltung/pressebereich/archiv_monate_jahr/<monat>-2026.php`) vollständig
erfasst: 589 Mitteilungen, alle per Python (`urllib`, Browser-Kopfzeilen; wuppertal.de antwortet ohne
`Sec-Fetch-*`-Kopfzeilen mit HTTP 403) abgerufen, HTML-Tags entfernt, Entities aufgelöst, Leerraum
vereinheitlicht und nach Zukunftsterminen durchsucht. Ebenso alle 128 WSW-Pressemitteilungen 2026
(`wsw-online.de/ueber-uns/presse/pressemitteilungen/`, Filter Jahr 2026). Lokalpresse nur für das Pina
Bausch Zentrum (talzeit, wuppertal-total), weil die Stadt dazu seit der verschobenen Ratsentscheidung
keine eigene Mitteilung hat. Die Zitate unten sind aus diesem Text kopiert. Ein Prüfskript hat jedes
Zitat (Teile zwischen „…") gegen einen **zweiten, frischen Abruf** geprüft: **15 von 15 stehen
wörtlich im Live-Text.**

**Vorbehalt-Spalte:** „voraussichtlich" (0,80), wenn der Satz „soll", „geplant", „vorgesehen",
„voraussichtlich", „derzeit", „angestrebt", „beabsichtigt", „rechnet mit" oder einen Bedingungssatz
enthält; sonst „angekuendigt" (1,00), wie in FORMAT.md §1.2.

**Wayback:** Für jede Quell-URL wurde am 04.10.2026 einmal `https://web.archive.org/save/<URL>`
ausgelöst (15 s Pause), danach die Availability-API (`…&timestamp=20261004`) abgefragt und die
Archivkopie (`id_`-Variante) auf den Wortlaut geprüft. Ergebnis unten unter „Archivbefund".

---

## wu-K01 — Spielplatz Werther Hof: offizielle Eröffnung am 08.10.2026

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/oktober/spielplatz-werther-hof.php
- **gesagt_am:** 01.10.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal (Ressort Grünflächen und Forsten mit Jugendamt), Mitteilungstext
- **Zitat:** „Der Kinderspielplatz Werther Hof ist frisch saniert." … „Am Donnerstag, 8. Oktober, wird er
  offiziell eröffnet."
- **Vorbehalt:** angekuendigt (1,00)
- **Frage:** Wird der Kinderspielplatz Werther Hof (Barmen) am 08.10.2026 offiziell eröffnet?
- **Stichtag:** 08.10.2026 · **Prüfdatum:** 09.10.2026 (früheste Auflösung im Buch)
- **Beleg später:** Pressemitteilung/Social Media der Stadt, WZ, talzeit, Radio Wuppertal.
- **Wahrscheinlichkeit Computer: 0,92.** Bau laut Mitteilung schon fertig (Ende März bis Ende September),
  der Termin liegt eine Woche nach der Ankündigung. Rest-Risiko: Unwetter, Absage, keine Meldung.
  Leichter Kandidat — als Eichwette fürs Buch brauchbar, aussagearm.

## wu-K02 — Brunnen Alte Freiheit (Elberfeld): fertig Anfang Oktober 2026

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/august/brunnen-elberfeld.php
- **gesagt_am:** 07.08.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal, Mitteilungstext
- **Zitat:** „Die Fertigstellung des Brunnens ist Anfang Oktober geplant."
- **Vorbehalt:** voraussichtlich („geplant")
- **Frage:** Ist der neue Brunnen an der Alten Freiheit bis einschließlich 10.10.2026 fertiggestellt
  (in Betrieb oder als fertig gemeldet)?
- **Stichtag:** 10.10.2026 („Anfang Oktober" = 1.–10.) · **Prüfdatum:** 11.10.2026
- **Beleg später:** Pressemitteilung der Stadt, Lokalpresse, Foto mit Datum. Ohne Beleg bis zum Prüftag: Nein.
- **Wahrscheinlichkeit Computer: 0,35.** Seit August keine weitere Meldung gefunden (ungeklärt, ob
  verzögert); Pflasterarbeiten in der Innenstadt rutschen oft, und „fertig" wird bei kleinen Bauten selten
  gemeldet.

## wu-K03 — Brücke Fischertal: Baumaßnahme bis Ende Oktober 2026 abgeschlossen

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/september/verzoegerung-fischertal.php
- **gesagt_am:** 10.09.2026 (Pressemitteilung „Bauarbeiten an der Brücke Fischertal verzögern sich bis
  Ende Oktober")
- **Wer:** Stadt Wuppertal (Verwaltung); Leitungsarbeiten durch die WSW
- **Zitat:** „Dennoch verzögert sich die Fertigstellung der Gesamtmaßnahme voraussichtlich bis Ende
  Oktober 2026." … „Die Verwaltung rechnet aus diesem Grund nun mit dem Abschluss der gesamten Baumaßnahme
  bis Ende Oktober 2026."
- **Vorbehalt:** voraussichtlich
- **Frage:** Ist die Baumaßnahme an der Brücke Fischertal bis zum 31.10.2026 abgeschlossen und die Brücke
  wieder für den Verkehr freigegeben?
- **Stichtag:** 31.10.2026 · **Prüfdatum:** 01.11.2026
- **Beleg später:** Freigabemeldung der Stadt, WSW-Meldung zur Rückkehr der Buslinie 644 auf den
  Linienweg, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,45.** Der Termin ist schon einmal gerutscht, hängt an einer
  Zulieferkette (Leitungsbau, dann Verfüllen, dann Restarbeiten). Unklar, wie viel Puffer drin ist.

## wu-K04 — WSW: Bergische Kooperation (Solingen/Remscheid/Wuppertal) im Oktober 2026 notariell gegründet

- **URL:** https://www.wsw-online.de/ueber-uns/presse/pressemitteilungen/pressemeldung/meldung/stadtwerke-buendeln-kraefte-fuer-erneuerbare-energien-projekte/
- **gesagt_am:** 20.07.2026 (Pressemitteilung WSW, gemeinsam mit den Stadtwerken Solingen und Remscheid)
- **Wer:** WSW Wuppertaler Stadtwerke (städtische Tochter), Mitteilungstext
- **Zitat:** „Die Räte der drei Städte haben der Gründung zugestimmt; vorbehaltlich der Genehmigung durch
  die Kommunalaufsicht ist die notarielle Gründung zum Oktober 2026 vorgesehen."
- **Vorbehalt:** voraussichtlich („vorbehaltlich", „vorgesehen")
- **Frage:** Wird die gemeinsame Gesellschaft der Stadtwerke Solingen, Remscheid und Wuppertal bis zum
  31.10.2026 notariell gegründet?
- **Stichtag:** 31.10.2026 · **Prüfdatum:** 01.11.2026
- **Beleg später:** Meldung der Stadtwerke; Handelsregister (Eintragung kann nach der notariellen Gründung
  folgen — die Wette fragt nach der Gründung, nicht nach der Eintragung; Gründungsdatum laut
  Registerbekanntmachung oder Meldung). Name der Gesellschaft: ungeklärt.
- **Wahrscheinlichkeit Computer: 0,45.** Ratsbeschlüsse liegen vor; Kommunalaufsicht bei drei Städten
  plus Notartermin in einem Monat ist knapp. Schwer belegbar, falls niemand die Gründung meldet.

## wu-K05 — Gartenhallenbad Cronenberg: geschlossen bis 15.11., ab 16.11.2026 wieder offen

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/september/baeder-oeffnungszeiten.php
- **gesagt_am:** 28.09.2026 (Pressemitteilung Sport- und Bäderamt)
- **Wer:** Stadt Wuppertal (Sport- und Bäderamt)
- **Zitat:** „Mit dem Feiertag beginnen im Gartenhallenbad Cronenberg zudem notwendige Wartungs- und
  Instandsetzungsarbeiten." … „Das Bad bleibt daher vom 3. Oktober bis 15. November geschlossen."
- **Vorbehalt:** angekuendigt (1,00)
- **Frage:** Ist das Gartenhallenbad Cronenberg am Montag, 16.11.2026, wieder für den Badebetrieb geöffnet?
- **Stichtag:** 16.11.2026 · **Prüfdatum:** 17.11.2026
- **Beleg später:** Bäderseite wuppertal.de/baeder (Wayback-Kopie vom 16./17.11.), Pressemitteilung zu
  Öffnungszeiten oder Verlängerung der Schließung.
- **Wahrscheinlichkeit Computer: 0,70.** Wartungsschließungen halten meist; Risiken sind Befunde bei der
  Instandsetzung und Personalmangel (im August war das Bad schon wegen Personal zu). Montag als erster Tag
  kann auch an einem regulären Schließtag hängen — dann gilt der erste reguläre Öffnungstag der Woche
  (in der Wette festschreiben).

## wu-K06 — Stadtbad Uellendahl: Kosten-Vorlage im Rat im November 2026

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/september/stadtbad-uellendahl-sanierung.php
- **gesagt_am:** 17.09.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal (Verwaltung)
- **Zitat:** „Zurzeit konkretisiert sich das Aufgabenvolumen gegenüber der damaligen Planung, sodass für die
  November-Sitzung des Rates beabsichtigt wird, eine Vorlage zur Kostenneufestsetzung einzubringen."
- **Vorbehalt:** voraussichtlich („beabsichtigt")
- **Frage:** Steht in der Sitzung des Rates der Stadt Wuppertal im November 2026 eine Vorlage zur
  Kostenneufestsetzung für die Sanierung des Stadtbads Uellendahl auf der Tagesordnung?
- **Stichtag:** 30.11.2026 · **Prüfdatum:** 01.12.2026
- **Beleg später:** Ratsinformationssystem (Tagesordnung der Novembersitzung; Termin der Sitzung ungeklärt).
- **Wahrscheinlichkeit Computer: 0,65.** Verwaltungsinterner Schritt, gut steuerbar; Risiko, dass die
  Vorlage erst in den Dezember-Rat geht oder nur in den Fachausschüssen läuft.

## wu-K07 — Spielplatz Ludgerweg: Freigabe im Herbst 2026

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/august/spielplatz-ludgerweg.php
- **gesagt_am:** 10.08.2026 (Pressemitteilung, zitiert Beigeordneten Gunnar Ohrndorf; Terminsatz ist
  Mitteilungstext)
- **Wer:** Stadt Wuppertal; Erschließung durch den Investor BEMA
- **Zitat:** „Doch die Stadt kann den neuen Spielplatz noch nicht freigeben:" … „Nach aktuellem Stand soll
  der Spielplatz im kommenden Herbst freigegeben werden können."
- **Vorbehalt:** voraussichtlich („soll", „nach aktuellem Stand")
- **Frage:** Gibt die Stadt den Spielplatz am Ludgerweg bis zum 20.12.2026 (Ende des kalendarischen Herbstes)
  für die Öffentlichkeit frei?
- **Stichtag:** 20.12.2026 · **Prüfdatum:** 21.12.2026
- **Beleg später:** Pressemitteilung der Stadt, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,45.** Hängt an Straßen, Entwässerung und Abnahme eines privaten
  Erschließungsträgers — die Stadt steuert das nicht selbst. Ob „kommender Herbst" 2026 meint, ist aus dem
  August-Datum klar, aber „Herbst" ist weit.

## wu-K08 — Pina Bausch Zentrum: drei Bauvarianten bis Jahresende 2026

- **URL:** https://www.talzeit.de/lokales/wuppertal/article413283190/pina-bausch-zentrum-kostet-228-millionen-wuppertal-fehlen-67-millionen-euro.html
- **gesagt_am:** 28.09.2026 in der Ratssitzung, berichtet von talzeit am 29.09.2026 (Niklas Berkel)
- **Wer:** Stadt Wuppertal, Kulturdezernent Dr. Hagen Lippe-Weißenfeld, wiedergegeben von talzeit
  (Bezahlartikel; der zitierte Satz steht im frei abrufbaren Teil). Eine Mitteilung der Stadt dazu wurde
  nicht gefunden.
- **Zitat:** „Kulturdezernent Hagen Lippe-Weißenfeld kündigte im Rat an, noch vor Ende des Jahres drei
  alternative Bauvarianten vorzulegen."
- **Vorbehalt:** angekuendigt (1,00; „kündigte an", ohne Einschränkung im wiedergegebenen Satz)
- **Frage:** Legt die Verwaltung dem Rat oder einem Ratsausschuss bis zum 31.12.2026 drei (mindestens zwei)
  alternative Bauvarianten für das Pina Bausch Zentrum vor? — Vorschlag: streng „drei" nehmen, damit die
  Frage eindeutig ist.
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** Ratsinformationssystem (Vorlage/Bericht), Pressemitteilung, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,55.** Politischer Druck ist hoch (SPD: Rat muss noch 2026 entscheiden),
  Bundesförderung hängt an Fristen; aber Kosten (228 statt 161 Mio. €), neuer Kämmerer ab November und
  das Ziel „drei Varianten, durchgerechnet" in drei Monaten sind viel.
- **Kontext:** Die für den 28.09.2026 geplante Grundsatzentscheidung des Rates wurde verschoben (talzeit,
  wuppertal-total). Die Stadt hatte im Februar noch „nach einem positiven Ratsbeschluss im September"
  geschrieben (PM 17.02.2026).

## wu-K09 — Spielplatz am Murmelbach: fertig Ende Dezember 2026

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/september/ksp-murmelbach.php
- **gesagt_am:** 15.09.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal
- **Zitat:** „Bis Ende Dezember entsteht eine moderne, barrierearme Piraten-Spiellandschaft mit Seilbahn und
  Schaukeln direkt am Murmelbachteich." … „Wenn das Wetter mitspielt, schließt die Stadt die Arbeiten Ende
  Dezember ab und übergibt die Anlage wieder an die Familien im Stadtteil."
- **Vorbehalt:** voraussichtlich (Bedingungssatz „Wenn das Wetter mitspielt")
- **Frage:** Ist der neu gestaltete Kinderspielplatz am Murmelbach (Heckinghausen) bis zum 31.12.2026
  fertig und wieder freigegeben?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** Pressemitteilung der Stadt (die Stadt meldet Spielplatz-Eröffnungen regelmäßig).
- **Wahrscheinlichkeit Computer: 0,35.** Bauzeit Mitte September bis Dezember, Winterwetter ausdrücklich als
  Risiko genannt; der Spielplatz Ludgerweg ist 2026 schon über seinen Termin gerutscht (K07).

## wu-K10 — Schwebebahn-Haltestelle Alter Markt: neues Dach bis Ende 2026 (WSW)

- **URL:** https://www.wsw-online.de/ueber-uns/presse/pressemitteilungen/pressemeldung/meldung/umbau-haltestelle-alter-markt-arbeiten-wechseln-auf-den-bahnsteig-richtung-vohwinkel/
- **gesagt_am:** 17.07.2026 (Pressemitteilung WSW; gleicher Satz schon am 01.06. und 24.06.2026)
- **Wer:** WSW mobil / WSW Wuppertaler Stadtwerke (städtische Tochter), Mitteilungstext
- **Zitat:** „Voraussichtlich ab Anfang August wird der Rückbau des bestehenden Daches beginnen." … „Die
  Fertigstellung des neuen Dachs ist weiterhin bis Ende 2026 geplant."
- **Vorbehalt:** voraussichtlich („geplant")
- **Frage:** Ist das neue Dach der Schwebebahn-Haltestelle Alter Markt bis zum 31.12.2026 fertiggestellt?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** WSW-Pressemitteilung, Lokalpresse, Foto. Ohne Meldung bis zum Prüftag: Nein.
- **Wahrscheinlichkeit Computer: 0,50.** Arbeiten über dem Fahrprofil nur nachts, Wintermontage; die WSW
  hielten den Termin im Juli „weiterhin" — ob es seit Juli eine Verzögerung gab, ist ungeklärt.

## wu-K11 — Zoosäle: Investorenverfahren Ende 2026 neu geöffnet

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/august/zoosaele.php
- **gesagt_am:** 31.08.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal
- **Zitat:** „Das Verfahren soll nun marktgängiger gestaltet werden:" … „Es wird angestrebt, das Verfahren
  Ende dieses Jahres fortzuführen und noch einmal für Investoren zu öffnen."
- **Vorbehalt:** voraussichtlich („soll", „angestrebt")
- **Frage:** Öffnet die Stadt das Investorenverfahren für die Zoosäle bis zum 31.12.2026 erneut (neue
  Ausschreibung/Interessenbekundung veröffentlicht)?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027
- **Beleg später:** Pressemitteilung, Grundstücksangebote auf wuppertal.de, polis-Marktplatz, ImmoScout24.
- **Wahrscheinlichkeit Computer: 0,35.** Vorgaben (Erbbaurecht, Denkmal, BUGA) müssen erst geändert und
  vermutlich politisch beschlossen werden; „Ende des Jahres" rutscht bei so etwas leicht ins Frühjahr.

## wu-K12 — Stadtplätze Vohwinkel: Wettbewerbsergebnisse Ende 2026 mit Ausstellung

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/mai/stadtpleaetze-vohwinkel.php
- **gesagt_am:** 22.05.2026 (Pressemitteilung, Dezernent Gunnar Ohrndorf zitiert; Terminsatz ist
  Mitteilungstext)
- **Wer:** Stadt Wuppertal
- **Zitat:** „Die Wettbewerbsergebnisse sollen Ende des Jahres vorliegen und in einer öffentlichen
  Ausstellung zu sehen sein."
- **Vorbehalt:** voraussichtlich („sollen")
- **Frage:** Liegt bis zum 31.12.2026 das Ergebnis (Preisgericht/Siegerentwurf) des Wettbewerbs für
  Lienhardplatz und Stationsgarten öffentlich vor?
- **Stichtag:** 31.12.2026 · **Prüfdatum:** 01.01.2027 (Ausstellung bewusst nicht Teil der Frage, weil sie
  auch im Januar liegen kann)
- **Beleg später:** Pressemitteilung, talbeteiligung.de, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,55.** Wettbewerbe mit Preisgericht laufen meist planbar; Entwurfsphase
  war für den Sommer angesetzt. Risiko: Preisgericht im Januar.

## wu-K13 — Deweerth'scher Garten: Wiedereröffnung im Frühjahr 2027

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/april/spatenstich-deweerth-scher-garten.php
- **gesagt_am:** 13.04.2026 (Pressemitteilung zum Spatenstich)
- **Wer:** Stadt Wuppertal (Mitteilungstext; OB Scherff und Dezernentin Linthorst zitiert)
- **Zitat:** „Im Moment ist die Anlage für Besucher geschlossen, wieder öffnen soll sie im Frühjahr 2027."
- **Vorbehalt:** voraussichtlich („soll")
- **Frage:** Ist der umgestaltete Deweerth'sche Garten bis zum 31.05.2027 wieder für Besucher geöffnet?
- **Stichtag:** 31.05.2027 (Ende des meteorologischen Frühjahrs) · **Prüfdatum:** 01.06.2027
- **Beleg später:** Eröffnungsmeldung der Stadt, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,40.** Projekt war schon von 2023 verschoben (Tiefgarage); im Oktober und
  November 2026 laufen dort zusätzlich archäologische Untersuchungen (PM 24.09.2026).

## wu-K14 — Grundschule Am Dönberg: Neubau nach den Sommerferien 2027 in Betrieb

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/august/gs-am-doenberg.php
- **gesagt_am:** 03.08.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal / Gebäudemanagement Wuppertal (GMW)
- **Zitat:** „Die bisher einzügige Grundschule Am Dönberg erhält einen Neubau." … „Mit der Inbetriebnahme
  des Neubaus wird nach den Sommerferien 2027 gerechnet."
- **Vorbehalt:** voraussichtlich („wird gerechnet")
- **Frage:** Ist der Neubau der Grundschule Am Dönberg bis zum 30.09.2027 in Betrieb?
- **Stichtag:** 30.09.2027 (Ende der NRW-Sommerferien 2027 nicht geprüft, ungeklärt; Puffer) ·
  **Prüfdatum:** 01.10.2027
- **Beleg später:** Pressemitteilung (Übergabe), Schulhomepage, Lokalpresse.
- **Wahrscheinlichkeit Computer: 0,55.** Holzsystembau mit Totalunternehmer, Baugenehmigung lag vor; rund ein
  Jahr Bauzeit ist für so einen Bau realistisch, aber eng.

## wu-K15 — Alte Zoobrücke: Sanierung Ende 2027 abgeschlossen

- **URL:** https://www.wuppertal.de/presse/meldungen/meldungen-2026/juni/sanierung-zoobruecke-beginnt.php
- **gesagt_am:** 05.06.2026 (Pressemitteilung)
- **Wer:** Stadt Wuppertal
- **Zitat:** „Die Brücke wird komplett saniert." … „Die Sanierungsarbeiten sollen Ende 2027 abgeschlossen
  sein."
- **Vorbehalt:** voraussichtlich („sollen")
- **Frage:** Ist die Sanierung der Alten Zoobrücke bis zum 31.12.2027 abgeschlossen?
- **Stichtag:** 31.12.2027 · **Prüfdatum:** 01.01.2028
- **Beleg später:** Abschluss-/Freigabemeldung der Stadt.
- **Wahrscheinlichkeit Computer: 0,40.** Stahlbrücken-Sanierung mit Einhausung und Trägertausch; Schäden
  zeigen sich oft erst nach dem Öffnen. Wuppertaler Brückenbaustellen 2026 (Waldeckstraße, Fischertal) sind
  gerutscht.

---

## Zusammenfassung

| ID | Thema | Stichtag | Prüfdatum | Stadt | Computer | live wörtlich |
|---|---|---|---|---|---|---|
| wu-K01 | Spielplatz Werther Hof eröffnet | 08.10.2026 | 09.10.2026 | 1,00 | 0,92 | ja |
| wu-K02 | Brunnen Alte Freiheit fertig | 10.10.2026 | 11.10.2026 | 0,80 | 0,35 | ja |
| wu-K03 | Brücke Fischertal fertig | 31.10.2026 | 01.11.2026 | 0,80 | 0,45 | ja |
| wu-K04 | WSW-Kooperation gegründet | 31.10.2026 | 01.11.2026 | 0,80 | 0,45 | ja |
| wu-K05 | Gartenhallenbad Cronenberg wieder offen | 16.11.2026 | 17.11.2026 | 1,00 | 0,70 | ja |
| wu-K06 | Uellendahl-Kostenvorlage im Nov.-Rat | 30.11.2026 | 01.12.2026 | 0,80 | 0,65 | ja |
| wu-K07 | Spielplatz Ludgerweg frei | 20.12.2026 | 21.12.2026 | 0,80 | 0,45 | ja |
| wu-K08 | PBZ: drei Bauvarianten | 31.12.2026 | 01.01.2027 | 1,00 | 0,55 | ja |
| wu-K09 | Spielplatz Murmelbach fertig | 31.12.2026 | 01.01.2027 | 0,80 | 0,35 | ja |
| wu-K10 | Dach Alter Markt fertig | 31.12.2026 | 01.01.2027 | 0,80 | 0,50 | ja |
| wu-K11 | Zoosäle-Verfahren neu offen | 31.12.2026 | 01.01.2027 | 0,80 | 0,35 | ja |
| wu-K12 | Wettbewerb Vohwinkel entschieden | 31.12.2026 | 01.01.2027 | 0,80 | 0,55 | ja |
| wu-K13 | Deweerth'scher Garten offen | 31.05.2027 | 01.06.2027 | 0,80 | 0,40 | ja |
| wu-K14 | GS Am Dönberg Neubau in Betrieb | 30.09.2027 | 01.10.2027 | 0,80 | 0,55 | ja |
| wu-K15 | Alte Zoobrücke saniert | 31.12.2027 | 01.01.2028 | 0,80 | 0,40 | ja |

Mischung: Verkehr/Brücken (K03, K10, K15), Grün/Spielplätze (K01, K02, K07, K09, K13), Bäder/Schule (K05,
K06, K14), Kultur/Stadtentwicklung (K08, K11, K12), Energie (K04). Schwäche: viele kleine Projekte;
Großprojekte (BUGA 2031, PBZ-Bau, Schulneubauten) haben ihre Termine erst 2028–2031.

---

## Verworfen

- **Haushalt 2027:** Wuppertal hat einen **Doppelhaushalt 2026/2027**; die Bezirksregierung hat ihn
  genehmigt (PM 28.07.2026 „Genehmigung des Haushalts sichert Handlungsfähigkeit"). Kein Ratsbeschluss zu
  2027 mehr offen. Ein Haushalt 2028(/29) wurde in den Mitteilungen nicht terminiert.
- **PBZ, Leistungsphase 4 „zum 30. November dieses Jahres abgeschlossen"** (PM 07.07.2026): von außen kaum
  belegbar; außerdem durch die verschobene Ratsentscheidung überholt. Ersetzt durch K08.
- **PBZ, Ratsbeschluss Gesamtprojekt „Ende September 2026"** (PM 07.07.2026) und „nach einem positiven
  Ratsbeschluss im September" (PM 17.02.2026): Termin verstrichen, Entscheidung verschoben (talzeit 29.09.2026).
- **Stadtbad Uellendahl, „Ab dem 19. Oktober 2026 muss das Bad … geschlossen werden"** (PM 17.09.2026):
  Schließung liegt allein in der Hand der Stadt, aussagearm. **„Im zweiten Quartal 2028 soll die umfangreiche
  Maßnahme beendet sein"**: brauchbar (Stichtag 30.06.2028), aber zu fern für die erste Runde.
- **Spielplatz Rabenweg, „voraussichtlich Anfang Oktober beendet"** (PM 27.05.2026): sehr klein, Fertigmeldung
  unwahrscheinlich; Platz geht an K02.
- **Spielplatz Meckelstraße, „Die Arbeiten sollen im Winter abgeschlossen werden"** (PM 25.09.2026): „Winter"
  reicht bis März 2027, zu unscharf neben K09.
- **Brücke Waldeckstraße, „wie geplant im Herbst 2026 abgeschlossen"** (PM 25.03.2026): seit April keine
  Terminaussage mehr gefunden; Stand ungeklärt. Kandidat für eine Nachrecherche.
- **Stadtteilzentrum Beyenburg, Abschluss „voraussichtlich im März des kommenden Jahres"** (PM 23.06.2026):
  brauchbar (Stichtag 31.03.2027), aber „mit den letzten technischen Abnahmen durch den TÜV" ist von außen
  kaum zu belegen; Wiedereröffnung der Bibliothek wäre die bessere Frage, dazu fehlt eine Aussage.
- **Gymnasium Siegesstraße, Rohbau „Ende des Jahres" — „Falls das Vergabeverfahren erfolgreich verläuft,
  könnten …"** (PM 03.09.2026): Konjunktiv, keine Zusage.
- **Hauptbahnhof/Döppersberg, „vollständige Fertigstellung … bis Mitte des kommenden Jahres"** (PM 02.09.2026):
  Aussage des privaten Investors Markus Bürger, nicht der Stadt.
- **WSW-Kundencenter Hauptbahnhof „im Herbst"** (WSW 10.02.2026): Eröffnung möglicherweise schon erfolgt
  (ungeklärt), „Herbst" unscharf.
- **WSW Kaiserwagen, Hochzeiten „voraussichtlich wieder ab Januar 2027"** (WSW 05.05.2026): kaum auflösbar
  (ab wann buchbar? erste Trauung?).
- **WSW Batteriepark, Inbetriebnahme „zweite Jahreshälfte 2028"** (WSW 22.09.2026), **Wuppersammler Baulos 2
  „Ende 2027"** (WSW 21.01.2026), **Zollstraße gesperrt „bis Ende Mai 2027"** (WSW 02.10.2026): zu fern bzw.
  Leitungsbaustelle ohne Abschlussmeldung.
- **Südsteg Hauptbahnhof „Ende 2027"** (PM 24.02.2026): Aussage der Deutschen Bahn, nicht der Stadt.
- **BUGA 2031, „Baustart … für das Jahr 2028 vorgesehen"** (PM 20.07.2026), **Seilbahn „ab 2031"**: zu fern;
  BUGA-Meilensteine 2026/27 mit prüfbarem Datum wurden nicht gefunden.
- **Stadthalle Fassade 1. Bauabschnitt „Frühjahr 2028"**, **Schule Hammesberger Weg „zweites Quartal 2028"**,
  **Turnhalle Hardt Umkleidegebäude „ab Herbst 2027"**, **Realschule Vohwinkel „drittes Quartal 2028"**
  („Zuletzt ging die Stadt … aus" — bereits überholt), **7. Gesamtschule „Schuljahr 2029/2030"**: zu fern für
  diese Runde; Hardt und Hammesberger Weg wären Nachrücker.
- **Mobilfunk-Messreihe „noch vor Jahresende"** (PM 14.09.2026): Ausgang von außen kaum prüfbar.
- **Termine von Veranstaltungen** (Ursula-Lietz-Weg-Einweihung 15.10., Jugendbudget-Abschluss 05.11.,
  Weihnachtscircus 30.12.): aussagearm.

---

## Archivbefund (04.10.2026)

**Ergebnis: 15 von 15 Zitaten stehen live wörtlich (zweiter Abruf), aber nur 4 von 15 tragen im Archiv**
(K04, K08, K10, K13). Grund: Save Page Now bekommt von **wuppertal.de durchgehend HTTP 520** (die Stadt-Seite
liegt hinter Cloudflare und weist offenbar den Archiv-Crawler ab; ohne Browser-Kopfzeilen antwortet sie auch uns
mit 403). Die einzige neue Kopie einer Stadt-Seite (K03) enthält nur die Sperrseite. wsw-online.de und talzeit
ließen sich sichern. Die Availability-API (`timestamp=20261004`) lieferte am 04.10.2026 für **alle** URLs
noch `null`, auch für die frisch gesicherten; die Zeitstempel unten stammen deshalb aus der CDX-API
(`web.archive.org/cdx/search/cdx`). Wortlaut im Archiv geprüft über `https://web.archive.org/web/<ts>id_/<URL>`
(gzip entpackt, Tags entfernt, Leerraum normalisiert), wegen HTTP 429 mit Pausen und Wiederholung.

| Kandidat | live wörtlich | Wayback-Zeitstempel | Save | Archiv |
|---|---|---|---|---|
| wu-K01 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K02 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K03 | ja | 20261004045918 (CDX-Status 204; `id_`-Abruf: HTTP 403) | Save fehlgeschlagen (HTTP 520) | trägt nicht |
| wu-K04 | ja | 20261004045944 | Save HTTP 429, Kopie trotzdem angelegt | trägt |
| wu-K05 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K06 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K07 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K08 | ja | 20261004050136 | Save HTTP 429, Kopie trotzdem angelegt | trägt |
| wu-K09 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K10 | ja | 20261004050342 | Save HTTP 200 | trägt |
| wu-K11 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K12 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K13 | ja | 20260414132150 (ältere Kopie, Tag nach der Mitteilung) | Save fehlgeschlagen (HTTP 520) | trägt |
| wu-K14 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |
| wu-K15 | ja | keiner | Save fehlgeschlagen (HTTP 520) | — |

**Folge für das Anlegen:** FORMAT.md §1.3 verlangt nur eine öffentlich erreichbare Quelle, Archiv ist
„empfohlen". Für die 11 Stadt-Seiten ohne Kopie braucht es einen anderen Weg, bevor Wetten angelegt werden:
erneuter Save-Versuch später, archive.today (`archive.ph`), oder eine lokale Kopie mit Hash (Rohtext liegt
aus diesem Lauf nur in `%TEMP%\wup\pm\`, nicht im Repo). Ungeklärt, ob die 520 dauerhaft ist.
