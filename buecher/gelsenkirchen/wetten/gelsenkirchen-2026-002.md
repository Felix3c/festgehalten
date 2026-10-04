---
id: gelsenkirchen-2026-002
institution: Stadt Gelsenkirchen
gesagt_von: 'Stadt Gelsenkirchen, Mitteilungstext (Pressemeldung „Gasleitung wird erneuert“)'
gesagt_am: 2026-07-20
quelle: https://www.gelsenkirchen.de/de/_meta/aktuelles/artikel/71978-gasleitung-wird-erneuert
zitat: "Die Arbeiten starten mit Beginn der Sommerferien in NRW und werden witterungsabhängig voraussichtlich im Oktober 2026 abgeschlossen."
frage: Ist die Erneuerung der Gasleitung auf der Kurt-Schumacher-Straße zwischen Florastraße und Berliner Brücke (Fahrtrichtung Buer) bis zum 31.10.2026 abgeschlossen?
typ: ja_nein
pruefung_am: 2026-11-01
prognosen:
  - von: Stadt Gelsenkirchen
    wert: 0.80
    hinterlegt_am: 2026-07-20
    art: voraussichtlich
  - von: Computer
    wert: 0.45
    hinterlegt_am: 2026-10-05
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-05
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle am 05.10.2026 zweimal abgerufen, Zitat beide Male wörtlich."
  - am: 2026-10-05
    text: "Archiv: Save Page Now am 05.10.2026 abgewiesen (HTTP 429, zu viele Anfragen), Archivkopie wird nachgezogen. Lokale Kopie der Quelle vom 05.10.2026: recherche/belege/2026-10-05-gelsenkirchen-artikel-71978.html, SHA-256 fe9cb174f999226982d37ccd2d894bb198cedc612d60d0acfbf1d3876d869f11."
---

## Kontext
Kurt-Schumacher-Straße: Erneuerung der Gasleitung im Auftrag der EVNG seit 20.07.2026, gleichzeitig mit der Baumaßnahme Berliner Brücke; Verkehr einspurig, Abschluss im Oktober 2026. Gesagt: 20.07.2026 (Pressemeldung „Gasleitung wird erneuert“); wer: Stadt Gelsenkirchen, Mitteilungstext.

## Übersetzung
Vorbehalt: „witterungsabhängig voraussichtlich“ → `voraussichtlich`, 0,80. Nur Monat genannt → Stichtag Monatsende 31.10.2026. Ja, wenn die Arbeiten an der Gasleitung bis zum Stichtag abgeschlossen sind und das öffentlich belegt ist (die Baumaßnahme Berliner Brücke selbst ist nicht gefragt). Beleg später: Pressemeldung der Stadt, Baustellenübersicht, Lokalpresse. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse Tiefbau, Termin wenige Monate voraus (0,50–0,60). Abzug: Die Leitung wird laut Mitteilung zusammen mit der Baumaßnahme Berliner Brücke eingebaut, hängt also an einem zweiten Bauablauf; und der Abschluss einer Leitungsbaustelle wird selten gemeldet. Rund 0,45. Hinterlegt am 05.10.2026, vor `pruefung_am`.
