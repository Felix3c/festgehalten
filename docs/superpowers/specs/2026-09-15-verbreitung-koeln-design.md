# Verbreitung: Köln zuerst (Design, 15.09.2026)

**Frage von Felix:** Doorway, Guard, belegbar.eu und das Wettbuch sind live, aber niemand sieht sie.
**Gegenfrage von Felix:** Wer von den möglichen Publika benutzt es? Die Antwort ist die Antwort.

## Befund (Stand 15.09.)

- Vier Wochen, etwa 20 Berührungen: 1 LinkedIn-Post (Konto mit 9 Kontakten), 5 LinkedIn-Nachrichten,
  8 Anbieter-Mails, 3 Presse-Mails (KStA 01.09., WDR + Express 11.09.), 1 NEGZ-Mail, 1 Mail an die
  CDU-Fraktion Köln (01.09.). Rücklauf: Scaleway (als Fall), ein Anwalt gegen Honorar. Presse und
  Fraktion: nichts.
- Nichts wiederholt sich, nichts wird gemessen (nur belegbar hat Search Console, zuletzt 24.08.).
- Doorway und das Paper wurden nie verbreitet.

## Wer benutzt es

| Publikum | Benutzt es? | Rolle |
|---|---|---|
| Kölner Ratsfraktion | ja, wiederholt (Material gegen die Verwaltung, kostenlos) | erster Leser |
| Lokaljournalist Köln | einmal pro Aufhänger | geliehene Reichweite |
| zweiter Halter (Civic Tech, OK Lab) | erst nach einem Zitat | Multiplikator, später |
| Datenschützer (belegbar) | kein Hinweis | warten bis Kill-Check 14.10. |
| Doorway-Nutzer | nicht ohne Fördergeber, der es verlangt | keine Verbreitung |
| Hacker News u. ä. | schaut, benutzt nicht | später, mit Geschichte |

Entscheidung (Felix, 15.09.): Köln, Ratsfraktion zuerst, Journalist als Aufhänger.

## Plan (bis nach der Oper, 28.09.)

1. **Messen zuerst.** Search Console für https://felix3c.github.io/festgehalten/ und
   https://felix3c.github.io/doorway/ (URL-Präfix, HTML-Datei im Repo, kein DNS, kein Skript).
   Messtabelle für alle drei Seiten in `~/wettbuch/MESSUNG.md`, gleicher Takt wie belegbar.
2. **Zweite Fraktion.** CDU hat 14 Tage geschwiegen (Frist 15.09.). Nächste Fraktion aus der
   Opposition, Satz "Stadt Köln, Brier 0,58", drei Zahlen (79 Ankündigungen, 24 aufgelöst, 10 Termine
   nicht eingetreten). Recherche Claude, Versand Felix.
3. **Nachfassen Meifert** (Entwurf 1 in `~/kybernokratie/mails/2026-09-15-welle-2.md`). Versand Felix.
4. **Atom-Feed "neu aufgelöst"** im festgehalten-Generator, je Buch und für alle Bücher.
   Abonnieren ohne zu fragen; kein Kanal, kein Betreiber (GUARD "Was Guard nicht ist").
5. **Nach dem 28.09.:** aufgelöste Opern-Wette an drei Redaktionen und beide Fraktionen, ein Absatz,
   mit Feed-Link.
6. **Erst danach** OK Lab Köln / Code for Germany mit ANLEITUNG.md, nur wenn ein Zitat existiert.

## Bewusst nicht

LinkedIn-Posting, eigener Newsletter, belegbar-Verbreitung vor dem 14.10., Hacker News.

## Erfolg messbar

Bis 15.10.: eine Antwort von Fraktion oder Redaktion, oder ein Zitat des Buchs. Search-Console-Klicks
für festgehalten > 0 aus einer Quelle, die nicht Felix ist. Sonst: dieser Plan hat nicht getragen,
nächste Publikumsfrage stellen.

## Stand 15.09.2026 abends (Claude, Home-Tab)

- **Feed gebaut:** Zweig `feed` (e666b96 + e1205f2), 94 Tests grün, Probebau aller Bücher: Köln-Feed 24
  Einträge, Sammelfeed 50. **Nicht gemergt** (Berechtigungsfilter). Felix: `git merge --ff-only feed`
  auf master und pushen, oder PR über github.com/Felix3c/festgehalten/compare/master...feed.
- **Search Console festgehalten:** Property `https://felix3c.github.io/festgehalten/` angelegt (Felix' Konto),
  Bestätigungsdatei `google5df4d68519dcb210.html` liegt im Repo, Workflow kopiert sie nach `site/`.
  Nach Merge und Pages-Lauf in der Search Console auf BESTÄTIGEN klicken (Tab ist offen), dann
  Sitemap gibt es keine; Startseite über „URL-Prüfung“ anstoßen. **Doorway-Property noch nicht angelegt.**
- **Fraktion:** FDP/KSG gewählt (Begründung und Adressen in
  `~/kybernokratie/mails/2026-09-15-fdp-fraktion-koeln.md`). Gmail-Entwurf liegt im Postfach.
  **Erst senden, wenn der Feed live ist** (die Mail verlinkt koeln/feed.xml).
- **Meifert-Nachfassen:** Gmail-Entwurf liegt im Postfach (an ksta-koeln@kstamedien.de), Zahlen 79/24/10
  am 15.09. gegen die Live-Seite gültig. Versand Felix.
- Offen danach: Doorway-Property, `MESSUNG.md` für festgehalten anlegen, nach 28.09. Opern-Auflösung
  an Redaktionen und beide Fraktionen.

## Stand 15.09.2026, 18:10 MESZ

- Zweig `feed` von Felix per Fast-Forward in master übernommen (0dcd0d0), Pages gelaufen: Köln-Feed live mit
  24 Einträgen, Bestätigungsdatei antwortet 200.
- Search Console: Inhaberschaft für https://felix3c.github.io/festgehalten/ **bestätigt** (HTML-Datei).
- **Gesendet 18:06 MESZ, beide von Felix:** Nachfassen Meifert (KStA) und FDP/KSG-Fraktion (CC Schöppen),
  beide mit dem Festakt 24.09. als Aufhänger (Wette koeln-2025-003, Buch 0,70, Auflösung 25.09.).
- Nächste Termine: 25.09. Festakt-Wette auflösen und in den Feed bringen; danach Opern-Wette 28.09.;
  Antworten von KStA und FDP im Postfach prüfen. Offen: Doorway-Property, MESSUNG.md für festgehalten.
