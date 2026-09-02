# festgehalten

Institutionen beim Wort genommen: was sie angekündigt haben, was eingetreten ist, wer wie oft recht hatte. Offenes Format (»festgehalten-Format v1«), ein Buch pro Institution, eine Übersicht über alle Bücher — in jeder Sprache, in der es jemand führt.

- **Format:** [FORMAT.md](FORMAT.md) — wer diese Regeln einhält, führt ein Wettbuch.
- **Methode:** [METHODE.md](METHODE.md) — wie die Computer-Prognosen entstehen (Referenzklassen, Tabelle, Nachmachen in fünf Schritten).
- **Anleitung:** [ANLEITUNG.md](ANLEITUNG.md) — ein Buch in einer Stunde, von der Installation bis zur öffentlichen Seite.
- **Generator:** `festgehalten bauen <buch> <ausgabe>` — macht aus einem Ordner
  eine statische Seite mit Rangliste. Nur `pyyaml` und `markdown`. `festgehalten neu <ordner>`
  legt ein Gerüst an; `festgehalten alle <buecher-ordner> <ausgabe>` baut jedes Unterverzeichnis
  mit `BUCH.md` und schreibt zusätzlich eine Übersichtsseite über alle Bücher.
- **Erstes Buch:** [buecher/koeln](buecher/koeln) — „Köln gegen Köln".

## Selbst ein Buch führen

1. `python -m pip install "festgehalten @ git+https://github.com/Felix3c/festgehalten"`
2. `festgehalten neu meinbuch --stadt "Stadt Musterstadt"` — legt `BUCH.md` (FORMAT.md §4),
   eine Beispielwette (§1) und einen Pages-Workflow an.
3. Ausfüllen, dann `festgehalten bauen meinbuch site`.
4. `site/` irgendwo hinlegen, oder pushen und GitHub Pages machen lassen. Fertig. Niemanden fragen.

Schritt für Schritt mit Zeitplan: [ANLEITUNG.md](ANLEITUNG.md).

Halter-Disziplin, die kein Programm prüfen kann: Einträge nach dem Commit nicht mehr
ändern (FORMAT.md §1.3.3), Teilerfüllung als Nein auflösen (§2.2), zurückgezogene
Aussagen als neue Wette führen (§1.3.5). Git zeigt, ob man sich daran hält.

Der Textteil einer Wette wird als Markdown gerendert; rohes HTML darin wird als Text
angezeigt, nicht ausgeführt. Links mit javascript: sind Sache des Halters — Wette-
Dateien nur von Leuten annehmen, denen man Schreibrechte gäbe.

## Entwickeln

    python -m pip install -e ".[test]"
    python -m pytest
    festgehalten bauen <ordner> site --pruefen  # nur prüfen, nichts schreiben

`python -m wettbuch` ist dasselbe wie `festgehalten` (der Modulname ist älter als der Name des Formats).

Lizenz: Code MIT, Bücher CC0.
