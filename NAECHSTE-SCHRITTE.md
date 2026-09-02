# festgehalten — Nächste Schritte

**Stand:** 02.09.2026 abends (4. Auflösungslauf, IFG-Entwürfe, Verfallsregel, Rechtsform entschieden; parallel aus anderem Tab: Paket 0.2.0 mit Befehl `festgehalten`, ANLEITUNG.md, METHODE.md; alles committet und gepusht bis 44c25e6)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte)
**Phase:** v1 live, Verfassung veröffentlicht, Bücher in laufender Auflösung

## Wo wir stehen

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten, Pages via GitHub Actions. Arbeitsbaum sauber, nichts ungepusht (geprüft 02.09. abends).
- Code: Paket `festgehalten` 0.2.0, Befehle `festgehalten neu <ordner>`, `festgehalten bauen <buch> <ausgabe>`, `festgehalten alle <buecher> <ausgabe>` (a4cd0ba, anderer Tab). 69 Tests grün (gemessen 02.09. abends). Stack: Python, pyyaml, markdown.
- Dokumente im Repo: FORMAT.md (Format + Verfassung §8), METHODE.md (wie die Computer-Basisraten entstehen, 889e3b6), ANLEITUNG.md („Ein Buch in einer Stunde", a4cd0ba/8d0de85), README auf „festgehalten-Format" umgestellt.
- Bücher: Köln 79 Wetten (3 per `ersetzt_durch` ersetzt), Essen 39, Bonn 36, Düsseldorf 35, Dortmund 20 = 209. 57 aufgelöst (vier Läufe, Protokolle in `recherche/AUFLOESUNG-2026-08-28.md`, `-08-30.md`, `-09-02.md`).
- 25 fällig und offen: 9 Jahresabschlüsse 2025 (Feststellung durch den Rat abwarten; Köln hat nicht mal einen Entwurf), 3 Ereignis steht aus (bonn-028, duesseldorf-021, koeln-042), 2 Kosten mit Wiedervorlage 2027 (duesseldorf-027, koeln-052), 11 Zahl liegt bei der Stadt → IFG-Entwürfe in `recherche/IFG-2026-09.md` (sieben Anfragen).
- Verfallsregel (Halter-Regel 02.09., in jeder BUCH.md): zwei Jahre nach Prüfdatum (Format-Standard §1.1), Jahresabschluss-Wetten drei Jahre; bei diesen 27 steht `verfall_am` explizit (44c25e6).
- Ergebnis Köln: Brier-Schnitt 0,59 über aufgelöste Ja/Nein-Ankündigungen (koeln-2025-051 Rondorf: mit 0,80 angekündigt, Nein).
- Auflösungen mit Vorbehalt (laden nach §2.4 zum Streit ein): duesseldorf-026 Luisen-Gymnasium (Ja; Stichtag lag einen Tag vor Ferienende, erster Schultag 02.09.), duesseldorf-019 Baumbilanz (städtische Vorlage als PDF-Kopie beim BUND), essen-027 Citybahn (Radio Essen mit Ruhrbahn-Zitat).
- Computer-Prognosen: nur für Wetten mit Prüfdatum nach 28.08.2026 (Basisraten, Methode in METHODE.md).
- Rechtsform (entschieden 02.09., Vorlage ~/kybernokratie/RECHTSFORM.md): gUG **nicht jetzt**, kein Geld; Gründung bei erster Förderzusage. Zwecke §52 Nr. 1+7+24 ja, Beirat mit leeren Sitzen ja, kein Steuerberater bis Geld da ist. Bis dahin: Satzungsentwurf, kostenlose Finanzamt-Vorprüfung, Anwaltsstunde nach dem 11.09. (Tab 3).
- Privates Wettbuch (Felix gegen Computer) liegt NICHT hier, sondern in ~/kybernokratie/WETTBUCH.md.

## Nächster konkreter Schritt

Generator: Feld `herkunft` (`zitiert` | `hinterlegt`) auf der Wetten-Seite und in der Buch-Tabelle anzeigen — lesen, nicht rechnen (in `generator/wettbuch/seiten.py` kommt `herkunft` bisher nicht vor). Test dazu in `generator/tests/`. Danach bauen, Tests, commit.

## Wartet auf Felix

- Sieben IFG-Anfragen aus `recherche/IFG-2026-09.md` bei FragDenStaat absenden (unter eigenem Namen). Antworten kommen binnen eines Monats; Antwort-URL wird `beleg_ausgang`.
- Vermögensbindung in der Satzung (wohin das Vermögen bei Auflösung geht; Vorschlag OKF Deutschland). Erklärt am 02.09., Entscheidung beim Satzungsentwurf. Nächste Häkchen-Runde: Satzungsentwurf Absatz für Absatz (Kybernokratie-Tab, nicht dieses Repo).
- Nachfolger als Hüter (§8.1, Frist 31.12.2026). Felix 02.09.: „hab noch niemanden", wartet.
- Zwei Mails freigeben (Ratsfraktion Köln, KStA). Entwürfe stehen noch aus.
- Luisen-Gymnasium (duesseldorf-2025-026, Ja) um den 09.09. gegenprüfen: Nachbericht über Unterricht im Neubau? Wenn nein, Vermerk ergänzen.

## Blocker

Keiner. Das Repo ist öffentlich; jede Änderung an FORMAT.md ist eine Änderung an einem veröffentlichten Format und läuft nach §8.3.
