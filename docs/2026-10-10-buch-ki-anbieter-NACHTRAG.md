# Buch „KI gegen KI“ — Nachtrag 2, recherchiert am 10.10.2026

Status: eine neue Wette (ki-2026-013, ServiceNow) lokal auf Zweig `buch-ki-3`, **nicht gepusht** (Push erst nach
„steht“). Die Nummer 012 bleibt frei, weil sie am 10.10. verworfen wurde (Frage 229).
Recherche: Unteragent des Dauerlaufs; Wortlautprüfung und Anlage: Claude, 10.10.2026, ohne Rückfrage.
Regeln wie am 03.10. und 09.10.: nur eigene Aussagen der Unternehmen, Zahl und Datum, Frist zwischen 01.11.2026
und 31.12.2028, höchstens zwei je Anbieter. Diesmal gezielt die Anbieter mit freiem Platz: Cohere, ServiceNow,
Mistral AI, Aleph Alpha, Black Forest Labs (OpenAI, Anthropic und IBM haben schon zwei).

## Prüfweg

Quelle am 10.10.2026 gegen 17:40 per `curl -sL --compressed` mit Browser-User-Agent abgerufen (HTTP 200), Text
normalisiert wie am 09.10., `zitat in text`: **True**. Die Seite trägt das Datum 05/06/2025 (US-Format, 06.05.2025).
Wayback `save` antwortete mit HTTP 520, eine ältere Kopie gibt es nicht (`available` leer); in
`recherche/archiv-quellen.csv` als `kein_archiv`, Abgleich in der nächsten Tagesprüfung.

| Wette | Anbieter | Quelle | Archiv |
|---|---|---|---|
| ki-2026-013 | ServiceNow | newsroom.servicenow.com, Pressemitteilung „ServiceNow Introduces ServiceNow University …“ (06.05.2025) | fehlt (HTTP 520) |

Zwischenstand für den Kontext: Pressemitteilung vom 05.05.2026 „ServiceNow University drives career growth with
real-time coaching and simulation“, Satz „ServiceNow University grows to almost 2 million learners, up 80%
year-over-year …“ (Wortlaut True, geprüft vom Unteragenten).

Schwächen, offen benannt: ServiceNow bestimmt selbst, was als „learner“ zählt; „plans“ ist weich; ohne
veröffentlichte Zahl gilt Nein.

## Verworfen

| Unternehmen | Fund | Grund |
|---|---|---|
| ServiceNow | FY-2026-Prognose Subscription-Umsatz 15.760–15.780 Mio. USD (Q2-Meldung 22.07.2026) | Zahl nur in einer Tabelle; Prognose wird mit den Q3-Zahlen am 28.10.2026 voraussichtlich geändert. Möglicher Kandidat, wenn der Halter Finanzprognosen aufnehmen will. |
| ServiceNow | Shift Zero „expected to be available in December 2026“ (04.08.2026) | Keine Zahl. |
| ServiceNow | West Palm Beach „expected to open in 2028“; „850 jobs over the next five years“ | Ohne Zahl bzw. Frist nach 2028. |
| ServiceNow | Indien, 1 Mio. Lernende bis 2027 | Nur in Medienberichten gefunden, keine eigene Seite mit Zitat. |
| ServiceNow | Analyst Day (30 Mrd. USD bis 2030) | Außerhalb des Fensters, nur aus Medien. |
| Mistral AI | „200 MW bis Ende 2027“ | Auf keiner Mistral-Seite (89 News-Beiträge, RSS, Compute, Cloud, About, Sovereign-AI durchsucht); nur Medienberichte. |
| Mistral AI | Schweden/EcoDataCenter 2027 | Eigene Seite nur „in motion“, Zahl nur bei einem Medium. |
| Cohere | Aussagen zu 2027/2028 im Blog (403 Seiten durchsucht) | Durchweg Zahlen Dritter (IDC, Gartner, BCG, Deloitte). |
| Cohere | London-Ausbau, Ottawa „expected to expand“; 6,5 MW mit Bell/Buzz HPC | Ohne Zahl bzw. Frist; die MW-Meldung ist von Bell/Hive, nicht Cohere. |
| Aleph Alpha | Newsroom DE/EN | Außer der Cohere-Transaktion nichts mit Zahl und Frist. |
| Black Forest Labs | 28 Blogposts inkl. Series B | Keine Zukunftsaussage mit Zahl und Datum. |

## Ungeklärt

- Mistral, 200 MW: vielleicht nur per Mail-Pressemitteilung oder LinkedIn verbreitet, nicht auf mistral.ai.
- Cohere/CoreWeave Kanada (240 Mio. CAD Förderung): kein aktueller eigener Cohere-Text mit Frist gefunden.
