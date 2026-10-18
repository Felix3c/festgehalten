---
id: dortmund-2026-027
institution: Stadt Dortmund
gesagt_von: 'Stadt Dortmund, Pressestelle (Medieneinladung „Grundsteinlegung für den neuen Zentralplatz im Westfalenpark Dortmund“)'
gesagt_am: 2026-10-11
quelle: https://www.dortmund.de/newsroom/presse-mitteilungen/medieneinladung-grundsteinlegung-fuer-den-neuen-zentralplatz-im-westfalenpark-dortmund.html
zitat: "Nach aktueller Prognose soll im Herbst 2027 alles fertig sein."
frage: Ist der umgestaltete Zentralplatz im Westfalenpark Dortmund bis zum 30.11.2027 fertig und für Besucher geöffnet?
typ: ja_nein
pruefung_am: 2027-12-01
prognosen:
  - von: Stadt Dortmund
    wert: 0.80
    hinterlegt_am: 2026-10-11
    art: voraussichtlich
  - von: Computer
    wert: 0.40
    hinterlegt_am: 2026-10-18
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-18
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Freigabe Felix 18.10.2026 zu Frage 397, Mail „Alles so wie du es vorgeschlagen hast“; Kandidat aus recherche/ANKUENDIGUNGEN-KW42-2026-10-18-ENTWURF.md). Quelle am 18.10.2026 abgerufen (auf der Seite datiert So 11.10.2026, 12:00 Uhr), Zitat wörtlich; lokale Kopie recherche/belege/2026-10-18-dortmund-pm-westfalenpark-zentralplatz.html, SHA-256 d36b47757cf5cc620c405923b919baf2262c21cb7142f52cc0d9cb5ce0f21ec8; Archiv https://web.archive.org/web/20261018180458/https://www.dortmund.de/newsroom/presse-mitteilungen/medieneinladung-grundsteinlegung-fuer-den-neuen-zentralplatz-im-westfalenpark-dortmund.html (am 18.10.2026 abgerufen, Zitat darin geprüft)."
---

## Kontext
Der Zentralplatz im Westfalenpark wird neu gestaltet: neue Wasserflächen, Aufenthaltsbereiche, eine offene, überdachte Terrasse, ein Café-Neubau, Beleuchtung, der Neubau der Vogelvoliere und barrierefreie Wege. Rückbau seit Februar 2026, Rohbau seit August 2026, symbolische Grundsteinlegung am 20.10.2026. Die Stadt nennt „rund 9,04 Millionen Euro netto“ als Investitionsvolumen (gleiche Quelle, Satz davor).

## Übersetzung
Vorbehalt „Nach aktueller Prognose soll“ → `voraussichtlich`, 0,80. „Im Herbst 2027“ → Stichtag Ende des meteorologischen Herbstes, 30.11.2027 (wie aachen-2026-009). Ja, wenn der Zentralplatz bis zum Stichtag fertig ist und Besuchern offensteht, also Wasserflächen, Terrasse und Café-Neubau nutzbar sind (Pressemitteilung, Westfalenpark-Seite, datiertes Foto vor Ort). Einzelne Restarbeiten an Beleuchtung oder Bepflanzung ändern nichts, ein abgesperrter Platz oder ein Café im Rohbau schon. Die Kosten (9,04 Mio. € netto) gehören nicht zur Wette und können später eine eigene werden. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse kommunaler Hochbau mit Wasser- und Gebäudeteil, Fertigstellung gut ein Jahr voraus: solche Termine halten selten mehr als zur Hälfte. Für die Stadt spricht, dass der Bau schon läuft. Dagegen: „alles fertig“ umfasst Café, Voliere und Technik, also mehrere Gewerke, und Prognosen in Medieneinladungen sind eher optimistisch. Rund 0,40. Hinterlegt am 18.10.2026, vor `pruefung_am`.
