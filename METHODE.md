# METHODE — wie die Computer-Prognosen entstehen

Stand 02.09.2026. Gilt für Lauf 1 (hinterlegt 28.08.2026): 133 Prognosen in fünf
Büchern, 65 Ja/Nein und 68 Punkt. Diese Seite beantwortet die Frage, die als erste
kommt: „Ein Sprachmodell? Also Zufall?" — Nein. Hier steht, wie die Zahlen
entstanden sind, und wie jeder sie nachrechnen oder besser machen kann.

## 1. Was der „Computer" ist

Ein Sprachmodell (Claude, Anthropic), das für den Halter Wette für Wette eine Zahl
hinterlegt hat. Keine Spezialsoftware, keine Datenbank, kein Zugriff auf
Nichtöffentliches. Es steht in jedem Buch in derselben Rangliste wie die gemessene
Stadt, nach denselben Regeln (FORMAT.md §3.4). Es hat keinen Sonderstatus und kann
verlieren.

## 2. Die Regel: Basisrate statt Recherche

Der Computer hat für keine Wette recherchiert, ob dieses Projekt gerade gut läuft.
Er hat jede Behauptung einer **Referenzklasse** zugeordnet und den Wert dieser Klasse
eingetragen — die Frage lautet nicht „schafft Köln das?", sondern „wie oft halten
Ankündigungen dieser Art?". Das ist Reference Class Forecasting (Flyvbjerg): Die
Innensicht der Institution („wir sind im Zeitplan") wird gegen die Außensicht
(„Projekte wie dieses") gestellt. Die Institution sagt in jeder Wette 1,00; der
Computer sagt die Basisrate. Aufgelöst wird gegen die Wirklichkeit.

Einzige Ausnahme: Vorgeschichte, die allgemein bekannt ist, senkt oder hebt den
Wert (Bühnen Köln seit 2012, Mülheimer Brücke). Das steht dann in der Begründung.

## 3. Die Tabelle (Lauf 1, 28.08.2026)

Aus den Begründungen aller 133 Einträge rekonstruiert; jede Wette-Datei trägt ihre
eigene Zeile unter „Begründung Computer".

**Ja/Nein** (Wert = Wahrscheinlichkeit, dass die Ankündigung eintritt):

| Referenzklasse | Wert | Beispiel |
|---|---|---|
| Veranstaltung, Sitzung, Fest mit festem Datum | 0,90–0,95 | Weihnachtsmarkt, Ausstellungseröffnung, Ausschusssitzung |
| Wahl- oder Fristverfahren | 0,90 | Briefwahl endet am Stichtag |
| Ratsbeschluss angesetzt: Kenntnisnahme / Beschluss / Inkrafttreten | 0,85 / 0,70–0,75 / 0,60 | Hauptsatzung, Masterplan, Verwaltungsreform |
| Laufendes Angebot bleibt bis Jahresende | 0,75 | Pop-up-Ausstellung |
| Tiefbau, Termin wenige Monate voraus | 0,50–0,60 | Kanal, Fahrbahn, Haltestelle |
| Kommunaler Hochbau, Termin 1–2 Jahre voraus | 0,35–0,45 | Schule, Bad, Kita; „voraussichtlich" +0,05–0,10; Modulbau/Interim 0,50–0,55 |
| Hochbau 3–4 Jahre, Kulturbau, Brücke | 0,30–0,35 | Museum, Sanierung im Bestand, Gesamtinstandsetzung |
| Mehrere Bauten oder ein Gesamtnetz gleichzeitig pünktlich | 0,25–0,30 | neun Erweiterungsbauten, drei Stufen Citybahn |
| Zielzahl erreicht (Plätze, Anschlüsse, Dächer) | 0,35–0,55 | Faustregel: Zielzahlen werden zu 70–85 % erreicht |
| Langfristziel mit Zieljahr (Modal Split 2030) | 0,20 | „fast nie im Zieljahr" |

**Punkt** (Wert = Zahl in der Einheit der Frage, abgeleitet aus der Ankündigung):

| Referenzklasse | Regel |
|---|---|
| Defizit im Jahresabschluss | Trend aus dem Vollzug 2025/26 fortgeschrieben (verschlechtert sich); Novemberprognose mit Haushaltssperre: etwas besser als angekündigt |
| Investitionsauszahlungen | Plan minus 15–25 % (NRW-Kommunen bleiben regelmäßig dahinter) |
| Kostenfeststellung Bau | letzte Ankündigung plus 10–20 %; Schule +15 %, Modulbau +10 %, Museum +30 % |
| Konsolidierungspakete, globale Minderaufwände | etwa 75 % werden realisiert |
| Gebaute Kapazität (Plätze, Züge) | Planungsgröße, wird gebaut wie geplant |

## 4. Warum das kein Zufall ist — und wie man es prüft

- Zufall hat einen Namen: 0,50 auf alles, Brier 0,25 (FORMAT.md §3.1). Liegt der
  Computer nach 10 aufgelösten Wetten darüber, ist er schlechter als eine Münze, und
  das steht öffentlich in der Rangliste.
- Die Basisraten sind falsifizierbar: Nach jedem Auflösungslauf lässt sich je Klasse
  zählen, wie oft die Ankündigung eintrat. Erste Messung: Stadt Köln, 15 aufgelöste
  Ja/Nein-Ankündigungen, 6 eingetreten (40 %), Brier 0,58 (Lauf 30.08.2026,
  `recherche/AUFLOESUNG-2026-08-30.md`). Die geschätzten „etwa ein Drittel" für
  Bautermine liegen in dieser Größenordnung.
- Das Buch eicht die Tabelle selbst: Weichen gemessene Raten ab, bekommt diese Seite
  eine neue datierte Tabelle für den nächsten Lauf. Alte Prognosen bleiben stehen
  (§1.3.3) und werden mit den alten Werten gewertet.

## 5. Nachmachen in fünf Schritten

1. Alle Wetten mit `pruefung_am` nach heute auflisten. Nur die. Nie eine Wette, deren
   Ausgang schon bekannt ist (siehe 6).
2. Jede Wette einer Klasse aus Abschnitt 3 zuordnen. Passt keine: neue Klasse, Wert
   begründen, hier eintragen.
3. Wert eintragen als Prognose `von: Computer`, `art: geschaetzt`,
   `hinterlegt_am: <heute>`.
4. Eine Zeile „Begründung Computer" in den Textteil: Klasse, Abweichung, und der Satz
   „Hinterlegt am <Datum>, vor `pruefung_am`."
5. Committen. Der Commit-Hash ist der Zeitstempel; `git log -p` auf die Datei zeigt
   jedem, wann die Zahl da war.

Wer ein anderes Modell, eine eigene Tabelle oder gar kein Modell nimmt, trägt einen
anderen Namen unter `von` ein und steht daneben in der Liste. Das Format vergleicht;
es schreibt keine Methode vor.

## 6. Was die Methode nicht kann

- Die Werte in Abschnitt 3 stammen aus allgemeinem Wissen über Referenzklassen
  (Bauprojekte, kommunale Haushalte), nicht aus einer Datenbank in diesem Repo. Die
  Datenbank entsteht erst durch die Bücher selbst.
- Keine Prognose nach dem Ereignis. Im ersten Lauf trugen drei Kölner Einträge
  (001, 002, 004) Computer-Werte, die nach dem Prüfdatum hinterlegt waren. Sie wurden
  per `ersetzt_durch` durch 077–079 ohne Computer-Zeile ersetzt (Commit 5435c48).
  Das Format hat dafür kein Feld (§6); die Disziplin liegt beim Halter, Git zeigt sie.
- Ein anderes Modell oder derselbe Halter an einem anderen Tag kann andere Werte
  setzen. Deshalb steht in jeder Datei die Begründung und nicht nur die Zahl.
