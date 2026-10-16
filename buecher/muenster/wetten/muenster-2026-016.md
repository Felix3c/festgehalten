---
id: muenster-2026-016
institution: Stadt Münster
gesagt_von: 'Stadt Münster, Mitteilungstext (Pressemitteilung „Vollsperrung: Stadt saniert Annette-von-Droste-Hülshoff-Straße in Roxel")'
gesagt_am: 2026-10-15
quelle: https://pressemitteilungen.stadt-muenster.de/api/item/1229716
zitat: "Die Stadt Münster saniert ab Montag, 19. Oktober, die Fahrbahn der Annette-von-Droste-Hülshoff-Straße in Roxel. … Die Arbeiten dauern voraussichtlich bis zum 6. November."
frage: Ist die Vollsperrung der Annette-von-Droste-Hülshoff-Straße in Roxel (zwischen Alter Gemeindeplatz und Kirchplatz/Pantaleonstraße) bis einschließlich 06.11.2026 aufgehoben?
typ: ja_nein
pruefung_am: 2026-11-07
prognosen:
  - von: Stadt Münster
    wert: 0.80
    hinterlegt_am: 2026-10-15
    art: voraussichtlich
  - von: Computer
    wert: 0.65
    hinterlegt_am: 2026-10-16
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-16
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle abgerufen 16.10.2026."
  - am: 2026-10-16
    text: "Quelle ist die Schnittstelle des Presseportals der Stadt (Feld plain_article); Leseansicht derselben Mitteilung: https://www.stadt-muenster.de/aktuelles/pressemitteilungen#/item/1229716."
  - am: 2026-10-16
    text: "Archiv: https://web.archive.org/web/20261016030014/https://pressemitteilungen.stadt-muenster.de/api/item/1229716 (beide Zitatteile am 16.10.2026 wörtlich in der Archivkopie geprüft). Lokale Kopie der Quelle: recherche/belege/2026-10-16-muenster-item-1229716.json, SHA-256 9cbb35fe9520469f6aaf262ea990ec6e04a71e8d0747b9e6d332ac57908293c2."
---

## Kontext
Fahrbahnsanierung im Ortskern von Roxel. Gesperrt für Kfz ist der Abschnitt zwischen Alter Gemeindeplatz und Kirchplatz/Pantaleonstraße; Umleitung über Tilbecker, Bösenseller und Havixbecker Straße, Fuß- und Radverkehr kommt an der Baustelle vorbei. Gesagt: 15.10.2026; wer: Stadt Münster, Pressemitteilung (SMS).

## Übersetzung
Vorbehalt: „voraussichtlich“ → `voraussichtlich`, 0,80. Ja, wenn bis einschließlich 06.11.2026 belegt ist, dass der gesperrte Abschnitt wieder für Kfz befahrbar ist (Freigabe-Meldung der Stadt, Verkehrsmeldung, Lokalpresse wie Westfälische Nachrichten, datiertes Foto). Restarbeiten unter halbseitiger Sperrung oder Ampel zählen als Ja, eine Verlängerung der Vollsperrung über den 06.11. hinaus als Nein. Startet die Sanierung später als am 19.10., ändert das die Frage nicht. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse reine Fahrbahnsanierung (Deckenerneuerung) auf kurzem Abschnitt, knapp drei Wochen angesetzt: solche Termine halten oft, Verzug kommt vor allem durch Regen und Kälte beim Asphalt (Ende Oktober/Anfang November) und durch Funde im Unterbau. Dafür: kleiner Abschnitt, Ankündigung vier Tage vor Beginn, also mit fertiger Planung. Dagegen: Herbstwetter, kein Puffer genannt. Dazu das Belegrisiko: Eine Freigabe nach drei Wochen bekommt nicht immer eine eigene Meldung. Rund 0,65. Hinterlegt am 16.10.2026, vor `pruefung_am`.
