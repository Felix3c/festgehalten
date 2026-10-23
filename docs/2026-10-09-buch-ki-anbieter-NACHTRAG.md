# Buch „KI gegen KI“ — Nachtrag, recherchiert am 09.10.2026

Status: drei neue Wetten (ki-2026-010 bis -012) lokal auf Zweig `buch-ki-2`, **nicht gepusht** (Push erst nach
„steht“). **Nachtrag 10.10.2026 (Felix, Frage 229):** 010 und 011 stehen, **012 (Dweve) ist verworfen**,
weil das gerechnete Datum nicht reicht; Wettdatei und Archivzeile entfernt, die Zeilen unten bleiben als Protokoll.
Recherche: Unteragent des Dauerlaufs; Wortlautprüfung und Anlage: Claude, 09.10.2026, ohne Rückfrage.
Regeln wie am 03.10. (`docs/2026-10-03-buch-ki-anbieter-KANDIDATEN.md`): nur eigene Aussagen der Unternehmen, Zahl
und Datum, Frist zwischen 01.11.2026 und 31.12.2028, höchstens zwei je Anbieter. Diesmal gezielt die
Unterzeichner, für die am 03.10. nur die Startseiten durchgesehen waren (Blogs, Presseseiten, Sitemaps).

## Prüfweg

Quellen am 09.10.2026 gegen 14:04 per `curl -sL --compressed` mit Browser-User-Agent abgerufen (HTTP 200).
Text normalisiert (script/style/noscript und Kommentare entfernt, Tags → Leerzeichen, `html.unescape`,
typografische Zeichen ersetzt, Whitespace zusammengefasst), dann `zitat in text`: alle drei **True**. Danach
Wayback-Kopie per `web.archive.org/save` angelegt, die Kopie (`id_`) erneut abgerufen und dasselbe geprüft:
alle drei **True**. Archivlinks in `recherche/archiv-quellen.csv`. Die Numerus-Seite (Runde 10, Zitat im Kontext
von ki-2026-012) war live wörtlich da; ihre Archivkopie kam am 09.10. nicht zustande.

| Wette | Anbieter | Quelle | Archiv |
|---|---|---|---|
| ki-2026-010 | Mistral AI | https://mistral.ai/news/mistral-x-mozilla/ (16.09.2026) | web.archive.org/web/20261009120459/… |
| ki-2026-011 | Domyn | https://www.domyn.com/news/orobix-joins-domyn-to-build-a-european-ai-leader-luca-antiga-named-cto (22.04.2026) | web.archive.org/web/20261009120518/… |
| ki-2026-012 | Dweve | https://dweve.com/open-source/ (ohne Datum, Abruf 09.10.2026) | web.archive.org/web/20261009120610/… |

Schwächen, offen benannt: 010 liegt in der Umsetzung vor allem bei Mozilla, „expected“ ist weich. 011 hängt
daran, dass Domyn (privat) überhaupt eine Zahl nennt; ohne Zahl gilt Nein. 012 hat kein zitiertes Enddatum,
der 04.02.2027 ist aus „fortnightly rounds from 1 October 2026“ und „tenth round“ gerechnet.

## Verworfen

| Unternehmen | Fund | Grund |
|---|---|---|
| Mistral AI | „We will release the weights by the end of the month.“ (Mistral Large 4, 06.10.2026, mistral.ai/news/mistral-large-4/) | Frist 31.10.2026 liegt vor dem Fenster (ab 01.11.2026). Eignet sich als kurze Nebenwette, falls das Fenster gelockert wird. |
| Mistral AI | „Mistral will build one gigawatt of European compute capacity by 2030.“ (hallo-deutschland, 28.09.2026) / „up to 1 GW of capacity by 2030“ (11.08.2026) | 2030 ist zu spät, außerdem „up to“. Schon am 03.10. abgelehnt. |
| Mistral AI | Les Ulis 10 MW „Scheduled to open in Q3 2026“ (AI Now Summit) | Frist ist vorbei, schon abgelehnt. |
| Mistral AI | HUMAIN-Kooperation („hundreds of millions of Euros“, „will explore using HUMAIN's data center“) | Kein Datum, „explore“. |
| Mistral AI | Mistral Compute: „tens of thousands of GPUs, and rapid expansion in the coming years“ | Kein Datum, keine feste Zahl. |
| Domyn | „positioned to deliver nine-figure revenue this year“ (22.04.2026) | Vorsichtig formuliert („positioned“). Domyn ist privat, der Umsatz wird voraussichtlich nicht öffentlich geprüft werden können. |
| Domyn | Europa-Konsortium: Modell mit mehr als 400 Mrd. Parametern, „up to 2.5% of the entire EuroHPC supercomputing capacity for one year“ (19.06.2026) | Keine Frist für das Modell, „up to“. |
| Domyn | NVIDIA: „initial anticipated deployment of nearly 6,000 NVIDIA Blackwell GPUs“ (11.06.2025) | Kein Datum. Colosseum wird laut Domyn-Seite schon betrieben. |
| Dweve | AION „public from 15 October 2026“ | Frist liegt vor dem Fenster. |
| Dweve | Fabric „opens to invited accounts on 1 September 2026“ | Frist ist vorbei. |
| Black Forest Labs | FLUX 3 Launch-Plan: „Over the next few weeks and months“ (Image/Video/Dev open weights), 23.07.2026 | Kein Datum, keine Zahl. Blog, Serie-B-Post, G7-Post und Modellseiten durchsucht (bfl.ai/blog, sitemap). |
| WRITER | Pressemitteilungen 2025–2026 (Series C, Global Expansion, Palmyra X6, Enterprise Brain, Personalien) | Keine Zusage mit Zahl und Frist. Einzige Frist: „general availability expected later this spring“ (AI HQ, 2025), längst vorbei. |
| LINAGORA | Newsroom bis 07.10.2026 (Twake.ai, Mêlée Numérique, „Nearly 200 employees and €20 M in turnover“) | Nur Ist-Zahlen, keine Zusagen mit Frist. |
| Pleias | Blog 2026 (Common Corpus Global, Synth, Sillon/RATP, Nemotron Personas) | Nur „plan to integrate over the next months“ ohne Zahl und Datum. |
| Bria AI | Blog und PR-Newswire-Mitteilungen 2026 (Preise, Integrationen, V-RMBG 3.0) | Keine zukunftsbezogene Aussage mit Zahl und Datum. |
| Fastweb (+Vodafone) | Comunicati stampa (Archiv bis 2025 auf fastweb.it), MIIA, NeXXt AI Factory, AI4I-Abkommen (27.01.2026) | Keine eigene Aussage mit Zahl und Datum im Fenster. Die neuen Mitteilungen liegen auf fastwebvodafone.it und wurden nur per Suche geprüft. |
| Open Hippo | Website und Presseseite | Nur Medienberichte, keine eigenen Zusagen. |

## Ungeklärt

- **Mistral AI, „200 MW bis Ende 2027“:** Viele Medien berichten darüber (u. a. Pulse2, Maddyness, techcentral.ie im März 2026 zur Schuldenfinanzierung über 830 Mio.; Berichte vom August 2026 zu den ECUs). Weder im Mistral-Newsroom (alle 89 Beiträge gelistet) noch auf /cloud, /compute oder /about habe ich den Satz gefunden. Die Finanzierung und Microsoft-Deal (21.07.2026) stehen nicht im Newsroom. Vielleicht gab es eine Pressemitteilung nur per Verteiler oder PDF. Ohne eigene Quelle ist das kein Kandidat. Mit eigener Quelle wäre es der stärkste Mistral-Kandidat (Frist 31.12.2027).
- **Dweve, Runde 1:** Ob Knot und Signum am 01.10.2026 tatsächlich erschienen sind (vielleicht nicht auf GitHub), ist offen.
- **Almawave (Almaviva):** Almawave wurde in Almaviva verschmolzen. Laut Suchergebnis ist Almawave Labs am 09.09.2026 gegründet worden. Das PDF der Pressemitteilung auf almaviva.it leitet auf almavivagroup.com um und war nicht abrufbar, die Website almawave.com ist inzwischen eine Single-Page-App ohne lesbaren Text. Ziele mit Zahl und Frist: ungeklärt.
- **AI Studio Delta:** Keine eigene Website gefunden, nicht geprüft.
- **Domyn, Belegschaft heute:** Ein aktueller Zwischenstand (nach April 2026) ist nicht veröffentlicht.

## Runde 3 (16.10.2026 ~02:50, Dauerlauf Laufend Guard): Newsrooms 09.–16.10. ohne neuen Kandidaten

Geprüft, nur Beiträge seit dem 09.10.2026 (Abruf 16.10.2026):

| Anbieter | Neu seit 09.10. | Ergebnis |
|---|---|---|
| Mistral AI | „Introducing Timestral“ (15.10.2026, mistral.ai/news/timestral/) | Keine Zusage mit Zahl und Datum, nur „A technical report with the full results will follow“. |
| Anthropic | Singapur-Büro + MOU (14.10.), Cyber Mission (08.10.), Genesis Mission (08.10.), Usage Policy (08.10.), unabhängige Evaluatoren (15.10.), US-Wahlen (14.10.) | Singapur ohne Zahl/Datum. Genesis: „committing $150 million over three years“ ist eine Ausgabezusage, die öffentlich nicht nachprüfbar ist (keine Pflicht zur Offenlegung), und läuft bis 2029 → nicht aufgenommen. |
| Cohere | Absichtserklärung Übernahme AISLE (15.10.2026) | Nur „proposed agreement“, kein Closing-Datum, kein Preis → nicht aufgenommen. Wieder prüfen, wenn Cohere ein Closing ankündigt. |
| IBM | Suche ergab keine Mitteilung nach dem 10.09. mit Europa-Bezug | Ungeklärt, ob der Index aktuell ist; Newsroom ohne Browser nicht vollständig lesbar. |
| OpenAI | openai.com antwortet ohne Browser mit HTTP 403; Suche: Berlin-Büro „very soon“ ohne Datum (Handelsblatt, Aug. 2026) | Kein Kandidat aus eigener Quelle. |
| ServiceNow | Pressebereich lädt Liste nur per Skript | Ungeklärt. |

Folge: Buch KI bleibt bei 11 Wetten. Nächste Runde frühestens in 7 Tagen (Pflege-Deckel), dann mit Browser für OpenAI, IBM und ServiceNow.

## Runde 4 (23.10.2026, Dauerlauf Laufend Guard): Newsrooms 16.–23.10. ohne neuen Kandidaten

Geprüft, nur Beiträge seit dem 16.10.2026 (Abruf 23.10.2026 zwischen ca. 08:05 und 08:45 per
`curl -sL --compressed` mit Browser-User-Agent, robots.txt beachtet, 3–10 s Pause je Domain; ServiceNow mit
Crawl-delay 10). Text normalisiert wie oben. Ohne Kandidat gab es nichts wörtlich zu prüfen und keine
Wayback-Kopie anzulegen.

| Anbieter | Neu seit 16.10. | Ergebnis |
|---|---|---|
| Mistral AI | „Voxtral 3“ (20.10.2026), „Mistral Advances AI for Engineering with NVIDIA“ (21.10.2026, mistral.ai/news/mistral-nvidia-ai-for-industrial-engineering/) | Keine Zusage mit Zahl und Datum im Fenster. Einzige Zahl mit Datum: „compute roadmap targeting 1 GW of capacity by 2030“ (zu spät, schon verworfen). |
| Anthropic | Public Benefit Fund (18.10.), Christopher Stubbs im LTBT (21.10.), Agent Skills an die Agentic AI Foundation (22.10.), Gastforscher Life Sciences (22.10.) | Keine Zusage mit Zahl und Datum. Limit 2 ist ohnehin voll. |
| Cohere | Rerank 5 (21.10.), Model Vault mit NVIDIA Confidential Computing, 2 Beiträge (22.10.), Forschung (20.10., 22.10.) | Model Vault: „as we move toward general availability“ ohne Datum → nichts. |
| Aleph Alpha | Newsroom (DE): letzter Beitrag 05.10.2026 (Reto Spörri) | Nichts Neues. |
| Black Forest Labs | Blog: letzter Beitrag 15.10.2026 (FLUX 3 Image Klein); Scorsese-Seite ohne Datum | Nichts mit Zahl und Datum. |
| Domyn | „Domyn begins rolling out Edge …“ (20.10.2026, domyn.com/news/domyn-edge-sovereign-ai-model) | Satz „will progress along different post-training stages into November 2026“: Datum ohne Zahl, „into November“ ist kein Stichtag → verworfen. |
| IBM | llm-d 1.0 (20.10.), Q3-Ergebnis (21.10.), Ferrari (22.10.); Liste über newsroom.ibm.com/announcements lesbar | Q3-Meldung bestätigt „full-year constant currency revenue growth in the range of four-to-five percent“ und neu „free cash flow to increase by more than $1 billion year-over-year“. Frist 31.12.2026 im Fenster, aber Limit 2 voll → nur Reserve. |
| ServiceNow | 20 Meldungen 15.–22.10. über den Q4-Feed (JSON) gelistet, u. a. NVIDIA-Agent (21.10.), AI Passport (15.10.) | Limit 2 voll; Texte nicht vertieft. Q3-Zahlen kommen am 28.10. |
| OpenAI | RSS openai.com/news/rss.xml lesbar (HTTP 200): 62 Beiträge seit 16.10. | Limit 2 voll; Titel und Kurztexte ohne Zusage mit Zahl und Datum. Volltexte nicht abgerufen. |
| Dweve | dweve.com/open-source/ (ohne Datum, Abruf 23.10.) | Neu: „The remaining repositories publish in fortnightly rounds from 25 October 2026, two at a time to begin with“. Der Start wurde vom 01.10. auf den 25.10. verschoben, ein Enddatum fehlt wieder, „to begin with“ → verworfen wie 012. Nebenbefund zu Runde 1: Laut Seite ist nur HEDL öffentlich, Knot und Signum also nicht am 01.10. erschienen. |
| WRITER | Newsroom: letzte Mitteilung 09.09.2026; Blog-Beiträge ohne Datum | Nichts mit Zahl und Datum. |
| LINAGORA | 4 Beiträge (15.10., 20.10., LinTO-Serie 22.10.) | Nichts mit Zahl und Datum. |
| Pleias | Blog: letzter Beitrag 05.10.2026 | Nichts Neues. |
| Bria AI | Blog: letzter Beitrag 08.09.2026; neue Seiten „Bria Create“ (Early Access) | Nichts mit Zahl und Datum. |
| xAI / SpaceXAI | „SpaceX Super Intelligence Partner Network“ (22.10.), Grok Bot IncidentSweep (20.10.) | Nichts mit Zahl und Datum. |
| Open Hippo | Startseite | Nichts mit Zahl und Datum. |
| Fastweb (+Vodafone) | fastwebvodafone.it antwortet mit HTTP 503 und Incapsula-Prüfung | Ungeklärt, Prüfung nicht umgangen. |
| Almawave (Almaviva) | almaviva.it/en/media/press-releases ist eine Single-Page-App ohne lesbaren Text | Ungeklärt. |
| AI Studio Delta | weiter keine eigene Website | Nicht geprüft. |

Amazon, Google und Microsoft gehören nicht in dieses Buch (DMA-Gatekeeper, siehe 03.10.).

Wiedervorlagen aus Runde 3:

- **Cohere/AISLE:** Der Beitrag vom 15.10.2026 (cohere.com/blog/cohere-and-aisle-sign-letter-of-intent-to-advance-cyber-resilient-sovereign-ai) nennt weiter nur „proposed agreement“ und „proposed transaction“, kein Closing-Datum, keinen Preis. Kein neuer Beitrag dazu → weiter kein Kandidat.
- **Nebenbefund für ki-2026-005/-006:** Derselbe Cohere-Beitrag schreibt „Following our acquisitions of Reliant AI and Aleph Alpha“. Eine eigene Abschlussmeldung habe ich weder im Cohere-Blog noch im Aleph-Alpha-Newsroom gefunden. Ob der Vollzug schon gemeldet ist: ungeklärt, bei der Auflösung prüfen.
- **Mistral Large 4, Gewichte (Frist 31.10., nur Vermerk):** mistral.ai/news/mistral-large-4/ sagt am 23.10. weiter „We will release the weights by the end of the month.“ Der NVIDIA-Beitrag vom 21.10. sagt „with weights planned for release at the end of October“. Am 21.10. waren sie also noch nicht veröffentlicht.
- **Mistral „200 MW bis Ende 2027“:** auch jetzt nicht auf eigener Seite. Durchsucht: die drei neuen Beiträge, /news/, /cloud, /cloud/compute/, /sovereign-ai/, /about (Suche nach „MW“, „GW“, „2027“, „2028“). /cloud nennt nur „1 GW … by 2030“. /compute liefert inzwischen HTTP 404.

Folge: Buch KI bleibt bei 11 Wetten; nächste Runde frühestens am 30.10.2026, dann ServiceNow-Q3 (28.10.) und Mistral-Gewichte (31.10.) als Vermerk mitnehmen.
