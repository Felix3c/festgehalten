---
id: oberhausen-2026-002
institution: Stadt Oberhausen
gesagt_von: 'Stadt Oberhausen, Mitteilungstext (Pressemeldung „Zweiter Bauabschnitt auf der Kewerstraße/Bebelstraße steht bevor“)'
gesagt_am: 2026-04-21
quelle: https://www.oberhausen.de/de/index/rathaus/aktuelle-pressemeldungen/meldungen_2026/zweiter_bauabschnitt_auf_der_kewerstraszebebelstrasze_steht_bevor.php
zitat: "Dafür muss das Teilstück zwischen der Behrensstraße und der Püttstraße von Montag, 27. April 2026, bis voraussichtlich Ende Dezember 2026 voll für den Fahrzeugverkehr gesperrt werden."
frage: Ist die Vollsperrung der Kewerstraße zwischen Behrensstraße und Püttstraße bis zum 31.12.2026 aufgehoben?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: Stadt Oberhausen
    wert: 0.80
    hinterlegt_am: 2026-04-21
    art: voraussichtlich
  - von: Computer
    wert: 0.40
    hinterlegt_am: 2026-10-05
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-05
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle am 05.10.2026 zweimal abgerufen, Zitat beide Male wörtlich."
  - am: 2026-10-05
    text: "Archiv: https://web.archive.org/web/20261005051945/https://www.oberhausen.de/de/index/rathaus/aktuelle-pressemeldungen/meldungen_2026/zweiter_bauabschnitt_auf_der_kewerstraszebebelstrasze_steht_bevor.php (Archivkopie vom 05.10.2026, Zitat am 05.10.2026 wörtlich in der Archivkopie geprüft). Lokale Kopie der Quelle vom 05.10.2026: recherche/belege/2026-10-05-oberhausen-kewerstrasse-bebelstrasse.html, SHA-256 9381d5dd7222c6adfbf56a6206504c36f63a152893ccfb1a3732b59f2a871c66."
---

## Kontext
Kewerstraße/Bebelstraße: Straßenausbau zusammen mit Kanalarbeiten, zweiter Bauabschnitt seit 27.04.2026. Die Meldung nennt keinen Bauherrn; der Straßenausbau wird hier als Vorhaben der Stadt gelesen (siehe BUCH.md). Gesagt: 21.04.2026 (Pressemeldung „Zweiter Bauabschnitt auf der Kewerstraße/Bebelstraße steht bevor“); wer: Stadt Oberhausen, Mitteilungstext.

## Übersetzung
Vorbehalt: „voraussichtlich“ → `voraussichtlich`, 0,80. „Ende Dezember 2026“ → Stichtag 31.12.2026. Ja, wenn das Teilstück bis zum Stichtag wieder für den Fahrzeugverkehr frei ist und das öffentlich belegt ist. Beleg später: Pressemeldung der Stadt, Lokalpresse (WAZ/NRZ Oberhausen), Baustellenübersicht der Stadt. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse Tiefbau, Termin wenige Monate voraus (0,50–0,60). Schlechter als die Klasse: acht Monate Vollsperrung für Kanal und Straße zusammen, Abschluss mitten im Winter (Asphalt- und Pflasterarbeiten sind frostabhängig); die Stadt hat im selben Jahr an der Hessenstraße einen Termin um acht Monate verschoben. Rund 0,40. Hinterlegt am 05.10.2026, vor `pruefung_am`.
