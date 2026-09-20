# Köln — Kandidaten für einen monatlich messbaren Fall

**Stand:** 08.09.2026 (Dienstag)
**Zweck:** Eine Kölner Verwaltungsleistung finden, deren Qualität die Stadt Köln selbst öffentlich beziffert oder verspricht und die ein Einzelner **monatlich ohne Behördenauskunft** nachmessen kann. Ergebnis soll ein Eintrag im festgehalten-Format werden (Behauptung wörtlich + Quelle-URL + Datum + Frist + Beleg).
**Methode:** WebSearch + WebFetch, nur tatsächlich aufgerufene URLs. Zwei PDFs (Haushaltsplan 2025/2026 Band 3, Ratsvorlagen) lokal mit pymupdf extrahiert. ksta.de, express.de, rundschau-online.de, wdr.de, rp-online.de blockieren den Crawler — Presse daher über koeln.t-online.de, report-k.de, porz-am-montag.de, nachrichtenlokal.de, change.org, YouTube (WDR aktuell).

---

## Vorab: Gibt es ein „Service-Versprechen" der Stadt Köln?

**Kein explizites Service-Versprechen gefunden** (keine Seite „Bürgeramt-Ziele", kein OZG-Dashboard mit Kölner Bearbeitungszeiten, kein Zielwert in der Digitalstrategie). Was es stattdessen gibt — und was als Zusage taugt:

### 1. Haushaltsplan 2025/2026, Band 3 „Produktgruppen mit Zielen und Kennzahlen" (die einzige Stelle, an der die Stadt Qualität beziffert)

URL (beschlossene Fassung, 389 S.): https://www.stadt-koeln.de/mediaasset/content/pdf20/4_hpl_2025_2026_band_3.pdf
URL (Entwurf, 406 S., identische Werte): https://www.stadt-koeln.de/mediaasset/content/pdf20/4_hpl_entwurf_2025_2026_band_3.pdf
Eingebracht 14.11.2024 (PM 27147: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/27147/index.html)

Wörtlich aus Band 3 (Spalten: Ergebnis 2022 | Ergebnis 2023 | 2024 | Plan 2025 | Plan 2026):

| Seite | Produkt | Kennzahl (wörtlich) | 2022 | 2023 | 2024 | Plan 2025 | Plan 2026 |
|---|---|---|---|---|---|---|---|
| 101 | 0207 Einwohnerangelegenheiten (= Kundenzentren) | „Durchschnittliche Wartezeit ohne Termin in Min." | 0,00 | 25,21 | 10,00 | **20,00** | **20,00** |
| 101 | 0207 | „Anteil der Kundenbesuche mit Terminvergabe in %" | 0,00 | 0,00 | 60,00 | 60,00 | 60,00 |
| 101 | 0207 | „Anzahl Bürgerbesuche" | 0 | 611.469 | 460.000 | 500.000 | 500.000 |
| 92 | 020402 Kfz-Zulassungsangelegenheiten | „Durchschnittliche Terminvorlaufzeit in Min." | 14,36 | 15,70 | 15,00 | **12,00** | **12,00** |
| 111 | 020901 Zentrale Ausländerangelegenheiten | „Anzahl der vollzogenen Einbürgerungen" | 3.469 | 3.800 | 3.000 | 7.000 | 8.000 |
| 111 | 020901 | „Anzahl der erteilten Aufenthaltserlaubnisse" | 34.840 | 26.600 | 30.000 | 28.000 | 28.000 |
| 233 | 060201 Elterngeld | „durchschnittliche Bearbeitungsdauer von Anträgen auf Elterngeld in Tagen" | 48,32 | 42,31 | 40,00 | 40,00 | 40,00 |
| 290 | 100102 Baugenehmigungen | „Anteil der nach Antragseingang fristgerecht erteilten Baugenehmigungen in %" | 61,00 | 27,00 | 50,00 | 50,00 | 50,00 |
| 300 | 100304 Wohngeld | (keine Dauer-Kennzahl; nur „Anzahl der Wohngeldbescheide" 46.182 / 54.112 / 25.000 / 55.000 / 55.000) | | | | | |

Wirkungsziel S. 101 wörtlich: „Die Kundinnen und Kunden sind mit dem städtischen Service in den Kundenzentren zufrieden."
Leistungsziel S. 233 wörtlich: „Die gesetzlich vorgeschriebene Bearbeitungsdauer ist eingehalten."

Anmerkung: Die Einheit „in Min." bei der Kfz-Terminvorlaufzeit steht so im Plan; eine Terminvorlaufzeit von 12–15 Minuten ist unplausibel, gemeint sind vermutlich Tage. Das ist eine Unklarheit der Quelle, kein Lesefehler — im Wettbuch als Vermerk führen.

### 2. Verwaltungsstruktur-Verständigung (22.04.2026) — enthält **keine** messbare Zusage

URL: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28349/index.html
Wörtlich: Entscheidungen sollen „schneller getroffen, Zuständigkeiten klarer gebündelt und vorhandene Ressourcen zielgerichteter eingesetzt werden können." — „Dabei kommt dem digitalen Fortschritt und dem Einsatz von KI eine zentrale Rolle zu." Keine Zahl, keine Frist.

### 3. Stellungnahme der Verwaltung 3008/2024 (25.10.2024, gez. Blome) zur Terminvergabe in Kundenzentren

URL: https://ratsinformation.stadt-koeln.de/vo0050.asp?__kvonr=123621 (PDF: https://ratsinformation.stadt-koeln.de/getfile.asp?id=1009840&type=do)
Wörtlich: „Eine feste Anzahl an Terminen wird dabei bereits bis zu 60 Tage im Voraus zur langfristigen Planung für die Bürger*innen freigegeben. Zu diesen langfristigen Terminen werden am Nachmittag des Vortages oder am frühen Morgen zusätzlich tagesaktuelle Termine freigeschaltet. […] Darüber hinaus werden abgesagte Termine automatisiert direkt wieder zur Buchung freigegeben, so dass immer wieder Terminbuchungen möglich sind."
Anlass: FDP-Antrag AN/1285/2024 (Eingang 19.09.2024, https://ratsinformation.stadt-koeln.de/vo0050.asp?__kvonr=123424), Begründung wörtlich: „Eine Terminvergabe nach dem Prinzip ‚Friss oder stirb' ist einer Millionenstadt wie Köln nicht angemessen. Dass Scheibchenweise neue Terminkontingente freigegeben werden, ist nicht nachvollziehbar." Antrag am 04.11.2024 im AVR-Ausschuss „endgültig abgelehnt" (https://ratsinformation.stadt-koeln.de/si0057.asp?__ksinr=29694).

### 4. Open-Data-Datensatz „Kundenzentren Köln Wartezeiten"

URL: https://offenedaten-koeln.de/dataset/kundenzentren-koeln-wartezeiten
Ressource (JSON, ohne Login): http://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php
Felder laut Datensatzbeschreibung: `title_anz`, `timestamp`, `link`, `status` (1 = offen, 2 = geschlossen, 3 = Sondertext vorhanden), `sondertext`, `wartezeit_minuten`. Lizenz dl-de/zero-2.0. Metadaten „zuletzt aktualisiert 27.11.2025".
Abruf 08.09.2026 (Dienstag, Terminpflicht-Tag): alle 9 Kundenzentren `status: 3`, `sondertext: „nur mit Terminvereinbarung"`, `wartezeit_minuten: 0`, Timestamps vom 08.09.2026. Zusätzlich ein Eintrag „Kfz-Zulassungsstelle" mit `status: 2`, 5 Minuten, **Timestamp 27.03.2022** — ein seit 4,5 Jahren toter Datensatz im selben Feed. Das ist der wichtigste Risikohinweis für Kandidat 1.
Anzeigeseite: https://www.stadt-koeln.de/artikel/72776/index.html („Wartezeiten in unseren Kundenzentren", mit Uhrzeit-Stempel, am 08.09.2026 „16:27 Uhr").

---

## Kandidat 1 — Kundenzentren: Wartezeit ohne Termin (Montag/Mittwoch)

### 1. Zusage der Stadt
- **Haushaltsplan 2025/2026 Band 3, S. 101**, Produktgruppe 0207 Einwohnerangelegenheiten: „Durchschnittliche Wartezeit ohne Termin in Min." — Plan 2025: **20,00**, Plan 2026: **20,00** (Ergebnis 2023: 25,21). URL: https://www.stadt-koeln.de/mediaasset/content/pdf20/4_hpl_2025_2026_band_3.pdf (Datum: eingebracht 14.11.2024, beschlossener Doppelhaushalt 2025/2026).
- Wirkungsziel ebd.: „Die Kundinnen und Kunden sind mit dem städtischen Service in den Kundenzentren zufrieden."
- Seite „Besuch der Kundenzentren ohne Termin" (https://www.stadt-koeln.de/service/besuch-der-kundenzentren-ohne-termin): Montag „7:30 bis 15 Uhr ohne Terminvereinbarung", Mittwoch „7:30 bis 12 Uhr ohne Terminvereinbarung". Seite „Termin vereinbaren – Wartezeit sparen" (https://www.stadt-koeln.de/artikel/68513/index.html): „An diesen Tagen müssen Sie jedoch mit Wartezeiten rechnen."

### 2. Messgröße
Wartezeit ohne Termin in Minuten je Kundenzentrum (9 Standorte: Chorweiler, Ehrenfeld, Innenstadt, Kalk, Lindenthal, Mülheim, Nippes, Porz, Rodenkirchen), wie von der Stadt selbst live veröffentlicht. Vergleichswert: Planziel 20 Minuten im Durchschnitt.

### 3. Messung, konkret
- **Quelle:** JSON-Feed http://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php oder die Anzeigeseite https://www.stadt-koeln.de/artikel/72776/index.html. **Ohne Login. Wert direkt ablesbar** (`wartezeit_minuten` + `timestamp`).
- **Rhythmus:** An jedem Montag und Mittwoch des Monats zu zwei festen Uhrzeiten (z. B. 09:00 und 11:00) den Feed abrufen und speichern (curl + Commit reicht; Datei = Beleg mit Git-Hash). Monatswert = Mittel aller Stichproben je Standort und über alle Standorte.
- Dienstag/Donnerstag/Freitag liefert der Feed systematisch „nur mit Terminvereinbarung"/0 — diese Tage nicht werten.
- **Veröffentlicht die Stadt selbst regelmäßig Zahlen?** Nur jährlich im Haushaltsplan/Jahresabschluss (Ist-Wert je Jahr). Kein Monatsbericht gefunden.

### 4. Presse 2025/2026
- Stadt Köln, PM 15.04.2026 „Aus Ämtern und Stadtbezirken": Kundenzentrum Innenstadt öffnet an vier Samstagen (25.04., 09.05., 16.05., 30.05.2026), Begründung wörtlich: „Die Nachfrage nach Reisepässen und Personalausweisen steigt zur Ferienzeit erfahrungsgemäß stark an." Termine „jeweils am 20. April, 4. Mai, 11. Mai und 26. Mai 2026 vormittags freigeschaltet". URL: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28328/index.html
- Ältere Kernzahlen (nicht 2025/26, aber Kontext): t-online 11.07.2024: Reisepass „statt 3-4 Wochen aktuell 6-8 Wochen", frühester Antragstermin bei Abfrage am 11.07. der 1. August. URL: https://koeln.t-online.de/region/koeln/id_100446762/koeln-reisepass-chaos-so-lange-muessen-buerger-jetzt-warten.html — t-online 29.06.2022 „Ansturm auf terminfreie Tage: Lange Schlangen vor Kölner Kundenzentren", Stadt: „mehrstündige Wartezeiten" möglich. URL: https://koeln.t-online.de/region/koeln/id_100024208/ansturm-auf-terminfreie-tage-lange-schlangen-vor-koelner-kundenzentren.html
- Kein Presseartikel 2025/2026 mit einer Wartezeit-Minutenzahl gefunden.

### 5. Bewertung
- **Messbarkeit: 5** — Zahl steht offen im Netz, maschinenlesbar, mit Zeitstempel, an 8–10 Tagen pro Monat; ein Cron-Job erledigt es.
- **Risiko: mittel.** (a) Der Wert ist eine Selbstauskunft des Kundenzentrums, keine unabhängige Messung — die Wette prüft also, ob die Stadt ihr eigenes Planziel nach ihren eigenen Zahlen hält. (b) Der Feed kann still veralten (Beleg: Kfz-Eintrag mit Timestamp 27.03.2022); Timestamp daher immer mitspeichern. (c) Stichprobe ≠ Jahresdurchschnitt; die Stadt kann den Ist-Wert 2026 anders berechnen. (d) Saisonal: Ferienzeit deutlich schlechter (PM 15.04.2026, t-online 2024).

---

## Kandidat 2 — Kfz-Zulassungsstelle: Vorlauf bis zum nächsten freien Termin

### 1. Zusage der Stadt
- **PM 28528 „Verlässlicher, verbindlicher und planbar — Kfz-Zulassungsstelle stellt komplett auf Termingeschäft um", 01.07.2026, 16:00 Uhr**, wörtlich: „Damit Kölner*innen keine unnötigen Wartezeiten mehr vor Ort verbringen müssen, bietet die Zulassungsstelle alle Angelegenheiten mit vorheriger Terminvereinbarung an. […] Künftig können solche Kurzanliegen als Termin kurzfristig über die Internetseite der Stadt Köln oder über das Bürgertelefon der Stadt Köln (Telefon 0221/221-0 oder 115) gebucht beziehungsweise vereinbart werden. Neue Terminangebote für Kurzanliegen werden kontinuierlich freigeschaltet. Die Anzahl der Termine entspricht den durchschnittlich bedienten Anliegen." Gilt ab 06.07.2026. URL: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28528/index.html
- **Haushaltsplan Band 3, S. 92**, Produkt 020402: „Durchschnittliche Terminvorlaufzeit in Min." Plan 2025/2026: **12,00** (Ergebnis 2022: 14,36; 2023: 15,70; 2024: 15,00). Einheit „Min." so im Original (siehe Vorab-Anmerkung).
- Adressseite Zulassungsstelle (https://www.stadt-koeln.de/service/adressen/00205/index.html), wörtlich: „Sobald Termine abgesagt werden oder zusätzliche Kapazitäten entstehen, werden diese im Online-Kalender freigegeben."
- Terminportal-Startseite: allgemeine Zulassungsangelegenheiten „bis zu 14 Tage im Voraus" buchbar, besondere „bis zu 30 Tage im Voraus" (URL unten).

### 2. Messgröße
Tage zwischen Abfragetag und nächstem freien Termin für ein festes Anliegen (Vorschlag: „Fahrzeug abmelden" als Kurzanliegen und „Umschreibung eines Fahrzeugs" als Standardanliegen). Vergleichswert: Planziel 12 (Einheit strittig) und die Zusage „kurzfristig".

### 3. Messung, konkret
- **Portal:** https://termine.stadt-koeln.de/m/kfz-zulassung/extern/calendar/?uid=67523a04-37af-4131-9495-0a3566e0eb8b — **ohne Login**; drei Schritte (Anliegen → Termin → Daten), Kalender mit freien Slots erscheint nach Wahl des Anliegens. Abbruch vor Dateneingabe, keine Buchung nötig. Sitzung läuft nach 20 min Inaktivität ab.
- **Rhythmus:** 1. Werktag des Monats, feste Uhrzeit (z. B. 10:00), plus eine zweite Abfrage am 15.; Screenshot des Kalenders = Beleg. Dauer: ~5 Minuten.
- **Veröffentlicht die Stadt selbst regelmäßig Zahlen?** Nur der Jahres-Ist im Haushaltsplan („Terminvorlaufzeit"). Kein Monatswert.

### 4. Presse 2025/2026
- t-online 01.07.2026 „Köln: Neue Regelung bei Kfz-Zulassungsstelle soll Wartezeit reduzieren": bisher „Wartezeiten von mehreren Stunden" für Kurzanliegen ohne Termin. URL: https://koeln.t-online.de/region/koeln/id_101323328/koeln-neue-regelung-bei-kfz-zulassungsstelle-soll-wartezeit-reduzieren.html
- Porz am Montag 13.07.2026 „Kfz-Zulassungsstelle nur noch mit Termingeschäft": „rund 40 Prozent der Fälle" laufen digital über i-Kfz. URL: https://www.porz-am-montag.de/3148064-kfz-zulassungsstelle-nur-noch-mit-termingeschaeft/
- change.org-Petition, gestartet 21.03.2025, 1.154 Unterschriften, wörtlich: „Termine weiterhin erst in 14 Tagen oder sogar noch später verfügbar". URL: https://www.change.org/p/wartezeiten-von-mindestens-14-tagen-k%C3%B6lner-zulassungsstellen-v%C3%B6llig-%C3%BCberfordert
- Report-K „Kölner KFZ-Innung schlägt Alarm: 4 Wochen bis zur Zulassung eines PKW" — Titel aus Suchergebnis, Seite am 08.09.2026 nicht abrufbar (404), Datum unbekannt: https://report-k.de/Wirtschaftsnachrichten/Koelner-Wirtschaft/Koelner-KFZ-Innung-schlaegt-Alarm-4-Wochen-bis-zur-Zulassung-eines-PKW-133915

### 5. Bewertung
- **Messbarkeit: 4** — ohne Login, 5 Minuten, klarer Wert (Datum). Punktabzug: Klicks statt Feed, Screenshot statt JSON.
- **Risiko: mittel bis hoch.** (a) **Zensur nach oben:** Das Buchungsfenster ist auf 14 bzw. 30 Tage begrenzt; ist alles voll, zeigt das Portal „kein Termin" statt „in 21 Tagen" — Messwert dann „> 14". (b) Tagesfreischaltungen („kontinuierlich freigeschaltet") machen die Uhrzeit der Abfrage entscheidend — festlegen und nie ändern. (c) Einheit der Haushaltskennzahl unklar. (d) Umstellung ist 2 Monate alt; die Stadt kann Anliegenkategorien und Portal-UID jederzeit ändern. Vorteil: die Zusage ist frisch (01.07.2026) und ausdrücklich („kurzfristig", „keine unnötigen Wartezeiten mehr").

---

## Kandidat 3 — Kundenzentren: Vorlauf bis zum nächsten freien Termin (Ausweis/Meldeangelegenheiten)

### 1. Zusage der Stadt
- Stellungnahme 3008/2024 (25.10.2024, gez. Blome), wörtlich: „Eine feste Anzahl an Terminen wird dabei bereits bis zu 60 Tage im Voraus zur langfristigen Planung für die Bürger*innen freigegeben. […] abgesagte Termine [werden] automatisiert direkt wieder zur Buchung freigegeben, so dass immer wieder Terminbuchungen möglich sind." URL: https://ratsinformation.stadt-koeln.de/getfile.asp?id=1009840&type=do
- Haushaltsplan Band 3, S. 101: „Anteil der Kundenbesuche mit Terminvergabe in %" Plan 2025/2026: 60,00.
- Stadtseite Personalausweis (https://www.stadt-koeln.de/service/produkte/00416/index.html): „Die Bearbeitung dauert in der Regel zwei bis drei Wochen." (Bundesdruckerei-Lieferzeit, nicht Terminvorlauf.)

### 2. Messgröße
Tage bis zum nächsten freien Termin für „Personalausweis beantragen" (1 Person), bezirksübergreifend (nächster Termin in irgendeinem Kundenzentrum) und für das Kundenzentrum Innenstadt.

### 3. Messung, konkret
- **Portal:** https://termine.stadt-koeln.de/m/kundenzentren/extern/calendar/?uid=b5a5a394-ec33-4130-9af3-490f99517071 (Smart CJM, „Licensed for Stadt Köln, kundenzentren") — **ohne Login**; Schritte Anliegen → Standort → Termin. Übersichtsseite aller Portale: https://www.stadt-koeln.de/artikel/06415/index.html
- **Rhythmus:** 1. Werktag des Monats, 10:00 Uhr (nach der morgendlichen Tagesfreischaltung), Screenshot. Zweite Abfrage 15., 15:00 Uhr (vor der Vortagsfreischaltung) — die Differenz zeigt, wie viel „scheibchenweise" Freigabe den Wert treibt.
- **Drittanbieter:** terminator.koeln (privater Bot von David Neukirchen, seit 2022; die Stadt prüfte damals rechtliche Schritte — t-online 22.04.2022: https://koeln.t-online.de/region/koeln/id_92056566/stadt-koeln-prueft-rechtliche-schritte-gegen-terminator-.html). Seite am 08.09.2026 nur per JavaScript, per Fetch leer — als Beleg ungeeignet, als Hilfsmittel unsicher.

### 4. Presse 2025/2026
- Wie Kandidat 1: PM 15.04.2026 (Samstagsöffnungen wegen Nachfrage). Kein Artikel 2025/2026 mit einer bezifferten Terminvorlaufzeit gefunden. 2024: t-online 11.07.2024 (Abfrage 11.07. → frühester Termin 01.08., also 21 Tage).

### 5. Bewertung
- **Messbarkeit: 4** — ohne Login, 5 Minuten, Datum ablesbar.
- **Risiko: hoch.** Die Stadt hat sich hier auf keine Zahl festgelegt („bis zu 60 Tage" ist ein Fenster, keine Zusage); der Wert schwankt durch Tageskontingente stark innerhalb eines Tages; Wette müsste gegen den weichen Satz „so dass immer wieder Terminbuchungen möglich sind" laufen.

---

## Kandidat 4 — Bezirksausländerämter: Vorlauf bis zum nächsten freien Termin (Aufenthaltstitel)

### 1. Zusage der Stadt
- Seite „Online-Terminvereinbarung in den Bezirksausländerämtern", wörtlich: „Seit dem 20. April 2026 können Sie sich online selbst einen Termin bei einem unserer Bezirksausländerämter buchen." URL: https://www.stadt-koeln.de/leben-in-koeln/soziales/auslaenderamt/74526/index.html (keine Pressemitteilung dazu gefunden; Datum aus dem Seitentext).
- Seite Bezirksausländerämter, wörtlich: „Aufgrund von Personalausfällen bearbeiten wir Anträge von Kund*innen aus Mülheim seit dem 1. Januar 2026 nicht mehr am Standort Mülheim." URL: https://www.stadt-koeln.de/service/adressen/00757/index.html
- Haushaltsplan Band 3, S. 111: „Anzahl der erteilten Aufenthaltserlaubnisse" Plan 2025/2026: 28.000 (Ist 2022: 34.840; 2023: 26.600). Keine Dauer-Kennzahl.

### 2. Messgröße
Tage bis zum nächsten freien Termin je Bezirksausländeramt (Erteilung/Verlängerung Aufenthaltstitel), 1 Person.

### 3. Messung, konkret
- **Portal:** https://termine.stadt-koeln.de/m/Auslaenderamt/extern/calendar/?uid=a8035e3c-9559-4ac6-b328-59c3d5cc7113 — **ohne Login**, vier Schritte (Anliegen → Termin → Daten → Bestätigung); Zuständigkeit über PLZ-Abfrage auf der Stadtseite. Screenshot des Kalenders = Beleg.
- **Rhythmus:** 1. Werktag, 10:00 Uhr, je Bezirksamt eine Abfrage (~10 Minuten für alle).
- **Veröffentlicht die Stadt Zahlen?** Nein (nur Jahres-Fallzahl im Haushaltsplan). FragDenStaat (https://fragdenstaat.de/behoerde/18010/auslaenderamt-stadt-koeln/): 12 Anfragen, keine zu Wartezeiten.

### 4. Presse 2025/2026
- Keine Berichte 2025/2026 mit Zahlen zu Aufenthaltstitel-Terminen gefunden (nur Drittanbieter-Blogs ohne Zahlen: terminli.de „wochenlang nur gähnende Leere oder graue Felder"). Presse 2026 zum Ausländeramt betrifft die Abschiebepraxis (nachrichtenlokal.de, aktualisiert 13.08.2026: https://nachrichtenlokal.de/koelner-auslaenderamt-unter-druck-ermittlungen-drohen/), nicht Wartezeiten.

### 5. Bewertung
- **Messbarkeit: 4** — Portal offen, Wert ablesbar; das Portal ist erst seit 20.04.2026 in Betrieb, also noch keine Erfahrung, ob dort überhaupt Slots erscheinen.
- **Risiko: hoch.** Keine bezifferte Zusage der Stadt — die Wette könnte nur gegen „können Sie sich online selbst einen Termin buchen" laufen (Ja/Nein: ist innerhalb von X Tagen ein Termin buchbar?). Personalausfall Mülheim zeigt, dass Standorte ausfallen. Ethisch heikel: Testbuchungen blockieren echte Slots — nur Kalender ansehen, nie buchen.

---

## Kandidat 5 — Einbürgerung: Wartezeit auf einen Termin (Selbstauskunft der Stadt)

### 1. Zusage der Stadt
- Seite „Einbürgerung in den deutschen Staatsverband", wörtlich: „Aktuell beträgt die Wartezeit auf einen Termin ungefähr 12 Monate." Weiter (sinngemäß, Wortlaut über Fetch nur teilweise abrufbar): Die Stadt meldet sich etwa 5 Monate vor einem freien Termin bei den Antragstellern. URL: https://www.stadt-koeln.de/service/produkte/00547/index.html (kein Datumsstempel auf der Seite).
- Seite „Einbürgerung" (Adresse), wörtlich: „Termine für 2025 werden schrittweise vergeben, dennoch kommt es auf Grund des erheblich gestiegenen Interesses an einer Einbürgerung weiter zu Wartezeiten." URL: https://www.stadt-koeln.de/service/adressen/00228/index.html
- FAQ Einbürgerung, wörtlich: „Wir können Ihnen nicht sagen, wie lange Ihr Einbürgerungsverfahren dauert." URL: https://www.stadt-koeln.de/artikel/73681/index.html
- Haushaltsplan Band 3, S. 111: „Anzahl der vollzogenen Einbürgerungen" Plan 2025: 7.000, Plan 2026: 8.000 (Ist 2023: 3.800) — das ist die eigentliche Zusage: Verdopplung des Durchsatzes.

### 2. Messgröße
(a) Die von der Stadt selbst genannte Wartezeit in Monaten auf Seite 00547 — monatlich ablesen, Änderungen datieren (Wayback-Snapshot als Beleg). (b) Jahreszahl vollzogener Einbürgerungen gegen Plan 7.000/8.000 (nur jährlich, Jahresabschluss/Haushalt).

### 3. Messung, konkret
- Seite ohne Login; Wert steht im Text. Monatlich: Seite aufrufen, Satz kopieren, Wayback-Snapshot auslösen (web.archive.org/save/…). 2 Minuten.
- Die Stadt veröffentlicht keine Monatszahlen; Jahreszahl im Haushaltsplan/Jahresabschluss.

### 4. Presse 2025/2026
- Aktuellste Zahlen stammen von **2024**: t-online 21.10.2024 „Chaos in Köln: Einbürgerungsanträge überlasten Stadtverwaltung, 16 Monate Wartezeit": bis zu 16 Monate auf einen Termin, etwa 8.000 unbearbeitete Anmeldungen, 25 Sachbearbeiter, 40 neue Stellen geplant. URL: https://koeln.t-online.de/region/koeln/id_100513824/koeln-chaos-bei-einbuergerung-wohl-8000-antraege-unbearbeitet.html
- WDR aktuell (YouTube): „Einbürgerungen im Kölner Ausländeramt: Mehr als 1 Jahr Wartezeit" (Datum über Fetch nicht ermittelbar). URL: https://www.youtube.com/watch?v=18opSkBib0k
- Sekundärquelle leben-test.de, 06.05.2026: Köln „12–18 Monate", „Trend: steigend" (Ratgeberseite, keine Primärquelle). URL: https://www.leben-test.de/ratgeber/einbuergerung-bearbeitungszeit-stadt-vergleich-2026
- 2025/2026 kein Primär-Pressebericht mit Zahl gefunden (ksta/wdr nicht crawlbar).

### 5. Bewertung
- **Messbarkeit: 3** — trivial ablesbar, aber es ist die Selbstauskunft der Stadt, keine Messung; ändert sich vermutlich nur alle paar Monate.
- **Risiko: mittel.** Die Stadt kann den Satz jederzeit streichen statt aktualisieren. Als Wette taugt eher die Haushaltszahl (7.000 Einbürgerungen 2025 / 8.000 in 2026 gegen Ist 2023 = 3.800) — Auflösung aber erst mit dem Jahresabschluss, nicht monatlich.

---

## Ausgeschieden (kurz)

| Leistung | Zusage der Stadt (wörtlich) | Warum nicht monatlich messbar |
|---|---|---|
| Elterngeld | Band 3 S. 233: „durchschnittliche Bearbeitungsdauer von Anträgen auf Elterngeld in Tagen" Plan 40,00 (Ist 2022: 48,32; 2023: 42,31); Ziel „Die gesetzlich vorgeschriebene Bearbeitungsdauer ist eingehalten." Stadtseite 00793 nennt keine Dauer. | Nur durch eigenen Antrag oder Ratsanfrage messbar. Messbarkeit 1. |
| Wohngeld | Stadtseite 00704: „Es ist daher leider mit deutlich längeren Bearbeitungszeiten zu rechnen." (unbeziffert); PM 27.10.2022 (Wohngeldreform): „Es ist jedoch absehbar, dass es zu Verzögerungen kom[mt]"; keine Dauer-Kennzahl im Haushalt. | Keine Zahl, kein Portal. Messbarkeit 1. |
| Bauantrag | FAQ: „Die Bearbeitung dauert durchschnittlich vier bis neun Monate nach Eingang Ihres Antrages beim Bauaufsichtsamt." (https://www.stadt-koeln.de/leben-in-koeln/planen-bauen/haeufig-gestellte-fragen-zur-baugenehmigung); Band 3 S. 290: „Anteil der nach Antragseingang fristgerecht erteilten Baugenehmigungen in %" Ist 2022: 61, 2023: 27, Plan 50; PM 18.11.2024 (digitaler Bauantrag ab 01.01.2025, 4.491 Anträge in Q1–Q3 2024, 19 % digital in Q3): keine Zusage schnellerer Bearbeitung. | Jahreswert; Einzelner kann nichts ablesen. Messbarkeit 1. Aber: Ist 27 % (2023) gegen Plan 50 % ist eine gute Jahres-Wette. |
| Führerschein-Pflichtumtausch | Stadtseite 00031: Abholung „ohne Terminvereinbarung zehn Wochen" nach Antrag; Online-Antrag 6–8 Wochen (Fetch gekürzt). | Nur durch eigenen Antrag messbar. |
| Personalausweis-Lieferzeit | Stadtseite 00416: „Die Bearbeitung dauert in der Regel zwei bis drei Wochen." | Nur durch eigenen Antrag messbar. |

---

## Rangtabelle

| Rang | Kandidat | Zusage der Stadt (beziffert?) | Messbarkeit (1–5) | Risiko | Empfehlung |
|---|---|---|---|---|---|
| 1 | Kundenzentren — Wartezeit ohne Termin (Mo/Mi) | Ja: Plan 2025/2026 „20,00 Min." (Band 3 S. 101) | **5** | mittel (Selbstauskunft; Feed kann veralten; Stichprobe ≠ Jahresmittel) | **Hauptfall** |
| 2 | Kfz-Zulassungsstelle — Terminvorlauf | Ja: PM 01.07.2026 „kurzfristig", „keine unnötigen Wartezeiten mehr"; Plan „12,00" (Einheit unklar) | 4 | mittel–hoch (14-Tage-Fenster zensiert; Uhrzeitabhängig) | **Zweitfall**, parallel führen |
| 3 | Kundenzentren — Terminvorlauf Ausweis | Nein, nur Fenster „bis zu 60 Tage" + „immer wieder Terminbuchungen möglich" | 4 | hoch (keine Zahl, starke Tagesschwankung) | nur als Nebenreihe zu Rang 1 |
| 4 | Bezirksausländerämter — Terminvorlauf | Nein, nur „können Sie sich online selbst einen Termin buchen" (seit 20.04.2026) | 4 | hoch (keine Zahl, Portal neu, Standortausfälle) | beobachten, kein Fall |
| 5 | Einbürgerung — Wartezeit lt. Stadt | Ja, aber Selbstauskunft: „ungefähr 12 Monate"; Haushalt 7.000/8.000 Einbürgerungen | 3 | mittel (Satz kann verschwinden; Jahresauflösung) | Jahres-Wette auf Haushaltszahl, nicht Monatsfall |
| — | Elterngeld / Wohngeld / Bauantrag / Führerschein / Ausweis-Lieferzeit | teils ja (Elterngeld 40 Tage, Bau 50 %) | 1 | — | nur Jahres-Wetten über Haushaltsplan-Ist |

## Empfehlung

Hauptfall wird **Kandidat 1**: Die Stadt Köln hat im beschlossenen Haushaltsplan 2025/2026 (Band 3, S. 101) als einzige Bürgerservice-Kennzahl mit Zeitbezug eine „Durchschnittliche Wartezeit ohne Termin" von 20 Minuten als Plan 2025 und 2026 festgeschrieben und veröffentlicht den Ist-Wert dazu selbst live als Open Data (waiting-od.php), sodass ein Cron-Job an jedem Montag und Mittwoch die Zahl mit Zeitstempel einsammelt und der Monatsbeleg ohne eine einzige Behördenanfrage im Git liegt. Als Zweitfall parallel **Kandidat 2** (Kfz-Zulassungsstelle), weil die Zusage vom 01.07.2026 („kurzfristig", „keine unnötigen Wartezeiten mehr vor Ort") frisch, wörtlich und öffentlich ist und der nächste freie Termin im Portal ohne Login ablesbar bleibt — mit dem festgehaltenen Vermerk, dass das 14-Tage-Buchungsfenster den Messwert nach oben deckelt und die Haushaltskennzahl „12,00 Min." in ihrer Einheit unklar ist. Kandidaten 3 bis 5 scheitern nicht an der Messbarkeit, sondern daran, dass die Stadt sich dort auf keine Zahl festgelegt hat; sie taugen als Beobachtungsreihen und für Jahres-Wetten (Einbürgerungen 7.000/8.000, Baugenehmigungen 50 % fristgerecht, Elterngeld 40 Tage), nicht als monatlicher Fall.

### Entwurf für die Wettbuch-Kopfzeilen (zur Übernahme in festgehalten-Format)

**Fall A (Kandidat 1)**
- institution: Stadt Köln
- gesagt_von: Stadt Köln, Kämmerei (Haushaltsplan 2025/2026, Band 3, S. 101, Produktgruppe 0207)
- gesagt_am: 2024-11-14 (Einbringung; Beschluss Doppelhaushalt 2025/2026)
- quelle: https://www.stadt-koeln.de/mediaasset/content/pdf20/4_hpl_2025_2026_band_3.pdf
- zitat: „Durchschnittliche Wartezeit ohne Termin in Min. […] Plan 2026: 20,00"
- frage: Liegt der Mittelwert der von der Stadt Köln selbst veröffentlichten Wartezeiten (waiting-od.php, alle Kundenzentren, Montage und Mittwoche 09:00 und 11:00 Uhr) im Zeitraum 01.10.2026–30.09.2027 bei höchstens 20 Minuten?
- typ: ja_nein
- pruefung_am: 2027-10-01 (Zwischenstände monatlich)

**Fall B (Kandidat 2)**
- gesagt_von: Stadt Köln, Amt für Presse- und Öffentlichkeitsarbeit (PM 28528)
- gesagt_am: 2026-07-01
- quelle: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28528/index.html
- zitat: „Künftig können solche Kurzanliegen als Termin kurzfristig über die Internetseite der Stadt Köln […] gebucht beziehungsweise vereinbart werden. Neue Terminangebote für Kurzanliegen werden kontinuierlich freigeschaltet."
- frage: Ist am 1. Werktag jedes Monats um 10:00 Uhr im Terminportal der Kfz-Zulassungsstelle für „Fahrzeug abmelden" ein Termin innerhalb von 7 Kalendertagen buchbar? (Messreihe Oktober 2026 – März 2027; „kurzfristig" übersetzt als ≤ 7 Tage — Übersetzung offenlegen)
- typ: ja_nein je Monat
- pruefung_am: 2027-04-01
