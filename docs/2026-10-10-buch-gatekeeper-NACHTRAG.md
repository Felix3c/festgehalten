# Buch „Gatekeeper gegen Gatekeeper“ — Nachtrag, recherchiert am 10.10.2026

Status: drei neue Wetten (gatekeeper-2026-011 bis -013) lokal auf Zweig `buch-gatekeeper-2`, **nicht gepusht**
(Push erst nach „steht“). Recherche: Unteragent des Dauerlaufs; Wortlautprüfung und Anlage: Claude, 10.10.2026.
Regeln wie am 03.10. (`docs/2026-10-03-buch-gatekeeper-KANDIDATEN.md`): nur eigene Aussagen der Gatekeeper,
Zahl und Datum, Frist zwischen 01.11.2026 und 31.12.2027, höchstens zwei je Unternehmen.

## Prüfweg

Quellen am 10.10.2026 gegen 14:57 per `curl -sL --compressed` mit Browser-User-Agent abgerufen (HTTP 200).
Text normalisiert (script/style/noscript und Kommentare entfernt, Tags → Leerzeichen, `html.unescape`,
typografische Anführungszeichen und Apostrophe ersetzt, Whitespace zusammengefasst), dann `zitat in text`:
alle drei **True**. Wayback-Kopie per `web.archive.org/save` angelegt, die Kopie (`id_`) abgerufen und dasselbe
geprüft: alle drei **True**. Datum aus `article:published_time` bzw. `datePublished` der Seite.

| Wette | Unternehmen | Quelle (Datum) | Archiv |
|---|---|---|---|
| gatekeeper-2026-011 | Amazon | aboutamazon.com, Proteus in Europa (04.06.2026) | web.archive.org/web/20261010125704/… |
| gatekeeper-2026-012 | Meta | about.fb.com, Meta VR Glasses (23.09.2026) | web.archive.org/web/20261010125843/… |
| gatekeeper-2026-013 | Alphabet | blog.google, Finnland/Kajaani 94 MW (09.09.2026) | web.archive.org/web/20261010125947/… |

Schwächen, offen benannt: 011 „planned“, ein Nein hinterlässt kein Dokument (Nein mangels Beleg). 012 ist
US-bezogen, ein EU-Start ist ungeklärt; „Spring“ ist als 20.06.2027 übersetzt. 013 „expected“, Google
„ermöglicht“ den Speicher nur, Betreiber ungeklärt.

## ByteDance: weiter kein Kandidat

Nachgesucht im TikTok-Newsroom (EN/DE/FR), DSA-Berichten, Transparenzzentrum, bytedance.com und per Websuche.
Lahti (08.04.2026) nur „Once operational“ ohne Datum; Project Clover „over the next ten years“; Shop-Ausweitung
(28.05.2026) Start 15.06.; „Sell across EU“ 19.10.2026 vor dem Fenster und nur aus Drittquellen; DSA-Bericht 7,
Desinformations-Kodex-Bericht 7, Datenschutztag 2026, Altersprüfung (16.01.2026): nichts mit Zahl und Frist.
Die 2027-Daten für Kouvola/Lahti stehen weiter nur in Drittberichten.

## AI-Act-Liste (Art. 52 Abs. 6)

Am 10.10.2026 erneut gesucht: weiter keine veröffentlichte Liste von GPAI-Modellen mit systemischem Risiko gefunden.

## Verworfen

| Unternehmen · Fund | Grund |
|---|---|
| Amazon · STARK „to 15 sites across Europe by 2027“ (04.06.2026, wörtlich) | „by 2027“ offen (Anfang/Ende), keine öffentliche Standortzählung. |
| Amazon · Dobromierz (PL) „In 2026, Amazon will open…“ | Laut Presse im September 2026 schon eröffnet. |
| Amazon · Spanien, 500.000 Lernende in KI/Digitales bis 2027 | Zahl öffentlich nicht prüfbar (Reserve). |
| Amazon · AWS Aragón Wasser „hope to double by the end of 2026“ | „hope“ zu weich. |
| Amazon · Investitionen FR/IE/PL | Zeitraum 2026–2028 oder ohne Stichtag. |
| Meta · „more than 100 different options for AI glasses“ bis Ende 2026 (24.09.2026, wörtlich) | „options“ undefiniert, eigene Zählung wäre angreifbar. |
| Meta · Petal-Kabel | 2029. |
| Meta · Ray-Ban Display in Deutschland ab 13.10. | Vor dem Fenster. |
| Google · 13 Mrd. € Finnland „over the next two years“ | Endet etwa 09/2028, nach dem Fenster. |
| Google · Verifizierung Finanzwerbung EU „in phases“ | Ohne Datum. |
| Google · Googlebook in Deutschland ab 05.10. | Vor dem Fenster. |
| Booking · Ziel „over 50% of our 2027 bookings … on more sustainable offerings“ (Bericht 2022, wörtlich), zurückgezogen im Bericht 2024 („our 2027 target is no longer applicable“, wörtlich) | Die 2027er Zahlen erscheinen erst etwa April 2028; wettfähig wäre nur „Ziel wieder in Kraft“, praktisch sicher Nein. Eher Beleg eines zurückgenommenen Versprechens als Wette. |
| Microsoft · „200 datacenters by 2027“; NRW-Standorte | Schon am 03.10. verworfen; kein eigenes Datum für NRW. |
| Apple · neue EU-Bedingungen ab 01.10.2026 | Vor dem Fenster; Apple hat schon zwei Wetten. |

## Hinweis zu gatekeeper-2026-006 (Booking)

Die Q2-Mitteilung vom 04.08.2026 (SEC-Anlage) erhöht die Zahl: „Increased our expected annual run-rate savings
through the Transformation Program(1) to approximately $650 million, and expect to realize these run-rate savings
by the end of 2027.“ (wörtlich, Unteragent). Die Wette 006 misst weiter ≥ 600 Mio.; eine Änderung nach Hinterlegung
macht nur der Halter (Frage an Felix).

Arbeitsdateien (Seiten, Bericht des Unteragenten): `~/allein/tmp/gk-1010/` (nicht im Repo).
