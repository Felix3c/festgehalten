# Auflösung vorbereitet: wuppertal-2026-001 (09.10.) und wuppertal-2026-002 (11.10.)

Stand 04.10.2026 11:20, Dauerlauf (Claude). Die Wetten liegen nur auf dem lokalen Zweig `buch-wuppertal`
(nicht gemergt, nicht öffentlich). Nichts committet, Wettdateien unverändert.

## Vorab: Zeitfenster für die Veröffentlichung (Frage 85)

Beide Wetten sind jetzt noch ehrlich, weil die Prognose des Computers am 04.10. hinterlegt wurde, also vor dem Ereignis.
Das beweist aber nur der lokale Commit `8250c39`. Öffentlich wird es erst mit dem Push.
- Wird `buch-wuppertal` **bis Mi 07.10.** gepusht, gehen beide Wetten offen live. Richtig.
- Wird erst **nach dem 08.10.** gepusht, erscheint wuppertal-2026-001 mit Ereignis und Prognose gleichzeitig.
  Für Leser ist dann nicht prüfbar, dass die 0,92 vorher feststand. Gleiches gilt für -002 nach dem 10.10.
  Empfehlung für diesen Fall: Beide Wetten vor dem Merge aus dem Zweig nehmen (verworfen mit Grund
  „Ereignis vor Veröffentlichung“), dann bleiben 13 Wetten. Erste Prüfung danach: 003/004 am 01.11.

## wuppertal-2026-001 — Spielplatz Werther Hof, Eröffnung 08.10.2026

- Stand 04.10.: Die Mitteilung vom 01.10. steht unverändert in der Liste „Aktuelle Meldungen“
  (https://www.wuppertal.de/presse/aktuelle-meldungen.php, abgerufen 04.10.2026 11:10): „Am Donnerstag, 8. Oktober, wird er
  offiziell eröffnet. Große und kleine Kinder können den Märchenwald von 15.30 bis 17.30 Uhr erobern.“ Keine Absage, keine
  Verschiebung gefunden.
- **Am 09.10. prüfen:** Liste „Aktuelle Meldungen“ und Oktober-Archiv
  (`/rathaus-buergerservice/verwaltung/pressebereich/archiv_monate_jahr/oktober-2026.php`) auf eine Nachmeldung,
  dazu Websuche „Werther Hof Spielplatz eröffnet“ (WZ, Wuppertaler Rundschau, Radio Wuppertal, Social Media der Stadt).
- **Regel (aus der Wette):** JA, wenn die Eröffnung am 08.10. öffentlich belegt ist. Eine bloße Ankündigung reicht nicht.
  Kein Beleg bis ~15.10. → Frage an Felix (Vorschlag: NEIN mangels Beleg, Vermerk).
- Abruf: wuppertal.de antwortet ohne `Sec-Fetch-*`-Kopfzeilen mit 403 (Methode wie im KANDIDATEN-Dokument). Das Archiv
  nimmt die Stadt nicht → Beleg wie beim Anlegen als lokale Kopie + SHA-256 nach `recherche/belege/`.

## wuppertal-2026-002 — Brunnen Alte Freiheit, fertig bis 10.10.2026

- Stand 04.10.: Keine Mitteilung seit dem 07.08. Die Quelle ist unverändert, der Satz „Die Fertigstellung des Brunnens ist
  Anfang Oktober geplant.“ steht dort weiter (abgerufen 04.10.2026 11:15).
  Die Projektseite „Unser Elberfeld“ (https://www.wuppertal.de/microsite/unser-elberfeld/projekte/laufende-projekte/alte-freiheit-poststrasse-und-kerstenplatz/alte-freiheit-poststrasse-und-kerstenplatz.php,
  04.10.) nennt nur „soll außerdem ein großer Brunnen platziert werden“, ohne Termin. In der Presse gibt es nichts Neueres
  als den 12.08. (WZ-Kolumne Uwe Becker: „Ab Oktober wird es sogar wieder einen Brunnen an der Alten Freiheit geben.“).
  Radio Wuppertal (Artikel 2724746) wiederholt „Anfang Oktober“.
- Richtung: Es ist ungeklärt, ob der Bau im Plan liegt. Die Stadt hat nichts gemeldet, auch keine Ankündigung einer Inbetriebnahme.
  Die Prognose 0,35 bleibt plausibel.
- **Am 11.10. prüfen:** Liste „Aktuelle Meldungen“ + Oktober-Archiv, Websuche „Brunnen Alte Freiheit“ (WZ, Rundschau,
  Radio Wuppertal, ISG Poststraße https://www.isg-poststrasse.de/meldungen.php).
- **Regel (aus der Wette):** JA nur mit öffentlichem Beleg „in Betrieb“ oder „fertig“ bis einschließlich 10.10.
  Ohne Beleg bis zum Prüftag gilt NEIN (so steht es in der Übersetzung der Wette).
  Eine Meldung, die nur die Fertigstellung ankündigt („geht nächste Woche in Betrieb“), reicht nicht.

## Wenn Felix nicht mergt

Dann gibt es nichts aufzulösen. Die Datei dient nur noch als Begründung, wenn 001/002 verworfen werden (siehe oben).

## Nachtrag 08.10.2026 05:30 (Dauerlauf, Vorprüfung am Ereignistag)

- wuppertal-2026-001: Detailseite der Mitteilung vom 01.10. heute abgerufen, Text wortgleich zur lokalen Kopie vom 04.10.
  („Am Donnerstag, 8. Oktober, wird er offiziell eröffnet. … von 15.30 bis 17.30 Uhr“); die Datei-Prüfsumme weicht ab
  (neu 81ad3485…, alt b3560e1c…), nur Rahmen der Seite. Liste „Aktuelle Meldungen“ (neueste Meldung 07.10.) und
  Oktober-Archiv: elf Oktober-Meldungen, keine Absage, keine Verschiebung, keine Nachmeldung. Save Page Now erneut
  HTTP 520 (dritter Versuch). Richtung unverändert: Termin steht; aufgelöst wird erst am 09.10. mit Beleg der
  Eröffnung (Ankündigung reicht nicht).
- wuppertal-2026-002: in Liste und Oktober-Archiv kein Treffer für „Brunnen“ oder „Alte Freiheit“. Prüftag 11.10.

## Nachtrag 08.10.2026 16:35 (Dauerlauf, Ereignistag nachmittags)

- wuppertal-2026-001: Liste „Aktuelle Meldungen“ um 16:29 abgerufen (HTTP 200, SHA-256 5207cdfb…): oben steht weiter nur
  die Ankündigung „Kinderspielplatz Werther Hof: Märchenwald für die Barmer City“, keine Nachmeldung, keine Absage.
  Websuche „Spielplatz Werther Hof Wuppertal eröffnet Märchenwald“ (16:30): Wuppertaler Rundschau
  (`wuppertaler-rundschau.de/…/ein-maerchenwald-mitten-in-der-barmer-city_aid-155818477`) und talzeit.de
  (`article413340867`) geben nur die Ankündigung wieder; ein Bericht über die stattgefundene Eröffnung ist noch nicht zu
  finden (Eröffnung lief 15:30–17:30). Am 09.10. dieselben drei Stellen plus WZ und Social Media der Stadt; ohne Bericht
  bleibt es bei der Regel oben (bis ~15.10. warten, dann Frage an Felix).

## Nachtrag 08.10.2026 16:48 (Dauerlauf, nach Ende des Eröffnungsfensters 15:30–17:30 noch nicht prüfbar)

- Liste „Aktuelle Meldungen“ um 16:48 erneut abgerufen (HTTP 200, SHA-256 10211fb0…): weiter nur die Ankündigung
  „Kinderspielplatz Werther Hof: Märchenwald für die Barmer City“, kein Treffer für „Brunnen“ oder „Alte Freiheit“.
  ISG Poststraße (meldungen.php): kein Treffer für „Brunnen“. Nächster Blick Fr 09.10. (001) und So 11.10. (002).

## Prüftag Fr 09.10.2026 00:20 (Dauerlauf, Tagesprüfung), wuppertal-2026-001

- Liste „Aktuelle Meldungen“ (HTTP 200) und Oktober-Archiv (HTTP 200): oben steht weiter nur die Ankündigung vom 01.10.,
  keine Nachmeldung zur Eröffnung, keine Absage.
- Presse: talzeit (Artikel 413340867, `datePublished` 08.10. 03:00 UTC, `dateModified` 07.10. 11:48) schreibt „Seit heute
  (8. Oktober) können Kinder anfangen, zu spielen“. Der Text ist vor dem Termin geschrieben, also eine Ankündigung, kein
  Bericht über die Eröffnung (SHA-256 a096cde7…e634). Wuppertaler Rundschau 02.10.: nur Ankündigung. Projektseite der
  Stadt („Im Bau / KSP Werther Hof“): „Die Eröffnung findet am 8.10.2026 von 15:30 bis 17:30 h statt“, ebenfalls Ankündigung.
- **Nicht aufgelöst.** Nach der Regel oben reicht eine Ankündigung nicht. Weiter prüfen bis ~15.10.; danach Frage an Felix
  (Vorschlag NEIN mangels Beleg, mit Vermerk).

## Vorprüfung Fr 09.10.2026 12:25 (Dauerlauf, Guard Laufend), wuppertal-2026-002

- Quelle (`…/august/brunnen-elberfeld.php`, HTTP 200, SHA-256 ced3be0f…3ed34): Satz „Die Fertigstellung des Brunnens ist
  Anfang Oktober geplant.“ steht unverändert, Seitenfeld `changed` weiter 2026-08-07.
- Liste „Aktuelle Meldungen“ und Oktober-Archiv (beide HTTP 200): 14 Oktober-Meldungen, keine zu „Brunnen“ oder
  „Alte Freiheit“. ISG Poststraße (meldungen.php): heute keine Verbindung (Zeitüberschreitung), ungeklärt.
- Websuche (zwei Suchen, 12:20): nichts nach August; neueste Treffer WZ/Rundschau/Radio Wuppertal/wuppertal-total vom
  August mit „Anfang Oktober“. Rahmenterminplan Elberfeld (Stand 18.04.2026) unter der alten Adresse HTTP 404.
- Richtung: kein Hinweis auf Fertigstellung, aber auch keine Verschiebung gemeldet. Am So 11.10. dieselben Stellen; ohne
  öffentlichen Beleg „fertig/in Betrieb“ bis 10.10. gilt NEIN (Regel oben).
