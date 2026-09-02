# festgehalten — Nächste Schritte

**Stand:** 02.09.2026 (4. Auflösungslauf: 4 aufgelöst, 57 gesamt, 25 fällig offen; IFG-Entwürfe für 11 Wetten; Rechtsform-Vorlage in ~/kybernokratie/RECHTSFORM.md; Köln Brier 0,59; noch nicht committet)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte)
**Phase:** v1 live, Verfassung committet (9be7842), 4. Lauf lokal

## Wo wir stehen

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten, Pages via GitHub Actions (Workflow grün, Stand 28.08. 23:45).
- Code: `python -m wettbuch bauen <buch> <ausgabe>` und `python -m wettbuch alle buecher site`. 66 Tests grün (gemessen 29.08. ~00:30). Stack: Python, pyyaml, markdown.
- Bücher: Köln 79 Wetten (davon 3 per `ersetzt_durch` ersetzt), Essen 39, Bonn 36, Düsseldorf 35, Dortmund 20 = 209. 57 aufgelöst (vier Läufe, Protokolle in `recherche/AUFLOESUNG-2026-08-28.md`, `-08-30.md`, `-09-02.md`). 25 fällig und offen: 9 Jahresabschlüsse 2025 (warten auf Feststellung), 3 Ereignis steht aus, 2 Kosten (Wiedervorlage 2027), 11 Zahl liegt bei der Stadt → IFG-Entwürfe in `recherche/IFG-2026-09.md`. Verfallsregel seit 02.09. in jeder BUCH.md: zwei Jahre nach Prüfdatum (Format-Standard), Jahresabschluss-Wetten drei Jahre, bei diesen 27 steht `verfall_am` explizit.
- Erstes Ergebnis: Stadt Köln Brier-Schnitt 0,59 über aufgelöste Ja/Nein-Ankündigungen (koeln-2025-051 Rondorf mit 0,80 angekündigt, wurde Nein).
- Computer-Prognosen: nur für Wetten mit Prüfdatum nach 28.08.2026 (Basisraten, keine Einzelrecherche; steht in jeder Begründung). Retro-datierte Köln 001/002/004 durch 077–079 ersetzt.
- Entschieden 28.08.: Format statt Plattform; Markdown+YAML pro Wette; Beleg-Pflicht; Teilerfüllung = Nein; Rang ab 10; Gleichstand bei Punkt = niemand gewinnt; Textteil wird escaped; Name „festgehalten", Format hieß bis 29.08. „Wettbuch-Format v1", seit 30.08. „festgehalten-Format v1".
- Privates Wettbuch (Felix gegen Computer) liegt NICHT hier, sondern in ~/kybernokratie/WETTBUCH.md; aus der Historie dieses Repos per filter-repo entfernt (Backup ~/wettbuch-vor-filter.bundle).

## Nächster konkreter Schritt

Committen und pushen (6 Wetten, 2 Protokolle). Dann Anleitung „Ein Buch in einer Stunde" (Kachel 2.2). Generator: `herkunft` anzeigen. Danach README/Übersicht auf „festgehalten-Format" umstellen und `herkunft` im Generator anzeigen (lesen, nicht rechnen).

## Wartet auf Felix

- Nachfolger als Hüter hinterlegen (§8.1, Frist 31.12.2026) — Felix 02.09.: „hab noch niemanden", wartet.
- Rechtsform entschieden 02.09.: gUG **nicht jetzt** (kein Geld), Gründung bei erster Förderzusage. Zwecke 1+7+24 ja, Beirat ja, Vermögensbindung offen (Felix will Erklärung), kein Steuerberater. Weg ohne Geld in ~/kybernokratie/RECHTSFORM.md Abschnitt 10: Satzungsentwurf (Claude), kostenlose Finanzamt-Vorprüfung, Anwaltsstunde nach 11.09.
- Zwei Mails freigeben (Ratsfraktion Köln, KStA) — Entwürfe folgen nach dem Review.
- Sieben IFG-Anfragen aus `recherche/IFG-2026-09.md` über FragDenStaat absenden (unter eigenem Namen).
- duesseldorf-2025-026 (Luisen-Gymnasium, Ja) nach dem ersten Schultag 02.09. gegenprüfen: gibt es einen Nachbericht, dass Unterricht im Neubau läuft?

## Blocker

Keiner. Das Repo ist öffentlich; jede Änderung an FORMAT.md ist ab jetzt eine Änderung an einem veröffentlichten Format.
