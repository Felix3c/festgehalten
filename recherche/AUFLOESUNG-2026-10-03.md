# Auflösung vergangener Wetten mit Beleg — 5. Lauf, Stand 03.10.2026

Geprüft: 13 überfällige Wetten, die weder IFG-Fall (`IFG-2026-09.md`) noch in einer `docs/…-VORBEREITET.md`
stehen: koeln-2025-032, -050, -059, die Kölner Jahresabschluss-Wetten 2025 (-005, -006, -007, -008, -015),
essen-2025-001, -032, -034, dortmund-2025-001, -014. **Keine aufgelöst.** Wettdateien nicht geändert.

Vorgehen: zwei parallele Recherche-Läufe (Köln; Essen/Dortmund) mit WebSearch/WebFetch, zentrale Stellen per curl
bzw. pdftotext wörtlich gegengeprüft, alle URLs abgerufen am 03.10.2026. Recherche: Claude (Dauerlauf).

## Befund 1: Jahresabschlüsse 2025 nur als Entwurf / vorläufiges Ist

Ein Entwurf ist kein festgestellter Jahresabschluss (Frage verlangt „laut festgestelltem Jahresabschluss“).
Die Zahlen sind trotzdem amtlich und zeigen die Richtung.

| Wette | angekündigt | Stand 2025 (nicht festgestellt) | Quelle |
|---|---|---|---|
| koeln-2025-005 | Fehlbetrag rund 582 Mio | **vorläufig 650,0 Mio** (Stand 16.07.2026) | Haushaltsentwurf 2027/2028 Bd. 1 Teil 1 |
| koeln-2025-008 | Plan 395,1 Mio | dto. 650,0 Mio | dto. |
| koeln-2025-015 | 399,34 Mio | dto. 650,0 Mio | dto. |
| koeln-2025-006 | Mehrerträge Grundsteuer B 23 Mio | „Planunterschreitungen bei Grundsteuer B i. H. v. 11,0 Mio. Euro“ (kein Absolutwert) | dto. |
| koeln-2025-007 | Grundsteuer-B-Ertrag 259,75 Mio | kein Absolutwert genannt | dto. |
| essen-2025-001 | Überschuss 3,4 Mio | **Entwurf: Jahresüberschuss 1,1 Mio** | PM Essen 27.05.2026 |
| essen-2025-032/-034 | Defizit ~120 / > 123 Mio | Entwurf: Jahresüberschuss 1,1 Mio; **ordentliches Ergebnis −73,8 Mio** | dto. |
| dortmund-2025-001 | Fehlbetrag rund 335 Mio | **Entwurf: Minus rund 352,7 Mio** | PM Dortmund 13.05.2026 |

Wörtlich:
- Köln, https://www.stadt-koeln.de/mediaasset/content/pdf20/hpl_2027_2028_band_1_entwurf_teil_1.pdf :
  „Der Jahresabschluss für das Jahr 2025 befindet sich in der Aufstellung.“ · „Der Jahresabschluss für 2025 ist noch
  nicht durch den Oberbürgermeister bestätigt. Es handelt sich hier um das vorläufige Ist, Stand 28.07.2026.“ ·
  „…voraussichtlich einen vorläufigen Jahresfehlbetrag von 650,0 Mio. Euro ausweisen. Im Haushaltsplan 2025/2026 war
  für das Jahr 2025 ein Jahresfehlbetrag von 399,3 Mio. Euro geplant.“ · Grundsteuer B: „Planunterschreitungen bei
  Grundsteuer B i. H. v. 11,0 Mio. Euro“ (begründet mit nachträglichen Wertkorrekturen der Finanzämter).
- Essen, https://www.essen.de/meldungen/pressemeldung_1595069.de.html (27.05.2026): „In seiner Mai-Ratssitzung (27.05.)
  wurde der vorläufige Jahresabschluss der Stadt Essen für das Jahr 2025 eingebracht. Der Jahresabschluss 2025 schließt
  in der Ergebnisrechnung mit einem Jahresüberschuss in Höhe von 1,1 Millionen Euro ab.“ · „Das ordentliche Ergebnis
  schließt mit einem Defizit in Höhe von 73,8 Millionen Euro ab. Gegenüber dem Plan 2025 verschlechtert es sich um
  -102,3 Millionen Euro“. Entwurf-PDF: „vom Kämmerer am 28. April 2026 aufgestellt und vom Oberbürgermeister am
  30. April 2026 bestätigt“ (https://service.essen.de/detail/-/vr-bis-detail/dokument/6635180/download?_19_WAR_vrportlet_priv_r_p_action=vr-bis-detail-dienstleistung-show).
- Dortmund, https://www.dortmund.de/newsroom/nachrichten-dortmund.de/schwache-konjunktur-belastet-haushalt-dortmund-schliesst-2025-mit-deutlichem-minus-ab.html
  (13.05.2026, nur per curl mit Cookies abrufbar): „Die Stadt Dortmund legt den Entwurf für den Jahresabschluss 2025
  vor … Unter dem Strich steht ein Minus von rund 352,7 Millionen Euro. Das sind 17,6 Millionen Euro mehr als
  ursprünglich erwartet.“ · „Die Verwaltung bringt den Jahresabschluss am 28. Mai in den Rat ein.“

**Wann wird festgestellt?**
- Köln: jüngster festgestellter Abschluss ist **2023** (Ratsbeschluss 04.09.2025, https://www.stadt-koeln.de/artikel/63738/index.html:
  „Der Rat der Stadt Köln hat mit Beschluss vom 4. September 2025 den vom Rechnungsprüfungsausschuss geprüften
  Jahresabschluss zum 31. Dezember 2023 festgestellt…“). 2024 eingebracht 04.09.2025 (Vorlage 2198/2025), Prüfung
  laut Haushaltsentwurf „derzeit noch nicht abgeschlossen“. Feststellung 2025 realistisch **frühestens Ende 2027**.
- Essen: Jahresabschluss 2024 laut Suchtreffer am 19.11.2025 festgestellt (Amtsblatt-Bekanntmachung 72/2026, Wortlaut
  NICHT geprüft) → Feststellung 2025 vermutlich **~November 2026**.
- Dortmund: Feststellung nicht gefunden (Ratsinformationssystem nicht gelesen) — ungeklärt.

**Wiedervorlage:** Essen 001/032/034 Ende November 2026; Dortmund 001 Dezember 2026; Köln 005–008/015 Ende 2027.

**Messgröße Essen 032/034 (Frage an Felix):** Die Wetten fragen nach dem „tatsächlichen Jahresdefizit“. Im Entwurf
ist das Jahresergebnis ein **Überschuss** (+1,1 Mio), das ordentliche Ergebnis ein Defizit (−73,8 Mio); das
Finanzergebnis gleicht aus. Empfehlung: das **Jahresergebnis** zählt (so steht es in der Frage, und so meint es
essen-2025-001); ordentliches Ergebnis als Vermerk. Vor der Auflösung festlegen, nicht danach.

## Befund 2: dortmund-2025-014 beruht wahrscheinlich auf einer Fehllesung

Zitat der Wette (electrive, 21.10.2024): „155 neue Dieselbusse für rund 55 Mio. € geplant statt einer reinen
E-Bus-Strategie.“ DSW21 hat Ende 2024 widersprochen, https://www.wirindortmund.de/dortmund/keine-beschaffung-mehr-von-e-bussen-dsw21-nimmt-stellung-zur-berichterstattung-257063 :
„Wir sprechen hier beim Einkauf von einer Aufteilung von etwa 2/3 E-Bussen (nur Gelenkbusse) und etwa 1/3
Dieselbussen (nur Solobusse). Das bedeutet bei einer Anschaffung von durchschnittlich rund 12 Bussen pro Jahr acht
E-Busse und vier Dieselbusse.“ Keine Vergabe, kein Auftragswert, keine Stückzahl gefunden (DSW21-PM Geschäftsjahr 2025
vom 22.04.2026 ohne Dieselbusse: https://www.bus-und-bahn.de/news-details/die-gegenwart-voll-im-griff-2035-fest-im-blick;
service.bund.de-Treffer „Beschaffung von 2+2 Diesel-Gelenkbussen“ 05/2025 liefert 404). Gleiches gilt vermutlich für
dortmund-2025-013 (Stückzahl, IFG-Liste).
Die Quelle ist Presse, nicht die Institution selbst; DSW21 bestreitet die Ankündigung. **Frage an Felix:** 013/014 mit
Vermerk „Ankündigung von DSW21 bestritten“ annullieren (nicht auflösen) und aus der IFG-Liste nehmen? Empfehlung: ja.

## Befund 3: koeln-2025-059 (Kreuzgasse) — offen, Richtung Nein

PM 13.05.2026, https://www.stadt-koeln.de/politik-und-verwaltung/presseservice/holzmodule-fliegen-am-gymnasium-kreuzgasse-ein
(per curl wörtlich): „Auch diese Arbeiten sollen an ein Totalunternehmen vergeben werden. Die Vergabeverhandlungen für
diese Hauptmaßnahme dauern noch an.“ Danach bis 18.09.2026 keine Gebäudewirtschafts-PM zu einem Auftrag, keine
Vergabebekanntmachung gefunden. Ein Nein ist damit nicht belegt (Vergabe kann still erfolgt sein). Nebenbefund:
Interim jetzt „Juli 2027“ statt „Frühjahr 2027“. Nächster Schritt: Projektdatenblatt Gebäudewirtschaft oder
Ratsinformation (JS-gesperrt für Claude) im Browser — oder in eine IFG-/Presseanfrage aufnehmen.

## Offen ohne neuen Befund

- **koeln-2025-032** (Großtagespflege 2024/25): keine Ist-Zahl in PM 26928, 27789 (11.08.2025), 27859 (05.09.2025),
  28216 (25.02.2026), „Start ins Schuljahr 2026/2027“. Jugendhilfeausschuss-Vorlagen nicht lesbar (Ratsinfo braucht JS,
  OParl unter /oparl/ liefert 404). Kandidat für die IFG-Liste.
- **koeln-2025-050** (62 Bäume Innenstadt): BUND Köln 13.07.2026 (https://www.bund-koeln.de/service/meldungen/detail/news/stadtbaeume-ein-wichtiger-verbuendeter-gegen-hitzebelastung-in-koeln/):
  „Insgesamt wurden bislang bereits über 300 Bäume in allen Bezirken außer Porz gepflanzt.“ Keine Bezirkszahl.
  Wie koeln-2025-049 (IFG-Liste) — 050 dort mit aufnehmen.

## Suchmethode und Sperren

Ratsinformation Köln (Suche per JavaScript, OParl 404) und Dortmund nicht im Volltext lesbar; dortmund.de nur per curl
mit Cookies; KStA, Rundschau, Express, WAZ, Ruhr Nachrichten nicht verwendet.
