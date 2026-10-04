# Bonn: die achtzehn „kein Treffer“-Zitate nachgeprüft (04.10.2026)

Dauerlauf, 04.10.2026, ab etwa 06:30. Grundlage war `recherche/wortlaut-vorschlaege.csv` mit der Bewertung `kein_treffer`,
nur `bonn-*` (18 Zitate aus sieben Pressemitteilungen). Für jede Wette habe ich die Archivkopie aus der CSV gelesen (Abruf
als `id_`, HTTP 200, Text ohne HTML). Die Wettdateien habe ich nicht geändert. Damit sind alle fünf Städte durch
(Köln, Düsseldorf, Dortmund, Essen, Bonn).

| Wette | Archivkopie | Ergebnis |
|---|---|---|
| bonn-2025-001 | 20250420215117 (PM März 2025, Ratsbeschluss) | **gedeckt.** „Die jährlichen Defizite stellen sich nun wie folgt dar: 2025 97 Millionen Euro, 2026 123 Millionen Euro, 2027 128 Millionen Euro, 2028 111 Millionen Euro und 2029 110 Millionen Euro.“ (in der Wette „97,0“) |
| bonn-2025-005 | 20250420215117 | **gedeckt.** wie -001 (128) |
| bonn-2025-006 | 20250420215117 | **gedeckt.** wie -001 (111) |
| bonn-2025-009 | 20250420215117 | **gedeckt.** wie -001 (110) |
| bonn-2025-003 | 20250327230932 (PM 20.06.2024, Entwurf) | **gedeckt.** „In den darauffolgenden Jahren wird mit Fehlbeträgen von 180 Millionen Euro (2027), 207 Millionen Euro (2028) und 179 Millionen Euro (2029) gerechnet.“ Der Zusatz „vor Beginn der politischen Konsolidierungsberatungen“ ist Einordnung, kein Wortlaut. |
| bonn-2025-004 | 20250423171259 (PM 19.12.2024, Konsolidierungspaket) | **gedeckt.** „2025: minus 96,9 Millionen Euro, 2026: minus 122 Millionen Euro, 2027: 119,9 Millionen Euro, 2028: 109,7 Millionen Euro und 2029: 105,4 Millionen Euro.“ |
| bonn-2025-012 | 20250423171259 | **Befund A.** „Beim Personal will die Stadtverwaltung bis 2029 rund 300 Stellen reduzieren.“ |
| bonn-2025-013 | 20250423171259 | **Befund A.** „Das Einsparvolumen wird in dem Fünf-Jahres-Zeitraum insgesamt knapp 67 Millionen Euro betragen.“ (Wette: „rund 67“) |
| bonn-2025-014 | 20250322053052 (PM 18.03.2024, Kita-Bedarfsplan 2023 bis 2027) | **gedeckt, Befund C.** „Die vom Rat der Stadt Bonn beschlossene Zielversorgungsquote von 58 Prozent, die auch zukünftig beibehalten wird“ |
| bonn-2025-015 | 20250322053052 | **Befund C.** „Hierzu müssen noch rund 890 U3-Betreuungsplätze geschaffen werden.“ (ohne Jahr) |
| bonn-2025-016 | 20250322053052 | **gedeckt, Befund C.** „Daher wurde die Versorgungsquote in der jetzigen Fortschreibung des Kitaplans auf 104 Prozent erhöht.“ |
| bonn-2025-017 | 20250322053052 | **Befund C.** „In den kommenden Jahren müssen über 1.000 Betreuungsplätze in Kindertageseinrichtungen und Tagespflege geschaffen werden.“ (ohne Jahr) |
| bonn-2025-018 | 20241212075633 (PM 07.06.2024, PV-Rahmenvertrag) | **Befund B.** siehe unten |
| bonn-2025-019 | 20241212075633 | **gedeckt.** „Für 2024 ist vorgesehen, Anlagen mit einer Gesamtleistung von 2.000 bis 2.500 kWp auf den Dächern städtischer Liegenschaften zu installieren. Bei dieser Zahl handelt es sich derzeit noch um eine Schätzung“ (bereits aufgelöst, Ausgang 617) |
| bonn-2025-022 | 20250316153243 (PM 23.04.2024, Hardtbergbad) | **gedeckt.** „Die voraussichtlichen Kosten für die gesamte Maßnahme werden sich nach derzeitigem Stand auf 51,5 Millionen Euro belaufen. Zur energetischen und barrierefreien Sanierung erhält die Bundesstadt Bonn sechs Millionen Euro aus dem Förderprogramm des Bundes“ |
| bonn-2025-023 | 20250121124703 (PM 22.03.2024, Klimaneutraler Konzern 2035) | **gedeckt, Befund D.** „Die VEBOWAG hat bereits konkrete Planungen zur seriellen Sanierung ihrer Mietobjekte inklusive der Umstellung der Wärmeversorgung bis einschließlich 2028.“ |
| bonn-2026-031 | 20260122141207 (PM 22.01.2026, Weihnachtsmarkt) | **gedeckt.** „Der Weihnachtsmarkt 2026 findet nunmehr von Mittwoch, 18. November, bis einschließlich Mittwoch, 23. Dezember 2026, statt.“ / „Am Totensonntag, 22. November 2026, wird der Markt wie in den Vorjahren geschlossen bleiben.“ / „Neu ist 2026 auch, dass die Stände des Marktes erstmals um 12 Uhr statt um 11 Uhr öffnen werden.“ (zu Frage 67: „öffnen um 12 Uhr“ ist eindeutig die Öffnungszeit der Stände) |

Bei den als gedeckt markierten Wetten ist das Zitat der Wette eine Umschreibung. Die Zahlen und Termine stehen wörtlich
in der Quelle. Die Sätze oben lassen sich direkt als Wortlaut übernehmen. Dass `wortlaut_vorschlag.py` bei den
Haushaltszahlen nichts fand, liegt an der Schreibweise: Die Wetten schreiben „97,0“, die Quelle schreibt „97“.

## Befund A: bonn-2025-012/013 sprechen vom „Konzern Stadt Bonn“, die Quelle von der Stadtverwaltung

In der Pressemitteilung vom 19.12.2024 steht der Stellenabbau unter „Dezernat Allgemeine Verwaltung, Digitalisierung
und Ordnung“: „Beim Personal will die Stadtverwaltung bis 2029 rund 300 Stellen reduzieren.“ Das Wort „Konzern“ kommt
in der ganzen Meldung nicht vor. Zum Konzern gehören auch Stadtwerke, VEBOWAG, Bonnorange usw. Eine Prüfung auf den
Konzern-Stellenplan 2029 würde also etwas anderes messen als das, was angekündigt wurde.

Vorschlag: In Zitat und Frage beider Wetten „im Konzern Stadt Bonn“ durch „in der Stadtverwaltung Bonn“ ersetzen. Bei
013 „rund 67“ durch „knapp 67“ ersetzen und „im Fünf-Jahres-Zeitraum (2025–2029)“ ergänzen. Die Zahlen bleiben gleich.

## Befund B: bonn-2025-018 — die 300 Dächer sind die zu prüfenden, nicht die geeigneten

Die Quelle sagt zwei getrennte Dinge:

- OB Dörner: „Bis zum Jahr 2028 wollen wir auf allen Dächern städtischer Liegenschaften, die sich baulich eignen,
  Photovoltaik-Anlagen installieren.“
- „Aktuell läuft die Ausschreibung für eine Machbarkeitsuntersuchung, im Zuge derer rund 300 städtische Gebäude auf ihre
  PV-Tauglichkeit geprüft werden sollen.“

Die Wette macht daraus „alle rund 300 geprüften und geeigneten Dächer“. Wie viele der 300 sich eignen, steht nirgends.
Die Frage „Sind am 31.12.2028 alle rund 300 geprüften, geeigneten Dächer … ausgestattet?“ lässt sich daher nicht sauber
auflösen. Liest man sie wörtlich (alle 300), ist sie strenger als die Ankündigung.

Vorschlag: Zitat = der Satz der OB oben. Frage: „Sind am 31.12.2028 alle städtischen Dächer in Bonn, die die
Machbarkeitsuntersuchung (rund 300 Gebäude) als baulich geeignet einstuft, mit Photovoltaik ausgestattet?“ Dazu im
Kontext: Die Zahl der geeigneten Dächer ist ungeklärt und muss bei der Auflösung aus dem Ergebnis der Untersuchung
kommen. Das ändert die Frage, also entscheidet Felix.

## Befund C: Kita-Wetten 014–017 — die Frist „2027“ kommt aus der Laufzeit des Plans, nicht aus den Sätzen

Die Meldung heißt „Kindertagesstättenbedarfsplan 2023 bis 2027 beschlossen“ und sagt „Für die Jahre 2023 bis 2027
formuliert …“. Die einzelnen Zahlen nennen kein Jahr. Bei 890 U3-Plätzen steht „müssen noch … geschaffen werden“, bei über
1.000 Plätzen „In den kommenden Jahren“. Die Lesart „bis zum Ende der Planlaufzeit“ ist vertretbar. Sie sollte aber im
Kontext jeder der vier Wetten stehen, damit am Prüftag niemand sagen kann, ein Termin sei nie genannt worden. Das betrifft
nur den Text, nicht die Frage.

## Befund D: bonn-2025-023 — gesagt hat es die Stadt über die VEBOWAG, nicht OB/SWB

Der Satz zur VEBOWAG steht im Fließtext der Stadt. Im Zitat danach spricht VEBOWAG-Vorstand Dr. Michael Kleine-Hartlage,
er nennt aber kein Jahr. `gesagt_von` lautet „OB Katja Dörner / SWB-Vorstand Olaf Hermes“. Hermes kommt in der Meldung
vor, aber zu den SWB, nicht zur VEBOWAG. Die Quelle sagt außerdem „konkrete Planungen … bis einschließlich 2028“, nicht
„schließt ab“. Vorschlag: `gesagt_von: Stadt Bonn (Pressemitteilung) über VEBOWAG`, das Zitat wörtlich wie oben. Die Frage
(Abschluss am 31.12.2028) bleibt.

## Was daraus folgt

- 12 von 18 gedeckt (014/016 mit Kontextsatz C, 023 mit Sprecher D), Wortlaut direkt übernehmbar (Teil von Frage 61).
  012/013 und 015/017: Zahlen stehen wörtlich, aber Befund A bzw. C. 018: Befund B.
- Frage an Felix: A und D sind Korrekturen an Zitat und Sprecher, die Zahlen bleiben gleich. C ist ein Kontextsatz. B
  ändert die Frage.
- Nichts gepusht, nichts an den Wettdateien geändert.
