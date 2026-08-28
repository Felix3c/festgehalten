# Wettbuch

Ein offenes Format, um Institutionen an ihren eigenen Prognosen zu messen.

- **Format:** [FORMAT.md](FORMAT.md) — wer diese Regeln einhält, führt ein Wettbuch.
- **Generator:** `python -m wettbuch bauen <buch> <ausgabe>` — macht aus einem Ordner
  eine statische Seite mit Rangliste. Nur `pyyaml` und `markdown`.
- **Erstes Buch:** [buecher/koeln](buecher/koeln) — „Köln gegen Köln".

## Selbst ein Buch führen

1. Ordner anlegen, `BUCH.md` nach FORMAT.md §4.
2. Eine Datei pro Wette nach FORMAT.md §1 in einen Unterordner `wetten/`.
3. `python -m pip install -e .` und `python -m wettbuch bauen <ordner> site`.
4. `site/` irgendwo hinlegen. Fertig. Niemanden fragen.

Halter-Disziplin, die kein Programm prüfen kann: Einträge nach dem Commit nicht mehr
ändern (FORMAT.md §1.3.3), Teilerfüllung als Nein auflösen (§2.2), zurückgezogene
Aussagen als neue Wette führen (§1.3.5). Git zeigt, ob man sich daran hält.

Der Textteil einer Wette wird als Markdown gerendert; rohes HTML darin wird als Text
angezeigt, nicht ausgeführt. Links mit javascript: sind Sache des Halters — Wette-
Dateien nur von Leuten annehmen, denen man Schreibrechte gäbe.

## Entwickeln

    python -m pip install -e ".[test]"
    python -m pytest
    python -m wettbuch bauen <ordner> site --pruefen  # nur prüfen, nichts schreiben

Lizenz: Code MIT, Bücher CC0.
