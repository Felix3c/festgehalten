# Auflösung vorbereitet: muenster-2026-001 (12.10.), bielefeld-2026-001 und hamm-2026-001 (14.10.), essen-2025-001 (15.10.)

Stand 08.10.2026 01:45, Dauerlauf (Claude). Alle vier Wetten sind seit 05.10. öffentlich (master, gepusht 05.10. 15:10).
Prognosen wurden vor dem Ereignis hinterlegt. Nichts committet, Wettdateien unverändert.

## muenster-2026-001: Blindgängerverdacht Lamberti-Kirchplatz, Prüfung 11.10.2026

- Stand 08.10.: Die Quelle (`pressemitteilungen.stadt-muenster.de/api/item/1227865`, abgerufen 08.10.2026 01:20) ist
  unverändert, der Satz „Am Sonntag, 11. Oktober 2026, überprüfen Kampfmittelräumer …“ steht weiter dort.
  In den 20 neuesten Mitteilungen (02.10.–07.10.2026, `api/items`) gibt es keine Absage und keine Verschiebung.
- **Am Mo 12.10. prüfen:** `api/items` nach „Lamberti“, „Blindgänger“, „Kampfmittel“, „Evakuierung“ durchsuchen (eine
  Ergebnismeldung kommt meist noch am Sonntag), dazu Websuche „Lamberti Blindgänger“ (Westfälische Nachrichten, WDR,
  Feuerwehr Münster).
- **Regel (aus der Wette):** JA, wenn belegt ist, dass der Verdachtspunkt am 11.10. freigelegt und begutachtet wurde.
  Ob eine Bombe gefunden oder entschärft wurde, zählt nicht. Eine Meldung „kein Blindgänger, Entwarnung“ ist also ein JA.
  NEIN bei Verschiebung oder Absage.
- Beleg: Mitteilung über die Schnittstelle abrufen, lokal nach `recherche/belege/` mit SHA-256, Archivkopie über Save Page
  Now (bei Münster hat das am 04.10. funktioniert).
- **Nachtrag 09.10.2026 12:40 (Dauerlauf):** Quelle `api/item/1227865` erneut abgerufen, SHA-256 23068f14…b7b2,
  byte-gleich mit der lokalen Kopie vom 04.10. Die 40 neuesten Mitteilungen (`api/items` Seite 1–2, 29.09.–09.10. 10:03)
  enthalten keine Absage und keine Verschiebung (einziger Treffer „Lamberti“ ist die Friedensvesper der Gemeinde
  St. Lamberti am 24.10.). Websuche „Lamberti-Kirchplatz Blindgänger 11. Oktober“ fand nur die Ankündigungen der Stadt
  und von ms-aktuell, keine neue Meldung. Prognosen bleiben unverändert. Am Mo 12.10. wie oben prüfen.

## bielefeld-2026-001: Infostand Am Pfarrholz/Tiesloh, 13.10.2026, 17.00–18.30 Uhr

- Stand 08.10.: `https://www.bielefeld.de/node/37317` (abgerufen 08.10.2026 01:20, HTTP 200) unverändert, Termin steht.
- **Am Mi 14.10. prüfen:** Projektseite `www.bielefeld.de/pfarrholz-tiesloh`, Pressemeldungen der Stadt, Neue Westfälische,
  Westfalen-Blatt. bielefeld.de hatte am 04.10. Zeitüberschreitungen; heute antwortete es sofort.
- **Regel (aus der Wette):** JA nur mit öffentlichem Beleg, dass der Stand am 13.10. stattfand. Bei Verschiebung wegen
  Regen gilt NEIN (steht so in der Übersetzung).
- **Wahrscheinlicher Ausgang ohne Beleg:** Ein Infostand wird selten nachträglich gemeldet. Gibt es bis zum 14.10. nichts,
  nicht gleich NEIN setzen, sondern bis ~21.10. warten (Nachbericht, Fotos der Bezirksbürgermeisterin, Ratsinformation
  der Bezirksvertretung Jöllenbeck). Danach Frage an Felix (Vorschlag: NEIN mangels Beleg, mit Vermerk; das war in der
  Begründung des Computers eingepreist).
- **Nachtrag 09.10.2026 12:37 (Dauerlauf):** `node/37317` erneut abgerufen (HTTP 200). Der Meldungstext ist wortgleich mit
  der lokalen Kopie vom 05.10.; anders ist nur die Seitenleiste mit den neuesten Pressemeldungen, darunter keine zu
  Pfarrholz/Tiesloh. Die Projektseite `www.bielefeld.de/pfarrholz-tiesloh` (HTTP 200) nennt weiter „Dienstag, 13. Oktober
  2026, von 17 bis etwa 18.30 Uhr“, Treffpunkt Am Pfarrholz nahe Weinbrennerstraße, und den Hinweis, eine Verschiebung
  wegen starken Regens werde „kurzfristig hier auf der Webseite“ mitgeteilt; ein solcher Vermerk steht dort nicht.
  Kopie neu: `recherche/belege/2026-10-09-bielefeld-pfarrholz-tiesloh.html`, SHA-256 8b66dbda…b408d. Damit ist am 14.10.
  zuerst diese Seite gegen die Kopie zu halten (ein Verschiebungsvermerk wäre NEIN). Online-Beteiligung läuft laut Seite
  bis So 18.10. Websuche „Am Pfarrholz Tiesloh Infostand Bielefeld“: keine Presse dazu. Prognosen bleiben unverändert.

## hamm-2026-001: Ratsbeschluss ISEK „Zukunftsplan Innenstadt 2040“ am 13.10.2026

- Stand 08.10.: Die Meldung (hamm.de, abgerufen 08.10.2026 01:25, HTTP 200) nennt den 13.10. weiter.
  **Ungeklärt:** ob der Punkt auf der Tagesordnung des Rates steht. `ratsinfo.hamm.de` antwortet am 08.10. mit einer
  Bot-Prüfung (HTTP 403, „rescaled-waf/verify“), auch die OParl-Schnittstelle. Nicht umgangen. Websuche fand keine
  Tagesordnung (08.10.).
- ~~Bis Di 13.10. (beiläufig):** Tagesordnung des Rates im eigenen Browser ansehen (Felix oder Chrome-Werkzeug),
  oder auf hamm.de nach einer Vorab-Meldung suchen. Fehlt der Punkt, ist NEIN sehr wahrscheinlich.~~ Erledigt 08.10.:
- **Nachtrag 08.10.2026 05:50 (Dauerlauf): Punkt steht auf der Tagesordnung.** Im Browser (Chrome-Werkzeug; die
  WAF-Prüfung lief ohne Zutun durch, nichts umgangen) zeigt ratsinfo.hamm.de für „Rat, 8. Sitzung, Di 13.10.2026
  16:00, Kurhaus“ (Bekanntmachung exportiert 01.10.2026) **TOP 2.15 „ISEK Zukunftsplan Innenstadt 2040“, BV-183/26**.
  Beschlussvorlage (exportiert 24.09.2026, 5 Seiten): „Der Rat der Stadt Hamm beschließt das Integrierte
  Stadtentwicklungskonzept (ISEK) „Zukunftsplan Innenstadt 2040“ als Grundlage …“ und „… beschließt, Fördermittel auf
  Grundlage des ISEKs zu beantragen.“ Beratungsfolge: ASWM/AKUN/BV Mitte 07.10. (vorberatend, Ergebnis am 08.10. noch
  nicht eingetragen), Haupt-, Personal- und Finanzausschuss 12.10. (vorberatend), Rat 13.10. (beschließend).
  Gesamtkosten 31.387.000 EUR, Förderung 28.718.200, Eigenanteil 2.668.800.
  Rohkopien außerhalb des Repos: `~/wettbuch-notizen/hamm-belege/2026-10-08-ratsinfo-rat-13-10-tagesordnung.html`
  (SHA-256 1776e40cdff775d6c7a39df42c56e198304953958cf8f8e2f4808775f354928d) und `2026-10-08-BV-183-26.pdf`
  (SHA-256 bbac3492982d0d6a2238d740ced656ccc4301d85809b8ed47ede0205c83d0e0d). Kein Wayback (Seiten-URL trägt ein
  Sitzungs-Token). Richtung: JA wahrscheinlich, gekippt nur durch Vertagung/Absetzung.
- **Am Mi 14.10. zusätzlich:** im Vorgang BV-183/26 die Spalte „Beschluss“ für 13.10. ansehen (Chrome-Werkzeug);
  vorher am 12.10. abends, ob der Hauptausschuss vertagt hat.
- **Am Mi 14.10. prüfen:** Meldung der Stadt (hamm.de/aktuelles), Westfälischer Anzeiger (wa.de), Beschlussauszug im
  Ratsinformationssystem (Niederschrift kommt erst Wochen später).
- **Regel (aus der Wette):** JA, wenn der Rat am 13.10. (oder früher) das ISEK oder die Einreichung des Förderantrags
  beschließt. Vertagung oder kein Tagesordnungspunkt = NEIN. Ob der Antrag danach eingereicht wird, zählt nicht.

## essen-2025-001: Überschuss 2025 laut festgestelltem Jahresabschluss (Punktwette, Prognose Stadt 3,4 Mio EUR, ±10 %)

- **Neu 08.10.:** Rat 9. Sitzung am Mi 14.10.2026 15:00 (OParl `meeting/33118`, geändert 07.10. 14:17):
  - TOP 7: Vorlage **1634/2026/OB** „Bericht über die Prüfung des Jahresabschlusses der Stadt Essen zum 31.12.2025“,
    Beschlussvorschlag: „Der Rat der Stadt stellt den vom Rechnungsprüfungsausschuss geprüften Jahresabschluss zum
    31.12.2025 fest und beschließt die Entlastung des Oberbürgermeisters gemäß § 96 Absatz 1 … GO NRW.“ Damit ist das die
    Feststellung, auf die die Wette wartet.
  - TOP 8: Vorlage **1577/2026/2** „Verwendung des Jahresüberschusses 2025“ (Datum 28.09.2026, gez. OB Kufen), wörtlich:
    „Die Ergebnisrechnung der Stadt Essen zum 31. Dezember 2025 schließt mit einem Jahresüberschuss in Höhe von
    1.072.393,88 EUR ab.“ und „Der bilanzielle Jahresüberschuss der Stadt Essen zum 31. Dezember 2025 beträgt
    186.130,17 EUR.“ (Differenz = 886.263,71 EUR Überschuss der unselbständigen Stiftungen, Produktbereich 17.)
  - Lokale Kopien: `recherche/belege/2026-10-08-essen-vorlage-1634-2026-OB.pdf`
    (SHA-256 f494f00f3e82c709ddc7ff2cc9dbcdf4528a46b8cab5142888b8ae7947f0eb69) und
    `recherche/belege/2026-10-08-essen-vorlage-1577-2026-2.pdf`
    (SHA-256 a4122d29c6c65410de451ffd097d6711a24c9982c4d852dcdfc6f036049c8f84). Unversioniert.
- **Am Do 15.10. prüfen:** Beschluss zu TOP 7 (Pressemeldung essen.de oder OParl-Beschlusstext der Sitzung). Nur wenn der Rat
  festgestellt hat, auflösen. Vertagt der Rat, bleibt die Wette offen (Verfall erst 31.12.2028).
- **Offen: welche Zahl zählt (Frage 183 an Felix).** Die Wette fragt nach „dem Überschuss laut Jahresabschluss“. Zwei Zahlen
  stehen in derselben Vorlage: 1,07 Mio EUR (Jahresergebnis der Ergebnisrechnung, das die Stadt schon am 27.05. als
  „Jahresüberschuss 1,1 Mio“ gemeldet hat) und 0,19 Mio EUR (bilanziell, ohne Stiftungen).
  Empfehlung: **1,07 Mio EUR**. Gründe: Die Stadt nennt selbst diese Zahl „Jahresüberschuss“, und die Prognose 3,4 Mio
  stammt aus dem Ergebnisplan, der der Ergebnisrechnung gegenübersteht. Die Abweichung wird im Vermerk genannt.
  **Für das Ergebnis ist es egal:** Beide Zahlen liegen weit außerhalb ±10 % um 3,4 (Korridor 3,06–3,74). Die Stadt hat
  also in jedem Fall daneben gelegen: −2,33 Mio EUR (−68 %) bzw. −3,21 Mio EUR (−95 %).
- Vorschlag Auflösung (nach Feststellung): `ausgang: 1.07`, `aufgeloest_am: 2026-10-15`, `beleg_ausgang`: Beschluss
  TOP 7 + Vorlage 1577/2026/2, Vermerk mit beiden Zahlen. Der Generator rechnet die Abweichung selbst.

## Was danach

- Die Kurzfassung `NAECHSTE-SCHRITTE.md` führt die Prüftage schon; essen-2025-001 dort unter Do 15.10. ergänzt.
- essen-2025-002 (Überschuss 2026) bleibt offen, Feststellung frühestens Herbst 2027.
