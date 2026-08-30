# festgehalten — Nächste Schritte

**Stand:** 30.08.2026 (Verfassung §8 beschlossen und in FORMAT.md; Format heißt jetzt festgehalten-Format v1)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte)
**Phase:** v1 live, Verfassung beschlossen, nicht committet

## Wo wir stehen

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten, Pages via GitHub Actions (Workflow grün, Stand 28.08. 23:45).
- Code: `python -m wettbuch bauen <buch> <ausgabe>` und `python -m wettbuch alle buecher site`. 66 Tests grün (gemessen 29.08. ~00:30). Stack: Python, pyyaml, markdown.
- Bücher: Köln 79 Wetten (davon 3 per `ersetzt_durch` ersetzt), Essen 39, Bonn 36, Düsseldorf 35, Dortmund 20 = 209. 28 mit Beleg aufgelöst (zwei Agentenläufe, Protokoll in `recherche/AUFLOESUNG-2026-08-28.md`), 38 vergangene ohne Quelle offen, 41 lösen sich bis 31.12.2026.
- Erstes Ergebnis: Stadt Köln Brier-Schnitt 0,58 über aufgelöste Ja/Nein-Ankündigungen — noch kein Rang (9 von 10).
- Computer-Prognosen: nur für Wetten mit Prüfdatum nach 28.08.2026 (Basisraten, keine Einzelrecherche; steht in jeder Begründung). Retro-datierte Köln 001/002/004 durch 077–079 ersetzt.
- Entschieden 28.08.: Format statt Plattform; Markdown+YAML pro Wette; Beleg-Pflicht; Teilerfüllung = Nein; Rang ab 10; Gleichstand bei Punkt = niemand gewinnt; Textteil wird escaped; Name „festgehalten", Format hieß bis 29.08. „Wettbuch-Format v1", seit 30.08. „festgehalten-Format v1".
- Privates Wettbuch (Felix gegen Computer) liegt NICHT hier, sondern in ~/kybernokratie/WETTBUCH.md; aus der Historie dieses Repos per filter-repo entfernt (Backup ~/wettbuch-vor-filter.bundle).

## Nächster konkreter Schritt

FORMAT.md (§8 + Umbenennung + optionales Feld `herkunft`) gegenlesen und committen/pushen — ab dann ist die Verfassung öffentlich. Danach README/Übersicht auf „festgehalten-Format" umstellen und `herkunft` im Generator anzeigen (lesen, nicht rechnen).

## Wartet auf Felix

- Nachfolger als Hüter hinterlegen (§8.1, Frist 31.12.2026).
- Rechtsform konkret: gemeinnütziger Träger (Verein/gGmbH) für festgehalten, Firma für Doorway (§8.4) — Beratung/Notar.
- Zwei Mails freigeben (Ratsfraktion Köln, KStA) — Entwürfe folgen nach dem Review.
- Die 38 offenen vergangenen Wetten: selbst auflösen, dritten Lauf oder bis `verfall_am` liegen lassen.

## Blocker

Keiner. Das Repo ist öffentlich; jede Änderung an FORMAT.md ist ab jetzt eine Änderung an einem veröffentlichten Format.
