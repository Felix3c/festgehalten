# festgehalten — Nächste Schritte

**Stand:** 08.09.2026 abends (Zweig `weitsicht`: alle acht Einträge des Weitsicht-Buches geschrieben, Bau und Tests grün, nichts committet)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte, Beschluss 08.09. „Partei oder Siegel, nie beides") · ~/weitsicht/STAND.md (Herkunft des neuen Buches)
**Phase:** v1 live; zwei Zweige vor master: `hinterlegt-sammelbuch` (bis cec32e9) und darauf `weitsicht` (uncommittet)

## Wo wir stehen

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten. master unverändert seit 44c25e6.
- Zweig `hinterlegt-sammelbuch` (nicht gemergt): Sammelbuch Hinterlegt, `institution` in Stadtbüchern, PR-Prüfung, Generator zeigt `herkunft` (cec32e9).
- **Zweig `weitsicht` (uncommittet):** `buecher/weitsicht/` mit BUCH.md, `docs/ARBEITSPAPIER.md` und **acht Einträgen** `wetten/weitsicht-2026-001.md` bis `-008.md`, je Forderung einer in Reihenfolge des Papiers. Alle tragen `herkunft: hinterlegt`, `quelle` = GitHub-URL des Arbeitspapier-Auszugs, wörtliches Zitat, Prüfdatum 2027, `verfall_am` = Prüfdatum + 1 Jahr, eine Prognose `von: Weitsicht, art: geschaetzt, wert: 0.50` als Platzhalter plus Vermerk, dass Felix' Zahl und die versiegelte Computer-Zahl ihn vor dem Commit ersetzen. In allen acht gilt dieselbe Richtung: **Ja = Diagnose hält**.
- Gemessen am 08.09.: `bauen buecher/weitsicht --pruefen` → „OK: 8 Wetten, keine Fehler"; `bauen buecher/koeln --pruefen` → „OK: 85 Wetten, keine Fehler"; `pytest generator -q` → 83 grün.
- Die acht Fragen (Kurzfassung, Schwelle und Prüfdatum):
  1. NKR-Jahresbericht 2027 weist Digitalcheck-Quote ≥ 85 % aus — 30.11.2027.
  2. Anteil Altersrentenzugänge 2026 mit Abschlägen ≥ 30,0 % (DRV „RV in Zahlen 2027") — 31.07.2027.
  3. Anteil ohne Ersten Schulabschluss, Abgangsjahr 2025, ≥ 7,8 % (Destatis-Bildungsindikator) — 01.03.2027.
  4. Anteil „sonstige (unbefristete) Lehrkräfte" an Einstellungen 2026 ≥ 13,0 % (KMK) — 31.10.2027.
  5. Kita-Personalschlüssel U3, Länderspanne ≥ 2,5 (Destatis, Stichtag 01.03.2026) — 31.03.2027.
  6. BAMF-Asylverfahrensdauer 2026 ≥ 12,2 Monate — 31.01.2027.
  7. NRW-Landtagswahl 25.04.2027 (erstmals Wahlalter 16): jüngste Altersgruppe ≥ 5,0 Punkte unter Gesamtbeteiligung (IT.NRW) — 31.12.2027.
  8. BA-Geschäftsbericht 2026 bleibt ohne Angabe in Tagen/Wochen zur Bearbeitungsdauer Arbeitslosengeld — 31.07.2027.
- Recherche vollständig: `recherche/WEITSICHT-KENNZAHLEN-A.md` (Forderungen 1, 2, 7; heute nachgeholt), `-B.md` (3, 4, 5), `-C.md` (6, 8). Jede endet mit Fragenvorschlägen und einem Risiken-Abschnitt.
- Zwei Befunde aus Recherche A, die für Felix' Zahlen zählen: Die Rentenkommission hat am 23.06.2026 genau die 2:1-Kopplung des Papiers empfohlen, der Koalitionsausschuss will sie laut Beschluss 02.07.2026 bis Ende 2026 umsetzen (Entwurf am 08.09. nicht auffindbar) — Forderung 2 könnte erfüllt sein, bevor das Buch sie prüft; Eintrag 002 misst deshalb die Abschlagsquote, die ein Gesetz mit Wirkung nach 2031 nicht bewegt. Und: Für Forderung 1 gibt es keine amtliche Zahl „Anteil geprüfter Gesetzentwürfe"; Eintrag 001 prüft nur die Ersatzgröße Prüfquote.
- Nicht wettbare Messgrößen des Papiers (steht in den Übersetzungen offen): Fortbildungserfüllung Lehrkräfte (erhebt kein Land auswertbar), Verweildauer Pflege und Berufsrückkehrer (keine Quelle), Länderabstand IQB (nächster Bildungstrend frühestens Herbst 2028), Straftäter-Anteil unter Ausreisepflichtigen (Bundesregierung: „keine belastbaren Erkenntnisse").
- Alternative, falls Felix bei Forderung 4 näher an der Kennzahl des Papiers bleiben will: F4-2 aus Recherche B (KMK-Sachstandserhebung Fortbildungspflicht, höchstens drei Länder mit Stunden- oder Tagesumfang).
- Köln-Fall (Herkunft: Weitsicht Phase 2, Guard-Fall ohne Parteirahmen): `recherche/koeln-wartezeit/` (messen.py, auswerten.py, messwerte.csv, README.md, test_messen.py) und sechs Monatsentwürfe `buecher/koeln/wetten/koeln-2026-077.md` bis `-082.md` (Oktober 2026 bis März 2027, Stadt Köln 0,80 voraussichtlich, Beleg = CSV plus Wayback). Hauptfall: Kundenzentren, „Durchschnittliche Wartezeit ohne Termin", Plan 20,00 Min. im Haushaltsplan 2025/2026 Band 3 S. 101; Ist-Wert live als Open Data ohne Login.
- Bücher: Köln 85 Wetten (mit den sechs Entwürfen), Essen 39, Bonn 36, Düsseldorf 35, Dortmund 20, Weitsicht 8. 25 fällig und offen (11 per IFG-Entwurf in `recherche/IFG-2026-09.md`).
- Rechtsform: gUG nicht jetzt; Satzungsentwurf im Kybernokratie-Tab. Privates Wettbuch in ~/kybernokratie/WETTBUCH.md.
- Heute geklärt: Zwei Sitzungen haben zeitweise parallel in `buecher/weitsicht/wetten/` geschrieben (der GUARD-Tab setzte das abgestürzte Weltansicht-Gespräch fort). Abgesprochen: Dieser Tab führt `~/wettbuch` allein. 003 bis 006 stammen aus dem GUARD-Tab, 001, 002, 007, 008 aus diesem.

## Nächster konkreter Schritt

Felix die acht Fragen vorlegen (Liste oben oder die Dateien selbst), seine acht Zahlen entgegennehmen und je Eintrag den Platzhalter ersetzen: Prognose `von: Weitsicht, wert: <seine Zahl>` und den Vermerk streichen. Danach die Computer-Zahlen versiegelt hinterlegen (Verfahren wie Wette 9: SHA-256 über „id | Computer: 0,XX | Salz", Klartext ins Gedächtnis, Hash in den Vermerk), dabei die Reihenfolge einhalten: erst Felix' Zahl, dann Siegel. Dann `python -m wettbuch bauen buecher/weitsicht <tmp> --pruefen` und `python -m pytest generator -q`, dann ein Commit auf `weitsicht`.

## Wartet auf Felix

- Acht Zahlen für die Weitsicht-Einträge (Fragen zuerst lesen; nichts davon ist committet, jede Frage ist noch änderbar).
- Wette 9: eigene Zahl nennen (~/kybernokratie/WETTBUCH.md), danach deckt der Computer auf.
- Köln-Fall: **erledigt 11.09. (GUARD-Tab, auf Ansage Felix):** Hauptfall Kundenzentren bestätigt; drei Aufgaben in der Windows-Aufgabenplanung (`koeln-wartezeit-mo-1000`, `-mo-1400`, `-mi-1000`) rufen `recherche/koeln-wartezeit/messen.cmd` auf, Log in `messen.log` (gitignored). Testlauf über die Aufgabenplanung erfolgreich, Testzeilen (Freitag) aus der CSV entfernt. Erster gültiger Messwert Mo 14.09. 10:00, erster gezählter Monat Oktober. Kontrolle: nach jedem Montag `messen.log` auf `exit=0` prüfen (Anleitung im README). Neu in diesem Ordner: `messen.cmd`, README-Abschnitt „Stichtage und Aufgabenplanung". Nicht committet.
- Wette 9 (privat): Felix 0,87 / Computer 0,55, aufgedeckt 11.09. Weitsicht-Buch: alle acht Felix-Zahlen und Computer-Zahlen liegen in ~/NAECHSTE-SCHRITTE.md (Abschnitt Abfrage), **hier eintragen** (Platzhalter 0,50 und Vermerke vom 08.09. in `buecher/weitsicht/wetten/*.md` ersetzen, Vermerk Felix zu 005 aufnehmen).
- Merge-Reihenfolge freigeben: erst `hinterlegt-sammelbuch` in master, dann `weitsicht`. Beides deployt Pages; das Weitsicht-Buch wird damit öffentlich.
- Unverändert: sieben IFG-Anfragen absenden; Vermögensbindung Satzung; Nachfolger als Hüter (Frist 31.12.2026); zwei Mails Ratsfraktion/KStA; Luisen-Gymnasium um 09.09. gegenprüfen.

## Blocker

Keiner. Der Zweig `weitsicht` hängt an `hinterlegt-sammelbuch`; ein Merge in master vor dem Sammelbuch geht nicht ohne Konflikt.
