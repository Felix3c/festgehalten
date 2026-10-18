# Buch „NRW gegen NRW“ — Nachtrag, recherchiert am 10.10.2026

Status: fünf neue Wetten (nrw-2026-012 bis -016) lokal auf Zweig `buch-nrw-2`, **nicht gepusht**
(Push erst nach „steht“). Recherche: Unteragent des Dauerlaufs (120 Mitteilungen auf land.nrw/pressemitteilungen,
03.09.–09.10.2026); Wortlautprüfung und Anlage: Claude, 10.10.2026. Regeln wie am 03.10.: nur eigene Aussagen der
Landesregierung, Zahl und Datum. Kandidatenliste mit Verworfenem: `~/allein/tmp/nrw2-kandidaten-2026-10-10.md`.

## Prüfweg

Quellen am 10.10.2026 gegen 16:43 per `curl -sL --compressed` mit Browser-User-Agent abgerufen. HTML: script/style
raus, Tags → Leerzeichen, `html.unescape`, Whitespace zusammengefasst; jedes durch „…“ getrennte Stück mit `in`
geprüft. Live: alle fünf **True**. Wayback-Kopie per `web.archive.org/save` angelegt; Kopie (`id_`) geprüft:
013 **True**, 014 **True** (zweiter Abruf). 012, 015, 016: Kopie angelegt, Abgleich zunächst offen, weil die
Wayback Machine die Abrufe danach als Bot-Verkehr sperrte; am 10.10.2026 ~19:35 nachgeholt: alle drei **True**
(Zitat wörtlich in der Kopie, Zeilen in `recherche/archiv-quellen.csv`).

| Wette | Stelle | Quelle (Datum) | Archiv |
|---|---|---|---|
| nrw-2026-012 | Finanzministerium | Altschulden übernommen (10.09.2026) | web.archive.org/web/20261010144410/… |
| nrw-2026-013 | Schulministerium | Schulstart: so viel Personal wie noch nie (03.09.2026) | web.archive.org/web/20261010144428/… |
| nrw-2026-014 | Wirtschafts- + Finanzministerium | NRW.BANK stärkt kommunale Energieversorger (09.10.2026) | web.archive.org/web/20261010144453/… |
| nrw-2026-015 | Wissenschaftsministerium | Plattform für sichere KI-Nutzung (24.09.2026) | web.archive.org/web/20261010144518/… |
| nrw-2026-016 | Familienministerium | Aktionsplan Jugendbeteiligung (08.10.2026) | web.archive.org/web/20261010144546/… |

Schwächen, offen benannt: 012 hängt wie nrw-2026-006 am Haushalt 2027 (darum nur eine weitere Haushaltswette,
Lehrerstellen und OGS-Plätze verworfen). 013 hat die Landtagswahl vor dem Stichtag und die hohe Schwelle „alle
Schulen“. 014 liest „Anfang 2027“ als 31.03. 015 verlangt eine öffentliche Meldung über Hardware (Ausschreibung
reicht nicht). 016: ob der Wahltag amtlich festgesetzt ist, ist ungeklärt; 2017 und 2022 war Mai.

## Verworfen

- 1.323 Lehrerstellen, 547.500 OGS-Plätze: wieder Haushalt 2027, zu eng an 006 und 012.
- Tag der Deutschen Einheit 2027 in Düsseldorf: fast sicher, nur Kontrollwette.
- Laienreanimation 300.000 €/Jahr: Sammeltitel, kaum einzeln belegbar.
- KIRO.NRW Projektstart Ende 2026: Plan des Konsortiums, nicht der Regierung.
- Rest (zu spät, kein Datum, keine eigene Zusage): siehe Kandidatenliste.
