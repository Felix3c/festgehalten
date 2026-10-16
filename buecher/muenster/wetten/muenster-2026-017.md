---
id: muenster-2026-017
institution: Stadt Münster
gesagt_von: 'Stadt Münster, Mitteilungstext (Pressemitteilung „Nachtarbeiten mit Vollsperrung an der Hörsterstraße")'
gesagt_am: 2026-10-12
quelle: https://pressemitteilungen.stadt-muenster.de/api/item/1229440
zitat: "Die Arbeiten für den Kreuzungsbereich Hörsterstraße/Lotharingerstraße beginnen am Montag, 19. Oktober, und dauern voraussichtlich bis Mittwoch, 21. Oktober."
frage: Sind die nächtlichen Asphaltarbeiten im Kreuzungsbereich Hörsterstraße/Lotharingerstraße bis einschließlich 21.10.2026 abgeschlossen und die nächtliche Vollsperrung dort aufgehoben?
typ: ja_nein
pruefung_am: 2026-10-22
prognosen:
  - von: Stadt Münster
    wert: 0.80
    hinterlegt_am: 2026-10-12
    art: voraussichtlich
  - von: Computer
    wert: 0.60
    hinterlegt_am: 2026-10-16
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-16
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle abgerufen 16.10.2026."
  - am: 2026-10-16
    text: "Quelle ist die Schnittstelle des Presseportals der Stadt (Feld plain_article); Leseansicht derselben Mitteilung: https://www.stadt-muenster.de/aktuelles/pressemitteilungen#/item/1229440."
  - am: 2026-10-16
    text: "Archiv: https://web.archive.org/web/20261016035420/https://pressemitteilungen.stadt-muenster.de/api/item/1229440 (Zitat am 16.10.2026 wörtlich in der Archivkopie geprüft). Lokale Kopie der Quelle: recherche/belege/2026-10-16-muenster-item-1229440.json, SHA-256 b76951f37b08751a4a2e1d25ddf3bfaa1dc2e6f05c657b267c6cf3fca1358df9."
  - am: 2026-10-16
    text: "Nur der zweite Abschnitt ist Gegenstand. Der erste (Gartenstraße/Hörstertor, 13. bis voraussichtlich 17.10.) lief beim Hinterlegen schon und wird darum nicht gewettet."
---

## Kontext
Asphaltierung zweier Kreuzungen am Rand der Altstadt, im Anschluss an Leitungsarbeiten der Stadtnetze vor der Umgestaltung des Martiniviertels. Gesperrt wird jeweils von 21 bis 5 Uhr; Fuß- und Radverkehr kommt durch, die Promenade dazwischen bleibt offen. Umleitung für den zweiten Abschnitt ab Kanalstraße über Lublinring, Gartenstraße und Hörstertor. Gesagt: 12.10.2026; wer: Stadt Münster, Pressemitteilung (SMS).

## Übersetzung
Vorbehalt: „voraussichtlich“ → `voraussichtlich`, 0,80. Ja, wenn belegt ist, dass im Kreuzungsbereich Hörsterstraße/Lotharingerstraße nach der Nacht vom 21. auf den 22.10.2026 keine nächtliche Vollsperrung mehr gilt (Meldung der Stadt, Verkehrsmeldung, Lokalpresse wie Westfälische Nachrichten, datiertes Foto). Kleine Nacharbeiten ohne Vollsperrung zählen als Ja; eine angekündigte oder belegte Verlängerung der Vollsperrung über den 21.10. hinaus als Nein. Beginnen die Arbeiten später als am 19.10., ändert das die Frage nicht. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse kurze nächtliche Deckenarbeiten an einer Kreuzung, drei Nächte angesetzt: Solche Fenster halten meist, weil Fräsen und Einbauen fest getaktet sind. Dagegen spricht: Regen oder Kälte Ende Oktober verschieben Asphaltnächte, und der erste Abschnitt direkt davor kann sich in die neue Woche ziehen. Größter Abzug ist das Belegrisiko: Für das Ende von drei Nachtschichten gibt es selten eine eigene Meldung, ohne Beleg bleibt die Wette offen. Rund 0,60. Hinterlegt am 16.10.2026, vor `pruefung_am`.
