"""Atom-Feed „neu aufgelöst“ (RFC 4287). Ein Eintrag je aufgelöster Wette, neueste zuerst.

Abonnieren, ohne zu fragen: kein Kanal, kein Betreiber, derselbe Stand wie die Seite,
weil der Feed aus denselben Wette-Dateien gebaut wird."""
from __future__ import annotations

from datetime import date, datetime, timezone
from xml.sax.saxutils import escape

FEED_MAX = 50
AUFGELOEST = "aufgeloest"


def _iso(d) -> str:
    if isinstance(d, datetime):
        return d.strftime("%Y-%m-%dT%H:%M:%SZ")
    if isinstance(d, date):
        return f"{d.isoformat()}T00:00:00Z"
    return str(d)


def _ausgang_wort(w: dict) -> str:
    if w["typ"] == "ja_nein":
        return "Ja" if int(w["ausgang"]) == 1 else "Nein"
    einheit = w.get("einheit") or ""
    return f"{w['ausgang']} {einheit}".strip()


def eintrag(w: dict, pfad: str) -> dict:
    """Ein Feed-Eintrag aus einer bewerteten Wette. `pfad` ist der Link relativ zur Feed-Wurzel."""
    zusammenfassung = (
        f"{w['institution']}: „{w['zitat']}“ ({w.get('gesagt_von', '')}, {w['gesagt_am']}). "
        f"Ausgang: {_ausgang_wort(w)}. Beleg: {w.get('beleg_ausgang', '')}"
    )
    return {
        "id": f"urn:festgehalten:{w['id']}",
        "titel": f"{_ausgang_wort(w)}: {w['frage']}",
        "link": pfad,
        "aktualisiert": w["aufgeloest_am"],
        "zusammenfassung": zusammenfassung,
    }


def eintraege_aus(wetten: list[dict], praefix: str = "") -> list[dict]:
    """Aufgelöste Wetten eines gebauten Buchs als Feed-Einträge. `praefix` z. B. 'koeln/'."""
    return [eintrag(w, f"{praefix}wette/{w['id']}.html")
            for w in wetten
            if w["_bewertung"]["status"] == AUFGELOEST and w.get("aufgeloest_am")]


def feed_xml(titel: str, eintraege: list[dict], build_zeit: str, url: str | None) -> str:
    """`url` ist die absolute Adresse des Ordners, in dem feed.xml liegt (mit Schrägstrich am Ende),
    oder None; dann bleiben die Links relativ und Leser lösen sie gegen die Feed-Adresse auf."""
    basis = url or ""
    sortiert = sorted(eintraege, key=lambda e: (_iso(e["aktualisiert"]), e["id"]), reverse=True)[:FEED_MAX]
    if sortiert:
        aktualisiert = _iso(sortiert[0]["aktualisiert"])
    else:
        try:
            aktualisiert = _iso(datetime.strptime(build_zeit, "%Y-%m-%d %H:%M"))
        except ValueError:
            aktualisiert = _iso(datetime.now(timezone.utc).replace(tzinfo=None))
    zeilen = ['<?xml version="1.0" encoding="utf-8"?>',
              '<feed xmlns="http://www.w3.org/2005/Atom">',
              f"  <title>{escape(titel)}</title>",
              f"  <id>urn:festgehalten:feed:{escape(basis or titel)}</id>",
              f'  <link rel="self" href="{escape(basis)}feed.xml"/>',
              f'  <link rel="alternate" type="text/html" href="{escape(basis)}index.html"/>',
              f"  <updated>{aktualisiert}</updated>",
              "  <generator>festgehalten</generator>"]
    for e in sortiert:
        zeilen += ["  <entry>",
                   f"    <id>{escape(e['id'])}</id>",
                   f"    <title>{escape(e['titel'])}</title>",
                   f'    <link rel="alternate" type="text/html" href="{escape(basis + e["link"])}"/>',
                   f"    <updated>{_iso(e['aktualisiert'])}</updated>",
                   f"    <summary>{escape(e['zusammenfassung'])}</summary>",
                   "  </entry>"]
    zeilen.append("</feed>")
    return "\n".join(zeilen) + "\n"
