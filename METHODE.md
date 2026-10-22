# METHODE — wie die Computer-Prognosen entstehen

Stand 02.09.2026, Abschnitt 7 (Nachrechnen) neu am 16.10.2026. Gilt für Lauf 1 (hinterlegt 28.08.2026): 133 Prognosen in fünf
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

## 7. Nachrechnen mit einem Befehl

Die Bewertung ist eine Formel, kein Urteil (FORMAT.md §3.1):

    brier = (wert − ausgang)²        ausgang = 1, wenn die Ankündigung eintrat, sonst 0

Kleiner ist besser. Wer 0,30 sagt und die Ankündigung tritt ein, bekommt
(0,30 − 1)² = 0,49; tritt sie nicht ein, (0,30 − 0)² = 0,09. Sagt die
Institution 1,00, bekommt sie 0 oder 1, nichts dazwischen. Die Münze (0,50 auf alles)
bekommt immer 0,25. Das ist die Latte, unter der der Computer liegen muss.

Jeder kann das über alle Bücher nachrechnen, ohne Konto und nach dem Herunterladen ohne
Netz. Gebraucht werden Python 3.11 oder neuer und die zwei Pakete aus `pyproject.toml`; aufgerufen wird im
obersten Ordner des Repos:

    git clone https://github.com/Felix3c/festgehalten.git && cd festgehalten
    pip install pyyaml markdown
    python werkzeuge/nachrechnen.py buecher            # Schnitt und Kalibrierung
    python werkzeuge/nachrechnen.py buecher --einzeln  # dazu der Rechenweg je Wette

Das Werkzeug wertet mit derselben Funktion wie die Seite
(`generator/wettbuch/bewerten.py`). Gezählt werden nur aufgelöste Ja/Nein-Wetten, für
die der Computer eine Zahl hinterlegt hat. Die Institution wird auf genau denselben
Wetten gerechnet, damit der Vergleich fair ist.

**Kalibrierung** heißt: Sagt der Computer bei vielen Wetten „0,30", sollten davon etwa
drei von zehn eintreten. Das Werkzeug teilt die Computer-Werte in Bänder zu 0,20 und
zählt je Band, wie oft es eintrat. Liegt „eingetreten" deutlich über dem Schnitt des
Bandes, war der Computer zu vorsichtig; liegt es darunter, zu zuversichtlich. Daraus
entsteht die nächste datierte Tabelle in Abschnitt 3 (§4 letzter Punkt).

**Stand 16.10.2026** (24 Bücher, 437 Wetten):

| Wer | Brier-Schnitt über 18 Wetten |
|---|---|
| Computer | 0,092 |
| Institution (angekündigt) | 0,147 |
| Münze (0,50 auf alles) | 0,250 |

| Computer-Wert | Wetten | Schnitt Computer | eingetreten |
|---|---|---|---|
| 0,20–0,40 | 1 | 0,35 | 0,00 |
| 0,40–0,60 | 4 | 0,49 | 0,25 |
| 0,60–0,80 | 5 | 0,70 | 1,00 |
| 0,80–1,00 | 8 | 0,89 | 1,00 |

(Bänder ohne Wette lässt die Tabelle weg; das Werkzeug zeigt sie mit „–“.)

Was diese Zahlen tragen und was nicht:

- **Nur 18 Wetten.** 48 Ja/Nein-Wetten sind aufgelöst, aber bei 30 davon war der
  Ausgang schon bekannt, als der Computer seine Werte hinterlegt hat. Für sie gibt es
  absichtlich keine Computer-Zahl (Abschnitt 6, keine Prognose nach dem Ereignis).
  Die 26 aufgelösten Punkt-Wetten haben aus demselben Grund keine.
- 18 Wetten sind zu wenig für ein Urteil über Bänder. Das Muster bis heute: Bei
  Werten ab 0,60 trat alles ein, was der Computer für wahrscheinlich hielt; er war dort
  eher zu vorsichtig. Ob das hält, zeigt erst eine größere Zahl. Die Tabelle in
  Abschnitt 3 bleibt bis dahin unverändert.
- Die Zahlen stehen hier mit Datum. Wer den Befehl später ausführt, bekommt neuere
  Zahlen; die alten bleiben über `git log -p METHODE.md` sichtbar.


### Was die Worte der Stadt wert waren

Die Stadt bekommt in jedem Buch einen festen Wert aus ihren eigenen Worten: Sagt sie etwas
ohne Vorbehalt zu, steht dort 1,00 („angekündigt“); schreibt sie „voraussichtlich“, „geplant“
oder Ähnliches, steht dort 0,80 (FORMAT.md §1.2). Diese Werte bleiben fest, denn das Buch
nimmt die Stadt beim Wort. Das Werkzeug zählt aber mit, wie oft das Wort dann gehalten hat.
Diese Tabelle ist nur eine Anzeige. Sie ändert keinen Wert und keine Rangliste.

**Stand 22.10.2026** (alle aufgelösten Ja/Nein-Wetten, auch die ohne Computer-Zahl):

| Institution | Wort (fester Wert) | aufgelöst | eingetreten |
|---|---|---|---|
| Stadt Bielefeld | angekündigt (1,00) | 1 | 1 von 1 |
| Stadt Bonn | angekündigt (1,00) | 4 | 3 von 4 |
| Stadt Bonn | voraussichtlich (0,80) | 3 | 3 von 3 |
| Stadt Dortmund | angekündigt (1,00) | 5 | 4 von 5 |
| Stadt Dortmund | voraussichtlich (0,80) | 1 | 1 von 1 |
| Stadt Düsseldorf | angekündigt (1,00) | 3 | 3 von 3 |
| Stadt Düsseldorf | voraussichtlich (0,80) | 2 | 1 von 2 |
| Stadt Essen | angekündigt (1,00) | 3 | 3 von 3 |
| Stadt Essen | voraussichtlich (0,80) | 4 | 1 von 4 |
| Stadt Hamm | voraussichtlich (0,80) | 1 | 1 von 1 |
| Stadt Köln | angekündigt (1,00) | 17 | 8 von 17 |
| Stadt Köln | voraussichtlich (0,80) | 5 | 3 von 5 |
| Stadt Münster | angekündigt (1,00) | 1 | 1 von 1 |
| Stadt Wuppertal | angekündigt (1,00) | 1 | 1 von 1 |
| Stadt Wuppertal | voraussichtlich (0,80) | 1 | 0 von 1 |
| **Alle** | angekündigt (1,00) | 35 | **24 von 35** |
| **Alle** | voraussichtlich (0,80) | 17 | **10 von 17** |

Wenn eine Stadt etwas ohne Vorbehalt angekündigt hat, kam es bisher in 24 von 35 Fällen,
also in gut zwei von drei. Bei „voraussichtlich“ kam es in 10 von 17 Fällen, das ist
seltener als die 0,80, die das Buch dafür einträgt. Die meisten Städte haben erst eine bis
fünf aufgelöste Wetten; einzeln trägt erst eine Stadt mit zehn oder mehr eine Aussage (bisher
nur Köln: 8 von 17). Nachrechnen mit demselben Befehl wie oben, die Tabelle steht am Ende der
Ausgabe.
