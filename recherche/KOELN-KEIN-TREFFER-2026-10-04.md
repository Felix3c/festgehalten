# Köln: die sechs „kein Treffer“-Zitate nachgeprüft (04.10.2026)

Dauerlauf, 04.10.2026 05:30–05:50. Grundlage: `recherche/wortlaut-vorschlaege.csv`, Bewertung `kein_treffer`,
nur `koeln-*` (6 von 50). Je Wette Archivkopie (`id_`-Abruf) und, wo nötig, Live-Seite gelesen. Wettdateien unverändert.

| Wette | Archivkopie | Ergebnis |
|---|---|---|
| koeln-2025-043 | 20250322113905 | **gedeckt.** Zitat ist Stichwort („GU-Beauftragung 3. Quartal 2025“). Quelle: „Im dritten Quartal dieses Jahres soll planmäßig ein Generalunternehmen beauftragt werden, welches dann die Leistungsphase 5 (Ausführungsplanung) startet.“ (PM vom März 2025 → „dieses Jahres“ = 2025). |
| koeln-2025-064 | 20251205122100 | **gedeckt.** Zitat „19.579 m² BGF“; Quelle: „Es entstehen 19.579 Quadratmeter Bruttogeschossfläche.“ |
| koeln-2026-073 | 20260819000811 | **gedeckt.** Quelle: „16. September 2026, 19 Uhr Eröffnung der Sonderausstellung "r e t u r n – Zwischen Vergangenheit und Zukunft entsteht ein anderer Ort"“. |
| koeln-2026-070 | 20260819000811 | **Archivkopie trägt nicht** (siehe unten). Live wörtlich vorhanden. |
| koeln-2026-071 | 20260819000811 | **Archivkopie trägt nicht** (siehe unten). Live wörtlich vorhanden. |
| koeln-2026-072 | 20260819000811 | **Archivkopie trägt nicht** (siehe unten). Live wörtlich vorhanden. |

## Befund 070–072: Bühnen-Absatz kam erst nach der Archivkopie

- Quelle aller drei: `https://www.stadt-koeln.de/politik-und-verwaltung/presseservice/kulturtermine-des-monats-september-2026`,
  in den Wettdateien `gesagt_am: 2026-08-18`.
- Die einzige Wayback-Kopie (CDX, Status 200: nur `20260819000811`, also 19.08.2026 00:08 UTC) hat 24 559 Zeichen sichtbaren
  Text und **keinen** Abschnitt „Bühnen der Stadt Köln“: „Eröffnungsfest“, „Offenbachplatz“, „In bester Lage“,
  „Rosenkavalier“ kommen nicht vor.
- Die Live-Seite (abgerufen 04.10.2026 05:31 MESZ) hat 25 736 Zeichen und den Abschnitt wörtlich:
  „Bühnen der Stadt Köln Nach Jahren der Sanierung kehren die Bühnen Köln an den Offenbachplatz zurück. Mit einem großen,
  kostenfreien Eröffnungsfest am 19. und 20. September 2026 sind alle Kölner*innen eingeladen, das sanierte Opernhaus und
  Schauspielhaus sowie die neue Kinderoper und das Kleine Haus zu entdecken. […] Das Schauspiel Köln eröffnet am
  25. September mit der Uraufführung " In bester Lage" im Schauspielhaus. Am 27. September folgt mit Richard Strauss'
  " Der Rosenkavalier" die Eröffnungspremiere der Oper Köln im Opernhaus.“
- Seitenkopf live: `datePublished 2026-08-18T13:00:00+00:00`, `Last-Modified: Thu, 20 Aug 2026 16:33:25` (Meta-Tag mit
  +0200, HTTP-Kopf mit GMT — die Seite widerspricht sich um zwei Stunden).
- **Schluss:** Der Abschnitt wurde zwischen 19.08. 00:08 UTC und 20.08. ~16:33 ergänzt. Für 070–072 stimmt `gesagt_am`
  wahrscheinlich nicht (18.08. → frühestens 19.08., spätestens 20.08.). Ob mehrere Änderungen dazwischen lagen, ist
  ungeklärt; Last-Modified zeigt nur die letzte.
- **Folgen:** (1) Alle drei Wetten sind aufgelöst (Termin gehalten), der Ausgang ändert sich nicht. (2) Der Vorlauf
  (gesagt_am → Termin) ist um ein bis zwei Tage kürzer als angegeben. (3) Für den Wortlaut gibt es keine öffentliche
  Archivkopie: Wayback-Speichern am 04.10. zweimal fehlgeschlagen (GET `/save/` → 520, POST → Job
  `spn2-2d8bfaf147e6bdd6535c95a8892b44e4113aa3f7` „job-failed“).
- **Lokale Kopie** (Behelf, nicht öffentlich prüfbar): `recherche/belege/2026-10-04-stadt-koeln-kulturtermine-september-2026.html`,
  83 597 Byte, SHA-256 `a7c61c3d6a14b29cd9d1d529bf9418e6edc97c8b32dfc97300aae472a43ac424`.

## Vorschlag (Frage an Felix, nichts geändert)

`gesagt_am` in koeln-2026-070, -071, -072 auf `2026-08-20` setzen (der spätestmögliche Tag, an dem die Stadt es sicher
gesagt hat) und je Wette einen Satz „Abschnitt am 20.08.2026 nachgetragen; Wayback 19.08. ohne Abschnitt“ ergänzen.
Wayback-Sicherung im nächsten Lauf erneut versuchen.

## Nebenbefund Werkzeug

Keiner. Ein erster Schnelltest mit `urllib` las die gzip-Antwort der Wayback-`id_`-Seite als Binärsalat; das Werkzeug
nutzt `requests`, das korrekt entpackt. Die drei „gedeckten“ Fälle sind Stichwort-Zitate, die der Satzvergleich
(Deckung 0,40–0,59) nicht findet — erwartbar, kein Fehler.
