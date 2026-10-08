# Auflösung vorbereitet, Nachtrag: Prüftage 01.11. bis 09.11.2026 (Bücher, die seit dem Morgen auf master sind)

Stand 08.10.2026 20:10, Dauerlauf (Claude). Die Vorlage `2026-10-08-aufloesung-0111-0811-VORBEREITET.md` (08:30)
hat aachen-001, gelsenkirchen-001/-002, krefeld-001 und muenster-002 bis -004 ausgelassen, weil sie damals nur auf
Zweigen lagen. Inzwischen sind alle acht auf origin/master (öffentlich). muenster-2026-005 (Prüftag 09.11.) war in
keiner Vorlage. Wettdateien unverändert, nichts aufgelöst.

Alle Quellen am 08.10.2026 um 20:06 abgerufen (curl, Browser-Kopfzeilen), jedes `zitat` wörtlich gefunden.
Prüfsummen (SHA-256, erste 16 Zeichen) nur zum Wiedererkennen, keine Kopie im Repo. Die vier Münster-Quellen sind
byte-gleich mit den hinterlegten lokalen Kopien (gleiche Prüfsumme wie im Vermerk).

Münster-Presseportal (Schnittstelle `api/items`, Seiten 1–6, 120 Meldungen vom 03.09. bis 08.10.2026) nach
Ratsgymnasium, Freiherr-vom-Stein, Margaretenschule, Wolbeck, Roxel, Herbstferien durchsucht: keine neue Meldung zu
den drei Schulen; zu Wolbeck nur die Quelle selbst (16.09.) und Fremdthemen (Feuerwehrhaus, Bäume am Schulzentrum).
Herbstferien NRW 2026 sind in den Wetten als „erste Schulwoche danach = bis 06.11.“ übersetzt; der Ferientermin
wurde hier nicht neu geprüft.

## 01.11. aachen-2026-001 — Weg Brander Wall / Schagenstraße wieder frei bis 31.10.

- Quelle (aachen.de, 17.07.) unverändert (`3cb6054f280b4be1`). Websuche 08.10.: nur Planungsunterlagen von 2025
  (Bezirksvertretung Brand, Fertigstellung damals „Frühjahr 2026“), nichts Neueres zur Fertigstellung oder Sperrung.
- **Am 01.11. prüfen:** aachen.de-Pressemitteilungen Oktober/November, Aachener Zeitung (Lokalteil Brand),
  Seite der Stadt zu Spiel- und Bolzplätzen.
- **Regel:** JA nur mit öffentlichem Beleg, dass der Weg bis 31.10. freigegeben ist. Ohne Beleg: NEIN.

## 01.11. gelsenkirchen-2026-001 — Vollsperrung Liboriusstraße aufgehoben bis 31.10.

- Quelle (gelsenkirchen.de, 25.09.) unverändert (`0dd8956c698d3010`).
- Baustellenkarte der Stadt, Eintrag `poi/164037-liboriusstrasse-zwischen-dresdener-strasse-und-bismarckstrasse-vollsperrung`
  (`df8fee029cd07429`): „22.09.2026 bis voraussichtlich 30.10.2026“. Termin hält damit nach Angabe der Stadt.
- **Am 01.11. prüfen:** derselbe Eintrag (verschwunden oder Datum geändert?), Pressemeldungen der Stadt, WAZ
  Gelsenkirchen. Ein verschwundener Karteneintrag allein ist kein Beleg; mit Archivkopie vorher/nachher als Indiz
  vermerken und nach einer Meldung suchen.
- **Regel:** JA, wenn die Aufhebung bis 31.10. öffentlich belegt ist. Ohne Beleg: NEIN.

## 01.11. gelsenkirchen-2026-002 — Gasleitung Kurt-Schumacher-Straße fertig bis 31.10.

- Quelle (gelsenkirchen.de, 20.07.) unverändert (`ba490e077655dc30`).
- Baustellenkarte `poi/164026-…` (`85a461d852f390cb`): weiter „bis voraussichtlich 30.11.2026“ (wie im Vermerk vom
  08.10.). **Richtung NEIN.**
- **Am 01.11. prüfen:** derselbe Eintrag; nennt er dann noch 30.11. und gibt es keine Fertigmeldung: NEIN,
  Beleg = Karteneintrag mit Archivkopie.

## 01.11. krefeld-2026-001 — Vereinstreffpunkt am CRC-Gebäude nutzbar bis 31.10.

- Quelle (krefeld.de, 18.09.) unverändert (`b90a6d7fc0a0d842`). Websuche 08.10.: nur die Ratsvorlage vom
  Dezember 2024 (Masterplan, drei Bewegungsflächen), nichts Neueres.
- **Am 01.11. prüfen:** krefeld.de-Pressemeldungen (die Stadt hat die ersten beiden Parks eigens gemeldet),
  Kommunalbetrieb Krefeld, Rheinische Post / WZ Krefeld.
- **Regel:** JA mit öffentlichem Beleg der Freigabe bis 31.10. Ohne Beleg: NEIN.

## 07.11. muenster-2026-002 — Ratsgymnasium im Erweiterungsbau bis 06.11.

- Quelle (`api/item/1219431`) byte-gleich (`88db73e698d6abb2`). Websuche: Stadtseiten und ms-aktuell wiederholen
  „nach den Herbstferien“, kein neuer Termin, keine Verschiebung.
- **Am 07.11. prüfen:** Presseportal Münster (`api/items`), Internetseite der Schule, Westfälische Nachrichten.
- **Regel:** JA, wenn Unterricht im Neubau bis 06.11. öffentlich belegt ist. Ohne Beleg: NEIN.

## 07.11. muenster-2026-003 — Freiherr-vom-Stein-Gymnasium im Erweiterungsbau bis 06.11.

- Quelle (`api/item/1211114`) byte-gleich (`27ddd9ad03e25652`). Keine neuere Meldung im Portal (03.09.–08.10.).
- **Am 07.11. prüfen und Regel:** wie 002.

## 07.11. muenster-2026-004 — Margaretenschule an den Brentanoweg umgezogen bis 06.11.

- Quelle (`api/item/1211274`) byte-gleich (`4cd7ddffd42b29e0`). Websuche: nur Richtfest-Meldung („Herbstferien“)
  und ältere Meldungen; kein neuer Termin.
- **Am 07.11. prüfen und Regel:** wie 002, dazu die Schulseite.

## 09.11. muenster-2026-005 — Hallenbad Wolbeck am 07. oder 08.11. öffentlich geöffnet

- Quelle (`api/item/1227091`) byte-gleich (`c4e00c7864564feb`). Die Meldung „Hallenbad Wolbeck diese Woche
  für Schul- und Vereinssport geschlossen“ stammt aus dem Januar 2026 (bis 18.01.) und ist in der Quelle schon
  berücksichtigt; nichts Neueres.
- **Am 09.11. prüfen:** Bäderseite der Stadt, Presseportal, Westfälische Nachrichten. Ende Oktober lohnt ein Blick
  ins Portal (eine Absage käme vorher).
- **Regel:** JA, wenn belegt ist, dass am 07. oder 08.11. öffentlich geschwommen werden konnte (Nachbericht, oder
  Bäderseite am Wochenende mit Öffnung). Nur die alte Ankündigung ohne Bestätigung: Frage an Felix.
