# Buch „KI gegen KI" — Kandidaten, recherchiert am 03.10.2026

Status: **Entwurf, nichts angelegt, nichts committet.** Vorschlag für ein neues Buch über Anbieter von
KI-Allzweckmodellen nach FORMAT.md v1. Recherche, Abruf und Wortlautprüfung: Claude, 03.10.2026, ohne
Rückfrage. Die Auswahl der Wetten trifft Felix.

**Interessenkonflikt, vorab:** Der „Computer", der hier schätzt, ist Claude, ein Modell von Anthropic.
Anthropic steht selbst auf der Liste (ki-2026-003, -004), alle anderen sind Wettbewerber. Das gehört als
Vermerk in jede Wette dieses Buchs, mindestens in die zwei Anthropic-Wetten. Eine Alternative wäre, die
Computer-Schätzung in diesem Buch von einem anderen Modell hinterlegen zu lassen (z. B. qwen3:4b lokal).

---

## Schritt 1 — Auswahlliste: gefunden

**Quelle:** https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
(Europäische Kommission, „The General-Purpose AI Code of Practice"; Seitenstand laut Fuß „Last update
31 July 2026"; abgerufen 03.10.2026 per `curl -sL --compressed` mit Browser-User-Agent, HTTP 200.)

Wortlaut-Auszug (normalisierter Seitentext):

> „The code was published on July 10, 2025 . […] Signatories of the code of practice Some signatories may
> not appear immediately, but we are making sure to continuously update the list as signatures are
> confirmed. AI Studio Delta Aleph Alpha Almawave Amazon Anthropic Black Forest Labs Bria AI Cohere Domyn
> Dweve Fastweb Google IBM LINAGORA Microsoft Mistral AI Open Hippo OpenAI Pleias ServiceNow WRITER In
> addition, xAI signed up to the Safety and Security Chapter; this means that it will have to demonstrate
> compliance with the AI Act's obligations concerning transparency and copyright via alternative adequate
> means."

**Vollständige Unterzeichnerliste (21 Vollunterzeichner, Reihenfolge wie auf der Seite):**
AI Studio Delta, Aleph Alpha, Almawave, Amazon, Anthropic, Black Forest Labs, Bria AI, Cohere, Domyn,
Dweve, Fastweb, Google, IBM, LINAGORA, Microsoft, Mistral AI, Open Hippo, OpenAI, Pleias, ServiceNow,
WRITER.
**Nur Teilkapitel:** xAI (nur Kapitel „Safety and Security"). xAI firmiert inzwischen als „SpaceXAI"
(xAI-Newsroom: „xAI joins SpaceX", 02.02.2026).
Nicht auf der Liste: u. a. Meta (hat nicht unterzeichnet).

**Liste nach Art. 52 Abs. 6 AI Act (GPAI-Modelle mit systemischem Risiko): nicht auffindbar.**
Geprüft am 03.10.2026: die Code-Seite, die Q&A „General-Purpose AI Models in the AI Act" (Stand 09.09.2025),
„Guidelines on obligations for General-Purpose AI providers", „The enforcement framework of the AI Act",
die AI-Office-Seite und eine Websuche. Gefunden nur die Pflicht selbst und das Benennungsverfahren
(„The Commission can designate a model as a general-purpose AI model with systemic risk …"), keine
veröffentlichte Modellliste. → **ungeklärt**, ob die Kommission sie an anderer Stelle führt.

## Schritt 2 — Auswahl

Raus, weil DMA-Gatekeeper (eigenes Buch): **Amazon, Google, Microsoft.**
(Apple, Booking, ByteDance, Meta stehen nicht auf der Liste.)

Im Buch, nach der Liste: AI Studio Delta, Aleph Alpha, Almawave, Anthropic, Black Forest Labs, Bria AI,
Cohere, Domyn, Dweve, Fastweb, IBM, LINAGORA, Mistral AI, Open Hippo, OpenAI, Pleias, ServiceNow, WRITER;
dazu xAI/SpaceXAI mit Vermerk „nur Safety & Security".

Ergebnis Schritt 3: Kandidaten für **6 Anbieter** (OpenAI, Anthropic, Cohere, Aleph Alpha, IBM,
ServiceNow), dazu eine Reserve von OpenAI. Für die übrigen fand sich keine prüfbare Aussage im Fenster
(siehe „Verworfen").

---

## Schritt 3 — Kandidaten (9 + 1 Reserve)

Prüfweg für alle: Quelle am 03.10.2026 zwischen 21:47 und 21:48 Uhr per
`curl -sL --compressed -A "<Chrome-UA>"` neu abgerufen; Text normalisiert (script/style/noscript und
Kommentare entfernt, Tags → Leerzeichen, `html.unescape`, typografische Anführungszeichen/Striche/geschützte
Leerzeichen/weiche Trennstriche ersetzt, Whitespace zusammengefasst; PDF über `pdftotext -layout`), dann
in Python `norm(zitat) in text`. Ergebnis jeweils **True** (auch ohne Normalisierung des Zitats True).

### ki-2026-001 — OpenAI: Stargate UAE, 200 MW live in 2026

```yaml
id: ki-2026-001
institution: OpenAI
gesagt_von: OpenAI, Global Affairs / „Introducing Stargate UAE"
gesagt_am: 2025-05-22
quelle: https://openai.com/index/introducing-stargate-uae/
zitat: "A 1GW Stargate UAE cluster in Abu Dhabi with 200MW expected to go live in 2026"
frage: Sind bis zum 31.12.2026 mindestens 200 MW des Stargate-UAE-Clusters in Abu Dhabi in Betrieb gegangen?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: OpenAI
    wert: 0.80
    hinterlegt_am: 2025-05-22
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „200MW expected to go live in 2026" → Ja/Nein am 31.12.2026. Ja nur, wenn eine
öffentliche Quelle (OpenAI, G42, Oracle oder Betreiber) sagt, dass ≥ 200 MW IT-Last im Betrieb sind
(„live", „operational", Kunden-/Trainingsbetrieb). Ein erster Teilabschnitt unter 200 MW, „Inbetriebnahme
begonnen" oder „mechanisch fertig" = Nein. Vorbehalt „expected" → `voraussichtlich` 0,80.

**Begründung Computer (0,55):** Der Bau läuft sichtbar, Presseberichte sprechen von einer ersten Phase,
die im Februar 2026 „commissioned" wurde, und von „on track for 2026". Rechenzentren dieser Größe rutschen
aber häufig um ein bis zwei Quartale, gerade bei Strom- und Kühlungsabnahme, und „200 MW live" muss
ausdrücklich belegt werden. Knapp über der Hälfte.

**Kontext:** Erste Partnerschaft aus „OpenAI for Countries"; Partner G42, Oracle, NVIDIA, Cisco, SoftBank.
Stand 03.10.2026 laut Medien (nicht amtlich): erste Phase im Bau bzw. in Inbetriebnahme. Ob schon 200 MW
laufen: ungeklärt.

### ki-2026-002 — OpenAI: „OpenAI for Germany" startet 2026

```yaml
id: ki-2026-002
institution: OpenAI
gesagt_von: OpenAI, Global Affairs / „OpenAI for Germany"
gesagt_am: 2025-09-24
quelle: https://openai.com/global-affairs/openai-for-germany/
zitat: "Through this collaboration, planned for launch in 2026, OpenAI, SAP and Microsoft will focus on helping employees in German governments, administrations and research institutions accelerate their daily work"
frage: Ist „OpenAI for Germany" bis zum 31.12.2026 gestartet, d. h. für mindestens eine deutsche Behörde, Verwaltung oder Forschungseinrichtung im Regelbetrieb verfügbar?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: OpenAI
    wert: 0.80
    hinterlegt_am: 2025-09-24
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „planned for launch in 2026" → Start bis 31.12.2026. Ja, wenn OpenAI, SAP/Delos Cloud
oder ein öffentlicher Kunde den Start (allgemeine Verfügbarkeit oder Produktivbetrieb bei mindestens einer
öffentlichen Stelle) belegt. Pilot, „Preview" oder reine Ankündigung eines Termins = Nein.

**Begründung Computer (0,55):** Das Angebot hängt an drei Parteien (OpenAI, SAP/Delos, Microsoft Azure)
und an deutscher Sicherheitsfreigabe für Verwaltungen; solche Freigaben dauern erfahrungsgemäß länger.
Andererseits ist ein symbolischer Start mit einem ersten Kunden bis Jahresende leicht zu inszenieren.

**Kontext:** Betrieb über die SAP-Tochter Delos Cloud auf Azure-Technik; SAP plant laut Medien 4.000 GPUs.
Stand 03.10.2026: kein Startbeleg gefunden → ungeklärt.

### ki-2026-003 — Anthropic: 10.000 Frontier Deployed Engineers bis Ende 2027

```yaml
id: ki-2026-003
institution: Anthropic
gesagt_von: Anthropic, Newsroom / „Anthropic invests $100 million to train 10,000 engineers and tackle the enterprise AI talent gap"
gesagt_am: 2026-10-02
quelle: https://www.anthropic.com/news/claude-frontier-academy
zitat: "Backed by a $100 million commitment, Anthropic aims to train 10,000 Frontier Deployed Engineers (FDEs) by the end of 2027."
frage: Hat Anthropic bis zum 31.12.2027 mindestens 10.000 Frontier Deployed Engineers über die Claude Frontier Academy ausgebildet?
typ: ja_nein
pruefung_am: 2028-01-01
prognosen:
  - von: Anthropic
    wert: 0.80
    hinterlegt_am: 2026-10-02
    art: voraussichtlich
  - von: Computer
    wert: 0.30
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „aims to train 10,000 … by the end of 2027" → Ja/Nein am 31.12.2027. Ja, wenn eine
Anthropic-Quelle (oder ein Partner mit Zahl) ≥ 10.000 Engineers nennt, die das Programm abgeschlossen
haben (Abzeichen „Claude Frontier Deployed Engineer" oder ausdrücklich „trained"). Angemeldete, nominierte
oder laufende Teilnehmer zählen nicht. Vorbehalt „aims" → `voraussichtlich` 0,80.

**Begründung Computer (0,30):** Das Programm dauert mehrere Tage Präsenz plus 12 Wochen Residency, die
ersten Abschlüsse kommen laut Quelle erst „early 2027", es gibt drei Standorte und die Teilnahme läuft
über Nominierung. 10.000 Absolventen in rund einem Jahr wäre ein sehr steiler Anlauf. Dazu kommt das
Belegrisiko: Ohne veröffentlichte Zahl verfällt die Wette.

**Kontext:** Veröffentlicht am Vortag der Recherche. Erste Kohorten in San Francisco, New York, London
(u. a. Accenture, Bain, Capgemini, CBA, Deloitte, McKinsey, Morgan Stanley, Novo Nordisk).
**Vermerk Interessenkonflikt:** Der Computer ist ein Anthropic-Modell.

### ki-2026-004 — Anthropic: über 1 GW TPU-Kapazität in 2026

```yaml
id: ki-2026-004
institution: Anthropic
gesagt_von: Anthropic, Newsroom / „Expanding our use of Google Cloud TPUs and Services"
gesagt_am: 2025-10-23
quelle: https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services
zitat: "The expansion is worth tens of billions of dollars and is expected to bring well over a gigawatt of capacity online in 2026."
frage: Ist durch die Google-TPU-Erweiterung bis zum 31.12.2026 mehr als 1 Gigawatt Rechenkapazität für Anthropic in Betrieb gegangen?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: Anthropic
    wert: 0.80
    hinterlegt_am: 2025-10-23
    art: voraussichtlich
  - von: Computer
    wert: 0.45
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „well over a gigawatt … online in 2026" → Ja, wenn Anthropic oder Google öffentlich
bestätigt, dass bis 31.12.2026 > 1 GW aus dieser Vereinbarung in Betrieb ist. „Well over" wird nicht
zusätzlich bewertet; die Schwelle ist > 1 GW. Vorbehalt „expected" → `voraussichtlich` 0,80.

**Begründung Computer (0,45):** In der Sache ist das plausibel, weil Google die TPU-Kapazität schnell
ausbaut. Kapazitätszahlen je Kunde werden aber selten öffentlich bestätigt. Das Hauptrisiko ist deshalb
„verfallen" mangels Beleg, nicht ein Nein.

**Kontext:** Bis zu 1 Mio. TPUs, „tens of billions of dollars". Parallel Amazon (Project Rainier) und
NVIDIA. **Vermerk Interessenkonflikt:** wie ki-2026-003. Auflösbarkeit schwach — im Zweifel weglassen.

### ki-2026-005 — Cohere: Zusammenschluss mit Aleph Alpha noch 2026 vollzogen

```yaml
id: ki-2026-005
institution: Cohere
gesagt_von: Cohere, Blog/Newsroom / „Cohere and Aleph Alpha sign agreement to become the first transatlantic sovereign AI solution"
gesagt_am: 2026-09-16
quelle: https://cohere.com/blog/cohere-and-aleph-alpha-sign-agreement
zitat: "Both appointments are contingent on completion of the transaction, which remains subject to regulatory approvals and is expected to close later this year"
frage: Ist der Zusammenschluss von Cohere und Aleph Alpha bis zum 31.12.2026 vollzogen (Closing)?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: Cohere
    wert: 0.80
    hinterlegt_am: 2026-09-16
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „expected to close later this year" → Closing bis 31.12.2026. Ja, wenn Cohere oder Aleph
Alpha den Vollzug meldet (z. B. „completed", „closed", Ernennungen Scheer/Weinbach wirksam). Nur
Genehmigungen ohne Vollzug = Nein.

**Begründung Computer (0,55):** Ein kanadischer Erwerber übernimmt einen deutschen KI-Entwickler mit
Behördenkunden. Das dürfte eine Investitionsprüfung nach AWV auslösen (KI ist ein ausdrücklich genannter
Sektor), in Phase 1 zwei Monate ab Kenntnis, in Phase 2 deutlich länger. 3,5 Monate ab Signing sind
machbar, aber eng.

**Kontext:** Geplant seit 24.04.2026; Schwarz-Gruppe 500 Mio. € in Coheres Series E; künftig Doppelsitz
Berlin/Toronto, über 1.000 Beschäftigte. Eng gekoppelt mit ki-2026-006 (gleiches Ereignis, andere
Institution) — beide anlegen oder nur eine.

### ki-2026-006 — Aleph Alpha: Transaktion „voraussichtlich noch in diesem Jahr vollzogen"

```yaml
id: ki-2026-006
institution: Aleph Alpha
gesagt_von: Aleph Alpha, Newsroom / „Cohere und Aleph Alpha unterzeichnen Vereinbarung und schaffen die erste transatlantische souveräne KI-Lösung"
gesagt_am: 2026-09-16
quelle: https://aleph-alpha.com/news/cohere-vereinbarung-transatlantische-souveraene-ki/
zitat: "Beide Ernennungen stehen unter dem Vorbehalt des Abschlusses der Transaktion, die weiterhin behördlicher Genehmigungen bedarf und voraussichtlich noch in diesem Jahr vollzogen wird."
frage: Ist die Transaktion zwischen Aleph Alpha und Cohere bis zum 31.12.2026 vollzogen?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: Aleph Alpha
    wert: 0.80
    hinterlegt_am: 2026-09-16
    art: voraussichtlich
  - von: Computer
    wert: 0.55
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** wie ki-2026-005. „voraussichtlich" → `voraussichtlich` 0,80.

**Begründung Computer (0,55):** Gleiche Begründung wie ki-2026-005. Die zwei Wetten sind nicht
unabhängig und dürfen in der Auswertung nicht als zwei getrennte Belege gelesen werden.

**Kontext:** Seit 28.09.2026 ist Ilhan Scheer alleiniger CEO (Co-CEO Reto Spörri ausgeschieden,
Aleph-Alpha-Newsroom). Laut derselben Meldung rund 200 Beschäftigte an vier Standorten in Deutschland.

### ki-2026-007 — IBM: B300-Inferenzcluster für Together AI im Q1 2027

```yaml
id: ki-2026-007
institution: IBM
gesagt_von: IBM Newsroom / „IBM and Together AI Sign Multi-Year Agreement to Scale Open-Source AI Inference with NVIDIA AI Infrastructure on IBM Cloud"
gesagt_am: 2026-08-11
quelle: https://newsroom.ibm.com/2026-08-11-IBM-and-Together-AI-Sign-Multi-Year-Agreement-to-Scale-Open-Source-AI-Inference-with-NVIDIA-AI-Infrastructure-on-IBM-Cloud
zitat: "Under a multi-year $240M agreement between IBM and Together AI, IBM is positioned to deploy a large cluster of NVIDIA HGX B300 systems on IBM Cloud with expected availability in Q1 2027."
frage: Ist der NVIDIA-HGX-B300-Cluster für Together AI auf IBM Cloud bis zum 31.03.2027 verfügbar?
typ: ja_nein
pruefung_am: 2027-04-01
prognosen:
  - von: IBM
    wert: 0.80
    hinterlegt_am: 2026-08-11
    art: voraussichtlich
  - von: Computer
    wert: 0.50
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „expected availability in Q1 2027" → Ja, wenn IBM, Together AI oder NVIDIA bis
31.03.2027 die Verfügbarkeit bzw. den Produktivbetrieb des Clusters meldet. Teilverfügbarkeit („first
racks", „early access") = Nein.

**Begründung Computer (0,50):** B300-Lieferungen sind 2026 knapp, und die Termine großer GPU-Cluster
rutschen oft. Zugleich ist Q1 2027 von August 2026 aus kein aggressiver Plan. Unsicher ist auch, ob jemand
die Verfügbarkeit überhaupt öffentlich meldet.

**Kontext:** Volumen 240 Mio. $ über mehrere Jahre; laut IBM der erste dedizierte Großcluster für Inferenz
auf IBM Cloud.

### ki-2026-008 — IBM: Quantum System Two für die Schweiz bis Ende 2026

```yaml
id: ki-2026-008
institution: IBM
gesagt_von: IBM Newsroom / „IBM, Lockheed Martin Announce Swiss Quantum Innovation Hub at ETH Zurich, Anchored by Switzerland's First IBM Quantum Computer"
gesagt_am: 2026-09-10
quelle: https://newsroom.ibm.com/2026-09-10-ibm,-lockheed-martin-announce-swiss-quantum-innovation-hub-at-eth-zurich,-anchored-by-switzerlands-first-ibm-quantum-computer
zitat: "Additionally, upon the system's deployment by the end of 2026, ETH Zurich will provide organizations with access to Switzerland's own dedicated IBM Quantum System Two."
frage: Ist das IBM Quantum System Two für den Schweizer Quantum-Hub (Standort CSCS Lugano) bis zum 31.12.2026 aufgestellt und in Betrieb?
typ: ja_nein
pruefung_am: 2027-01-01
prognosen:
  - von: IBM
    wert: 1.00
    hinterlegt_am: 2026-09-10
    art: angekuendigt
  - von: Computer
    wert: 0.40
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „deployment by the end of 2026" ohne Vorbehalt → `angekuendigt` 1,00. Ja, wenn IBM, ETH
Zürich oder CSCS bis 31.12.2026 Aufstellung und Inbetriebnahme melden (z. B. Einweihung, erste Nutzer
auf dem lokalen System). Nur Lieferung oder Baubeginn = Nein.

**Begründung Computer (0,40):** Zwischen Ankündigung (10.09.) und Frist liegen nur 3,5 Monate. Frühere
System-Two-Installationen außerhalb der USA brauchten von der Ankündigung bis zur Einweihung deutlich
länger (Erfahrungswert, hier nicht einzeln belegt). Die Formulierung „upon the system's deployment" klingt
eher nach Plan als nach fast fertig.

**Kontext:** Offset-Vereinbarung von Lockheed Martin mit armasuisse; der Prozessor soll ein IBM Quantum
Nighthawk sein. Kein KI-Thema im engeren Sinn, aber eine harte, datierte Aussage des Anbieters.

### ki-2026-009 — ServiceNow: 240.000 Lernende im Vereinigten Königreich bis 2027

```yaml
id: ki-2026-009
institution: ServiceNow
gesagt_von: ServiceNow, News Release (Investor Relations, Q4-CDN) / „ServiceNow pledges $1.5bn investment into UK business over five years"
gesagt_am: 2024-10-14
quelle: https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-pledges-1-5bn-investment-into-UK-business-over-five-years-10-14-2024-traffic-2024.pdf
zitat: "ServiceNow has committed to reaching 240,000 UK learners by 2027"
frage: Hat ServiceNow bis zum 31.12.2027 mindestens 240.000 Lernende im Vereinigten Königreich erreicht?
typ: ja_nein
pruefung_am: 2028-01-01
prognosen:
  - von: ServiceNow
    wert: 1.00
    hinterlegt_am: 2024-10-14
    art: angekuendigt
  - von: Computer
    wert: 0.40
    hinterlegt_am: 2026-10-03
    art: geschaetzt
```

**Übersetzung:** „has committed to reaching … by 2027" → `angekuendigt` 1,00, Stichtag 31.12.2027. Ja,
wenn eine ServiceNow-Quelle ≥ 240.000 erreichte UK-Lernende nennt (Definition „learner" nach ServiceNow).

**Begründung Computer (0,40):** Bei der Zusage waren es laut derselben Quelle „nearly 30,000"; nötig ist
also etwa das Achtfache in drei Jahren. Online-Lernplattformen zählen großzügig, das ist erreichbar.
Ob ServiceNow eine UK-Einzelzahl veröffentlicht, ist offen; das Verfallsrisiko ist hoch.

**Kontext:** Teil einer Zusage über 1,5 Mrd. $ in fünf Jahren (bis 2029, außerhalb des Fensters). Die
Website servicenow.com war am 03.10.2026 per curl nicht erreichbar (Verbindungsabbruch). Die Quelle ist das
PDF auf dem IR-Host von ServiceNow (newsroom.servicenow.com verweist auf denselben Q4-Speicher).

### Reserve (über dem Limit von 2 je Anbieter) — OpenAI: Stargate Norway, 100.000 GPUs bis Ende 2026

- quelle: https://openai.com/index/introducing-stargate-norway/ (OpenAI, 2025-07-31)
- zitat: "The facility will target to deliver 100,000 NVIDIA GPUs by the end of 2026" — Prüfung True
- Frage wäre: Sind in Stargate Norway (Kvandal bei Narvik) bis 31.12.2026 ≥ 100.000 NVIDIA-GPUs geliefert?
  `voraussichtlich` 0,80 („target").
- Kontext: Eine Websuche liefert Hinweise, dass sich die kommerzielle Zuteilung des Standorts geändert hat
  (nicht amtlich geprüft) → ungeklärt. Nur nachrücken, wenn eine der OpenAI-Wetten wegfällt.

---

## Verworfen

| Anbieter | Aussage / Fund | Grund |
|---|---|---|
| Mistral AI | „Scheduled to open in Q3 2026" (Rechenzentrum Les Ulis, 10 MW; mistral.ai/news/ai-now-summit-2026, 28.05.2026) | Stichtag 30.09.2026, vor dem Fenster |
| Mistral AI | „Mistral will build one gigawatt of European compute capacity by 2030" (hallo-deutschland, 28.09.2026) bzw. „up to 1 GW of capacity by 2030" (11.08.2026) | Stichtag 2030, nach dem Fenster |
| Mistral AI | Rechenzentrum Borlänge/Schweden „ab 2027", 1,2 Mrd. € | nur Medien (Bloomberg, CNBC u. a.); auf mistral.ai keine eigene Meldung gefunden, Compute-Seite nennt nur „Sweden site (EcoDataCenter) in motion" ohne Datum |
| Mistral AI | „opening in the coming months an office in Germany" (ki-fur-deutschland, 19.11.2025) | kein Datum, inzwischen erledigt (Hub München 28.09.2026) |
| OpenAI | „invest $500 billion over the next four years" (Stargate, 21.01.2025) | Frist Januar 2029, nach dem Fenster |
| OpenAI | Broadcom 10 GW „to complete by end of 2029" (13.10.2025) | nach dem Fenster |
| OpenAI | AMD „first 1 gigawatt deployment … set to begin in the second half of 2026" (06.10.2025) | „begin" kaum prüfbar; Limit 2 je Anbieter |
| OpenAI | Stargate UK „offtake up to 8,000 GPUs in Q1 2026" (16.09.2025) | Stichtag vorbei, zudem „explore" |
| Anthropic | 50 Mrd. $ USA, „sites coming online throughout 2026" (12.11.2025) | keine Schwelle, nicht eindeutig auflösbar |
| IBM | „first cases of verified quantum advantage … by the end of 2026" (12.11.2025) | praktisch schon entschieden: IBM meldet am 30.07.2026 drei Quantum-Advantage-Demonstrationen; als Wette wertlos |
| IBM | Nighthawk „up to 7,500 gates by the end of 2026", „up to 10,000 gates in 2027" | „up to" = Obergrenze, keine prüfbare Zusage |
| IBM | Gesamtjahr 2026 „constant currency revenue growth in the range of four-to-five percent" (Q2-Ergebnis, 22.07.2026) | möglicher Kandidat, aber Limit 2 je Anbieter; Beleg erst mit Q4-Zahlen Ende Januar 2027 |
| IBM | 150 Mrd. $ USA „over the next five years" (28.04.2025) | Frist 2030 |
| ServiceNow | Kanada: 110 Mio. CAD, „approximately 100 new … jobs" (08.12.2025) | kein Datum |
| Cohere | London-Büro, Ausbau „due to complete later this year" (15.06.2026) | trivial, keine Zahl zum Prüfen; Kandidat 005 ist stärker |
| xAI / SpaceXAI | Newsroom x.ai durchgesehen (Series E, Saudi-Arabien, Anthropic-Compute, SpaceX) | keine Aussage mit Zahl und Datum im Fenster; nur Teilunterzeichner |
| WRITER, Black Forest Labs, Pleias, LINAGORA, Dweve, Bria AI | Startseiten bzw. Blog-Übersicht nach Jahreszahlen 2026–2028 durchsucht | nichts Prüfbares gefunden (Kurzprüfung, keine Tiefenrecherche) |
| Almawave | almawave.com liefert nur eine Weiterleitung auf Almaviva (4 KB); Websuche: kein Plan 2026–2028 mit Zielwerten | nichts Prüfbares gefunden |
| Domyn | Startseite ohne Datumsaussage; Colosseum-Supercomputer laut Medien „2025" | Frist vorbei, nur Medien |
| Fastweb | nur Konzern-/Telekomaussagen (Swisscom-Dividende 2027), keine KI-Aussage mit Datum im Fenster | nicht passend |
| AI Studio Delta, Open Hippo | nicht recherchiert (keine Quelle gefunden) | ungeklärt |

**Nicht prüfbar (Bot-Sperre):** keine der verwendeten Quellen. servicenow.com brach die Verbindung ab
(curl-Code 000); umgangen über den IR-Host. openai.com/index/stargate-norway/ lieferte 403, das war aber
eine falsche URL; die richtige (/introducing-stargate-norway/) ging mit 200.

## Ungeklärt

1. **Liste nach Art. 52 Abs. 6 AI Act**: auf digital-strategy.ec.europa.eu nicht gefunden. Ob die
   Kommission sie anderswo führt (z. B. AI-Office-Register), ist offen. Für die Auswahl reicht die
   Unterzeichnerliste.
2. **Wiederkehrende Auswahl:** Die Code-Seite ändert sich („continuously update the list"). Vorschlag:
   Seite mit Datum archivieren (Wayback war am 03.10. per curl gedrosselt, HTTP 429) und im BUCH.md die
   Liste mit Stichtag 31.07.2026 einfrieren.
3. **Stand heute** bei 001 (Stargate UAE live?) und 002 (OpenAI for Germany gestartet?): nur Medien
   gesichtet, kein amtlicher Stand. Wenn schon erledigt, entfällt die Wette.
4. **005/006 gekoppelt:** eine oder beide anlegen? Entscheidung Felix.
5. **Verfallsrisiko** hoch bei 003, 004, 009 (Zahlen werden vielleicht nie veröffentlicht). Der Abschnitt
   „Rechenschaft" (§3.3) fängt das auf. Wer nichts Prüfbares sagt, steht dort.
6. **Interessenkonflikt Computer = Claude:** Vermerk in jeder Wette oder Schätzung durch ein anderes
   Modell. Entscheidung Felix.
7. Geprüft wurde, ob die Zitate wörtlich in der Quelle stehen, nicht, ob die Aussage richtig ist.
