# festgehalten — Nächste Schritte

**Stand:** 03.10.2026 22:10 (Dauerlauf: Felix „Alles steht“ 21:58 zu 48–50 → **`koeln-rueckfall` (`dd9ddc5`) und `buch-ki` (`7aa4232`, Claude-Zahlen mit Offenlegung) lokal in master gemergt**, 99 + 43 Tests grün; **Push macht Felix: `cd ~/wettbuch && git push origin master`** (bringt 848e48b, NRW, Köln-Rückfall, KI live; ein `git merge` ist nicht mehr nötig). Presseamt-Entwurf (49) sendet Felix. Bund (44) und Gatekeeper (46) weiter offen) · 03.10.2026 21:55 (Dauerlauf: neues Buch **„KI gegen KI“** auf lokalem Zweig `buch-ki` (`7542338`), Frage 50) · 03.10.2026 21:15 (Dauerlauf: **Köln-Feed seit 16.09. 07:45 eingefroren**, http 403; Fix auf lokalem Zweig `koeln-rueckfall`, Frage 48/49, Entwurf ans Presseamt) · 03.10.2026 20:50 (Dauerlauf: neues Buch **„Gatekeeper gegen Gatekeeper“** auf lokalem Zweig `buch-gatekeeper` (`9db3728`): 10 Wetten zu Alphabet, Amazon, Apple, Booking, Meta, Microsoft aus eigenen Firmenquellen, Zitate wörtlich geprüft; Auswahl = DMA-Gatekeeper-Liste der Kommission; GPAI-Liste Art. 52 Abs. 6 AI Act nicht veröffentlicht (ungeklärt), ByteDance ohne Kandidaten; Kandidaten/Verworfene in `docs/2026-10-03-buch-gatekeeper-KANDIDATEN.md`; Prüfung 9 Bücher/245 Wetten OK, 99 Tests grün; Merge+Push erst nach „steht“ (Frage 46)) · 03.10.2026 18:55 (Dauerlauf: Felix „Alles steht“ 18:42 → Frage 27 Köln-Fix und 30 Buch NRW freigegeben; **buch-nrw lokal in master gemergt (`ec5dd7e`), 99 Tests grün; Push vom Rechte-Filter des Dauerlaufs gesperrt → Felix pusht selbst: `cd ~/wettbuch && git push origin master`** (bringt 848e48b + NRW live, eilig vor Mo 05.10.). Frage 32: für Wette 16 zählen nur Plan-Foren, Stand 0 von 3, Frist 08.10.) · 03.10.2026 15:25 (Dauerlauf: Datei auf git-Stand gebracht; **Befund Köln-Messung: seit 16.09. keine einzige Messung**, Fix `848e48b` lokal, Push wartet auf Felix) · 03.10.2026 15:00 (Dauerlauf: bonn-2026-032 JA, dortmund-2026-019 JA, duesseldorf-2026-033 JA, essen-2025-030 NEIN aufgelöst und gepusht, `7560373`; 99 Tests grün, alle Bücher OK) · 03.10.2026 14:50 (Entschieden Felix per Mail, Fragen 14/15 „steht“ = Empfehlung: bonn-2026-032 JA, dortmund-2026-019 JA, duesseldorf-2026-033 JA, essen-2025-030 NEIN übernehmen, committen, pushen; dortmund-2026-020 erst mit Bericht vom 21.09., koeln-2026-073 offen lassen. Umsetzung als Aufgabe in ~/allein/ALLEIN.md) · 03.10.2026 14:30 (Dauerlauf: 072/083 gepusht) · 03.10.2026 (Dauerlauf, Tagesprüfung Guard: zehn fällige Ereignis-Wetten recherchiert, zwei Auflösungs-Dateien vorbereitet, nichts committet) · 11.09.2026 nachts (Weitsicht-Buch mit allen sechzehn Zahlen committet, in master gemergt und öffentlich)
**Führendes Dokument:** FORMAT.md (festgehalten-Format v1 inkl. §8 Verfassung) · ~/GUARD.md (Ebenen-Karte, Beschluss 08.09. „Partei oder Siegel, nie beides") · ~/weitsicht/STAND.md (Herkunft des neuen Buches)
**Phase:** v1 live, 6 Bücher öffentlich. origin/master = `7560373` (03.10. 14:46), lokal ein Commit voraus (`848e48b`, Köln-Messung, nicht gepusht).

## Neu 03.10.2026 21:55 (Dauerlauf): Buch „KI gegen KI“ (Ebene KI-Anbieter), lokal

- Lokaler Zweig `buch-ki`, Commits `cba4157` + `7542338` (nicht in master, nicht gepusht): `buecher/ki/` mit BUCH.md und 9 Wetten
  `ki-2026-001` bis `-009`. Auswahl ohne Ermessen = Vollunterzeichner des GPAI-Verhaltenskodex laut Kommission
  (https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai, Stand 31.07.2026, 21 Unterzeichner) ohne die DMA-Gatekeeper
  (Amazon, Google, Microsoft haben das Gatekeeper-Buch); xAI nur Teilunterzeichner, Meta kein Unterzeichner; Liste nach Art. 52 Abs. 6
  AI Act am 03.10. weiter nicht auffindbar.
- Wetten: OpenAI Stargate UAE 200 MW live 2026, OpenAI for Germany Start 2026; Anthropic 10.000 Frontier Deployed Engineers bis Ende
  2027, > 1 GW TPU in Betrieb 2026; Cohere/Aleph Alpha Closing 2026 (zwei Wetten, ein Ereignis); IBM B300-Cluster Q1 2027, Quantum
  System Two Schweiz Ende 2026; ServiceNow 240.000 Lernende UK bis 2027. Alle Zitate aus Firmenquellen, per curl wörtlich geprüft.
- **Interessenkonflikt offengelegt:** der Computer ist ein Anthropic-Modell (BUCH.md + Vermerk bei 003/004). Dazu Offenlegung
  GitHub/Microsoft/OpenAI.
- Verworfen (Gründe in `docs/2026-10-03-buch-ki-anbieter-KANDIDATEN.md`): Mistral (nichts Eigenes im Fenster), Stargate 500 Mrd. (bis
  2029), IBM Quantum Advantage (schon gemeldet), kleine Unterzeichner ohne Prüfbares; Reserve Stargate Norway.
- Prüfung 9 Bücher/244 Wetten OK (Zweig gegen master), 99 Tests grün.
- **Wartet auf Felix:** Frage 50 (mergen + pushen; 003/004 mit Claude-Zahl oder qwen3:4b schätzen lassen).

## Neu 03.10.2026 21:15 (Dauerlauf): Köln-Feed eingefroren, Fix lokal

- **Befund:** `waiting-od.php` liefert seit **Mi 16.09.2026 07:45** für alle neun Kundenzentren dieselben Werte (Status
  „geöffnet“, Chorweiler 71 … Innenstadt 6 Min.). Wayback 16.09. 13:27 UTC und 20.09. 08:47 UTC gleicher Digest (`5HSZ6PS2…`),
  03.10. unverändert: https://web.archive.org/web/20261003190545/https://www.stadt-koeln.de/externe-dienste/open-data/waiting-od.php
  `http://` leitet seit 20.09. per 301 um und liefert am 03.10. **403**; `https://` liefert 200.
- Folge: Auch ein pünktlicher Lauf (Fix `848e48b`) misst nichts Echtes. Der alte Code scheitert an 403, oder er schreibt bei einer Umleitung die Zahlen vom
  16.09. als Oktober-Messung.
- **Fix auf lokalem Zweig `koeln-rueckfall`** (`dfa94cb`, `0d22085`, nicht in master): `FEED_URL` https; `frische_records` /
  `feed_veraltet`: nur Zentren mit `timestamp` von heute (nicht Zukunft), sonst keine Zeile, Exit 1, Wayback-Beleg (Wächter
  mailt). Laptop-Rückfallebene: `messen.cmd` → `messwerte-laptop.csv` (gitignored), `nachtragen.py` übernimmt nur fehlende
  Slots (Probe ohne `--schreiben`). 43 Mess-Tests, 99 Generator-Tests grün; Review: Slot nach Uhrzeit vs. Cron als Grenze in README.
- Gmail-Entwurf an presseamt@stadt-koeln.de (Kontakt laut offenedaten-koeln.de), Felix sendet (Frage 49).
- koeln-2026-077–082 bleiben offen; Windows-Aufgaben bleiben aus, bis der Feed wieder frisch ist.
- **Wartet auf Felix:** Frage 48: vor dem Push `git merge koeln-rueckfall`, dann `git push origin master`.

## Neu 03.10.2026 20:20 (Dauerlauf): Buch „Bund gegen Bund“ (Ebene Bund), lokal

- Lokaler Zweig `buch-bund`, Commit `d36d468` (nicht in master, nicht gepusht): `buecher/bund/` mit BUCH.md und 8 Wetten
  `bund-2026-001` bis `-008`: d-you-Wallet 02.01.2027, Kindergeld 267 € ab 2027, Wohngeld-Absenkung 01.01.2027, Pflege-
  Strukturreform 01.07.2027, Pflegekommission bis 31.01.2027, digitaler Führerschein bis 31.12.2026, Bundeswehr ≥ 187.000
  zum 31.12.2026, 11 GW Kapazitätsausschreibung bis 03.09.2027. Alle Zitate zweimal unabhängig per curl wörtlich geprüft.
- Halter-Festlegungen nach Empfehlung (änderbar vor dem Livegang): Bundeswehr-Schwelle 187.000 („deutlich im Korridor“),
  Kraftwerks-Frist ab Seitendatum 03.09.2026, Führerschein „Ende des Jahres“ = 31.12.2026.
- Nicht übernommen (Gründe in `docs/2026-10-03-buch-bund-KANDIDATEN.md`): Haushalt 2027 ≤ 119 Mrd. (BMF-Bot-Sperre, Zitat nur
  einmal gesehen), zentrale Kfz-Zulassung (Abgrenzung), BIP/Inflation 2027 (Prognosen, Prüfung 2028); keine Bahn-Quelle gefunden.
- `alle buecher … --pruefen`: 9 Bücher, 243 Wetten, keine Fehler; 99 Tests grün.
- **Wartet auf Felix:** Frage 44 (Zweig mergen und pushen = Buch geht live).

## Neu 03.10.2026 17:55 (Dauerlauf): Buch „NRW gegen NRW“ (Ebene Land), lokal

- Lokaler Zweig `buch-nrw`, Commit `d12696f` (nicht in master, nicht gepusht): `buecher/nrw/` mit BUCH.md und 11 Wetten
  `nrw-2026-001` bis `-011`, alle Quellen Pressemitteilungen auf land.nrw, Zitate wörtlich geprüft (Skript + zwei Stichproben
  per curl). Erste Prüftage 01./02.01.2027 (Forensik Lünen fertig, Entlastungsgesetz, Lebensarbeitszeitkonto, Besoldung);
  dazu Radwege 1.000 km bis Ende Legislatur (Stichtag 31.05.2027 gesetzt), 3.000 Kommissaranwärter 01.09.2027 (2026 nur
  ~2.600), Nettoneuverschuldung 2027 (5,0 Mrd), GreenTech-Messe 09.09.2027, Abiture 2027, fünftes Abiturfach BK.
- `python -m wettbuch alle buecher … --pruefen`: 8 Bücher, 235 Wetten, keine Fehler; 99 Tests grün.
- Verworfen (Gründe im Lauf): Windkraft 1.000 Anlagen, RE 13 Eindhoven, Termine ab 2029, Mittelzusagen ohne Auflösbarkeit.
- **Wartet auf Felix:** Frage 30 (Zweig in master mergen und pushen = Buch geht live).

## Tagesprüfung 03.10.2026 (Dauerlauf)

- **43 Wetten fällig und offen** (pruefung_am ≤ 17.10., ohne ausgang, ohne ersetzt_durch). Die alten hängen an Jahresabschlüssen und IFG (`recherche/IFG-2026-09.md`); bearbeitet wurden die zehn Ereignis-Wetten aus September.
- `docs/2026-10-03-aufloesung-bonn-dortmund-VORBEREITET.md`: bonn-2026-032 **JA** (WDR 25.09., 36:27), dortmund-2026-019 **JA** (DOSB, amtlich), dortmund-2026-020 **JA mit Vorbehalt** (Start amtlich, Ende 21.09. nur Programm), bonn-2026-036 und -035 ungeklärt (bonn.de und Ratsinfo hinter Bot-Sperre, Felix kann im Browser nachsehen, Stellen in der Datei).
- `docs/2026-10-03-aufloesung-koeln-duesseldorf-essen-VORBEREITET.md`: duesseldorf-2026-033 **JA**, essen-2025-030 **NEIN** (Eröffnung Hallenbad Borbeck auf Frühjahr 2027 verschoben, radioessen.de 09.07. mit Stadt-Zitat), koeln-2026-073 ungeklärt (nur WZ-Bericht ohne Uhrzeit, Option JA in der Datei), duesseldorf-2026-034 ungeklärt (Indiz für NEIN), essen-2025-031 bleibt offen bis Verfall 2028.
- **032/019/033 JA, 030 NEIN aufgelöst und gepusht 03.10. 15:00 (`7560373`, Freigabe Felix Fragen 14/15).** Weiter offen: dortmund-2026-020 (wartet auf Bericht zum 21.09.), koeln-2026-073 (offen gelassen), bonn-2026-035/036 (Felix im Browser), duesseldorf-2026-034 (ungeklärt, Indiz NEIN). Die vorbereiteten „Beleg gesucht“-Vermerke für 073/034/031 sind nicht übernommen (nicht freigegeben).
- **072 JA / 083 NEIN aufgelöst und gepusht 03.10. 14:28 (`3734488`, Freigabe Felix per Mail „1-10 steht").** Köln jetzt: 21 aufgelöste Ja/Nein, 11 nicht eingetreten, 10 eingetreten. Nachfass-Entwürfe mit 083-NEIN liegen in Gmail (FDP/KSG mit CC Schöppen, Meifert/KStA), Felix sendet; alter Festakt-Entwurf an Meifert muss Felix noch löschen (Löschen war für den Dauerlauf gesperrt), der an FDP ist gelöscht.
- Köln-Messung: **korrigiert 15:25** — die Zeile hier vorher („am Nachmittag gemessen“, „Remote ist weiter“) war falsch. Siehe Abschnitt „Köln-Messung steht still“ unten.
- Postfach: keine Antwort von Köln, Podcasts oder Redaktionen.

## Köln-Messung steht still (Befund 03.10.2026, 15:20)

- `messwerte.csv` auf origin/master endet am **16.09.2026** (letzter „data:“-Commit `5638a62`). Seitdem: null Zeilen.
- Ursache (GitHub-API, öffentliche Run-Liste, abgerufen 03.10.): jeder geplante Lauf startete 5–7 h zu spät, frühester Start je Tag
  21.09. 13:16, 23.09. 12:03, 28.09. 14:24, 30.09. 12:57 UTC. Das Fenster endet Mo 13:00 UTC, Mi 10:00 UTC (MESZ).
  `messen.py` verwirft Läufe außerhalb korrekt („keine Messung“, Lauf trotzdem „success“); der Wächter schlug fehl und stieß per
  Dispatch nach, aber ebenfalls nach Schließung. Die Härtung `0f305db` funktioniert also, nur kommt kein Lauf rechtzeitig an.
- **Folge:** koeln-2026-077 (Oktober) braucht Oktober-Messungen; Wette 9 (privat) braucht ≥ 6 Monate mit Messwerten. Der September
  hat nur den 16.09. (ein Abruf, 15:27, außerhalb der Wertung).
- **Fix lokal, `848e48b`:** acht zusätzliche Startversuche Mo+Mi 00:07–04:03 UTC (Slot „vormittag“). Kommen sie pünktlich, enden sie
  vor 7:30 ohne Zeile; kommen sie 5–7 h zu spät, landen sie im Fenster. Neuer Test, 30 Mess-Tests + 99 Generator-Tests grün.
  **Nicht gepusht** (öffentliches Repo, Frage an Felix). Wirkt erst nach Push; nächster Messtag Mo 05.10.
- Rückfallebene, falls auch das nicht greift: die drei Windows-Aufgaben auf dem Laptop (deaktiviert seit 11.09., README im Ordner)
  oder ein externer Auslöser für `workflow_dispatch` (braucht Konto/Token = Felix).

## Wo wir stehen (03.10.2026)

- Live: https://felix3c.github.io/festgehalten/ — Repo https://github.com/Felix3c/festgehalten. Pages-Build zuletzt grün 03.10. 12:46 UTC.
- Zweige `weitsicht` und `hinterlegt-sammelbuch` sind in master gemergt (lokal und auf origin noch vorhanden, löschbar).
- Bücher (Stand Dateien 03.10.): Köln 86 (29 aufgelöst, 54 offen, 3 ersetzt), Essen 39 (11/28), Düsseldorf 35 (16/19),
  Bonn 36 (5/31), Dortmund 20 (5/15), Weitsicht 8 (0/8). `buecher/hinterlegt/` leer.
- Fällig und offen (pruefung_am ≤ 03.10.): **32**, bis 17.10.: 37. Davon
  - 25 Alt-Wetten 2025 (Jahresabschlüsse, Baukosten, Bäume, Brücken) mit 1–4 Suchvermerken: warten auf Jahresabschlüsse
    (Köln festgestellt zuletzt 2023, Muster ~20 Monate) bzw. auf IFG (`recherche/IFG-2026-09.md`, sieben Anfragen nicht gesendet).
  - Ereignis-Wetten September: 073 (offen gelassen, Felix 03.10.), bonn-2026-035/-036 (Felix im Browser), dortmund-2026-020
    (wartet auf Bericht 21.09.), duesseldorf-2026-034 (Indiz NEIN), essen-2025-031 (bis Verfall 2028).
  - neu fällig: bonn-2025-001 (Defizit 2025, seit 01.10.).
  - nächste Stichtage: bonn-2026-034 (09.10., Heussallee), essen-2026-035 bis -038 (Rat 14.10., Prüfung 15.10.).
- Weitsicht-Buch: acht Einträge mit Felix- und Computer-Zahl, live seit 11.09. (`1d714bc`), Zahlen-Tabelle in der Git-Historie
  dieser Datei (Stand 11.09.).
- Seit 11.09. hinzugekommen (git log): Atom-Feed je Buch (`e666b96`), Impressum/Datenschutz (`d616c0f`), Köln sieben neue Wetten
  077–083 (`de299e8`), Auflösungen koeln-2025-003 (`4b0957c`), 070/071 (`5eb1a16`), 072/083 (`3734488`), Bonn/Dortmund/
  Düsseldorf/Essen (`7560373`).
- Ungetrackt in `docs/`: vier `*-VORBEREITET.md` (Arbeitsdateien der Auflösungen; 25.09., 01.10., zweimal 03.10.).
- Privates Wettbuch `~/kybernokratie/WETTBUCH.md`: offene private Fristen bis 31.10.: Wette 16 (Foren, 15.10., Bedingung drei
  Beiträge bis 08.10.), Wette 20 (Sprint, 31.10.). Wette 19 war in der Tabelle noch „offen“, obwohl der Eintrag sie am 27.09.
  zurückzieht → Tabellenzelle am 03.10. nachgezogen (Wettstand zeigt sie nicht mehr).
- Rechtsform: gUG nicht jetzt. Köln: 21 aufgelöste Ja/Nein (11 nicht eingetreten, 10 eingetreten).

## Nächster konkreter Schritt

1. **Felix:** erst `git merge koeln-rueckfall` (Frage 48), dann Push von `848e48b` freigeben (Frage in ~/allein/ALLEIN.md), am besten vor Mo 05.10. 02:00 Uhr; danach Di 06.10.
   prüfen, ob ein „data:“-Commit vom Montag da ist.
2. Recherche 03.10. (`docs/2026-10-03-aufloesung-haushalt-bonn-VORBEREITET.md`, Vermerke vorbereitet, nicht übernommen):
   bonn-2025-001 ungeklärt (Entwurf JA 2025 ~96,6 Mio nur aus Suchauszug, Quelle passwortgeschützt; bonn.de/Ratsinfo Bot-Sperre),
   dortmund-2025-001 ungeklärt (weiter nur Entwurf 352,7 Mio, nicht festgestellt), duesseldorf-2026-034 ungeklärt, Indiz NEIN,
   **bonn-2026-034 starkes Indiz JA** (SWB 28.09.: „Nach erfolgreichen Sanierungsarbeiten an Gleis 1 …“) → am Fr 09.10. auflösen.
3. Do 15.10.: essen-2026-035 bis -038 (Rat 14.10.) auflösen vorbereiten.

## Wartet auf Felix

- Frage 50: Buch KI (Zweig `buch-ki`, `7542338`) mergen und pushen.

- Frage 30: Buch NRW (Zweig `buch-nrw`, `d12696f`) mergen und pushen.

- Push `848e48b` (Köln-Messung).
- bonn-2026-035/-036 im Browser nachsehen (Stellen in `docs/2026-10-03-aufloesung-bonn-dortmund-VORBEREITET.md`).
- Sieben IFG-Anfragen absenden (`recherche/IFG-2026-09.md`); Vermögensbindung Satzung; Nachfolger als Hüter (Frist 31.12.2026).
- Zwei Gmail-Entwürfe mit 083-NEIN senden (FDP/KSG + CC Schöppen; Meifert/KStA), alten Festakt-Entwurf an Meifert löschen.
- Zweige `weitsicht` und `hinterlegt-sammelbuch` löschen (gemergt; Löschen nur mit „steht“).

## Blocker

Köln-Messung: ohne Push des Fixes (oder Rückfallebene) bleibt der Oktober leer, koeln-2026-077 und Wette 9 laufen ins Leere.
