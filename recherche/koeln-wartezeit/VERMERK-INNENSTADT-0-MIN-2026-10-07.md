# Vermerk: Innenstadt 0 Min. am Mi 07.10.2026 — „keine Wartenden“ oder „kein Wert“?

Geprüft 08.10.2026 01:25 (Dauerlauf). Anlass: `NAECHSTE-SCHRITTE.md` „Ungeklärt“; Monatsmittel und
Kill-Check 15.10. hängen daran.

## Was die Rohkopien zeigen

`belege-anzeige/wartezeiten-20261007-074307-9a1abd67.json` (Stand 07:40) und
`belege-anzeige/wartezeiten-20261007-100011-4abeafb3.json` (Stand 10:00), beide `status: 1`,
`sondertext` leer:

- Kundenzentrum Innenstadt steht unter „Unter 30 Minuten“ mit `"wartezeit": 0`, beide Male an erster Stelle.
- Alle anderen acht Zentren haben echte Werte (07:40: 6–39 Min., 10:00: 2–83 Min.).
- Führerscheinstelle Innenstadt ebenfalls 0 (Rodenkirchen auch, schon am 05.10.).
- Am Mo 05.10. 14:00 hatte Innenstadt 68 Min. (`wartezeiten-20261005-140009-43fc412b.json`).

Die Datei hat kein Feld, das „geschlossen“ oder „kein Wert“ von „niemand wartet“ trennt. Eine 0 ist in
der Datei eine Zahl wie jede andere. Aus den Rohkopien allein ist die Frage also **nicht entscheidbar**.

## Was die Stadt selbst dazu sagt (Abruf 08.10.2026 ~01:20)

Seite Kundenzentrum Innenstadt, `https://www.stadt-koeln.de/service/adressen/00183/index.html`,
Kopie `belege-hinweise/kundenzentrum-innenstadt-00183-20261008-0125.html`
(SHA-256 `27be6065ce43b245ffe36f6567f357d7c85b8ba4d2cdb81cc7344b590c02a154`),
Wayback `https://web.archive.org/web/20261007231945/https://www.stadt-koeln.de/service/adressen/00183/index.html`:

- „Die Kasse im Kundenzentrum Innenstadt ist vom 7. Oktober bis 8. Oktober 2026 geschlossen. Sie können in
  dieser Zeit weiterhin bargeldlos zahlen.“ — nur Innenstadt hat diesen Hinweis.
- „Die Ausgabe der Aufrufmarken für das Führerscheinwesen wird am 7. Oktober 2026 eingestellt.“ — steht bei
  allen Zentren (gleich bei Kalk: `belege-hinweise/kundenzentrum-kalk-00181-20261008-0125.html`,
  SHA-256 `1f18492a77258e02640fa09670b6467a461ef4e47461f23b788c1af453723ddd`). Erklärt die Nullen der
  Führerscheinstellen, betrifft aber nicht den gezählten Bereich `meldeangelegenheiten`.
- Öffnungszeiten Innenstadt I: Mittwoch 7:30 bis 12 Uhr ohne Terminvereinbarung. Das Zentrum war zu beiden
  Messzeiten also regulär für Laufkundschaft offen.
- **Neu und wichtiger:** „Aufgrund einer Personalversammlung bleiben die Kundenzentren am Montag, den
  12. Oktober 2026 geschlossen.“ (bei allen Zentren). Mo 12.10. ist ein Messtag (10:00 und 14:00).

## Einordnung

- Belegt: Am 07.10. lief in der Innenstadt etwas nicht regulär (Kasse zu, Führerschein-Marken eingestellt).
- Nicht belegt: dass die Anzeige deshalb 0 meldet. Möglich ist auch, dass um 07:40 und 10:00 wirklich
  niemand ohne Termin wartete. Das Muster spricht eher für „kein echter Wert“ (das sonst vollste Zentrum
  zweimal genau 0, während Ehrenfeld 83 Min. zeigt), ist aber kein Beweis.
- Frühere Nullen der Innenstadt im alten Feed (08.09. Stand 12:15, 10.09. Stand 13:35) fielen auf
  Dienstag/Donnerstag, also Tage nur mit Termin. Das passt zu „0 = keine Laufkundschaft-Schlange“.
- Bleibt **ungeklärt**. Klären könnte es nur die Stadt (Fachfrage an die Kundenzentren) oder ein
  Augenschein vor Ort.

## Wirkung auf die Zahl

`python auswerten.py --quelle anzeige --monat 2026-10` (08.10. 01:25): 2 Messtage, 18 gezählte Werte,
Gesamtmittel **18,1 Min.** mit der Innenstadt-0 vom 07.10. (gezählt wird nur der Abruf 07:43, 10:00 liegt
im selben Slot). Ohne diesen Wert: 325,8 / 17 = **19,2 Min.** Beide unter dem Planwert 20,0; die 0 kippt
die Aussage heute nicht, verschiebt das Mittel aber um gut 1 Minute.

## Offen (Entscheidung Felix, Frage 184 in ALLEIN.md)

Wie mit Nullen an Tagen umgehen, an denen die Stadt selbst eine Störung oder Schließung meldet — vor allem
Mo 12.10. (alle Zentren zu). `messen.py` prüft weder `status` noch Schließtage; meldet die Datei am 12.10.
einen Stand von heute mit Nullen, landen neun Nullen im Mittel. Nichts am Code geändert.
