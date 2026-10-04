# Buch „Gatekeeper gegen Gatekeeper“: Kandidaten (Recherche 03.10.2026)

Das hier ist eine Arbeitsliste und noch kein Bucheintrag. Recherchiert hat Claude im Auftrag des Halters am Sa 03.10.2026.
Die Felder folgen FORMAT.md §1.1/1.2. Erlaubte Werte für `art` sind laut FORMAT.md `angekuendigt` (Wert 1,00 bzw. bei
`punkt` die genannte Zahl), `voraussichtlich` (Wert 0,80 bei `ja_nein`, wenn die Aussage einen Vorbehalt trägt wie „expects“,
„plans“, „projected“) und `geschaetzt` (nur für Schätzende). Bei Finanzprognosen („we expect“, „we anticipate“) wird
durchgehend `voraussichtlich` gesetzt.

**Prüfmethode Wortlaut (für alle Kandidaten gleich):** Jede Quelle wurde am 03.10.2026 per `curl -sL --compressed`
(Browser-User-Agent) abgerufen. Bei HTML wurden `script`/`style` entfernt, alle übrigen Tags durch Leerzeichen ersetzt,
HTML-Entities aufgelöst, Whitespace zusammengefasst und Anführungszeichen, Gedankenstriche, geschützte Bindestriche (U+2011),
geschützte Leerzeichen sowie Soft-Hyphens normalisiert. PDFs wurden mit `pdftotext -enc UTF-8` in Text umgewandelt und dann
genauso normalisiert. Die Microsoft-Telefonkonferenz liegt nur als `.docx` vor, dort wurde `word/document.xml` entpackt und
von Tags befreit. Geprüft wurde dann `zitat in text` mit Ergebnis `True` (Skript `/tmp/gk/chk.py`, liegt nicht im Repo).
Ein Sonderfall ist 006 (Microsoft): Dort stehen Ländernamen in `<strong>`-Tags, die Tag-Ersetzung ergibt
„Switzerland , the United Arab Emirates , and“. Laut Roh-HTML steht `Switzerland</strong>, the&nbsp;<strong>United Arab
Emirates</strong>, and`, sichtbar also ohne Leerzeichen vor dem Komma, und so wird zitiert.

Vorgeschlagene IDs: `gatekeeper-2026-001` … `-010`. Institution jeweils wie in der Gatekeeper-Liste der Kommission.

---

## Auswahlliste (wer gemessen wird)

### (1) DMA-Gatekeeper

- **Quelle:** Europäische Kommission, „DMA designated Gatekeepers“, https://digital-markets-act.ec.europa.eu/gatekeepers_en
  (abgerufen 03.10.2026 per curl).
- **Wortlaut der Seite (Auszug):** „On 6 September 2023 the European Commission designated for the first time six gatekeepers -
  Alphabet, Amazon, Apple, ByteDance, Meta, Microsoft - under the Digital Markets Act (DMA).“ Danach: iPadOS (29.04.2024),
  Booking (13.05.2024), Entbenennung von Facebook Marketplace (23.04.2025). „In total, 23 core platform services provided by
  those gatekeepers are currently designated.“
- **Liste (7 Gatekeeper):**

| Gatekeeper (wie auf der Seite) | Benannte zentrale Plattformdienste |
|---|---|
| Alphabet Inc. | Google Play, Google Maps, Google Shopping, Google Search, YouTube, Android Mobile, Online-Werbung, Google Chrome |
| Amazon.com Inc. | Marketplace, Amazon Advertising |
| Apple Inc. | App Store, iOS, Safari, iPadOS |
| Booking | Online-Vermittlungsdienste (Booking.com) |
| ByteDance Ltd. | TikTok |
| Meta Platforms, Inc. | Facebook, Instagram, WhatsApp, Messenger, Meta Ads, Marketplace (entbenannt 23.04.2025) |
| Microsoft Corporation | LinkedIn, Windows PC OS |

### (2) GPAI-Anbieter mit systemischem Risiko (AI Act)

- **Ergebnis: ungeklärt, keine öffentliche Liste gefunden.**
- Rechtsgrundlage: Art. 52 Abs. 6 AI Act verpflichtet die Kommission, eine solche Liste zu veröffentlichen. Wortlaut auf dem
  AI Act Service Desk der Kommission (https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-52, abgerufen 03.10.2026):
  „… list of general-purpose AI models with systemic risk is published and shall keep that list up to date …“.
- Abgesucht am 03.10.2026, jeweils ohne eine solche Liste:
  - AI Office, https://digital-strategy.ec.europa.eu/en/policies/ai-office (Stand laut Seite 8. September 2026)
  - Regulatory framework AI, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (Stand 3. August 2026)
  - Guidelines for providers of GPAI models, https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers (Stand 28. April 2026)
  - GPAI-FAQ, https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers (Stand 9. September 2025)
  - Websuche nach einer veröffentlichten Liste nach Art. 52 Abs. 6 (ohne Treffer)
- Öffentlich ist nur die **Liste der Unterzeichner des GPAI-Verhaltenskodex**
  (https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai, Stand 31. Juli 2026). Sie ist keine Liste der Modelle mit
  systemischem Risiko und taugt nach der Auswahlregel nicht als Ersatz.
- **Folge für dieses Buch:** Es misst vorerst nur die sieben DMA-Gatekeeper. Sobald die Kommission die Liste nach Art. 52 Abs. 6
  veröffentlicht, kommen deren Anbieter hinzu, ohne Ermessen.

---

## gatekeeper-2026-001 · Alphabet: Investitionen 2026 zwischen 195 und 205 Mrd. Dollar

- **institution:** Alphabet
- **gesagt_von:** Alphabet Inc. (Anat Ashkenazi, SVP und CFO, Telefonkonferenz zum zweiten Quartal 2026)
- **gesagt_am:** 2026-07-22
- **quelle:** https://s206.q4cdn.com/479360582/files/doc_events/2026/Jul/22/2026_Q2_Earnings_Transcript.pdf (verlinkt von der Event-Seite https://abc.xyz/investor/events/event-details/2026/2026-Q2-Earnings-Call-2026-GgTAq7Is0z/default.aspx)
- **zitat:** „Moving to investments, we are updating our full year 2026 CapEx guidance range to $195‑205 billion, up from our previous estimate of $180‑190 billion.“
- **Wortlaut geprüft:** ja (PDF per curl, pdftotext, `True`; im PDF stehen geschützte Bindestriche U+2011)
- **frage:** Liegen die Investitionsausgaben (CapEx) von Alphabet für das Gesamtjahr 2026 laut Jahreszahlen zwischen 195 und 205 Mrd. US-Dollar (jeweils einschließlich)?
- **typ:** ja_nein · **pruefung_am:** 2027-02-15
- **art (Alphabet):** `voraussichtlich` („guidance range“, eine Prognose) → **wert 0,80**
- **Übersetzung:** Gemessen wird die CapEx-Zahl 2026, die Alphabet mit den Zahlen zum vierten Quartal 2026 nennt (Anfang Februar
  2027), ersatzweise „Purchases of property and equipment“ aus der Kapitalflussrechnung. Unter 195,0 oder über 205,0 Mrd. $ ist
  Nein. Eine Anhebung der Spanne im Oktober 2026 ändert die Wette nicht (FORMAT §1.3 Nr. 5), sie wäre eine neue Wette.
- **Kontext:** Im zweiten Quartal 2026 lag die CapEx laut derselben Konferenz bei 44,9 Mrd. $ („CapEx was $44.9 billion in the
  second quarter“). Die Spanne wurde schon zweimal angehoben. Ashkenazi begründete das mit einer „acceleration in the delivery of
  capacity“. Medien (Motley Fool, 11.08.2026) melden einen Kursrückgang von 7 % nach der Anhebung. Zwillingswette möglich: „we
  continue to expect our CapEx to increase significantly in 2027“ (gleiche Quelle, Wortlaut geprüft).
- **Computer: 0,55.** Die Spanne ist mit 10 Mrd. $ eng, und Alphabet hat 2025 und 2026 immer wieder nach oben korrigiert. Für das
  zweite Halbjahr müssten rund 57–62 Mrd. $ pro Quartal anfallen. Steigende Speicherpreise und Lieferengpässe ziehen in
  verschiedene Richtungen. Eine weitere Anhebung über 205 Mrd. $ ist das Hauptrisiko.

---

## gatekeeper-2026-002 · Alphabet: Google in Deutschland 2026 bei rund 85 % CO₂-freiem Strom

- **institution:** Alphabet
- **gesagt_von:** Google (Pressemitteilung „Google Announces €5.5 Billion Investment in Germany“, Google Cloud Press Corner)
- **gesagt_am:** 2025-11-11
- **quelle:** https://www.googlecloudpresscorner.com/2025-11-11-Google-Announces-EUR5-5-Billion-Investment-in-Germany,-including-AI-Infrastructure,-through-2029
- **zitat:** „Leveraging the CFE Manager and Google's other clean energy initiatives, Google's German operations are projected to run at or near 85% carbon-free energy in 2026“
- **Wortlaut geprüft:** ja (curl, `True`). Die Seite hängt eine Fußnote an: „Actual CFE score achieved may vary …“
- **frage:** Weist Google für das Jahr 2026 für seine deutschen Cloud-Regionen (europe-west3 Frankfurt und europe-west10 Berlin) einen „Google CFE%“ von mindestens 83 % aus?
- **typ:** ja_nein · **pruefung_am:** 2027-08-01
- **art (Alphabet):** `voraussichtlich` („projected“, dazu „at or near“) → **wert 0,80**
- **Übersetzung:** Beleg ist Googles Tabelle „Carbon free energy for Google Cloud regions“
  (https://cloud.google.com/sustainability/region-carbon) mit den Jahresdaten 2026 oder der Umweltbericht 2027. „At or near 85 %“
  wird als ≥ 83 % übersetzt. Weisen die beiden Regionen unterschiedliche Werte aus, zählt der niedrigere. Liegen die Daten 2026 zum
  `pruefung_am` noch nicht vor, wird gewartet (Verfall nach FORMAT).
- **Kontext:** Für 2025 nennt dieselbe Google-Tabelle (abgerufen 03.10.2026, „provided the 2025 data below“) für Frankfurt und
  Berlin jeweils 70 %. Verlangt ist also ein Sprung um 15 Punkte in einem Jahr. Mittel dazu sind laut Pressemitteilung der
  erweiterte CFE-Vertrag mit Engie (bis 2030, mit Batteriespeichern) und die Abnahme aus dem Offshore-Windpark Borkum Riffgrund 3
  (Ørsted).
- **Computer: 0,30.** 15 Punkte in einem Jahr sind viel, und das deutsche Netz wird wegen Dunkelflauten nur langsam CO₂-ärmer.
  Gleichzeitig wächst Googles Verbrauch in Deutschland durch den Ausbau in Hanau und Dietzenbach. Dass Google selbst eine
  Fußnote mit Vorbehalt angehängt hat, spricht ebenfalls gegen das Ziel.

---

## gatekeeper-2026-003 · Amazon: Verteilzentrum Ensisheim (Elsass) startet Ende 2027

- **institution:** Amazon
- **gesagt_von:** Amazon (About Amazon Team, aboutamazon.eu, „Amazon announces plans to invest more than €15 billion in France“)
- **gesagt_am:** 2026-05-05
- **quelle:** https://www.aboutamazon.eu/news/job-creation-and-investment/amazon-announces-plans-to-invest-more-than-15-billion-in-france-creating-more-than-7-000-permanent-jobs
- **zitat:** „Job creation begins as early as 2026, with the upcoming opening of three distribution centres in Illiers-Combray (1,000 permanent jobs), Beauvais (1,000 permanent jobs), and Colombier-Saugnieu (3,000 jobs permanent jobs) and the launch in late 2027 of a distribution centre in Ensisheim (2,000 permanent jobs).“
- **Wortlaut geprüft:** ja (curl, `True`, einschließlich des Tippfehlers „3,000 jobs permanent jobs“ im Original)
- **frage:** Hat Amazons Verteilzentrum in Ensisheim (Haut-Rhin) bis zum 31.12.2027 den Betrieb aufgenommen, also erste Kundensendungen bearbeitet?
- **typ:** ja_nein · **pruefung_am:** 2028-01-01
- **art (Amazon):** `angekuendigt` („the launch in late 2027“, ohne Vorbehalt) → **wert 1,00**
- **Übersetzung:** Ja nur, wenn Amazon (aboutamazon.fr/.eu) oder regionale Medien bis zum Stichtag die Eröffnung bzw. den
  Betriebsstart melden. Fertiger Bau ohne Betrieb, eine reine Einweihung ohne Betrieb oder ein Start im Jahr 2028 ist Nein. Die
  Zahl der Stellen wird nicht geprüft.
- **Kontext:** Das Projekt war seit 2019 umstritten. Laut Medien (rue89strasbourg, LSA) hat die Cour administrative d'appel de
  Nancy die Baugenehmigung am 11.09.2025 bestätigt, und die Klage gegen die Umweltgenehmigung wurde am 17.02.2025 abgewiesen
  (TA Strasbourg). Alsace Nature und Les Amis de la Terre waren die Kläger. Die drei anderen Zentren aus dem Zitat sollten laut
  aboutamazon.fr im September 2026 öffnen, Colombier-Saugnieu ist laut Medien (brefeco) bereits eingeweiht. Sie sind deshalb
  nicht als Wette aufgenommen.
- **Computer: 0,60.** Die Rechtswege sind weitgehend durch, und die anderen drei französischen Zentren hat Amazon offenbar pünktlich
  geöffnet. Das Fenster „late 2027“ lässt aber kaum Spielraum, und große Logistikbauten verzögern sich leicht um ein Quartal. Ein
  Start Anfang 2028 wäre schon Nein.

---

## gatekeeper-2026-004 · Apple: Live Rewind (Apple Watch) startet Ende 2026 als Beta

- **institution:** Apple
- **gesagt_von:** Apple Newsroom („Siri AI, a profoundly more capable and personal assistant … is here“)
- **gesagt_am:** 2026-09-14
- **quelle:** https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/
- **zitat:** „Live Rewind will be available in beta in late 2026, and requires Apple Watch Series 12 or Apple Watch Ultra 4, paired with an Apple Intelligence-enabled iPhone 16 or later (excluding iPhone 16e).“
- **Wortlaut geprüft:** ja (curl, `True`; ebenso „Siri Recap and Live Rewind arrive in beta later this year.“ `True`)
- **frage:** Ist die Funktion „Live Rewind“ bis zum 31.12.2026 in einer öffentlich ausgelieferten (Nicht-Entwickler-)Version von watchOS/iOS für Nutzer in mindestens einem Land als Beta nutzbar?
- **typ:** ja_nein · **pruefung_am:** 2027-01-01
- **art (Apple):** `angekuendigt` („will be available“) → **wert 1,00**
- **Übersetzung:** Beta zählt, solange sie in einem regulären Software-Update für alle Nutzer mit passendem Gerät steckt (wie
  Apples „beta“-Kennzeichnung bei Siri AI). Eine reine Entwickler- oder Public-Beta des Betriebssystems ist Nein. Die EU ist laut
  Apple ausgenommen und spielt für die Wette keine Rolle.
- **Kontext:** Laut gleicher Seite gilt: „It will be available in English to start and will not initially be available in the
  EU.“ Siri AI selbst kam am 14.09.2026 auf iPhone und iPad nicht in die EU (Apple Newsroom 08.06.2026: „Due to DMA, Siri AI
  delayed in EU for iOS 27 and iPadOS 27“). 2025 hatte Apple angekündigte Siri-Funktionen um ein Jahr verschoben.
- **Computer: 0,70.** Apple liefert „later this year“-Funktionen meist mit dem x.2-Update im Dezember aus, und die Hardware ist
  schon im Handel. Die Funktion hängt aber an Servermodellen mit Nutzungsgrenzen, und 2025 hat Apple ein Siri-Versprechen
  gebrochen. Das Restrisiko liegt bei einer Verschiebung in den Januar.

---

## gatekeeper-2026-005 · Apple: Kein Plastik mehr in der Verpackung von Refurbished-Produkten bis 2027

- **institution:** Apple
- **gesagt_von:** Apple (Environmental Progress Report 2026, für das Geschäftsjahr 2025)
- **gesagt_am:** 2026-04-16 (Veröffentlichung laut Apple Newsroom „Apple accelerates progress with highest-ever recycled material in its products“, April 2026; genaues Datum bitte vor dem Eintragen gegenprüfen)
- **quelle:** https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2026.pdf
- **zitat:** „We plan to remove plastic from the packaging of refurbished products by 2027, once old product packaging designs are phased out.“
- **Wortlaut geprüft:** ja (PDF per curl, pdftotext, `True`)
- **frage:** Erklärt Apple in seinem nächsten Umweltbericht, der das Jahr 2027 abdeckt, die Verpackung von Refurbished-Produkten bis Ende 2027 vollständig plastikfrei gemacht zu haben (in der Abgrenzung des Berichts)?
- **typ:** ja_nein · **pruefung_am:** 2028-01-01
- **art (Apple):** `voraussichtlich` („We plan“) → **wert 0,80**
- **Übersetzung:** „By 2027“ wird als „bis spätestens 31.12.2027“ gelesen. Beleg ist Apples Environmental Progress Report 2028
  (erwartet etwa April 2028), ersatzweise eine frühere Apple-Erfolgsmeldung. Meldet Apple nur einen Teilfortschritt (z. B. „most“)
  oder schweigt der Bericht, ist das Nein. Die Ausnahmen, die Apple für das Plastikziel 2025 definiert hat (Tinten, Beschichtungen,
  Klebstoffe), gelten auch hier.
- **Kontext:** Das Ziel „plastikfreie Verpackung bis 2025“ für Neuprodukte hat Apple laut gleichem Bericht erfüllt (100 %
  faserbasierte Verpackung). Refurbished-Produkte wurden ausdrücklich nachgelagert, weil alte Verpackungsdesigns erst auslaufen
  müssen. Gegenstimmen mit Quelle wurden nicht gefunden.
- **Computer: 0,65.** Apple hat das Hauptziel erfüllt, und der Rest betrifft nur das Auslaufen alter Kartons. „By 2027“ ist
  aber dehnbar, und ein Bericht kann still auf „2028“ verschieben. Der Beleg kommt erst gut vier Monate nach `pruefung_am`.

---

## gatekeeper-2026-006 · Booking: Einsparungen von rund 650 Mio. Dollar jährlich bis Ende 2027

- **institution:** Booking
- **gesagt_von:** Booking Holdings Inc. (Pressemitteilung zum zweiten Quartal 2026)
- **gesagt_am:** 2026-08-04
- **quelle:** https://s25.q4cdn.com/383369491/files/doc_news/2026/08/Q2-26-BKNG-Earnings-Release-Final.pdf
- **zitat:** „Increased our expected annual run-rate savings through the Transformation Program(1) to approximately $650 million, and expect to realize these run-rate savings by the end of 2027.“
- **Wortlaut geprüft:** ja (PDF per curl, pdftotext, `True`; „(1)“ ist ein Fußnotenzeichen im Original). Ein zweiter Abruf
  derselben Datei über `s201.q4cdn.com` lieferte 403, die SEC-Fassung (8-K) war per Bot-Sperre blockiert.
- **frage:** Meldet Booking Holdings mit den Zahlen zum vierten Quartal 2027, bis Ende 2027 annualisierte Run-Rate-Einsparungen aus dem Transformation Program von mindestens 600 Mio. US-Dollar realisiert zu haben?
- **typ:** ja_nein · **pruefung_am:** 2028-03-01
- **art (Booking):** `voraussichtlich` („expect to realize“) → **wert 0,80**
- **Übersetzung:** „Approximately $650 million“ wird als ≥ 600 Mio. $ übersetzt. Beleg ist die Q4-2027-Pressemitteilung (ca. Ende
  Februar 2028) oder eine frühere Booking-Meldung. Nennt Booking dort nur ein Ziel und keinen realisierten Wert, ist das Nein.
  Spätere Anhebungen ändern die Wette nicht.
- **Kontext:** Booking hat die Zielgröße des Programms laut eigener Pressemitteilung im Q2 2026 angehoben („Increased our
  expected …“). Gegenstimmen mit Quelle wurden nicht gefunden. Die Abgrenzung von „run-rate savings“ legt Booking selbst fest,
  das macht die Zahl schwer prüfbar.
- **Computer: 0,75.** Wer ein Sparziel im laufenden Programm anhebt, liegt in der Regel vor dem Plan, und Booking definiert die
  Messgröße selbst. Unsicher ist vor allem, ob Booking im Februar 2028 überhaupt eine realisierte Zahl nennt.

---

## gatekeeper-2026-007 · Meta: Investitionen 2026 zwischen 130 und 145 Mrd. Dollar

- **institution:** Meta
- **gesagt_von:** Meta Platforms, Inc. (Pressemitteilung „Meta Reports Second Quarter 2026 Results“, Abschnitt „CFO Outlook Commentary“)
- **gesagt_am:** 2026-07-29
- **quelle:** https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx
- **zitat:** „We anticipate 2026 capital expenditures, including principal payments on finance leases, to be in the range of $130-145 billion, narrowed from our prior outlook of $125-145 billion.“
- **Wortlaut geprüft:** ja (curl, `True`)
- **frage:** Liegen Metas Investitionsausgaben 2026 einschließlich Tilgung von Finanzierungsleasing laut Jahreszahlen zwischen 130 und 145 Mrd. US-Dollar (jeweils einschließlich)?
- **typ:** ja_nein · **pruefung_am:** 2027-02-15
- **art (Meta):** `voraussichtlich` („We anticipate“) → **wert 0,80**
- **Übersetzung:** Gemessen wird die Summe aus „Purchases of property and equipment“ und „Principal payments on finance leases“ für
  das Gesamtjahr 2026 aus der Kapitalflussrechnung der Q4-Pressemitteilung (ca. Ende Januar 2027).
- **Kontext:** Laut derselben Pressemitteilung betrug die Summe im ersten Halbjahr 2026 rund 50,9 Mrd. $ (49,113 + 1,805 Mrd.).
  Für das zweite Halbjahr bleiben damit 79–94 Mrd. $, also deutlich mehr als die 31,08 Mrd. $ aus dem zweiten Quartal. Als Gründe
  für die angehobene Untergrenze nennen Medien (remio.ai u. a.) höhere Komponentenpreise.
- **Computer: 0,65.** Meta hat die Spanne verengt statt angehoben, das deutet auf Planungssicherheit hin. Für die Untergrenze ist
  aber ein kräftiger Anstieg im zweiten Halbjahr nötig. Bei Lieferverzögerungen von Servern könnte die Zahl unter 130 Mrd. $ fallen.

---

## gatekeeper-2026-008 · Meta: Gesamtkosten 2026 zwischen 165 und 169 Mrd. Dollar

- **institution:** Meta
- **gesagt_von:** Meta Platforms, Inc. (wie 007, „CFO Outlook Commentary“)
- **gesagt_am:** 2026-07-29
- **quelle:** https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx
- **zitat:** „We now expect full year 2026 total expenses to be in the range of $165-169 billion.“
- **Wortlaut geprüft:** ja (curl, `True`)
- **frage:** Liegen Metas „Total costs and expenses“ für das Gesamtjahr 2026 laut Jahreszahlen zwischen 165 und 169 Mrd. US-Dollar (jeweils einschließlich)?
- **typ:** ja_nein · **pruefung_am:** 2027-02-15
- **art (Meta):** `voraussichtlich` („We now expect“) → **wert 0,80**
- **Übersetzung:** Maßgeblich ist die GAAP-Zeile „Total costs and expenses“ in der Q4-2026-Pressemitteilung. Einmaleffekte, etwa aus
  Rechtsstreitigkeiten, zählen mit, so wie Meta sie selbst einrechnet.
- **Kontext:** Im ersten Halbjahr 2026 lagen die Kosten bei 75,464 Mrd. $, für das zweite Halbjahr bleiben 89,5–93,5 Mrd. $. Meta
  hob die Untergrenze wegen Rechtskosten von 2,4 Mrd. $ im zweiten Quartal an und nennt in derselben Mitteilung anstehende
  Jugendschutzprozesse in den USA, die „may ultimately result in a material loss“. Das ist ein Risiko nach oben.
- **Computer: 0,55.** Die Spanne beträgt nur 4 Mrd. $ bei fast 170 Mrd. $ Kosten. Neue Rechtskosten aus den Jugendschutzprozessen
  könnten die Obergrenze sprengen, Verzögerungen beim Personal- und Rechenaufbau dagegen die Untergrenze verfehlen lassen.

---

## gatekeeper-2026-009 · Microsoft: Zweistelliges Umsatz- und Gewinnwachstum im Geschäftsjahr 2027

- **institution:** Microsoft
- **gesagt_von:** Microsoft Corporation (Amy Hood, EVP und CFO, Telefonkonferenz zum vierten Quartal des Geschäftsjahres 2026)
- **gesagt_am:** 2026-07-29
- **quelle:** https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY26Q4.docx (verlinkt als https://aka.ms/transcriptfy26q4 von https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- **zitat:** „At the company level, with strong commercial momentum, we continue to expect another fiscal year of double-digit revenue and operating income growth.“
- **Wortlaut geprüft:** ja (docx per curl, `word/document.xml` ohne Tags, normalisiert, `True`)
- **frage:** Wachsen Microsofts Umsatz und operatives Ergebnis (GAAP) im Geschäftsjahr 2027 (Juli 2026 bis Juni 2027) jeweils um mindestens 10 % gegenüber dem Geschäftsjahr 2026?
- **typ:** ja_nein · **pruefung_am:** 2027-08-15
- **art (Microsoft):** `voraussichtlich` („we continue to expect“) → **wert 0,80**
- **Übersetzung:** Beide Werte müssen ≥ 10,0 % wachsen, gemessen an den GAAP-Zahlen der Q4-FY27-Pressemitteilung (ca. Ende Juli 2027).
  Weist Microsoft „non-GAAP“ oder um Sondereffekte bereinigte Zahlen aus, zählt GAAP. Liegt einer der beiden Werte darunter, ist
  das Nein.
- **Kontext:** Laut Medien (Yahoo Finance, Konferenz-Highlights, 30.07.2026) wuchs der Umsatz im GJ 2026 um 18 % auf rund 331 Mrd. $,
  das operative Ergebnis um 21 %. In derselben Konferenz erwartet Hood für das GJ 2027 einen Umsatzrückgang im „high-teens“-Bereich
  bei Windows OEM und Devices sowie Rückgänge im mittleren einstelligen Bereich bei M365 Commercial products und Server products.
  Die Nutzungsdauer von Rechenzentren wird ab GJ 2027 von 15 auf 25 Jahre verlängert, was das operative Ergebnis leicht stützt.
- **Computer: 0,80.** Microsoft hat dieses Ziel in den letzten Jahren regelmäßig erreicht, Azure wächst über 40 %, und der Abstand
  zur 10-%-Schwelle ist groß. Risiken sind steigende Abschreibungen aus dem KI-Ausbau, die das operative Ergebnis drücken, und eine
  schwache PC-Nachfrage.

---

## gatekeeper-2026-010 · Microsoft: Copilot-Datenverarbeitung in Deutschland im Jahr 2026 (inzwischen zurückgenommen)

- **institution:** Microsoft
- **gesagt_von:** Microsoft (Paul Lorimer, Microsoft 365 Copilot Blog, „Microsoft offers in-country data processing to 15 countries …“)
- **gesagt_am:** 2025-11-04
- **quelle:** https://www.microsoft.com/en-us/copilot/blog/2025/11/04/microsoft-offers-in-country-data-processing-to-15-countries-to-strengthen-sovereign-controls-for-microsoft-365-copilot/
- **zitat:** „In 2026, we'll expand this option to customers in eleven more countries including Canada, Germany, Italy, Malaysia, Poland, South Africa, Spain, Sweden, Switzerland, the United Arab Emirates, and the United States.“
- **Wortlaut geprüft:** ja, mit Sonderfall `<strong>`-Tags (siehe Prüfmethode oben): Die Tag-Ersetzung ergibt Leerzeichen vor zwei
  Kommas, laut Roh-HTML steht sichtbar „Switzerland, the United Arab Emirates, and“. Der Satz steht weiterhin auf der Seite, und
  zwar unter der „Editor's note“ vom 03.04.2026.
- **frage:** Können Kunden in Deutschland bis zum 31.12.2026 wählen, dass ihre Microsoft-365-Copilot-Interaktionen in Rechenzentren in Deutschland verarbeitet werden (in-country, nicht nur innerhalb der EU)?
- **typ:** ja_nein · **pruefung_am:** 2027-01-01
- **art (Microsoft):** `angekuendigt` („we'll expand“, ohne Vorbehalt) → **wert 1,00**
- **Übersetzung:** Ja nur, wenn Microsoft-Dokumentation oder -Blog am Stichtag eine In-Country-Option für Deutschland als
  verfügbar ausweist. Eine Verarbeitung auf EU-/EFTA-Ebene („regional level“) ist Nein. Nach FORMAT §1.3 Nr. 5 bleibt die
  zurückgenommene Aussage eine Wette.
- **Kontext:** In der „Editor's note - April 3, 2026 update“ auf derselben Seite (Wortlaut geprüft, `True`) schreibt Microsoft: „As
  an update to our earlier announcement, local inferencing will be delivered at a regional level for countries in the European
  Union (EU) and European Free Trade Association (EFTA), aligned with our commitments under the EU Data Boundary.“ Bis Ende 2026
  sind demnach nur Australien, Indien, VAE, Großbritannien und die USA vorgesehen. heise.de (Nov. 2025) hatte für deutsche Nutzer
  noch eine Verarbeitung „ausschließlich in deutschen Rechenzentren“ ab Ende 2026 gemeldet.
- **Computer: 0,03.** Microsoft hat die Zusage für EU-Länder selbst in eine EU-weite Verarbeitung umgewandelt. Ein Ja würde eine
  erneute Kehrtwende binnen weniger Monate verlangen. Die Wette misst genau das, was dieses Buch messen soll: ob eine
  Gatekeeper-Ankündigung mit Datum gehalten wird.

---

## Verworfene Kandidaten

| Gatekeeper · Thema | Grund |
|---|---|
| ByteDance · Rechenzentrum Kouvola „bis Ende 2026“, Lahti „2027“ (Project Clover) | Die Daten stehen nur in Medien (TechRepublic, CNBC 08.09.2026). Die TikTok-Newsroom-Seiten (06.05.2025 `/en-eu/finlanddatacenter`, 11.09.2025 `/en-eu/cornerstonefinland`, 08.04.2026 Lahti) nennen geprüft **kein** Datum. Die Kapazitäts- und Terminangaben vom Sept. 2026 stammen aus einem von TikTok beauftragten Gutachten, nicht aus einer eigenen Mitteilung. **Damit hat ByteDance vorerst keinen Kandidaten.** |
| ByteDance · TikTok Shop in AT/BE/NL/PL (28.05.2026), EU-Wirtschaftszahlen (19.01.2026) | Ohne künftiges Datum oder Ziel. |
| Apple · Siri AI für EU-Nutzer auf macOS 27 und visionOS 27 (Newsroom 08.06.2026, Wortlaut vorhanden) | Bereits eingetreten: macOS 27 erschien am 14.09.2026, laut Apple-Support (support.apple.com/en-us/127893) ist Siri AI auf dem Mac in der EU verfügbar (nur Englisch). |
| Apple · Siri AI in Französisch, Japanisch, Koreanisch, Portugiesisch, Spanisch „next month“ (Newsroom 14.09.2026) | Stichtag Oktober 2026, also vor dem Fenster Nov. 2026 bis Ende 2027. Deutsch wird nicht genannt. |
| Apple · alternative ATT-Abfrage in der EU „Beginning with iOS 27.2“ (Developer News 16.09.2026) | Versionsnummer statt Datum. |
| Apple · neue EU-Geschäftsbedingungen ab 01.10.2026 (Developer News 18.08.2026) | Stichtag vorbei. |
| Apple · Siri AI auf iPhone/iPad in der EU | Apple nennt ausdrücklich keinen Termin („we do not currently have a timeline“). |
| Microsoft · „more than 200 datacenters on the continent by 2027“, Kapazität +40 % (Blog 29.04.2026, Wortlaut vorhanden) | Microsoft veröffentlicht keine laufende Zählung seiner europäischen Rechenzentren, und „by 2027“ ist offen. Ohne Beleg wäre die Wette faktisch nicht auflösbar. |
| Microsoft · „we expect FY27 capital expenditures will grow year-over-year“ (Wortlaut geprüft) | Microsoft verlagert ab GJ 2027 Leasing von Finance- zu Operating-Leases, die CapEx-Abgrenzung ändert sich nach eigener Aussage. Der Vergleich mit dem Vorjahr wäre strittig. |
| Microsoft · Rechenzentren Bergheim/Bedburg/Elsdorf (NRW) | Microsoft nennt keinen Termin, nur Bürgermeister und Kommunalpolitik (Medien). |
| Microsoft · lokale Copilot-Verarbeitung in AU/IN/VAE/UK/USA „by the end of 2026“ (Editor's note 03.04.2026) | Ohne EU-Bezug. Als Zwillingswette zu 010 möglich. |
| Amazon · drei Verteilzentren in Frankreich 2026 (Illiers-Combray, Beauvais, Colombier-Saugnieu) | Laut aboutamazon.fr für September 2026 angekündigt, Colombier-Saugnieu laut Medien bereits eingeweiht. Kaum Unsicherheit. |
| Amazon · CapEx 2026 „approximately $220 billion“ (Jassy, Telefonkonferenz 30.07.2026) | Steht nur in der Konferenz. Amazon veröffentlicht kein eigenes Transkript, die Pressemitteilung enthält keine Jahres-CapEx. Wortlaut nur über Medien (CNBC). |
| Amazon · Amazon Leo kommerziell „mid-2026“ (Aktionärsbrief April 2026, laut Medien) | Termin vorbei. Für Deutschland und Frankreich wurde kein eigenes Amazon-Datum gefunden. |
| Amazon · AWS Sovereign Local Zones in Belgien, Niederlanden, Portugal (Presse 15.01.2026, Wortlaut geprüft) | Ohne Datum. |
| Amazon · 7,8 Mrd. € in die European Sovereign Cloud bis 2040; 8,8 Mrd. € in Frankfurt „by 2026“ (2024) | 2040 liegt außerhalb des Fensters. Die Investitionssumme bis 2026 wird nicht veröffentlicht und wäre nicht belegbar. |
| Alphabet · Arnulfpost München, öffentliche Flächen „upon completion at the end of 2026“ (Presse 11.11.2025, Wortlaut geprüft) | Zurückgestellt. Was „completion“ heißt, ist unklar, und Google wird kaum ein Abnahmedatum melden. Bei Bedarf mit der Übersetzung „öffentliche Bereiche bis 31.12.2026 zugänglich“ möglich. |
| Alphabet · 5,5 Mrd. € in Deutschland 2026–2029 | Zeitraum endet nach 2027, die Summe wird nicht jährlich ausgewiesen. |
| Alphabet · „we continue to expect our CapEx to increase significantly in 2027“ (Wortlaut geprüft) | Ohne Zahl, „significantly“ ist unscharf. Als Zwillingswette zu 001 nur mit selbst gesetzter Schwelle möglich. |
| Meta · Wahlmöglichkeit „weniger personalisierte Werbung“ in der EU ab Januar 2026 | Stichtag vorbei. Die Zusage stammt zudem aus einer Kommissionsmitteilung (08.12.2025), nicht von Meta. |
| Meta · „operating income this year that is above 2025 operating income“ | Kaum Unsicherheit (erstes Halbjahr 2026 schon 41,6 Mrd. $ gegenüber 38,0 Mrd. $ im Vorjahr). |
| Booking · Gesamtjahresprognose 2026 „High Single Digits“ (Pressemitteilung 04.08.2026) | Steht nur in einer Tabelle, die als Text nicht wörtlich zitierbar ist. „High single digits“ ist zudem unscharf. |
| Booking · Ziel „über 50 % Buchungen nachhaltiger Unterkünfte bis 2027“ | Laut Skift (23.04.2025) 2025 gestrichen. Die ursprüngliche Booking-Quelle wurde nicht geprüft. Nach FORMAT §1.3 Nr. 5 wäre es als zurückgezogene Aussage grundsätzlich wettfähig, die Nachprüfung lohnt sich. |

## Offene Punkte für den Halter

1. **GPAI-Liste:** Keine öffentliche Liste nach Art. 52 Abs. 6 AI Act gefunden. Das Buch misst vorerst nur die sieben
   DMA-Gatekeeper. Die AI-Office-Seite sollte regelmäßig neu geprüft werden.
2. **ByteDance** hat keinen Kandidaten. Nachsuchen in TikToks DSA-Berichten und im Newsroom (auch nicht englische Ausgaben) wären möglich.
3. **005:** Das genaue Veröffentlichungsdatum des Apple-Umweltberichts 2026 gegenprüfen (Newsroom April 2026).
4. **006:** Die SEC-Fassung der Booking-Mitteilung war wegen Bot-Sperre nicht abrufbar. Einmal im Browser gegenprüfen und
   Wayback-Links für alle Quellen anlegen (FORMAT §1.3 Nr. 1).
5. Bei den Finanzwetten (001, 007, 008, 009) liegt der Beleg erst Wochen nach Ende des Messzeitraums vor. `pruefung_am` ist deshalb
   auf den erwarteten Veröffentlichungstermin plus Puffer gesetzt und nicht auf den Folgetag nach dem 31.12.
