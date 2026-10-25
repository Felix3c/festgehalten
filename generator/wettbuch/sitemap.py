"""sitemap.xml (sitemaps.org 0.9) über alles, was `alle` gebaut hat.

Damit Google auch Wetten findet, auf die nichts verlinkt. lastmod kommt aus den Daten der Wette
(jüngstes Datum), nie aus der Bauzeit: sonst wäre jede Seite bei jedem Bau „geändert“."""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape


def _tag(d) -> str | None:
    if d is None or d == "":
        return None
    return str(d)[:10]


def letztes_datum(w: dict) -> str | None:
    """Jüngstes Datum einer Wette: gesagt, hinterlegt, Vermerk oder aufgelöst (JJJJ-MM-TT)."""
    daten = [_tag(w.get("gesagt_am")), _tag(w.get("aufgeloest_am"))]
    daten += [_tag(p.get("hinterlegt_am")) for p in w.get("prognosen") or []]
    daten += [_tag(v.get("am")) for v in w.get("vermerke") or []]
    daten = [d for d in daten if d]
    return max(daten) if daten else None


def eintraege_buch(name: str, wetten: list[dict], institution_slug) -> list[tuple[str, str | None]]:
    """(Pfad relativ zur Wurzel, lastmod) für Buchseite, Institutionen und Wetten eines Buchs."""
    aus: list[tuple[str, str | None]] = []
    je_inst: dict[str, list[str]] = {}
    for w in wetten:
        lm = letztes_datum(w)
        aus.append((f"{name}/wette/{w['id']}.html", lm))
        je_inst.setdefault(institution_slug(w["institution"]), []).append(lm or "")
    for s, daten in je_inst.items():
        aus.append((f"{name}/institution/{s}.html", max(daten) or None))
    alle = [lm for _, lm in aus if lm]
    aus.insert(0, (f"{name}/index.html", max(alle) if alle else None))
    return aus


def zusatz_eintraege(ausgabe: Path, bekannt: set[str]) -> list[tuple[str, None]]:
    """Übrige gebaute HTML-Seiten (Übersicht, Impressum …) ohne Datum aus den Daten."""
    return [(rel, None) for rel in sorted(p.relative_to(ausgabe).as_posix() for p in ausgabe.rglob("*.html"))
            if rel not in bekannt]


def sitemap_xml(eintraege: list[tuple[str, str | None]]) -> str:
    """`eintraege`: (absolute Adresse, lastmod oder None)."""
    zeilen = ['<?xml version="1.0" encoding="utf-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lm in eintraege:
        zeilen.append(f"  <url><loc>{escape(loc)}</loc>" + (f"<lastmod>{lm}</lastmod>" if lm else "") + "</url>")
    zeilen.append("</urlset>")
    return "\n".join(zeilen) + "\n"
