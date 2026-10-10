# Buch „Bund gegen Bund“ — Nachtrag, recherchiert am 10.10.2026

Status: vier neue Wetten (bund-2026-009 bis -012) lokal auf Zweig `buch-bund-2`, **nicht gepusht**
(Push erst nach „steht“). Recherche: Unteragent des Dauerlaufs; Wortlautprüfung und Anlage: Claude, 10.10.2026.
Regeln wie am 03.10.: nur eigene Aussagen der Bundesregierung (Presseamt, Ministerien), Zahl und Datum.

## Prüfweg

Quellen am 10.10.2026 gegen 16:26 per `curl -sL` mit Browser-User-Agent abgerufen. HTML: Tags → Leerzeichen,
`html.unescape`, Whitespace zusammengefasst; PDF: Text mit `pypdf`, Whitespace zusammengefasst; dann `zitat in text`.
Live: alle vier **True**. Wayback-Kopie per `web.archive.org/save` angelegt, die Kopie (`id_`, mit `--compressed`)
abgerufen und dasselbe geprüft: 009, 010, 012 **True**; 011 erst **True**, nachdem die Leerzeichen vor „-“ und „,“
entfernt wurden, die von `<abbr>`-Tags um „Lkw“ und „GmbH“ stammen (Text sonst identisch).

| Wette | Stelle | Quelle (Datum) | Archiv |
|---|---|---|---|
| bund-2026-009 | BMG | PM Finanzentwicklung GKV 1. Hj. 2026 (04.09.2026) | web.archive.org/web/20261010142659/… |
| bund-2026-010 | Presseamt | Beitragsbemessungsgrenzen 2027 (07.10.2026) | web.archive.org/web/20261010142718/… |
| bund-2026-011 | Presseamt | Im Kabinett: Autobahn GmbH (07.10.2026) | web.archive.org/web/20261010142737/… |
| bund-2026-012 | BMDS | Bericht Staatsmodernisierung, PM 61/2026 (07.10.2026) | web.archive.org/web/20261010142802/… |

Schwächen, offen benannt: alle vier tragen einen Vorbehalt („soll“, „sollen“, „Geplant ist“) und stehen deshalb
bei `voraussichtlich` 0,80. 009 ist die früheste Auflösung des Buchs (02.11.2026). 010 ist fast sicher (Formel,
Bundesrat), bewusst als Gegengewicht. 011 „Nein mangels Beleg“, wenn keine Mitteilung über eine Kreditaufnahme
erscheint. 012 hängt an zwei offenen Rechtsänderungen.

## Verworfen

- Superreichensteuer 47 % ab 280.000 € (BMF, 02.09.2026): steht im selben Gesetz wie das Kindergeld (bund-2026-002),
  die beiden Wetten hingen fast vollständig aneinander.
- Deutschlandticket-Preis 2027: keine Bundesquelle mit dem Preis gefunden (Beschluss des Koordinierungsrats).
- Förderzentrale Deutschland „bis Ende 2027 alle Förderportale“: „alle“ nicht eindeutig prüfbar.
- Grundfreibetrag 2027: selbes Gesetz wie bund-2026-002.

## Nachtrag 10.10.2026 abends: bund-2026-013 bis -016 (Prüftag 02.01.2027)

Anlass: Keins der Bücher Bund, NRW, KI und Gatekeeper hatte eine Wette, die noch 2026 aufgelöst wird (außer bund-2026-009).
Gesucht wurden deshalb Ansagen der Bundesregierung mit Frist bis 31.12.2026. Recherche: Unteragent des Dauerlaufs.
Wortlautprüfung und Anlage: Claude, 10.10.2026 gegen 17:55. Gleicher Prüfweg wie oben (curl, Text normalisiert,
`zitat in text`; das PDF über `pdftotext`).

| Wette | Quelle (Datum) | live | Archiv |
|---|---|---|---|
| bund-2026-013 Spritpreisdeckel zum 01.01.2027 | bundesregierung.de, FAQ Spritpreise (01.10.2026) | True | Kopie angelegt web.archive.org/web/20261010155234/…, Abgleich offen (Wayback sperrte den Abruf) |
| bund-2026-014 Haftbefehl → keine Grundsicherung, Bundestag bis 31.12. | bundesregierung.de, RegPK 23.09.2026 | True | web.archive.org/web/20261010155302/… wörtlich True |
| bund-2026-015 Kabinett Arbeitszeitgesetz bis 31.12. | dieselbe RegPK | True | dieselbe Kopie, True |
| bund-2026-016 UVgO im Bundesanzeiger bis 31.12. | bmds.bund.de, Bericht Entlastungskabinett (15.07.2026), Nr. 16 | True | vorhandene Kopie web.archive.org/web/20260901210029/…, Abgleich offen (Wayback sperrte) |

Schwächen, offen benannt: 014 misst nur eine Maßnahme des Aktionsplans (die der Sprecher selbst als Beispiel nennt).
015 übersetzt „vorlegen“ als Kabinettsbeschluss; ein Referentenentwurf soll laut Fachpresse schon existieren
(auf bmas.de ungeklärt). 016 misst die Bekanntmachung, strenger als „finalisiert“.

Verworfen: Energiesteuersenkung bis Ende 2026 (verkündet, Ende ist Normalfall); Gemeinschaftsaufgabe Klimaanpassung
(Entwurf kommt von der Umweltministerkonferenz der Länder); Panzerbrigade Litauen (BMVg korrigierte 02.10. auf Ende 2027);
Einkommensteuerreform 2027 (selbes Gesetz wie 002); Pflegeneuordnungsgesetz (Nähe zu 004/005); Bonpflicht (wirkt 2028);
33 Initiativen „ganz überwiegend“ bis Jahresende (Zählung nicht eindeutig); FPfZG-Darlehen abschaffen „noch in diesem
Jahr“ (kein Entwurf gefunden, Reserve); Schiffssicherheits-Verordnung Dezember 2026 (Reserve, randständig).
