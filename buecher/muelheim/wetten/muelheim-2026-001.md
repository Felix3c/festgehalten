---
id: muelheim-2026-001
institution: Stadt Mülheim an der Ruhr
gesagt_von: 'Stadt Mülheim an der Ruhr, Mitteilungstext (Meldung „Brücke Saarner Straße: Neuer Belag für Fahrbahn und Gehwege“)'
gesagt_am: 2026-08-21
quelle: https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen/bruecke-saarner-strasse-neuer-belag-fuer-fahrbahn-und-gehwege
zitat: "Im Bereich der Brücke Saarner Straße starten am Montag, 24. August 2026 Bauarbeiten. … Die Arbeiten dauern voraussichtlich neun Wochen."
frage: Sind die Bauarbeiten am Belag der Brücke Saarner Straße in Mülheim an der Ruhr (zwischen Karlsruher Straße und Steinbruchstraße) bis zum 25.10.2026 abgeschlossen?
typ: ja_nein
pruefung_am: 2026-10-26
prognosen:
  - von: Stadt Mülheim an der Ruhr
    wert: 0.80
    hinterlegt_am: 2026-08-21
    art: voraussichtlich
  - von: Computer
    wert: 0.50
    hinterlegt_am: 2026-10-05
    art: geschaetzt
ausgang: null
aufgeloest_am: null
beleg_ausgang: null
vermerke:
  - am: 2026-10-05
    text: "Hinterlegt durch Claude für den Halter (Dauerlauf, Auftrag Guard weiterbauen, Felix 03.10.2026); Quelle am 05.10.2026 zweimal abgerufen (Seite der Meldung, zwei getrennte Abrufe am selben Mittag), Zitat beide Male wörtlich."
  - am: 2026-10-05
    text: "Archiv: Save Page Now am 05.10.2026 ohne geprüfte Kopie (HTTP 404; Save Page Now nannte danach die Aufnahme 20261005102106, sie ließ sich am selben Tag nicht abspielen). Lokale Kopie der Quelle vom 05.10.2026: recherche/belege/2026-10-05-muelheim-bruecke-saarner-strasse.html, SHA-256 47b9479a64120c48fb2ced628ae626227efed832d1af31f474e33f9363671d2c."
  - am: 2026-10-08
    text: "Archiv nachgetragen: https://web.archive.org/web/20261005102106/https://cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen/bruecke-saarner-strasse-neuer-belag-fuer-fahrbahn-und-gehwege (Archivkopie vom 05.10.2026, am 08.10.2026 abspielbar, HTTP 200; Zitat am 08.10.2026 wörtlich in der Archivkopie geprüft, Kopie byte-gleich mit der lokalen Kopie, SHA-256 wie oben)."
  - am: 2026-10-26
    text: "Prüftag, nicht aufgelöst: keine Quelle für den Ausgang. Gesucht am 26.10.2026 abends: Meldungsliste der Stadt (cms.muelheim-ruhr.de/rathaus/aktuelles/aktuelle-meldungen, 202 Einträge, neueste Meldung zur Brücke weiter die vom 21.08.2026, keine Fertigmeldung); Baustellenportal der Stadt (geo.muelheim-ruhr.de/baustellen): kein Eintrag zur Brücke Saarner Straße, nur eine RWW-Maßnahme Saarner Straße Hausnummer 75 bis Wintgensweg (Ende 10.2026), die nichts mit der Brücke zu tun hat; Websuche (Radio Mülheim, WAZ) ohne Bericht nach dem 24.08.2026. Dass die Brücke im Portal fehlt, belegt weder Ja noch Nein (sie stand dort am 05.10. auch nicht). Ausgang bleibt offen; weiter suchen über Lokalpresse oder eine Anfrage bei der Pressestelle."
  - am: 2026-10-27
    text: "Zweite Suche 27.10.2026 mittags, weiter keine Quelle: Meldungsliste der Stadt (neueste Meldung zur Brücke weiter die vom 21.08.2026); Websuche WAZ Mülheim und Radio Mülheim ohne Bericht zur Brücke. verkehrslage.de führt am 27.10.2026 mehrere Einträge „Baustellen auf der Saarner Straße“ ohne Abschnitt (Kopie recherche/belege/2026-10-27-verkehrslage-muelheim-baustellen.html, SHA-256 a04ff981b0d2ae56f5994f129d4f2cc9ea5156ed071c1c9e388a99185d0db5fd); auf der Saarner Straße läuft daneben eine RWW-Maßnahme bis Ende 10.2026, die Einträge lassen sich der Brücke nicht zuordnen. Ausgang bleibt offen; nächster Weg ist eine Anfrage bei der Pressestelle (wartet auf Felix' Antwort zu Frage 553)."
---

## Kontext
Die Stadt erneuert seit dem 24.08.2026 den Belag auf Fahrbahn und Gehwegen der Brücke Saarner Straße, in zwei Bauabschnitten; der Verkehr wird an der Baustelle vorbeigeführt. Die Brücke von 1963 (Spannbeton) überspannt Gleise der Deutschen Bahn. Die Meldung beruft sich auf das Amt für Verkehrswesen und Tiefbau. Gesagt: 21.08.2026 (Meldung „Brücke Saarner Straße: Neuer Belag für Fahrbahn und Gehwege“); wer: Stadt Mülheim an der Ruhr, Mitteilungstext.

## Übersetzung
Vorbehalt: „voraussichtlich“ → `voraussichtlich`, 0,80. Der Satz nennt eine Dauer, kein Datum: neun Wochen ab Montag, 24.08.2026 enden am Sonntag, 25.10.2026; das ist der Stichtag. Ja, wenn bis zum Stichtag beide Bauabschnitte fertig sind und die Verkehrsführung an der Baustelle aufgehoben ist; Restarbeiten ohne Einschränkung des Verkehrs schaden nicht. Beleg später: Meldung der Stadt, Lokalpresse (WAZ Mülheim), Baustellenmeldungen der Stadt. `pruefung_am` ist der Folgetag.

## Begründung Computer
Referenzklasse Tiefbau mit Termin in wenigen Wochen bis Monaten (0,45–0,60). In der Mitte: Die Arbeit ist überschaubar (Belag auf Fahrbahn und Gehwegen), die Dauer hat die Stadt selbst erst zum Baubeginn genannt. Dagegen: Abdichtung und Belag auf Brücken hängen an trockenem Wetter, der zweite Abschnitt fällt in den Oktober, und eine Woche Verzug reicht für ein Nein. Wie weit die Baustelle am 05.10.2026 ist, ist nicht geprüft. Rund 0,50. Hinterlegt am 05.10.2026, vor `pruefung_am`.
