---
id: muenster-2026-018
institution: Stadt Münster
gesagt_von: 'Stadt Münster, Mitteilungstext (Pressemitteilung „Bäume am Schulzentrum Wolbeck werden seit Dienstag umgesetzt")'
gesagt_am: 2026-10-20
quelle: https://pressemitteilungen.stadt-muenster.de/api/item/1230062
zitat: "Der Baubeginn ist für das erste Quartal 2027 geplant, die Fertigstellung für das zweite Quartal 2029."
frage: Haben die Bauarbeiten für den Erweiterungsbau der Hauptschule Wolbeck und der Musikschule am Schulzentrum Wolbeck bis einschließlich 31.03.2027 begonnen?
typ: ja_nein
pruefung_am: 2027-04-01
prognosen:
  - von: Stadt Münster
    wert: 0.80
    hinterlegt_am: 2026-10-20
    art: voraussichtlich
  - von: Computer
    wert: 0.50
    hinterlegt_am: 2026-10-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-28
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026; Münster zweiter Durchgang); Quelle abgerufen 28.10.2026."
  - am: 2026-10-28
    text: "Quelle ist die Schnittstelle des Presseportals der Stadt (Feld plain_article); Leseansicht derselben Mitteilung: https://www.stadt-muenster.de/aktuelles/pressemitteilungen#/item/1230062."
  - am: 2026-10-28
    text: "Lokale Kopie der Quelle: recherche/belege/2026-10-28-muenster-item-1230062.json, SHA-256 8fa1da513780028b4cc30cf2919056176e75c3fd161673d5f2188bfb69e5ffe0. Archivkopie noch offen (am 28.10.2026 nicht angelegt)."
---

## Kontext
Erweiterung des Schulzentrums Wolbeck: Neubau für die Hauptschule Wolbeck und die Musikschule im Nordwesten des Schulgeländes. Baubeschluss Juli 2025; der Rat bestätigte am 20.05.2026 die Verpflanzung von 24 Bäumen, die am 20.10.2026 begann. Gesagt: 20.10.2026; wer: Stadt Münster, Pressemitteilung (SMS).

## Übersetzung
Vorbehalt: „geplant" → `voraussichtlich`, 0,80. Stichtag 31.03.2027 (Ende des ersten Quartals). Ja, wenn bis zum Stichtag belegt ist, dass die Bauarbeiten am Erweiterungsbau selbst begonnen haben (Baustelle mit Aushub oder Gründung, Spatenstich mit anschließendem Bau; Meldung der Stadt, Westfälische Nachrichten, datiertes Foto). Baumverpflanzung, Fällungen, Kampfmittelsuche und reine Ausschreibung zählen nicht. Ohne Beleg bis zum Prüftag: Nein. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse städtischer Schulneubau mit fertigem Baubeschluss: Der Baustart rutscht oft um ein Quartal, meist wegen Vergabe und Bauantrag. Dafür: Beschluss seit 2025, das Baufeld wird im Herbst 2026 frei gemacht, die Vorbereitung läuft also. Dagegen: Ausschreibung im Winter, Münster hat 2026 mehrere Hochbauten verschoben (siehe muenster-2026-015), und „Baubeginn" kann auch ein Spatenstich ohne echten Bau sein, der hier nicht zählt. Rund 0,50. Hinterlegt am 28.10.2026, vor `pruefung_am`.
