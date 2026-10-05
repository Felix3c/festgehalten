---
id: gelsenkirchen-2026-001
institution: Stadt Gelsenkirchen
gesagt_von: 'Stadt Gelsenkirchen, Mitteilungstext (Pressemeldung „Liboriusstraße voll gesperrt“)'
gesagt_am: 2026-09-25
quelle: https://www.gelsenkirchen.de/de/_meta/aktuelles/artikel/72807-liboriusstrasse-voll-gesperrt
zitat: "Die Fahrbahn wurde großflächig unterspült, sodass die Reparaturarbeiten bis Ende Oktober 2026 dauern werden."
frage: Ist die Vollsperrung der Liboriusstraße zwischen Dresdener Straße und Bismarckstraße bis zum 31.10.2026 aufgehoben?
typ: ja_nein
pruefung_am: 2026-11-01
prognosen:
  - von: Stadt Gelsenkirchen
    wert: 1.00
    hinterlegt_am: 2026-09-25
    art: angekuendigt
  - von: Computer
    wert: 0.50
    hinterlegt_am: 2026-10-05
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-05
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle am 05.10.2026 zweimal abgerufen, Zitat beide Male wörtlich."
  - am: 2026-10-05
    text: "Archiv: https://web.archive.org/web/20261004231657/https://www.gelsenkirchen.de/de/_meta/aktuelles/artikel/72807-liboriusstrasse-voll-gesperrt (Archivkopie vom 04.10.2026, Zitat am 05.10.2026 wörtlich in der Archivkopie geprüft). Lokale Kopie der Quelle vom 05.10.2026: recherche/belege/2026-10-05-gelsenkirchen-artikel-72807.html, SHA-256 942014e552c2659721858297911b55689977fb61b754319580a5f498292d2454."
---

## Kontext
Liboriusstraße: seit 22.09.2026 nach einem Wasserrohrbruch voll gesperrt, Fahrbahn großflächig unterspült, Reparatur bis Ende Oktober 2026. Gesagt: 25.09.2026 (Pressemeldung „Liboriusstraße voll gesperrt“); wer: Stadt Gelsenkirchen, Mitteilungstext.

## Übersetzung
Vorbehalt: keiner im Satz („dauern werden“) → `angekuendigt`, 1,00. Nur Monat genannt → Stichtag Monatsende 31.10.2026. Ja, wenn die Vollsperrung bis zum Stichtag aufgehoben und das öffentlich belegt ist. Beleg später: Pressemeldung der Stadt (Freigabe oder Verlängerung), Baustellenübersicht, Lokalpresse (WAZ Gelsenkirchen). `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse Tiefbau, Termin wenige Monate voraus (0,50–0,60). Notreparatur nach Unterspülung: der Schaden wird oft erst beim Aufgraben ganz sichtbar; dafür ist der Termin frisch gesetzt und nur fünf Wochen weit. Die Stadt meldet Freigaben selten eigens (ohne Beleg kein Ja). Rund 0,50. Hinterlegt am 05.10.2026, vor `pruefung_am`.
