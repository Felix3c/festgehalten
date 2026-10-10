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
