# Archivsicherung und Wörtlichkeits-Prüfung, 04.10.2026 (Dauerlauf)

Werkzeug: `werkzeuge/archivsicherung.py` (15 Tests), Tabelle: `recherche/archiv-quellen.csv`.
Geprüft: alle 273 Wetten aus master (Bonn, Dortmund, Düsseldorf, Essen, Köln, NRW, KI, Weitsicht) und den
lokalen Zweigen buch-bund, buch-gatekeeper, buch-duisburg. Je Wette: jüngste Wayback-Kopie (CDX, Status 200),
steht das Zitat darin (Buchstaben/Ziffern-Folge, Auslassungen „…“ erlaubt)? Wenn nein: steht es auf der Live-Seite?
Nichts beim Archiv angestoßen, keine Wettdatei geändert (FORMAT §1.3 Regel 3).

## Ergebnis

| Buch | trägt (Archiv + Zitat) | Zitat live wörtlich, Archiv fehlt | nicht wörtlich (weder Archiv noch live) | nicht erreichbar |
|---|---|---|---|---|
| Köln | 18 | 2 | 66 | – |
| Essen | 1 | – | 38 | – |
| Düsseldorf | – | 3 | 31 | 1 (404) |
| Dortmund | 1 | 1 | 18 | – |
| Bonn | – | – | – | 36 (bonn.de Bot-Prüfung, 302) |
| NRW | 4 | 7 | – | – |
| KI | 7 | 2 | – | – |
| Weitsicht | 8 | – | – | – |
| Bund (Zweig) | 7 | 1 | – | – |
| Gatekeeper (Zweig) | 8 | 1 | 1 | – |
| Duisburg (Zweig) | 7 | 2 | 2 | – |
| **Summe** | **61** | **19** | **156** | **37** |

Nach Jahrgang: von den „nicht wörtlich“ sind 130 Wetten aus 2025 (Alt-Bestand), 26 aus 2026.
Die Bücher vom 03.10. (NRW, KI, Bund, Gatekeeper, Duisburg; Zitate per curl geprüft) sind fast sauber.

## Was „nicht wörtlich“ heißt (Stichproben, live nachgesehen 04.10.)

- Stichworte statt Satz: essen-2025-008 „U3-Quote 42 %“; koeln-2025-043 „GU-Beauftragung 3. Quartal 2025“;
  koeln-2025-012 „Konsolidierungsmaßnahmen 93,5 Mio Euro 2025“.
- Umformuliert: duesseldorf-2025-007 „Für den ÖPNV sind 2025 99 Mio eingeplant“ — Quelle: „… ÖPNV mit 99 Millionen
  Euro, davon 53,9 Millionen Euro für die Stadtbahnlinie U81“; bonn-2025-001 „… weist der Haushaltsplan ein Defizit
  von 97,0 Millionen Euro aus“ — Quelle (Archiv 20.04.2025): „Die jährlichen Defizite stellen sich nun wie folgt dar:
  2025 97 Millionen Euro …“.
- Wörter eingefügt ohne Klammer: dortmund-2026-015 „… könnten die Bauarbeiten (2. Bauabschnitt RS1 Sonnenstraße)
  Ende 2026 beginnen“ — Quelle ohne den Einschub.
- Sätze zusammengezogen ohne „…“: dortmund-2026-017 („… Kabeltrassen. 150 Schulen profitieren“),
  dortmund-2026-019; dortmund-2025-010 „sollen dann alle … über Breitbandanschluss“ — Quelle „sollen alle … dann
  über einen Breitbandanschluss“.

Inhaltlich erfunden war in keiner Stichprobe etwas; verletzt ist FORMAT.md Z. 74 („wörtlich, gekürzt mit … ;
keine Paraphrase“) und die Prüfregel Z. 261 („jede Quelle enthält das wörtliche Zitat“).

## Grenzen

- Seiten, die Text per JavaScript nachladen, würden fälschlich als „nicht wörtlich“ zählen; in den 10 Stichproben
  kam das nicht vor (Text stand jeweils im HTML).
- Bonn ist ungeklärt: bonn.de leitet Programme auf eine Bot-Prüfung um; die Archivkopien gibt es (29 von 36),
  das Zitat steht darin aber nicht (Stichprobe 001/002: Paraphrase).
- Eine Wette (bund) brach mit Netzfehler ab, beim Neulauf erfasst.

## Was daraus folgt (Entscheidung Felix, Frage 61)

Kopf ist eingefroren (§1.3 Regel 3), Korrektur nur als neuer Eintrag mit `ersetzt_durch` oder als Vermerk.
Vorschlag: je betroffener Wette ein Vermerk „Zitat nicht wörtlich, Wortlaut der Quelle: »…« (Archiv: …)“, ohne
Prognose oder Frage zu ändern; Generator-Prüfung danach um „Zitat wörtlich in Quelle oder Archiv“ als Warnung erweitern.

## Nachtrag 04.10. ~02:20: die 19 „live wörtlich, Archiv fehlt“ gesichert

Lauf `python werkzeuge/archivsicherung.py buecher <bund> <gatekeeper> <duisburg> --speichern --nur-live`
(neue Option `--nur-live`, 16 Tests). Ergebnis: **alle 19 tragen jetzt** (18 Archivkopie mit wörtlichem Zitat,
ki-2026-009 als PDF). Neuer Stand: **80 tragen** (76 ok + 4 pdf_ok), 166 nicht wörtlich, 27 ohne Archiv
(Bonn-Bot-Prüfung u. a.); die 166 bleiben bis zur Antwort auf Frage 61 unverändert.

Zwei Befunde fürs Werkzeug (noch nicht behoben, nur notiert):
- Save Page Now meldete bei radioduisburg.de und microsoft.com zweimal einen Fehler, hatte die Kopie aber angelegt
  (zwei Minuten später per CDX da). Ein Prüflauf ohne `--speichern` nach dem Speicherlauf fängt das auf.
- ki-2026-006 galt zuerst als `zitat_fehlt`, weil die jüngste Kopie auf eine andere Aleph-Alpha-Seite umgeleitet
  hatte (…/ilhan-scheer-zum-co-ceo-ernannt/). Nach frischer Kopie ok. Weitere `zitat_fehlt` könnten solche
  Umleitungen sein; Prüfung „Ziel-URL der Kopie = Quelle“ fehlt im Werkzeug.
