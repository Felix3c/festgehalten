# Wortlaut-Vorschläge zu den nicht wörtlichen Zitaten (Vorarbeit Frage 61)

Stand 04.10.2026, Dauerlauf. Keine Wette geändert. Werkzeug `werkzeuge/wortlaut_vorschlag.py` (26 Tests mit
`test_archivsicherung.py`), Tabelle `recherche/wortlaut-vorschlaege.csv`, Lauf-Log `recherche/wortlaut-lauf.log`.

## Was gemacht wurde

Für alle 164 Wetten mit Status `zitat_fehlt` aus `archiv-quellen.csv` (nur Bücher in master + archiv-sicherung;
Bund/Gatekeeper/Duisburg liegen auf eigenen Zweigen) wurde die Archivkopie geholt und die Stelle aus 1–3 Sätzen
gesucht, die die meisten Zitat-Wörter enthält (`deckung`). Zusätzlich: welche Zahlen des Zitats in der Stelle
fehlen (`zahlen_fehlen`) und welche nirgends auf der Seite stehen (`zahl_nicht_auf_seite`, genau wie geschrieben).

| Bewertung | Anzahl | Bedeutung |
|---|---|---|
| vorschlag | 92 | Deckung ≥ 0,6 und alle Zahlen in der Stelle |
| zahl_abweichend | 22 | Deckung ≥ 0,6, aber eine Zahl fehlt in der Stelle (meist Datumsschreibweise) |
| kein_treffer | 50 | Deckung < 0,6 (oft steht die richtige Stelle trotzdem da, nur umgebaut) |
| archiv_leer | 0 | (bis 04.10. 02:51 fünf: duesseldorf-2025-004 bis -008, siehe Nachtrag) |

## Befunde

- **Nichts erfunden, soweit nachprüfbar.** Die Bonner Haushaltszahlen (bonn-2025-001/-002/-005/-006/-009) wirkten
  zuerst wie „Zahl nicht in der Quelle“, stehen aber als Liste da: „Die jährlichen Defizite stellen sich nun wie folgt
  dar: 2025 97 Millionen Euro, 2026 123 Millionen Euro, 2027 128 Millionen Euro, 2028 111 Millionen Euro und 2029 110
  Millionen Euro.“ Das Zitat hat daraus ganze Sätze mit „97,0“ gemacht. Formfehler, kein Inhaltsfehler.
- **Inhaltlich zu prüfen (Wortlaut sagt weniger oder anderes als das Zitat):**
  - duesseldorf-2025-016: „bis 2030“ steht nicht in der Quelle (Zitat-Zusatz).
  - koeln-2025-023: Zitat „Ende 2. Halbjahr 2025“, Quelle „Bauliche Fertigstellung bis Ende 2025“.
  - bonn-2026-031: „(22.11.)“ und Totensonntag-Zusatz nicht in der gefundenen Stelle.
  - bonn-2025-022: „davon 6 Millionen Euro Bundesförderung“ nicht in der Archivkopie.
  - dortmund-2025-005/-006/-007: Platz- und Gruppenzahl je Kita (200/72/108) nicht auf der Seite; Quelle ist ein
    Ruhr-Nachrichten-Artikel hinter Bezahlschranke, die Kopie zeigt nur „insgesamt 491 Betreuungsplätzen“ → ungeklärt.
- **Archiv ohne Wert:** die Düsseldorfer Haushalts-Meldung (5 Wetten) ist im Archiv nur eine Bot-Schutzseite; in
  `archiv-quellen.csv` stehen sie deshalb fälschlich als „zitat_fehlt“. Neue Kopie oder andere Quelle nötig.

## Grenzen des Werkzeugs

Die Deckung zählt Wörter, sie versteht nichts. Stichprobe (8 Fälle): Vorschläge meist richtig (essen-2025-007,
dortmund-2026-019), aber koeln-2025-012 zeigt einen falschen Satz; bei kein_treffer liegt die richtige Stelle oft
knapp darunter (essen-2025-002: „in 2026 ist ein Überschuss von 3,5 Millionen Euro geplant“). Jeder Vermerk braucht
deshalb einen Blick auf die Stelle; die Tabelle spart das Suchen, nicht das Prüfen.

## Nächster Schritt (erst nach „steht“ zu Frage 61)

Je Wette Vermerk „Zitat nicht wörtlich; Wortlaut der Quelle: »…« (Archiv: …)“ aus der Spalte `wortlaut`, von Hand
nachgesehen; zuerst die 9 inhaltlichen Fälle oben, dann die 88 Vorschläge, dann kein_treffer von Hand.
Düsseldorf 004–008: erledigt, siehe Nachtrag.

## Nachtrag 04.10.2026 02:58: Düsseldorf 004–008 nachgesichert

- Die Live-Seite (rat-verabschiedet-haushalt-2025-1) liefert mit Browser-Kennung den vollen Text (64.436 Byte,
  SHA-256 `37ed9e5b…77ea54`); die Bot-Schutzseite kam nur bei der alten Kopie vom 20.07.2025.
- Neue Wayback-Kopie https://web.archive.org/web/20261004005146/https://www.duesseldorf.de/aktuelles/news/detailansicht/newsdetail/rat-verabschiedet-haushalt-2025-1
  (Rohkopie gzip, entpackt 64.436 Byte); „-214,5 Millionen Euro“, „972,6 Millionen Euro“, „459,1 Millionen Euro“ und
  „davon 53,9 Millionen Euro für die Stadtbahnlinie U81“ stehen wörtlich darin. `archiv-quellen.csv` zeigt sie.
- Inhaltlich decken die Quelle alle fünf Zahlen; die Zitate sind Umschreibungen (Formfehler wie bei Bonn):
  - 004: »Während der Haushaltsplanentwurf für das Jahr 2025 noch einen Jahresfehlbetrag in Höhe von -261,8 Millionen
    Euro vorgesehen hat, konnte dieser Fehlbetrag auf -214,5 Millionen Euro verbessert werden.«
  - 005: »Im Jahr 2025 kratzt das Investitionsvolumen dabei mit 972,6 Millionen Euro an der Marke von 1 Milliarden Euro
    und ist damit so hoch wie nie zuvor.« (Teil eines Zitats der Stadtkämmerin)
  - 006/007/008: »Die Schwerpunkte liegen im Jahr 2025 beim Schulbau mit 459,1 Millionen Euro, dem ÖPNV mit 99 Millionen
    Euro (davon 53,9 Millionen Euro für die Stadtbahnlinie U81) …« (006 vom Werkzeug als kein_treffer, Stelle von Hand bestätigt).
- Zählung jetzt: 92 vorschlag, 22 zahl_abweichend, 50 kein_treffer, 0 archiv_leer.
