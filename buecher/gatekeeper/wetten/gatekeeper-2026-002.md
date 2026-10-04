---
id: gatekeeper-2026-002
institution: Alphabet
gesagt_von: "Google (Pressemitteilung „Google Announces €5.5 Billion Investment in Germany“, Google Cloud Press Corner)"
gesagt_am: 2025-11-11
quelle: https://www.googlecloudpresscorner.com/2025-11-11-Google-Announces-EUR5-5-Billion-Investment-in-Germany,-including-AI-Infrastructure,-through-2029
zitat: "Leveraging the CFE Manager and Google's other clean energy initiatives, Google's German operations are projected to run at or near 85% carbon-free energy in 2026"
frage: "Weist Google für das Jahr 2026 für seine deutschen Cloud-Regionen (europe-west3 Frankfurt und europe-west10 Berlin) einen „Google CFE%“ von mindestens 83 % aus?"
typ: ja_nein
pruefung_am: 2027-08-01
prognosen:
  - von: Alphabet
    wert: 0.80
    hinterlegt_am: 2025-11-11
    art: voraussichtlich
  - von: Computer
    wert: 0.30
    hinterlegt_am: 2026-10-03
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-03
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle abgerufen und Zitat wörtlich geprüft 03.10.2026, Prüfweg in docs/2026-10-03-buch-gatekeeper-KANDIDATEN.md."
---

## Kontext
Für 2025 nennt dieselbe Google-Tabelle (abgerufen 03.10.2026, „provided the 2025 data below“) für Frankfurt und Berlin jeweils 70 %. Verlangt ist also ein Sprung um 15 Punkte in einem Jahr. Mittel dazu sind laut Pressemitteilung der erweiterte CFE-Vertrag mit Engie (bis 2030, mit Batteriespeichern) und die Abnahme aus dem Offshore-Windpark Borkum Riffgrund 3 (Ørsted).

## Übersetzung
Beleg ist Googles Tabelle „Carbon free energy for Google Cloud regions“ (https://cloud.google.com/sustainability/region-carbon) mit den Jahresdaten 2026 oder der Umweltbericht 2027. „At or near 85 %“ wird als ≥ 83 % übersetzt. Weisen die beiden Regionen unterschiedliche Werte aus, zählt der niedrigere. Liegen die Daten 2026 zum `pruefung_am` noch nicht vor, wird gewartet (Verfall nach FORMAT).

## Begründung Computer
15 Punkte in einem Jahr sind viel, und das deutsche Netz wird wegen Dunkelflauten nur langsam CO₂-ärmer. Gleichzeitig wächst Googles Verbrauch in Deutschland durch den Ausbau in Hanau und Dietzenbach. Dass Google selbst eine Fußnote mit Vorbehalt angehängt hat, spricht ebenfalls gegen das Ziel. Hinterlegt am 03.10.2026, vor `pruefung_am`.
