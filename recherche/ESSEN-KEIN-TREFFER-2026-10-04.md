# Essen: die dreizehn „kein Treffer“-Zitate nachgeprüft (04.10.2026)

Dauerlauf, 04.10.2026, ab etwa 06:20. Grundlage war `recherche/wortlaut-vorschlaege.csv` mit der Bewertung `kein_treffer`,
nur `essen-*` (13 Zitate). Für jede Wette habe ich die Archivkopie aus der CSV gelesen (Abruf als `id_`, HTTP 200,
Text ohne HTML). Die Wettdateien habe ich nicht geändert.

| Wette | Archivkopie | Ergebnis |
|---|---|---|
| essen-2025-002 | 20260412121252 (PM 25.09.2024) | **gedeckt.** „in 2026 ist ein Überschuss von 3,5 Millionen Euro geplant“ |
| essen-2025-003 | 20260412121252 | **gedeckt.** „in den Jahren 2025 bis 2029, werden insgesamt 2,7 Milliarden Euro investiert. Darin enthalten sind beispielsweise 965,4 Millionen Euro im Rahmen der Schulbauoffensive“ |
| essen-2025-004 | 20260412121252 | **gedeckt.** wie -003 |
| essen-2025-005 | 20260412121252 | **gedeckt.** „Anstieg unserer Verbindlichkeiten für Investitionskredite um rund 1,22 Milliarden Euro auf dann 3,4 Milliarden Euro“ (Zeitraum: „Innerhalb der nächsten fünf Jahre“) |
| essen-2025-013 | 20260519185805 (PM 02.05.2025) | **Befund A.** Die Pressemeldung nennt für die Moltkestraße kein Jahr. |
| essen-2025-014 | 20260610190648 (PM 27.08.2025) | **gedeckt.** „34.000 Quadratmetern“, „rund 1.300 Schüler*innen“, „bis Ende 2027 abgeschlossen sein“, „rund 137 Millionen Euro“ |
| essen-2025-015 | 20260610190648 | **gedeckt.** wie -014 |
| essen-2025-016 | 20260610190648 | **gedeckt.** wie -014 |
| essen-2025-017 | 20260610190648 | **gedeckt.** wie -014 |
| essen-2025-020 | 20260616115305 (Ruhrbahn 10.07.2024) | **gedeckt.** „werden die neuen Fahrzeuge die alten Docklands und B-Wagen der Ruhrbahn dann bis zum Jahr 2026 komplett ersetzen. Investition: rund 150 Millionen Euro.“ Gesagt hat es die Ruhrbahn, das steht so schon in `gesagt_von`. |
| essen-2025-023 | 20260315232553 (e-Magazin 22.10.2025) | **gedeckt, mit Vorbehalt (Befund C).** Die Aussage steht unter einer Bedingung und stammt vom Investor. |
| essen-2025-024 | 20260210002131 (PM 19.09.2025) | **Befund B.** Angekündigt war eine Grundsatzentscheidung über den Neubau, keine Entscheidung über den Standort. |
| essen-2025-033 | 20251209081411 (PM 19.11.2025) | **gedeckt.** „(Nach-)Besetzungssperre für Stellen innerhalb der Verwaltung bis zum 30.04.2026“ (im Zitat steht „Einstellungsstopp“) |

Bei den als gedeckt markierten Wetten ist das Zitat der Wette eine Umschreibung. Die Zahlen und Termine stehen
wörtlich in der Quelle. Die Wortlaut-Vorschläge aus den Sätzen oben lassen sich direkt übernehmen.

## Befund A: Bei essen-2025-013 (Grundschule Moltkestraße) steht der Satz auf der Projektseite, nicht in der Pressemeldung

Die Pressemeldung vom 02.05.2025 (`pressemeldung_1564958`, Pressegespräch Schulbau) sagt zur Moltkestraße nur, dass
die Vorbereitungen für die Entkernung abgeschlossen sind. „Spätestens 2027/2028“ steht dort nicht, und ein Jahr nennt
sie gar nicht.

Der Wortlaut steht auf der **Projektseite der Stadt**:

- https://www.essen.de/leben/planen_bauen_und_wohnen/schulausbau/grundschule_moltkestrasse.de.html
  - live abgerufen 04.10.2026, SHA-256 `4b5954f93e0719620c5a21374873438d53bd9404247ae10e9aa8d42b2496d8c0`,
    lokale Kopie nur auf Felix' Rechner, seit 09.10.2026 nicht mehr im Repo (Beleg: Wayback-Kopie + SHA-256) `recherche/belege/2026-10-04-essen-grundschule-moltkestrasse-projektseite.html`
  - Wayback: neu gespeichert **20261004041946**, ältere Kopie 20260308101315. Beide habe ich als `id_` abgerufen, und
    der Satz steht in beiden.
  - Wortlaut: „Spätestens zum Schuljahr 2027/2028 soll die Schule ihren Betrieb aufnehmen.“ Dazu der Abschnitt „Klage
    führt zu Verzögerungen - Beginn des Schulbetriebs erst zum Schuljahr 2027/2028“, in dem die Beschlüsse des
    VG Gelsenkirchen vom 05.03.2025 und des OVG vom 26.03.2025 genannt werden. Der Satz ist also frühestens Ende März 2025
    entstanden. Wann genau, ist ungeklärt; die älteste Archivkopie stammt vom 08.03.2026.

Dazu ein Befund, der für das Buch wichtiger ist: **Die erste Ankündigung lautete auf ein Jahr früher.** Die Pressemeldung
vom 20.11.2024 (`pressemeldung_1546565`, live abgerufen 04.10.2026) sagt: „Damit die städtische Schule möglichst schon
zum Schuljahr 2026/2027 bezugsfertig ist, beginnen nun die vorbereitenden Maßnahmen“. Der Termin ist dann nach der
Klage auf 2027/2028 gerutscht. Am 08.07.2026 hat der Rat die Gründung zum 1. August 2027 beschlossen
(`pressemeldung_1599445`: „Die neue Grundschule soll zum 1. August 2027 ihren Betrieb aufnehmen“).

**Vorschlag (Frage an Felix, nichts geändert):** In 013 `quelle` auf die Projektseite setzen und `zitat` wörtlich
übernehmen. `gesagt_am` bleibt 2025-05-02 mit dem Vermerk „Satz auf der Projektseite, Entstehungsdatum ungeklärt,
frühestens 26.03.2025“. Der Vorhersage-Abstand bleibt dabei etwa gleich. Optional kommt eine neue Wette aus der
Meldung vom 20.11.2024 dazu: „Bezugsfertig zum Schuljahr 2026/2027?“ Ihr Ausgang wäre NEIN (Schulbeginn 2027/2028 laut
Ratsbeschluss 08.07.2026). Das wäre eine schon gebrochene Ankündigung, die im Buch bisher fehlt.

## Befund B: Bei essen-2025-024 (Rechenzentrum) war keine Entscheidung über den Standort angekündigt

Wortlaut der Pressemeldung vom 19.09.2025:

> „Die Entscheidung über den Standort ist in der finalen Abstimmungsphase. Im 1. Quartal 2026 soll der Rat der Stadt
> Essen eine Grundsatzentscheidung für den Neubau treffen.“

Das Zitat der Wette („soll im 1. Quartal 2026 die Ratsentscheidung [über den Standort] fallen“) vermischt die beiden
Sätze. Die Wette ist aufgelöst (JA, Rat 11.02.2026, TOP 54 „Konzeptionierung eines Rechenzentrums“). Der Vermerk vom
30.08. hält fest, dass Streit möglich ist, weil der Titel „Konzeptionierung“ und nicht „Standort“ lautet.
**Mit dem richtigen Wortlaut fällt dieser Vorbehalt weg:** Angekündigt war eine Grundsatzentscheidung über den Neubau,
und genau dazu hat der Rat beschlossen. Am Ausgang ändert sich nichts.

**Vorschlag (Frage an Felix, nichts geändert):** In 024 `zitat` und `frage` auf „Grundsatzentscheidung für den Neubau“
setzen und dazu einen Vermerk eintragen. Der Ausgang bleibt JA.

## Befund C: essen-2025-023 (ESSEN 51) ist eine bedingte Aussage des Investors

Wortlaut im e-Magazin vom 22.10.2025: „Vorbehaltlich des Ratbeschlusses zum Bebauungsplan könnten die Bauarbeiten 2026
beginnen und die ersten Wohnhäuser ESSEN 51. im Jahr 2027 fertiggestellt werden.“ Dazu eine Bildunterschrift: „Die
ersten Wohngebäude sollen 2027 einzugsbereit sein“, und Thelen selbst: „Die ersten fertigen Wohnhäuser sieht er ab 2027
auf dem Gelände.“ `gesagt_von` nennt die Thelen-Gruppe schon. Die Bedingung (Ratsbeschluss Bebauungsplan) fehlt aber
im Zitat. **Vorschlag:** Die Bedingung als Vermerk eintragen. Falls der Bebauungsplan bis 2027 nicht beschlossen ist,
hat die Stadt nichts gebrochen; das muss bei der Auflösung bedacht werden.

Verbleibend „kein Treffer“: Bonn 17.
