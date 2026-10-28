---
id: muenster-2026-020
institution: Stadt Münster
gesagt_von: 'Stadt Münster, Mitteilungstext (Pressemitteilung „Bahnhof Hiltrup: Stadt erneuert Pflaster der Unterführung")'
gesagt_am: 2026-10-27
quelle: https://pressemitteilungen.stadt-muenster.de/api/item/1230542
zitat: "Die Stadt Münster erneuert voraussichtlich ab Montag, 2. November, das Pflaster im Bereich der Unterführung am Bahnhof Münster-Hiltrup. … Die Bauarbeiten sind voraussichtlich nach ungefähr drei Monaten abgeschlossen."
frage: Ist die Erneuerung des Pflasters in der Unterführung am Bahnhof Münster-Hiltrup (parallel zur Straße Osttor) bis einschließlich 02.02.2027 abgeschlossen?
typ: ja_nein
pruefung_am: 2027-02-03
prognosen:
  - von: Stadt Münster
    wert: 0.80
    hinterlegt_am: 2026-10-27
    art: voraussichtlich
  - von: Computer
    wert: 0.45
    hinterlegt_am: 2026-10-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-28
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026; Münster zweiter Durchgang); Quelle abgerufen 28.10.2026."
  - am: 2026-10-28
    text: "Quelle ist die Schnittstelle des Presseportals der Stadt (Feld plain_article); Leseansicht derselben Mitteilung: https://www.stadt-muenster.de/aktuelles/pressemitteilungen#/item/1230542."
  - am: 2026-10-28
    text: "Lokale Kopie der Quelle: recherche/belege/2026-10-28-muenster-item-1230542.json, SHA-256 88489bd645433dbbafdb48c2eaa18ee33d6df5b4762c45b542f40a91e4ddf149. Archivkopie noch offen (am 28.10.2026 nicht angelegt)."
---

## Kontext
Neues Pflaster in der Fuß- und Radunterführung am Bahnhof Hiltrup, parallel zur Straße Osttor. Arbeiten in mehreren Abschnitten, der Zugang zu den Bahnsteigen bleibt offen. Gesagt: 27.10.2026; wer: Stadt Münster, Pressemitteilung (SMS).

## Übersetzung
Vorbehalt: „voraussichtlich", „ungefähr" → `voraussichtlich`, 0,80. Stichtag: 02.11.2026 plus drei Monate = 02.02.2027. Ja, wenn bis zum Stichtag belegt ist, dass die Pflasterarbeiten fertig und die Absperrungen weg sind (Meldung der Stadt, Westfälische Nachrichten, datiertes Foto). Beginnen die Arbeiten später als am 02.11., ändert das die Frage nicht. Ohne Beleg bis zum Prüftag: Nein. `pruefung_am` ist der Folgetag.

## Begründung Computer
Pflasterarbeit in Abschnitten von November bis Januar: Frost und Nässe halten solche Arbeiten oft auf, und „ungefähr drei Monate" lässt Spielraum, den die Frage nicht gibt. Dafür: kleine Fläche in der Unterführung, also weniger wetterabhängig als eine offene Straße. Dazu das Belegrisiko einer fehlenden Abschlussmeldung. Rund 0,45. Hinterlegt am 28.10.2026, vor `pruefung_am`.
