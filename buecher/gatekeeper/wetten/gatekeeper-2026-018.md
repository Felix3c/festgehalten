---
id: gatekeeper-2026-018
institution: Amazon
gesagt_von: "Amazon.com, Inc. (Pressemitteilung zum dritten Quartal 2026, Highlights)"
gesagt_am: 2026-10-29
quelle: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx
zitat: "Remains on track to begin initial service of its Amazon Leo low Earth orbit satellite service later this year"
frage: "Hat Amazon bis zum 31.12.2026 den ersten Dienst von Amazon Leo für Kunden außerhalb von Amazon begonnen, und sagt das eine eigene Mitteilung von Amazon?"
typ: ja_nein
pruefung_am: 2027-01-15
prognosen:
  - von: Amazon
    wert: 0.80
    hinterlegt_am: 2026-10-29
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-10-30
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-30
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Guard Laufend, Q3-Zahlen Amazon). Quelle am 30.10.2026 abgerufen, Zitat wörtlich. Lokale Kopie: recherche/belege/2026-10-30-amazon-q3-2026-results.html, SHA-256 b41d6222769d6d5c9fa49470829795cdad5a379c4e5faaa32afb3487ee27a670."
---

## Kontext
Der Satz steht in der Liste der Fortschritte seit den letzten Zahlen, zusammen mit einem Abkommen mit AT&T, das Leo an Firmen und Behörden anbieten soll. Ein Startdatum nennt die Mitteilung nicht, nur „later this year“.

## Übersetzung
„Remains on track“ → `voraussichtlich`, 0,80. „Later this year“ wird zu 31.12.2026. „Initial service“ gilt als begonnen, wenn eine eigene Mitteilung von Amazon (Pressemitteilung, Blog, Investor Relations) sagt, dass Kunden außerhalb von Amazon Leo nutzen, auch als begrenzter Vorab-Dienst. Interne Tests von Amazon zählen nicht, Ankündigungen ohne laufenden Dienst auch nicht. Die Mitteilung darf nach dem 31.12. erscheinen, wenn sie einen Start bis dahin belegt; deshalb liegt `pruefung_am` zwei Wochen später.

## Begründung Computer
Amazon formuliert das im Quartalsbericht mit neun Wochen Restzeit, und die Hürde „initial service“ ist niedrig gewählt; das spricht für Ja. Dagegen: Satellitendienste verschieben sich oft, und der Start hängt an genügend Satelliten im Orbit, deren aktuelle Zahl hier nicht geprüft wurde. Rund 0,55. Hinterlegt am 30.10.2026, vor `pruefung_am`.
