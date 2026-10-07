# London: Aufwand der englischen Ausgabe und Rechtslage, Prüfung vom 07.10.2026

Anlass: Frage 143 a („steht“): vor dem ersten Abruf für ein Buch „Mayor of London und TfL“ prüfen,
was eine englische Ausgabe kostet und was Lizenz und englisches Äußerungsrecht verlangen. Grundlage
der Stadtwahl: `recherche/GROSSSTADT-AUSWAHL-2026-10-05.md`. Kein Abruf von Meldungen, kein Zweig,
nichts gebaut. Keine Rechtsberatung; die Rechtsstellen sind Gesetzestexte, gelesen von einem Laien.

## Ergebnis in fünf Sätzen

1. **Technik:** Englischer Inhalt läuft heute ohne Code-Änderung durch den Generator, die Seite drum
   herum bleibt aber deutsch (Beschriftungen, `lang="de"`, Datum 07.10.2026, Dezimalkomma). Sauber
   wird es mit einem optionalen Feld `sprache: en` in `BUCH.md`: geschätzt 5–7 h, plus 2–4 h für eine
   englische Einstiegsseite.
2. **Lizenz:** Weder TfL noch GLA stellen ihre Meldungen unter die Open Government Licence. TfL
   verbietet jede Vervielfältigung außer zum privaten, nicht kommerziellen Gebrauch.
3. **Folge daraus:** Kurze Zitate mit Quellenangabe sind durch das britische Zitatrecht gedeckt. Ganze
   Kopien der Meldungen im öffentlichen Repo (wie bei den NRW-Büchern in `recherche/belege/`) wären es
   wahrscheinlich nicht: Rohkopien für London nur lokal mit Prüfsumme halten, öffentlich nur Wayback-Link.
4. **Äußerungsrecht:** Gegen Felix als in Deutschland Wohnenden ist ein englisches Gericht nur
   zuständig, wenn England „clearly the most appropriate place“ ist; bei einem englischen Buch über London
   ist das gut möglich. Das Format (wörtliches Zitat, Datum, Link, Frage ohne Wertung) passt zu den
   Verteidigungen des Defamation Act 2013; GLA und TfL selbst können als Behörden nach der Derbyshire-
   Rechtsprechung wohl nicht wegen Rufschädigung klagen, Einzelpersonen schon.
5. **Empfehlung:** Bauen mit Stufe (b) „sauber“, Rohkopien nicht veröffentlichen, im Buch keine Namen
   von Beamten außer dem Bürgermeister als Sprecher, Wetten nur über Termine, nie über Absichten.

## 1. Aufwand der englischen Ausgabe

Geprüft am Code (`generator/wettbuch/`, Stand master 07.10.2026; 99 Tests grün), nur gelesen.

| Stelle | Heute | Was für Englisch fehlt |
|---|---|---|
| `seiten.py` | rund 65 deutsche Beschriftungen fest im Code, `lang="de"` an zwei Stellen (:59, :232), `datum()` als `%d.%m.%Y` (:31), `zahl()` mit Komma (:35) | Texttabelle de/en, Datum und Zahl je Sprache, `lang` aus dem Buch |
| `feed.py` | „Ja“/„Nein“, „Ausgang:“, „Beleg:“, deutsche Anführungszeichen (:24–33) | dieselbe Texttabelle |
| Feste Werte | `typ`, `art`, `ausgang`, `herkunft` sind deutsche Wörter und werden roh angezeigt (`seiten.py` :87, :118, :129, :135) | nur für die Anzeige zuordnen (`angekuendigt` → „announced“); in den Dateien bleiben sie deutsch, weil sie Teil von Format v1 sind |
| Prüfung | keine sprachabhängige Prüfung; Datum ISO, Zahlen über YAML | nichts (Achtung: `1,000` wird Text, also `1000` schreiben) |
| Einstellung je Buch | gibt es nicht | optionales Feld `sprache: en` im Kopf von `BUCH.md`; nach FORMAT.md §7 keine neue Version, weil optional |
| Fußzeile | Impressum/Datenschutz global (`cli.py` :188–189) | englische Fassung je Buch verlinken |
| CLI, Fehlermeldungen, Vorlagen | deutsch | bleiben deutsch (nur Felix sieht sie) |

Drei Stufen (Schätzung eines Prüf-Unteragenten, Zeilenangaben von ihm, Stichproben nicht einzeln nachgesehen):

- **(a) Minimal, ~1 h:** englischer Buchtext, deutsche Seite drum herum. Ergebnis gemischt
  („gesagt am 07.10.2026 … angekuendigt“). Für Leser in London nicht vorzeigbar.
- **(b) Sauber, ~5–7 h:** Texttabelle mit ~70 Einträgen, englische Monatsnamen von Hand (kein `locale`,
  damit der Bau auf jedem Rechner gleich bleibt), `lang`-Attribut, Feed, neue Tests; die bestehenden
  ~53 Prüfzeilen mit deutschem Text müssen mit Standard `de` grün bleiben. FORMAT.md §4 ergänzen.
- **(c) Englische Einstiegsseite, ~2–4 h:** z. B. `site/en/` mit kurzem Was-ist-das, englische
  Rechtsseiten, Fußzeilen-Links je Buch, `hreflang`. Rechtstexte selbst nicht eingerechnet.

Dazu der Inhalt selbst: `BUCH.md` auf Englisch, je Wette Frage und Lesart auf Englisch. Bei 10–15 Wetten
wie in den NRW-Büchern schätze ich 4–6 h inklusive Abruf mit 10 s Abstand (GLA ~100, TfL ~130 Meldungen
seit 01.01.2026, Zahlen aus dem Vergleich vom 05.10.).

## 2. Lizenz der Quellen

**TfL** (`https://tfl.gov.uk/corporate/terms-and-conditions/website`, abgerufen 07.10.2026 ~13:50, kein
Datum auf der Seite), Abschnitt „Copyright“, wörtlich:

> „TfL owned material on these websites including text and images, may not be printed, copied,
> reproduced, republished, downloaded, posted, displayed, modified, reused, broadcast or transmitted in
> any way, except for your own personal non-commercial use. You must gain our permission for any other
> type of use.“

Ebenda zu Links: „Providers of other websites may place text-based links to pages on the TfL websites
without seeking prior permission. However such links must not open TfL website pages into frames“.
Und: „The courts of England shall have exclusive jurisdiction over disputes between a user and TfL
arising out of the access or use of these websites.“ Die Open Government Licence v3.0 nennt TfL nur für
zugekaufte Fahrplan- und Haltestellendaten (`https://tfl.gov.uk/corporate/data-sources`, abgerufen
07.10.2026), nicht für eigene Texte.

**GLA** (`https://www.london.gov.uk/terms-and-conditions/terms-and-conditions-use-our-website-and-talk-london-website`,
abgerufen 07.10.2026, kein Datum): „The entire contents of the site are protected by copyright law.“ Die
Seite sei „maintained for your personal use and viewing“; Links ohne Erlaubnis erlaubt, keine Rahmen,
keine Logos. Ein Hinweis auf die Open Government Licence fehlt auf dieser Seite; die OGL gilt beim
London Datastore (nur laut Suchergebnis, nicht an der Quelle gelesen), nicht nachweislich für
Pressemeldungen. Die alte Adresse `london.gov.uk/about-us/about-site/copyright-and-licensing` gibt HTTP 404.

**Was trotzdem geht** — Copyright, Designs and Patents Act 1988, s. 30 (legislation.gov.uk, abgerufen
07.10.2026), Absatz 1ZA:

> „Copyright in a work is not infringed by the use of a quotation from the work (whether for criticism
> or review or otherwise) provided that— (a) the work has been made available to the public, (b) the
> use of the quotation is fair dealing with the work, (c) the extent of the quotation is no more than is
> required by the specific purpose for which it is used, and (d) the quotation is accompanied by a
> sufficient acknowledgement“

Absatz 4 beginnt: „To the extent that a term of a contract purports to prevent or restrict the doing of
any act which, by virtue of subsection (1ZA), would not …“ — Nutzungsbedingungen können das Zitatrecht
also nicht aushebeln (Rest des Absatzes nicht gelesen). Das Buchformat — ein wörtlicher Satz mit Datum,
Sprecher und Link — erfüllt (a), (c) und (d); (b) „fair dealing“ ist Wertungssache, bei einem Satz je
Wette aber naheliegend.

**Folgen für das London-Buch:**

- **Rohkopien nicht ins öffentliche Repo.** Die NRW-Bücher legen ganze Seiten ab (`recherche/belege/`,
  136 HTML-Dateien, z. B. 141 KB für eine Bielefelder Meldung). Für TfL/GLA wäre das „reproduced,
  republished“ ohne Zitatzweck. Lösung: Rohkopie mit SHA-256 nur lokal (außerhalb des Repos), öffentlich
  Wayback-Link und Prüfsumme. Die Prüfsumme belegt dann, dass die lokale Kopie unverändert ist.
- **Lizenz-Zeile im Buch:** `lizenz: CC0` (README: „Bücher CC0“) kann die Zitate Dritter nicht
  freigeben. Im London-Buch einen Satz ergänzen, etwa: „Quotations remain © TfL / GLA and are used under
  s. 30(1ZA) CDPA 1988; everything else CC0.“ Wortlaut vor dem Push mit Felix.
- **Keine Logos, keine Bilder** von TfL/GLA (s. 30(2) nimmt Fotos ausdrücklich aus).

## 3. Englisches Äußerungsrecht (England und Wales)

Quelle: Defamation Act 2013, legislation.gov.uk, abgerufen 07.10.2026.

- **Zuständigkeit, s. 9:** Gilt für Beklagte „not domiciled in the United Kingdom“; die früheren
  Ausnahmen für EU- und Lugano-Staaten (Buchst. b, c) sind gestrichen, also gilt s. 9 auch für Felix.
  Absatz 2: zuständig nur, wenn das Gericht „satisfied that, of all the places in which the statement
  complained of has been published, England and Wales is clearly the most appropriate place“. Bei einem
  englischen Buch über London, gelesen vor allem in London, dürfte das erfüllt sein: **„ich sitze in
  Deutschland“ schützt nicht.** Ob ein englisches Urteil in Deutschland vollstreckt würde: ungeklärt.
- **Schwelle, s. 1:** „A statement is not defamatory unless its publication has caused or is likely to
  cause serious harm to the reputation of the claimant“; bei gewinnorientierten Firmen nur bei „serious
  financial loss“.
- **Öffentliches Interesse, s. 4:** Verteidigung, wenn die Aussage „a matter of public interest“
  betrifft und der Beklagte „reasonably believed that publishing the statement complained of was in the
  public interest“; gilt für Tatsachen und Meinungen (Abs. 5).
- **Behörden als Kläger:** Nach Derbyshire County Council v Times Newspapers [1993] AC 534 (House of
  Lords) kann eine Gebietskörperschaft nicht wegen Rufschädigung klagen; Mitglieder und Beamte können es
  persönlich (Zusammenfassung der Kanzlei Brodies,
  `https://brodies.com/insights/government-and-public-sector/the-right-to-sue-public-authorities-and-defamation/`,
  über Websuche 07.10.2026; das Urteil bei BAILII war hinter einer Bot-Sperre, nicht selbst gelesen).
  Ob das auch für TfL als gesetzliche Körperschaft gilt: **ungeklärt.**

**Was das Format ohnehin schützt** (eigene Einschätzung, keine Beratung): Jede Wette ist ein wörtliches
Zitat mit Link, eine Frage nach einem Termin und eine Auflösung mit Beleg; behauptet wird nur, was die
Stelle selbst gesagt hat und ob der Termin gehalten wurde. Das ist belegbar und Thema öffentlichen
Interesses. Risiko entsteht erst durch Zusätze: Wertungen über Personen, Lesarten, die mehr behaupten als
das Zitat, Kommentare in Reddit-Posts.

**Regeln für das London-Buch, die ich vorschlage:**

1. Sprecher nur Institution oder Bürgermeister im Amt; keine Namen von Beamten oder Projektleitern.
2. Wetten nur über Termine und Zahlen aus dem Zitat, nie über Absichten oder Ehrlichkeit.
3. Auflösung „nein“ nur mit Primärbeleg (Meldung, Board-Papier) und Datum; im Zweifel `strittig`.
4. Eine Korrektur-Adresse auf Englisch auf der Buchseite; Beschwerden binnen 48 h prüfen und vermerken.

## Was ungeklärt bleibt

- Ob ganze Kopien unter s. 30(2) „reporting current events“ fallen könnten — deshalb der vorsichtige
  Weg „nur lokal“.
- UK GDPR für eine statische Seite ohne Zähler: nicht geprüft; das deutsche Impressum bleibt nötig.
- Ob TfL unter Derbyshire fällt; Vollstreckung englischer Urteile in Deutschland.
- s. 2 (Truth) und s. 3 (Honest opinion) nicht an der Quelle gelesen.
- Oxford-Street-Primärquelle (aus dem Vergleich vom 05.10.) weiter offen.

## Nächster Schritt

Laut G14 nach diesem Bericht: Abruf beider Listen mit 10 s Abstand auf eigenem Zweig `buch-london`,
Rohkopien nur lokal. Push erst nach Freigabe. Vorher zwei Entscheidungen von Felix (Fragen 165/166 in
`~/allein/ALLEIN.md`): Stufe (b) bauen? Rohkopien für London nur lokal statt in `recherche/belege/`?
