---
id: muelheim-2026-009
institution: Stadt Mülheim an der Ruhr
gesagt_von: 'Stadt Mülheim an der Ruhr, Mitteilungstext (Meldung „Land Nordrhein-Westfalen fördert Neubau mit über 10 Millionen Euro: Regierungspräsident Schürmann überreicht Zuwendungsbescheid“)'
gesagt_am: 2026-03-04
quelle: https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen/land-nordrhein-westfalen-foerdert-neubau-mit-ueber-10
zitat: "Mit der Übergabe des Bewilligungsbescheides beginnt nun die konkrete Umsetzungsphase: Der geplante Baubeginn ist für Anfang 2028 vorgesehen, die voraussichtliche Fertigstellung ist zum Schuljahr 2029/2030 geplant."
frage: Ist die Dreifachsporthalle mit Krafttrainingsraum an der Luisenschule (Südstraße) in Mülheim an der Ruhr bis zum 30.09.2029 fertiggestellt und in Benutzung?
typ: ja_nein
pruefung_am: 2029-10-01
prognosen:
  - von: Stadt Mülheim an der Ruhr
    wert: 0.80
    hinterlegt_am: 2026-03-04
    art: voraussichtlich
  - von: Computer
    wert: 0.30
    hinterlegt_am: 2026-10-05
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-05
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle am 05.10.2026 zweimal abgerufen (Seite der Meldung, zwei getrennte Abrufe am selben Mittag), Zitat beide Male wörtlich."
  - am: 2026-10-05
    text: "Archiv: https://web.archive.org/web/20260412134832/https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen/land-nordrhein-westfalen-foerdert-neubau-mit-ueber-10 (Archivkopie vom 12.04.2026, Zitat am 05.10.2026 wörtlich in der Archivkopie geprüft). Lokale Kopie der Quelle vom 05.10.2026: recherche/belege/2026-10-05-muelheim-sporthalle-luisenschule.html, SHA-256 3491f59a5fe4c7553e34468ed4f9a6ae7cdc827b60e22dafdef850d7d64622e7."
---

## Kontext
Die Stadt baut mit 10.121.096 Euro vom Land (Bescheid vom 04.03.2026) eine Dreifachsporthalle nach DIN 18032 mit Gymnastik- und Krafttrainingsraum an der NRW-Sportschule Luisenschule, Gesamtvolumen rund 13,9 Millionen Euro. Geplant sind Photovoltaik auf dem Dach und ein Anschluss an ein Nahwärmenetz; abends und am Wochenende sollen Vereine die Halle nutzen. Gesagt: 04.03.2026 (Meldung „Land Nordrhein-Westfalen fördert Neubau mit über 10 Millionen Euro: Regierungspräsident Schürmann überreicht Zuwendungsbescheid“); wer: Stadt Mülheim an der Ruhr, Mitteilungstext.

## Übersetzung
Vorbehalt: „voraussichtliche“, „geplant“ → `voraussichtlich`, 0,80. Gemessen wird der zweite Teil des Satzes. „Zum Schuljahr 2029/2030“ → Stichtag 30.09.2029 (Puffer nach Schuljahresbeginn; das genaue Ferienende NRW 2029 ist hier ungeklärt). Ja, wenn bis zum Stichtag in der Halle Schul- oder Vereinssport stattfindet. Der Baubeginn steht in muelheim-2026-008. Beleg später: Meldung der Stadt, Lokalpresse (WAZ Mülheim), Seite der Luisenschule. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse Hochbau, Termin über ein Jahr voraus (0,30–0,45). Am unteren Rand: Der Plan lässt vom Baubeginn Anfang 2028 bis zum Schuljahr 2029/2030 rund anderthalb Jahre, das ist für eine Dreifachhalle machbar, aber nur, wenn der Baubeginn hält (eigene Wette, vom Computer mit 0,45 geschätzt). Der Termin liegt drei Jahre voraus, Planung und Vergabe stehen noch aus. Dafür: feste Förderung, eine Halle ist ein Standardbau. Rund 0,30. Hinterlegt am 05.10.2026, vor `pruefung_am`.
