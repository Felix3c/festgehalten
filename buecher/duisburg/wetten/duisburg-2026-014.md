---
id: duisburg-2026-014
institution: Stadt Duisburg
gesagt_von: 'Duisburger Verkehrsgesellschaft AG (DVG), Pressemitteilung „Arbeiten an der Kehranlage Watereck: Busse statt Bahnen auf einem Teil der Linie 903“'
gesagt_am: 2026-10-09
quelle: https://www.dvg-duisburg.de/die-dvg/news-presse/pressemitteilung/arbeiten-an-der-kehranlage-watereck-busse-statt-bahnen-auf-einem-teil-der-linie-903
zitat: "Wegen Arbeiten im Bereich der Kehranlage Watereck wird die Straßenbahnlinie 903 der Duisburger Verkehrsgesellschaft AG (DVG) von Samstag, 17. Oktober, bis einschließlich Sonntag, 15. November 2026, an der Haltestelle „Walsum Betriebshof“ getrennt."
frage: Fährt die Straßenbahnlinie 903 am Montag, 16.11.2026, wieder durchgehend zwischen „Walsum Betriebshof“ und „Dinslaken Bahnhof“, ohne Schienenersatzverkehr wegen der Arbeiten an der Kehranlage Watereck?
typ: ja_nein
pruefung_am: 2026-11-17
prognosen:
  - von: Stadt Duisburg
    wert: 1.00
    hinterlegt_am: 2026-10-09
    art: angekuendigt
  - von: Computer
    wert: 0.85
    hinterlegt_am: 2026-10-28
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-28
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Guard reihum, Duisburg zweiter Durchgang); Quelle am 28.10.2026 zweimal abgerufen, beide Kopien byte-gleich, Zitat beide Male wörtlich. robots.txt der DVG sperrt nur /typo3/."
  - am: 2026-10-28
    text: "Archiv: kein Save Page Now (Archiv-Sicherung wartet auf eine Entscheidung des Halters). Lokale Kopie der Quelle vom 28.10.2026: recherche/belege/2026-10-28-duisburg-dvg-903-sev.html, SHA-256 81c4936206fb4e94a1d31409875573c3ebe7ebbd9b08635bc393fa94a6c4c4ae."
---

## Kontext
Die DVG ist der Verkehrsbetrieb der Stadt Duisburg (DVV-Konzern), das Buch zählt ihre Mitteilungen zur Stadt. Während der Arbeiten an der Kehranlage Watereck fahren die Bahnen der Linie 903 nur bis „Walsum Betriebshof“, zwischen dort und „Dinslaken Bahnhof“ fahren Busse im Schienenersatzverkehr. Radio Duisburg hat die Meldung am 14.10.2026 wiedergegeben („Die Änderung gilt bis einschließlich Sonntag, 15. November 2026.“). Gesagt: 09.10.2026; wer: DVG, Pressemitteilung.

## Übersetzung
Kein Vorbehalt im Satz → `angekuendigt`, 1,00. Der letzte Tag mit getrennter Linie ist Sonntag, 15.11.2026; gefragt ist der erste Betriebstag danach. Ja, wenn die 903 am 16.11.2026 laut DVG (Verkehrsmeldungen, Fahrplanauskunft, Mitteilung) wieder bis „Dinslaken Bahnhof“ fährt. Nein, wenn die DVG die Trennung wegen der Arbeiten an der Kehranlage verlängert. Eine Störung an diesem Tag aus anderem Grund (Unfall, Polizeieinsatz) zählt nicht als Nein. Ohne Beleg bleibt die Wette offen. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse: kurze, angekündigte Gleisbaustellen im Straßenbahnnetz mit festem Enddatum (vergleichbar bochum-2026-013, Rückbau bis 13.11.). Dafür: Der Zeitraum ist auf den Tag genannt, die Busse sind bestellt, und Ersatzverkehr kostet den Betrieb jeden Tag Geld. Dagegen: Arbeiten im November hängen am Wetter, und Gleisbau wird öfter um Tage oder Wochen verlängert, als dass er früher endet. Rund 0,85. Hinterlegt am 28.10.2026, vor `pruefung_am`.
