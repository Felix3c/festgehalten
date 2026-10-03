# Buch „Bund“: Kandidaten (Recherche 03.10.2026)

Das hier ist eine Arbeitsliste und noch kein Bucheintrag. Recherchiert hat Claude im Auftrag des Halters am Sa 03.10.2026.
Die Felder folgen FORMAT.md §1.1/1.2. Erlaubte Werte für `art` sind laut FORMAT.md `angekuendigt` (Wert 1,00 bzw. bei
`punkt` die genannte Zahl), `voraussichtlich` (Wert 0,80 bei `ja_nein`) und `geschaetzt` (nur für Schätzende). Den
Begriff „zugesagt“ aus dem Auftrag gibt es im Format nicht. Gemeint ist `angekuendigt`.

**Prüfmethode Wortlaut (für alle Kandidaten gleich):** Die Seite wurde am 03.10.2026 per `curl -sL --compressed` (Browser-User-Agent) abgerufen.
Danach wurden alle HTML-Tags durch Leerzeichen ersetzt, HTML-Entities aufgelöst, Whitespace zusammengefasst und
Anführungszeichen, Bindestriche, geschützte Leerzeichen sowie Soft-Hyphens normalisiert. Geprüft wurde dann `zitat in text` mit Ergebnis `True`
(Skript `/tmp/bund/chk.py`, liegt nicht im Repo). Ein Sonderfall sind Abkürzungen in `<abbr>`-Tags („BIP“, „Kfz“): Dort ergibt
die Tag-Ersetzung „BIP -Zuwachs“. Laut Roh-HTML steht auf der Seite `<abbr …>BIP</abbr>-Zuwachs`, sichtbar also
„BIP-Zuwachs“, und so wird zitiert.

Vorgeschlagene IDs: `bund-2026-001` … `-012`. Vorgeschlagene Institution: `Bundesregierung` (Bundesrepublik
Deutschland).

---

## bund-2026-001 · Haushalt: Nettokreditaufnahme 2027

- **gesagt_von:** Bundesministerium der Finanzen (Bundesfinanzminister Lars Klingbeil, Pressekonferenz zum Regierungsentwurf)
- **gesagt_am:** 2026-07-06
- **quelle:** https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Video-Textfassungen/2026/textfassung-2026-07-06-bundeshaushalt-2027.html
- **zitat:** „Die Nettokreditaufnahme im Bundeshaushalt wird im Jahr 2027 bei 119 Milliarden Euro voraussichtlich liegen.“
- **Wortlaut geprüft:** ja, beim **ersten** curl-Abruf am 03.10.2026 wörtlich im Text gefunden (Kontextauszug liegt
  vor). Alle späteren Abrufe (curl und WebFetch) liefen in eine Radware-Bot-Sperre (Captcha). Im Browser ist die Seite normal erreichbar.
  **Vor dem Eintragen bitte einmal im Browser gegenprüfen und einen Wayback-Link anlegen.** Die
  Pressemitteilung des BMF vom selben Tag (`…/Pressemitteilungen/Finanzpolitik/2026/07/2026-07-06-regierungsentwurf-bundeshaushalt-2027.html`)
  war durchgehend gesperrt und konnte nicht geprüft werden.
- **frage:** Weist das vom Bundestag bis zum 31.12.2026 beschlossene Haushaltsgesetz 2027 für den Kernhaushalt eine Nettokreditaufnahme von höchstens 119,0 Mrd. Euro aus?
- **typ:** ja_nein · **pruefung_am:** 2027-01-01
- **art (Bund):** `voraussichtlich` (das Zitat sagt selbst „voraussichtlich“) → **wert 0,80**
- **Übersetzung:** Gemessen wird die im beschlossenen Haushaltsgesetz ausgewiesene Nettokreditaufnahme des Kernhaushalts, ohne Sondervermögen.
  Ist bis 31.12.2026 kein Haushalt beschlossen, ist die Antwort Nein. Die Ist-Zahl 2027 bleibt außen vor, sie wäre eine eigene Wette mit
  Prüfung 2028.
- **Kontext:** Laut hib-Meldung des Bundestags („Haushaltsentwurf 2027 zugeleitet“,
  https://www.bundestag.de/presse/hib/kurzmeldungen-1205070) soll die Nettokreditaufnahme des Kernhaushalts „um 20,7
  Milliarden Euro auf 118,7 Milliarden Euro steigen“. 33,4 Mrd. davon entfallen auf die reguläre Schuldenregel und werden voll
  ausgeschöpft. Die erste Lesung war am 08.09.2026 (Rede Klingbeil, Bulletin 81‑1). Bis zum Beschluss kommen noch die
  Steuerschätzung im November und die Bereinigungssitzung des Haushaltsausschusses. Klingbeil sprach in der Pressekonferenz von
  einer geschlossenen Lücke von 34 Mrd. Euro und von wirtschaftlichen Folgen des Irankriegs.
- **Computer: 0,45.** Der Entwurf liegt mit 118,7 Mrd. nur 0,3 Mrd. unter der Schwelle. Die Bereinigungssitzung verschiebt die
  Zahl erfahrungsgemäß um Milliarden, in beide Richtungen. Gegen die Einhaltung sprechen schwächeres Wachstum (Frühjahrsprojektion
  0,5 % für 2026), Mehrbedarfe aus dem Irankrieg und eine voll ausgeschöpfte Regelgrenze. Eine bessere Steuerschätzung
  könnte die Zahl dagegen senken. Die Tendenz geht leicht Richtung Überschreitung.

---

## bund-2026-002 · Digitales: Staatliche EUDI-Wallet „d-you“ startet am 02.01.2027

- **gesagt_von:** Bundesministerium für Digitales und Staatsmodernisierung (Pressemitteilung 53/2026, Minister Dr. Karsten Wildberger)
- **gesagt_am:** 2026-09-09
- **quelle:** https://bmds.bund.de/aktuelles/pressemitteilungen/detail/d-you-deutschland-startet-digitale-identitaet-fuer-alle
- **zitat:** „Zum Launch am 2. Januar 2027 werden rund 40 Partner aus Wirtschaft, Wissenschaft und Verwaltung mit eigenen Anwendungen dabei sein. … Direkt am 2. Januar 2027 stehen verschiedene Anwendungen bereit, die es ermöglichen, das Alter nachzuweisen, rechtssicher Verträge abzuschließen oder ein Bankkonto zu eröffnen.“
- **Wortlaut geprüft:** ja, beide Sätze per curl gefunden (`True`, `True`).
- **frage:** Ist die staatliche EUDI-Wallet „d-you“ am 02.01.2027 für die Allgemeinheit (ohne Testanmeldung) in den App-Stores für iOS und Android herunterladbar und mit dem Personalausweis einrichtbar?
- **typ:** ja_nein · **pruefung_am:** 2027-01-03
- **art (Bund):** `angekuendigt` (ohne Vorbehalt: „Zum Launch am …“, „stehen … bereit“) → **wert 1,00**
- **Übersetzung:** Ja nur, wenn die App am Stichtag öffentlich verfügbar ist. Eine geschlossene Beta oder ein späterer Start ist
  Nein. Ob die 40 Partner dabei sind, wird nicht geprüft und könnte eine eigene Wette werden.
- **Kontext:** netzpolitik.org (Daniel Leisegang, 10.09.2026, „Neuer Name, alte Baustellen …“) schreibt: „Bis dahin
  muss das Digitalministerium aber noch Probleme bei der IT-Sicherheit lösen. Bei ‚Restrisiken‘ könnte die
  Bundesregierung den Start verschieben.“ Laut it-fachportal.de (06/2026) ist der „Starttermin der deutschen Eudi-Wallet 2027 in
  Gefahr“. Nach eIDAS 2.0 muss jeder Mitgliedstaat bis Ende 2026 eine Wallet bereitstellen, der 02.01.2027 liegt also schon knapp danach.
- **Computer: 0,55.** Name, Datum und Partner stehen öffentlich fest, der politische Druck ist hoch, und es gibt die EU-Frist.
  Dagegen stehen die offenen BSI- und Sicherheitsfragen und der von der Regierung selbst angedeutete Vorbehalt bei Restrisiken.
  Große staatliche IT-Starts in Deutschland verschieben sich häufig. Ein Start am exakten Tag ist nur knapp wahrscheinlicher als nicht.

---

## bund-2026-003 · Soziales/Steuern: Kindergeld 267 Euro ab 2027

- **gesagt_von:** Bundesregierung / Presse- und Informationsamt (Kabinettsbeschluss Einkommensteuerreform 2027; federführend BMF, Lars Klingbeil)
- **gesagt_am:** 2026-09-02
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/einkommensteuerreform-2027-2451192
- **zitat:** „Das Kindergeld steigt von 259 Euro auf 267 Euro (2027) und dann 272 Euro (2028) je Kind und Monat.“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Beträgt das gesetzliche Kindergeld für Januar 2027 mindestens 267 Euro je Kind und Monat?
- **typ:** ja_nein · **pruefung_am:** 2027-01-02
- **art (Bund):** `angekuendigt` („steigt“, kein Vorbehalt) → **wert 1,00**
- **Übersetzung:** Maßgeblich ist der Betrag nach § 66 EStG, der für Januar 2027 gilt, belegt durch das Bundesgesetzblatt oder die Familienkasse.
  Eine rückwirkende Erhöhung, die erst nach dem 02.01.2027 verkündet wird, zählt nur, wenn sie bis `pruefung_am` im BGBl
  steht. Die Stufe 2028 (272 €) wäre eine eigene Wette.
- **Kontext:** Das Kabinett hat den Entwurf am 02.09.2026 beschlossen, laut Bundesregierung mit „rund zehn Milliarden Euro pro Jahr“
  Entlastung (https://www.bundesregierung.de/breg-de/schwerpunkte/reformen-fuer-deutschland/reformen-steuern-entlastung-2446816).
  Einkommensteuer- und Kindergeldänderungen brauchen die Zustimmung des Bundesrats (Art. 105 Abs. 3 GG). Die Länder fordern laut
  Presseberichten (Sept. 2026, Sekundärquellen) einen Ausgleich für ihre Steuerausfälle. Laut Sekundärquellen liegt der Entwurf seit
  28.09.2026 als BT-Drs. 21/8235 vor, erste Lesung am 08.10.2026. Ein Teil der Erhöhung ist wegen des Existenzminimumberichts
  verfassungsrechtlich ohnehin geboten.
- **Computer: 0,80.** Kindergeld-Erhöhungen zum Jahresbeginn kamen in den letzten Jahren regelmäßig auch unter Zeitdruck
  noch durch, und der Kinder-Teil ist politisch kaum umstritten. Risiken sind der Streit über die Länderkompensation im
  Bundesrat und der knappe Zeitplan bis Dezember. Ein Kompromiss könnte den Betrag zudem verschieben, wobei eine Senkung unter 267 € unwahrscheinlich ist.

---

## bund-2026-004 · Wohnen: Wohngeld-Absenkung tritt am 01.01.2027 in Kraft

- **gesagt_von:** Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen (Ministerin Verena Hubertz). Seite „Entwurf eines Gesetzes zur Vereinfachung und Fortentwicklung des Wohngeldgesetzes“, Kabinett 06.07.2026
- **gesagt_am:** 2026-06-24 (Seitendatum; Kabinettsbeschluss 06.07.2026 auf derselben Seite)
- **quelle:** https://www.bmwsb.bund.de/SharedDocs/gesetzgebungsverfahren/DE/wohngeld-2026/wohngeldreform.html
- **zitat:** „Zum Inkrafttreten am 1. Januar 2027 ist eine Absenkung des Wohngeldes vorgesehen: Die Fortschreibung des Wohngeldes zum 1. Januar 2027 wird ausgesetzt, die Heizkostenkomponente wird halbiert und die Wohngeldformel wird angepasst.“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Ist am 01.01.2027 eine Änderung des Wohngeldgesetzes in Kraft, mit der die Fortschreibung zum 01.01.2027 ausgesetzt und die Heizkostenkomponente halbiert wird?
- **typ:** ja_nein · **pruefung_am:** 2027-01-02
- **art (Bund):** `voraussichtlich` („ist … vorgesehen“) → **wert 0,80**
- **Übersetzung:** Ja nur, wenn beide Kernpunkte (Aussetzen der Fortschreibung und Halbierung der Heizkostenkomponente) am
  01.01.2027 gelten, belegt durch Verkündung im BGBl. Ein späteres Inkrafttreten oder eine abgeschwächte Fassung (z. B. nur Aussetzen)
  ist Nein.
- **Kontext:** Die Ausschüsse des Bundesrats empfahlen eine ablehnende Stellungnahme (BR-Drs. 474/1/26 vom 11.09.2026). Am
  25.09.2026 hat der Bundesrat den Entwurf kritisiert, laut Sekundärquellen (haufe.de: „Bundesrat lehnt Einschnitte beim
  Wohngeld 2027 ab“; buerger-geld.org). Genannte Folgen: rund 381.000 Haushalte verlieren den Anspruch, 143.000 wechseln in die
  Grundsicherung. Die Einsparung soll 2027 rund 1,5 Mrd. Euro betragen. Bund und Länder zahlen das Wohngeld je zur Hälfte. Ob das Gesetz
  zustimmungspflichtig ist, muss vor dem Eintragen geprüft werden (bei Zustimmungspflicht ist die Unsicherheit deutlich größer).
- **Computer: 0,45.** Der Haushalt 2027 rechnet mit der Einsparung, das spricht für einen Beschluss. Dagegen stehen ein geschlossen
  ablehnender Bundesrat, die SPD-Basis gegen Kürzungen bei einer SPD-Ministerin und ein knapper Zeitplan. Wahrscheinlich ist ein
  Kompromiss, etwa ohne Halbierung der Heizkostenkomponente oder mit späterem Start, und der wäre nach der Übersetzungsregel ein Nein.

---

## bund-2026-005 · Pflege: Strukturreform tritt zum 01.07.2027 in Kraft

- **gesagt_von:** Bundesregierung / Presse- und Informationsamt (Kabinett Pflegeneuordnungsgesetz; Bundesgesundheitsminister Carsten Linnemann)
- **gesagt_am:** 2026-09-30
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/pflegeneuordnungsgesetz-2454862
- **zitat:** „Die Kommission soll ihre Vorschläge bis Ende Januar 2027 vorlegen. Angestrebt wird, darauf aufbauende Reformen zum 1. Juli 2027 in Kraft treten zu lassen.“
- **Wortlaut geprüft:** ja (curl, `True`, mit dem vorangehenden Satz zum Einsetzungsbeschluss geprüft).
- **frage:** Ist am 01.07.2027 ein Gesetz zur Pflegeversicherung in Kraft, das nach seiner Begründung auf den Vorschlägen der Pflegestrukturkommission aufbaut?
- **typ:** ja_nein · **pruefung_am:** 2027-07-02
- **art (Bund):** `voraussichtlich` („Angestrebt wird“) → **wert 0,80**
- **Übersetzung:** Ja nur, wenn ein solches Gesetz spätestens am 01.07.2027 verkündet ist und mindestens teilweise gilt. Ein
  Kabinettsentwurf oder ein Bundestagsbeschluss ohne Inkrafttreten zählt nicht. Das jetzt eingebrachte Pflegeneuordnungsgesetz
  (PNOG) zählt nicht, weil es vor der Kommission kommt.
- **Kontext:** Das Kabinett hat das PNOG am 30.09.2026 nach wochenlangem Koalitionsstreit beschlossen. Laut BMG bzw. Bundesregierung
  droht ohne Gegenmaßnahmen für 2027 ein Defizit von rund 7,6 Mrd. Euro. Die Kommission soll am 07.10.2026 eingesetzt werden. Zwischen
  Kommissionsbericht (Ende Januar) und Inkrafttreten (1. Juli) blieben dann gut fünf Monate für Referentenentwurf, Kabinett,
  Bundesrat und Bundestag.
- **Computer: 0,12.** Fünf Monate von Kommissionsvorschlägen bis zum Inkrafttreten wären für eine Strukturreform der Pflege
  sehr schnell. Schon das kleinere PNOG brauchte Wochen Streit allein bis zum Kabinett. Schon eine kleine Verspätung der Kommission
  macht den Termin unhaltbar.

---

## bund-2026-006 · Pflege: Kommission legt Vorschläge bis Ende Januar 2027 vor

- **gesagt_von:** wie 005
- **gesagt_am:** 2026-09-30
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/pflegeneuordnungsgesetz-2454862
- **zitat:** „Der Einsetzungsbeschluss ist für den 7. Oktober 2026 vorgesehen. Die Kommission soll ihre Vorschläge bis Ende Januar 2027 vorlegen.“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Hat die Pflegestrukturkommission ihre Vorschläge bzw. ihren Bericht bis einschließlich 31.01.2027 öffentlich vorgelegt?
- **typ:** ja_nein · **pruefung_am:** 2027-02-01
- **art (Bund):** `voraussichtlich` („soll“) → **wert 0,80**
- **Übersetzung:** „Vorlegen“ heißt Übergabe an die Bundesregierung mit öffentlicher Bekanntgabe (Pressemitteilung oder veröffentlichter
  Bericht). Ein Zwischenbericht zählt nur, wenn er als „Vorschläge“ der Kommission ausgewiesen ist. Mit 005 hängt
  die Wette zusammen, beide sind aber getrennt prüfbar.
- **Kontext:** wie 005. Für die Arbeit bleiben weniger als vier Monate, Weihnachten eingeschlossen.
- **Computer: 0,40.** Kommissionen mit festem Abgabetermin halten ihn oft knapp. Weniger als vier Monate für
  ein umstrittenes Finanzierungsthema sind aber kurz, und schon eine verspätete Einsetzung verschiebt alles. Die Kommission
  könnte auch nur Eckpunkte liefern, und die zählen nach der Übersetzungsregel nicht.

---

## bund-2026-007 · Verkehr/Digitales: Digitaler Führerschein bis Ende 2026

- **gesagt_von:** Bundesministerium für Verkehr (Pressemitteilung 037/2026, Bundesverkehrsminister Patrick Schnieder)
- **gesagt_am:** 2026-05-05
- **quelle:** https://www.bmv.de/SharedDocs/DE/Pressemitteilungen/2026/037-schnieder-ein-jahr-bmv.html
- **zitat:** „Ende des Jahres wollen wir auch mit dem digitalen Führerschein so weit sein, Mitte kommenden Jahres mit der digitalen Kfz-Zulassung.“
- **Wortlaut geprüft:** ja (curl, `True`). Im HTML steht `<abbr>Kfz</abbr>-Zulassung`, sichtbar also „Kfz-Zulassung“.
- **frage:** Können Bürgerinnen und Bürger am 31.12.2026 ihren Führerschein in der i-Kfz-App (oder einer anderen staatlichen App) digital hinterlegen und vorzeigen?
- **typ:** ja_nein · **pruefung_am:** 2027-01-01
- **art (Bund):** `voraussichtlich` („wollen wir … so weit sein“ ist eine Absicht, keine Zusage) → **wert 0,80**
- **Übersetzung:** Ja, wenn die Funktion am 31.12.2026 für die Allgemeinheit freigeschaltet ist. Eine Pilotgruppe oder eine
  angekündigte Freischaltung im Januar ist Nein.
- **Kontext:** Laut Sekundärquellen ist das Gesetz für den digitalen Führerschein seit 01.07.2026 in Kraft. KBA-Präsident Richard Damm
  sagte im August 2026, man liege im Zeitplan und wolle den Führerschein im vierten Quartal 2026 in der i-Kfz-App bereitstellen
  (t-online, deskmodder.de 28.08.2026). Einen konkreten Starttag gibt es nicht. Den digitalen Fahrzeugschein in der i-Kfz-App gibt es seit
  November 2025 (BMV-PM 057/2025), laut BMV mit mehr als 1,4 Mio. Downloads.
- **Computer: 0,55.** Die Grundlage steht (App, Gesetz, Fahrzeugschein-Vorbild), und KBA wie BMV bekräftigen das Q4. Bei
  „Ende des Jahres“ führt aber schon ein Rutsch in den Januar zum Nein, und staatliche Apps starten oft in Wellen.

---

## bund-2026-008 · Verkehr/Digitales: Zentrale digitale Kfz-Zulassung bis Mitte 2027

- **gesagt_von:** wie 007
- **gesagt_am:** 2026-05-05
- **quelle:** https://www.bmv.de/SharedDocs/DE/Pressemitteilungen/2026/037-schnieder-ein-jahr-bmv.html
- **zitat:** wie 007 (zweiter Halbsatz: „… Mitte kommenden Jahres mit der digitalen Kfz-Zulassung.“). Im selben Text steht davor: „ebenso an der digitalisierten und zentralisierten Fahrzeugzulassung über das Kraftfahrt-Bundesamt in Flensburg.“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Ist am 30.06.2027 eine zentrale, über das Kraftfahrt-Bundesamt bereitgestellte digitale Fahrzeugzulassung für Bürgerinnen und Bürger bundesweit nutzbar?
- **typ:** ja_nein · **pruefung_am:** 2027-07-01
- **art (Bund):** `voraussichtlich` → **wert 0,80**
- **Übersetzung:** „Mitte kommenden Jahres“ wird als 30.06.2027 gelesen (Halter-Festlegung). Die dezentrale i-Kfz-Online-Zulassung
  über die Portale der Zulassungsbehörden gibt es schon und zählt **nicht**. Gemeint ist das neue zentrale KBA-Verfahren. Gilt es nur für
  einzelne Länder oder Vorgänge, ist die Antwort Nein.
- **Kontext:** Gesetzesstand und Zeitplan der Zentralisierung wurden nicht weiter recherchiert. Das sollte vor dem Eintragen geschehen.
  Wegen der bestehenden dezentralen Online-Zulassung ist die Abgrenzung heikel. Halterentscheidung: eintragen oder
  verwerfen.
- **Computer: 0,20.** Eine Zentralisierung braucht Bund-Länder-Abstimmung, Rechtsänderungen und die Anbindung der Zulassungsstellen.
  Das alles in gut einem Jahr ab Mai 2026 ist für die deutsche Verwaltungs-IT ehrgeizig. Ohne bekannten Gesetzentwurf ist ein bundesweiter
  Start zum 30.06.2027 wenig wahrscheinlich.

---

## bund-2026-009 · Bundeswehr: Personalstärke Ende 2026 „deutlich im Aufwuchskorridor“

- **gesagt_von:** Bundesministerium der Verteidigung (Pressemitteilung „Bundeswehr weiter auf gesetzlich festgelegtem Aufwuchspfad“; Minister Boris Pistorius)
- **gesagt_am:** 2026-09-18
- **quelle:** https://www.bmvg.de/de/presse/bundeswehr-weiter-auf-gesetzlich-festgelegtem-aufwuchspfad-6156012
- **zitat:** „Wir rechnen bis zum Jahresende weiter mit steigenden Zahlen der Personalgewinnung und werden zum Jahresende deutlich im Aufwuchskorridor liegen.“
- **Wortlaut geprüft:** ja (curl `--compressed`, `True`). Ebenso geprüft: „Zum Stichtag 31. August 2026 dienten in der Bundeswehr rund 186.400 aktive Soldatinnen und Soldaten.“
- **frage:** Dienen nach Angabe des BMVg zum Stichtag 31.12.2026 mindestens 187.000 aktive Soldatinnen und Soldaten in der Bundeswehr?
- **typ:** ja_nein · **pruefung_am:** 2027-01-01 (aufgelöst wird mit der BMVg-Personalmeldung für Dezember, erfahrungsgemäß Mitte Januar bis Februar 2027)
- **art (Bund):** `angekuendigt` („werden … liegen“) → **wert 1,00**
- **Übersetzung:** Der gesetzliche Korridor für 2026 liegt bei 186.000 bis 190.000 aktiven Soldatinnen und Soldaten
  (Wehrdienstmodernisierungsgesetz, BGBl. 2025 I Nr. 370). „Deutlich im Korridor“ wird als mindestens 1.000 über der
  Untergrenze gelesen, also ≥ 187.000 (Halter-Festlegung). Die Alternative wäre die Untergrenze 186.000 als Schwelle, das ist weicher.
- **Kontext:** Stand Ende Juli 2026: rund 186.700. Stand Ende August 2026: rund 186.400. Ende 2025 waren es rund 184.200
  (aus „um mehr als 2.200 … gewachsen“). Im Vorjahr stieg die Stärke von August bis Dezember um rund 1.800
  (182.400 → 184.200). Laut suv.report („knapp über der gesetzlichen Untergrenze“) ist der Puffer dünn. Neueinstellungen
  liegen 13 % über dem Vorjahr.
- **Computer: 0,65.** Wiederholt sich das Vorjahresmuster (+1.800 von August bis Dezember), landet die Stärke bei etwa 188.000.
  Abgänge zum Jahresende und das Auslaufen kurzer Wehrdienstzeiten können das aber schnell aufzehren. Bei der Schwelle
  186.000 läge die Schätzung bei etwa 0,85.

---

## bund-2026-010 · Energie: 11 Gigawatt steuerbare Kapazität binnen zwölf Monaten ausgeschrieben

- **gesagt_von:** Bundesregierung / Presse- und Informationsamt (FAQ „Für eine verlässliche Stromversorgung – auch in Zukunft“ zum StromVKG; federführend BMWE, Ministerin Katherina Reiche)
- **gesagt_am:** 2026-09-03 (Seitendatum; ursprünglich zum Kabinettsbeschluss 13.05.2026, aktualisiert nach Inkrafttreten am 22.07.2026)
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/kabinett-stromversorgungssicherheit-2430320
- **zitat:** „Bereits in den nächsten zwölf Monaten sollen steuerbare Kapazitäten im Umfang von insgesamt elf Gigawatt ausgeschrieben werden“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Summiert sich die von der Bundesnetzagentur nach StromVKG ausgeschriebene Menge aller Gebotstermine zwischen 03.09.2026 und 03.09.2027 auf mindestens 11.000 MW?
- **typ:** ja_nein · **pruefung_am:** 2027-09-04
- **art (Bund):** `voraussichtlich` („sollen“) → **wert 0,80**
- **Übersetzung:** Gezählt werden die von der BNetzA bekannt gemachten Ausschreibungsmengen von Gebotsterminen im Zeitraum, egal ob
  Langzeitkapazitäten oder Erzeugungskapazitäten. Die Einheit ist so, wie die BNetzA sie angibt (auch „MW reduzierte Leistung“). Ein Gebotstermin
  muss im Zeitraum **stattgefunden** haben. Eine bloße Bekanntmachung reicht nicht. Wird nicht das Seitendatum gewählt, sondern der Kabinettstermin
  (13.05.2026 → Frist 13.05.2027), wird die Wette deutlich unsicherer, weil die 2‑GW-Runde für „Mai 2027“ angesetzt ist.
- **Kontext:** BNetzA-PM vom 21.07.2026: erster Gebotstermin am 08.09.2026 mit 4.500 MW reduzierter Leistung. Laut iwr.de
  war er „deutlich überzeichnet“. Für den zweiten Gebotstermin über 4.500 MW nennen Sekundärquellen den 08.12.2026, eine Quelle
  nennt den 29.12.2026. Für Mai 2027 sind weitere 2 GW geplant. Zusammen ergibt das genau 11 GW, ohne jeden Puffer.
- **Computer: 0,70.** Die ersten 4,5 GW sind schon gelaufen, die zweite Runde ist gesetzlich terminiert. Das Risiko liegt allein in
  der 2‑GW-Runde 2027, die verschoben oder verkleinert werden könnte. Die Wette hängt außerdem an der Mengenzählung („reduzierte
  Leistung“ gegen installierte Leistung).

---

## bund-2026-011 · Wirtschaft: Wachstum 2027 laut Frühjahrsprojektion 0,9 %

- **gesagt_von:** Bundesregierung / BMWE (Frühjahrsprojektion 2026, vorgestellt von Bundeswirtschaftsministerin Katherina Reiche)
- **gesagt_am:** 2026-04-22
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/fruehjahrsprojektion-2026-2422692
- **zitat:** „Für 2027 rechnet die Bundesregierung mit einem realen BIP-Zuwachs von 0,9 Prozent.“
- **Wortlaut geprüft:** ja (curl, `True` in der Form „BIP -Zuwachs“ nach Tag-Ersetzung; Roh-HTML `<abbr>BIP</abbr>-Zuwachs`).
- **frage:** Um wie viel Prozent wächst das preisbereinigte Bruttoinlandsprodukt 2027 gegenüber 2026 laut erster Jahresschätzung des Statistischen Bundesamts?
- **typ:** punkt · **einheit:** Prozent · **toleranz:** Vorschlag absolut ±0,3 Prozentpunkte. FORMAT.md kennt nur relative Toleranz, deshalb Toleranz weglassen oder im Textteil erklären.
- **pruefung_am:** 2028-01-14 (Destatis veröffentlicht die erste Jahreszahl erfahrungsgemäß Mitte Januar; **Ausnahme vom
  Wunschfenster bis 12/2027**, aber vor 2029)
- **art (Bund):** `voraussichtlich` (Projektion, „rechnet mit“) → **wert 0.9** (bei `punkt` ist der Wert die Zahl)
- **Übersetzung:** Gemessen wird die nicht kalenderbereinigte Veränderungsrate aus der ersten Destatis-Pressemitteilung zum
  Jahres-BIP 2027. Spätere Revisionen zählen nicht. Die Herbstprojektion (Oktober 2026) und die Jahresprojektion (Januar 2027) sind neue
  Aussagen und damit nach §1.3 Regel 5 eigene Wetten.
- **Kontext:** Dieselbe Projektion erwartet für 2026 nur 0,5 % „auch als Folge der Auswirkungen des Irankrieges“. Die Regierung
  verweist auf fiskalische Impulse (Sondervermögen, laut Klingbeil 2027 insgesamt 118 Mrd. Euro Investitionen, Rede vom 08.09.2026,
  https://www.bundesregierung.de/breg-de/suche/bmf-haushaltsgesetz-2027-2451896).
- **Computer: 0,8 (Prozent).** Die Investitionsimpulse wirken 2027 stärker als 2026, dagegen stehen die Folgen des Irankriegs und
  hohe Energiepreise. Projektionen der Bundesregierung lagen in den letzten Jahren eher zu hoch als zu niedrig.

---

## bund-2026-012 · Wirtschaft: Inflationsrate 2027 laut Frühjahrsprojektion 2,8 %

- **gesagt_von:** wie 011
- **gesagt_am:** 2026-04-22
- **quelle:** https://www.bundesregierung.de/breg-de/aktuelles/fruehjahrsprojektion-2026-2422692
- **zitat:** „Die Regierung rechnet mit einer Inflationsrate von 2,7 Prozent für 2026 und 2,8 Prozent im kommenden Jahr.“
- **Wortlaut geprüft:** ja (curl, `True`).
- **frage:** Wie hoch ist die Inflationsrate (Veränderung des Verbraucherpreisindex VPI, Jahresdurchschnitt 2027 gegenüber 2026) laut erster Destatis-Veröffentlichung?
- **typ:** punkt · **einheit:** Prozent
- **pruefung_am:** 2028-01-07 (Destatis-Vorabschätzung Anfang Januar; Ausnahme vom Wunschfenster wie 011)
- **art (Bund):** `voraussichtlich` → **wert 2.8**
- **Übersetzung:** „im kommenden Jahr“ ist 2027 (Aussage vom April 2026). Maßgeblich ist der VPI, nicht der HVPI, nach der ersten Destatis-
  Jahreszahl (Vorabschätzung oder Pressemitteilung, je nachdem, was zuerst kommt).
- **Kontext:** wie 011. Die Regierung nennt das Kraftstoffmaßnahmenpaket und das Energie-Sofortprogramm als Dämpfer. Zum 01.01.2027
  steigt außerdem der CO2-Preis mit dem Übergang zum EU-ETS2. Das ist nicht geprüft und vor dem Eintragen zu verifizieren.
- **Computer: 2,5 (Prozent).** Ölpreisschocks klingen im zweiten Jahr meist ab, deshalb wird ein Wert etwas unter der
  Regierungsprojektion erwartet. Aufwärtsrisiken sind CO2-Bepreisung und Lohnrunden. Die Unsicherheit ist groß, deshalb nur mäßige Abweichung von 2,8.

> Hinweis: 011 und 012 kommen aus derselben Quelle und sind Prognosen, keine Handlungszusagen. Wer das Buch auf Zusagen
> beschränken will, streicht beide. Dann bleiben zehn Kandidaten.

---

## Verworfene Kandidaten

| Thema | Grund |
|---|---|
| Frühstartrente startet 01.01.2027 (BMF/Klingbeil) | BMF-FAQ (`bundesfinanzministerium.de/Content/DE/FAQ/fruehstart-rente.html`) liefert nur Radware-Captcha. Auf bundesregierung.de (Artikel 12.08.2026, Rede Klingbeil 25.09.2026) steht kein Startdatum der Frühstartrente im Wortlaut. |
| Altersvorsorgedepot „ab Januar 2027“ (bundesregierung.de, 12.08.2026, Zitat geprüft) | Das Gesetz ist schon beschlossen (BT 27.03.2026, BR 08.05.2026) und verkündet. Praktisch sicher, also kein Wettgegenstand. |
| BMF-Pressemitteilung Regierungsentwurf Haushalt 2027 (06.07.2026) | Radware-Bot-Sperre bei curl und WebFetch. Ersatzweise wird die BMF-Textfassung der Pressekonferenz genutzt (001). |
| Deutschlandticket kostet ab 01.01.2027 66,80 € | Beschluss der Verkehrsministerkonferenz (Bund und Länder) mit Indexformel, keine Ankündigung der Bundesregierung allein. Auf bmv.de wurde keine Primärquelle gefunden. Der Preis steht nach Index praktisch fest. |
| Mindestlohn 14,60 € ab 01.01.2027 | Per Verordnung festgesetzt, praktisch sicher. Wortlaut nicht geprüft. |
| Netzentgelt-Zuschuss 5,525 Mrd. €/Jahr 2027–2029 (Kabinett 02.09.2026) | Die ÜNB rechnen ihn schon in die vorläufigen Netzentgelte 2027 ein (TransnetBW 10/2026). Kaum Unsicherheit. Eine Primärquelle mit Zitat wurde nicht gesichert. |
| Führerscheinreform „könnte Anfang 2027 in Kraft treten“ (BMV 05.05.2026) | „könnte“ ist keine Ankündigung, nicht einmal `voraussichtlich`. |
| Bayern/Hessen: fünf Online-Dienste „bis Ende 2026 flächendeckend“ (BMDS-PM 03/2026, 21.01.2026) | Das Leistungsversprechen geben die Länder ab, nicht der Bund. „Flächendeckend“ ist ohne Länderdaten nicht prüfbar. Wäre eher ein Kandidat für ein Landesbuch. |
| Bahn: verbindliche Pufferzeiten „ab 2027“, vier Digitale Steuerzentralen-Piloten „bis 2027“, drei Regelwerke „bis Ende 2026“ (BMV-PM 020/2026, 20.03.2026) | Für Pufferzeiten fehlt eine Zahl. Die Piloten und Regelwerke sind Taskforce-Empfehlungen ohne öffentliche Erfolgsmeldung und deshalb schwer zu belegen. |
| Bahn-Pünktlichkeit ≥ 70 % Fernverkehr bis Ende 2029 (Agenda 09/2025) | Gesagt vor 01/2026 und Prüfdatum nach 2028. |
| Stuttgart 21 Eröffnung Dezember 2026 | Nur DB-Quelle (2024/25), kein Ministerium. Der Termin gilt zudem als aufgegeben. |
| Generalsanierungen 2026 (Hagen–Köln, Nürnberg–Regensburg u. a.) Wiederinbetriebnahme | Auf bmv.de stehen nur Termine (Spatenstich), keine Fertigstellungszusage mit Datum im Wortlaut. **Damit fehlt dem Buch ein Bahn-Kandidat.** Eine Nachsuche wäre in Reden Schnieders im Bulletin sinnvoll. |
| Investitionen 2027 „insgesamt 118 Milliarden Euro“ (Rede Klingbeil 08.09.2026, Zitat geprüft) | Messbar erst mit dem Haushaltsabschluss 2028. Die Abgrenzung „Investitionen“ über Kern- und Sonderhaushalte ist strittig. Zurückgestellt, nicht endgültig verworfen. |
| Grundfreibetrag 12.564 € 2027 | Gleiches Gesetz wie 003, wäre redundant. Als Zwillingswette möglich. |
| Infrastruktur-Zukunftsgesetz Art. 10 tritt am 01.02.2027 in Kraft | Schon verkündet, sicher. |
| Gebäudemodernisierungsgesetz | Seit 29.07.2026 in Kraft. |
| Gebäudetyp-E-Gesetz | Weder Kabinettsbeschluss noch ein datiertes Zitat der Bundesregierung gefunden. Nur Presseberichte („wohl nicht vor 2027“). |
| Mütterrente III ab 01.01.2027 | Bereits 2025 beschlossen, sicher. |
| Merz: „weiteres Entlastungskabinett zum Ende des Jahres“ (Sommer-PK 2026) | Indirekte Rede ohne Zahl. Ein „Entlastungskabinett“ ist kaum operationalisierbar. |
| 1.500 neue E-Busse mit Haushaltsmitteln 2026 (BMV-PM 044/2026) | Förderzusage. Gezählt würden Bewilligungen, für die es keine öffentliche Endzahl gibt. |

## Offene Punkte für den Halter

1. **001:** BMF-Zitat einmal im Browser gegenprüfen (Bot-Sperre) und einen Wayback-Link anlegen.
2. **004:** Zustimmungspflicht des Wohngeldgesetzes klären. Sie entscheidet viel.
3. **008:** Eintragen oder verwerfen, die Abgrenzung zur bestehenden dezentralen Online-Zulassung ist heikel.
4. **009:** Schwelle festlegen: 187.000 („deutlich“) oder 186.000 (Untergrenze).
5. **010:** Fristbeginn festlegen: Seitendatum 03.09.2026 (empfohlen) oder Kabinettsdatum 13.05.2026.
6. **011/012:** Prognosen ins Buch aufnehmen oder nicht. Die Prüfdaten liegen im Januar 2028.
7. Eine Lücke bleibt bei **Bahn**, dafür gibt es keinen Kandidaten mit Bundes-Primärquelle.
