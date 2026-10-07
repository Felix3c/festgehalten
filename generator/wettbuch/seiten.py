# generator/wettbuch/seiten.py
"""HTML und JSON erzeugen. Rechnet nichts, bekommt fertige Daten."""
from __future__ import annotations

import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

import markdown

from . import feed, sprache
FEED_MAX = feed.FEED_MAX

STIL = Path(__file__).with_name("stil.css")


class SlugKollision(ValueError):
    """Zwei Institutionen ergeben denselben Slug."""
UMLAUTE = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"})


def slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", text.translate(UMLAUTE)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "x"


def datum(d, sp: str = sprache.STANDARD) -> str:
    return sprache.datum(d, sp)


def zahl(x, stellen: int = 2, sp: str = sprache.STANDARD) -> str:
    return sprache.zahl(x, stellen, sp)


def _e(x) -> str:
    return html.escape(str(x), quote=True)


def _markdown_sicher(text: str) -> str:
    return markdown.markdown(text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


FussLinks = list[tuple[str, str]]


def _fuss(wurzel: str, fuss_links: FussLinks | None) -> str:
    """Zusätzliche Fußzeilen-Links (z. B. Impressum · Datenschutz). `href` ist relativ zu `wurzel`."""
    return "".join(f' · <a href="{_e(wurzel + href)}">{_e(text)}</a>' for text, href in (fuss_links or []))


def _texte(sp: str) -> dict[str, str]:
    """Alle Anzeigetexte einer Sprache, schon für HTML escaped."""
    return {k: _e(v) for k, v in sprache.TEXTE[sp].items()}


def _seite(titel: str, koerper: str, tiefe: int, build_zeit: str, buch_titel: str,
           fuss_links: FussLinks | None = None, sp: str = sprache.STANDARD) -> str:
    wurzel = "../" * tiefe
    t = _texte(sp)
    return (
        f'<!doctype html>\n<html lang="{sp}"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{_e(titel)} · {_e(buch_titel)}</title>\n"
        f'<link rel="stylesheet" href="{wurzel}stil.css">\n'
        f'<link rel="alternate" type="application/atom+xml" href="{wurzel}feed.xml" title="{t["feed_titel"]}"></head>\n<body>\n'
        f'<p class="mute"><a href="{wurzel}index.html">{_e(buch_titel)}</a></p>\n'
        f"{koerper}\n"
        f'<footer>{_e(sprache.t(sp, "fuss_format", zeit=build_zeit))} · <a href="{wurzel}wettbuch.json">wettbuch.json</a>'
        f"{_fuss(wurzel, fuss_links)}</footer>\n"
        "</body></html>\n"
    )


def _herkunft(w: dict) -> str:
    """FORMAT.md §1.1: `herkunft` ist optional, Standard `zitiert`."""
    return str(w.get("herkunft") or "zitiert")


def _status_text(w: dict, sp: str = sprache.STANDARD) -> str:
    t = _texte(sp)
    s = w["_bewertung"]["status"]
    if s == "ersetzt":
        return f'<span class="status mute">{t["ersetzt_durch"]} {_e(w.get("ersetzt_durch", ""))}</span>'
    if s == "offen":
        gesucht = w["_bewertung"].get("zuletzt_gesucht")
        if gesucht:
            hinweis = _e(sprache.t(sp, "beleg_gesucht", datum=datum(gesucht, sp)))
            return f'<span class="status">{t["offen"]}</span> <span class="mute">· {hinweis}</span>'
        return f'<span class="status">{t["offen"]}</span>'
    if s != "aufgeloest":
        return f'<span class="status">{_e(sprache.wert(s, sp))}</span>'
    if w["typ"] == "ja_nein":
        if w["ausgang"] == 1:
            return f'<span class="status ja">{t["ja"]}</span>'
        return f'<span class="status nein">{t["nein"]}</span>'
    return f'<span class="status">{zahl(w["ausgang"], 2, sp)} {_e(w.get("einheit", ""))}</span>'


def _tabelle_html(tabelle: list[dict], rang_ab: int, sp: str = sprache.STANDARD) -> str:
    t = _texte(sp)
    z = ['<div class="tabelle-wrap"><table><thead><tr>',
         f"<th>{t['rang']}</th><th>{t['wer']}</th><th class=zahl>{t['trefferquote']}</th>"
         f"<th class=zahl>{t['ja_nein_aufgeloest']}</th>",
         f"<th class=zahl>{t['naeher_dran_spalte']}</th><th class=zahl>{t['rechenschaft']}</th>"
         f"<th class=zahl>{t['wetten_als_institution']}</th>",
         "</tr></thead><tbody>"]
    for r in tabelle:
        rang = (str(r["rang"]) if r["rang"]
                else f'<span class="mute">{_e(sprache.t(sp, "kein_rang", n=rang_ab))}</span>')
        wer = _e(r["von"])
        if r["ist_institution"]:
            wer = f'<a href="institution/{slug(r["von"])}.html">{wer}</a>'
        naeher = _e(sprache.t(sp, "von_n", a=r["punkt_gewonnen"], b=r["punkt_n"]))
        z.append(f"<tr><td>{rang}</td><td>{wer}</td><td class=zahl>{zahl(r['ja_nein_schnitt'], 2, sp)}</td>"
                 f"<td class=zahl>{r['ja_nein_n']}</td><td class=zahl>{naeher}</td>"
                 f"<td class=zahl>{r['rechenschaft_verfallen']}</td><td class=zahl>{r['wetten_gesamt']}</td></tr>")
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wettenliste_html(wetten: list[dict], tiefe: int, sp: str = sprache.STANDARD) -> str:
    p = "../" * tiefe
    t = _texte(sp)
    z = [f'<div class="tabelle-wrap"><table><thead><tr><th>{t["wette"]}</th><th>{t["institution"]}</th>'
         f'<th>{t["gesagt_am"]}</th><th>{t["pruefung_ab"]}</th><th>{t["herkunft"]}</th>'
         f'<th>{t["ausgang"]}</th></tr></thead><tbody>']
    for w in wetten:
        z.append(f'<tr><td><a href="{p}wette/{_e(w["id"])}.html">{_e(w["frage"])}</a></td>'
                 f'<td><a href="{p}institution/{slug(w["institution"])}.html">{_e(w["institution"])}</a></td>'
                 f'<td>{datum(w["gesagt_am"], sp)}</td><td>{datum(w["pruefung_am"], sp)}</td>'
                 f'<td>{_e(sprache.wert(_herkunft(w), sp))}</td><td>{_status_text(w, sp)}</td></tr>')
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wette_html(w: dict, sp: str = sprache.STANDARD) -> str:
    b = w["_bewertung"]
    t = _texte(sp)
    z = [f"<h1>{_e(w['frage'])}</h1>",
         f'<p><strong>{_e(w["institution"])}</strong> · {_e(w["gesagt_von"])} · {t["gesagt_am"]} '
         f'{datum(w["gesagt_am"], sp)} · <a href="{_e(w["quelle"])}">{t["quelle"]}</a></p>',
         f"<blockquote>{_e(w['zitat'])}</blockquote>",
         f"<p>{t['typ']}: {_e(sprache.wert(w['typ'], sp))} · {t['pruefung_ab']} {datum(w['pruefung_am'], sp)} · "
         f"{t['herkunft']}: {_e(sprache.wert(_herkunft(w), sp))} · {t['status']}: {_status_text(w, sp)}</p>",
         f"<table><thead><tr><th>{t['wer']}</th><th class=zahl>{t['prognose']}</th><th>{t['art']}</th>"
         f"<th>{t['hinterlegt_am']}</th><th class=zahl>{t['score']}</th></tr></thead><tbody>"]
    for p in w["prognosen"]:
        s = b["scores"].get(p["von"])
        z.append(f"<tr><td>{_e(p['von'])}</td><td class=zahl>{zahl(p['wert'], 2, sp)}</td>"
                 f"<td>{_e(sprache.wert(p['art'], sp))}</td>"
                 f"<td>{datum(p['hinterlegt_am'], sp)}</td><td class=zahl>{zahl(s, 2, sp)}</td></tr>")
    z.append("</tbody></table>")
    if b["status"] == "ersetzt":
        e = _e(w["ersetzt_durch"])
        link = f'<a href="{e}.html">{e}</a>'
        z.append(f"<p>{t['ersetzt_satz'].replace('{link}', link)}</p>")
    if b["status"] == "aufgeloest":
        naeher = f' · {t["naeher_dran"]}: <strong>{_e(b["naeher_dran"])}</strong>' if b["naeher_dran"] else ""
        z.append(f'<p>{t["aufgeloest_am"]} {datum(w["aufgeloest_am"], sp)} · '
                 f'<a href="{_e(w["beleg_ausgang"])}">{t["beleg"]}</a>{naeher}</p>')
    if w.get("vermerke"):
        z.append(f"<h2>{t['vermerke']}</h2><ul>")
        for v in w["vermerke"]:
            z.append(f"<li>{datum(v.get('am'), sp)}: {_e(v.get('text', ''))}</li>")
        z.append("</ul>")
    z.append(_markdown_sicher(w.get("_text", "")))
    return "\n".join(z)


def _json_faehig(x):
    if isinstance(x, date):
        return x.isoformat()
    if isinstance(x, dict):
        return {k: _json_faehig(v) for k, v in x.items() if not k.startswith("_") or k == "_bewertung"}
    if isinstance(x, list):
        return [_json_faehig(v) for v in x]
    return x


def seiten_schreiben(meta: dict, bewertet: dict, ausgabe: Path, build_zeit: str,
                     url: str | None = None, fuss_links: FussLinks | None = None) -> list[Path]:
    """`fuss_links`: (Text, href) je Link in der Fußzeile jeder Seite, href relativ zum Buch-Ordner."""
    # Build nach_inst and check for slug collisions before any filesystem writes
    nach_inst: dict[str, list[dict]] = {}
    for w in bewertet["wetten"]:
        nach_inst.setdefault(w["institution"], []).append(w)

    slugs: dict[str, str] = {}
    for inst in nach_inst:
        s = slug(inst)
        if s in slugs and slugs[s] != inst:
            raise SlugKollision(f"Slug-Kollision: {inst!r} und {slugs[s]!r} ergeben beide {s!r}")
        slugs[s] = inst

    # Now safe to write files
    ausgabe.mkdir(parents=True, exist_ok=True)
    (ausgabe / "institution").mkdir(exist_ok=True)
    (ausgabe / "wette").mkdir(exist_ok=True)
    titel = str(meta.get("titel", "Wettbuch"))
    geschrieben: list[Path] = []

    def schreib(rel: str, inhalt: str) -> None:
        p = ausgabe / rel
        p.write_text(inhalt, encoding="utf-8")
        geschrieben.append(p)

    schreib("stil.css", STIL.read_text(encoding="utf-8"))

    sp = sprache.von_meta(meta)
    t = _texte(sp)
    lizenz = f' · {t["lizenz"]} {_e(meta["lizenz"])}' if meta.get("lizenz") else ""
    koerper = [f"<h1>{_e(titel)}</h1>",
               f'<p class="mute">{t["halter"]}: {_e(meta.get("halter", ""))} · {t["seit"]} {datum(meta.get("seit"), sp)} · '
               f'{t["format"]} {_e(meta.get("format", ""))}{lizenz}</p>',
               _markdown_sicher(meta.get("_text", "")),
               f"<h2>{t['rangliste']}</h2>", _tabelle_html(bewertet["tabelle"], bewertet["rang_ab"], sp),
               f"<h2>{t['alle_wetten']}</h2>", _wettenliste_html(bewertet["wetten"], 0, sp),
               f'<p class="mute">{sprache.t(sp, "abonnieren")}</p>']
    schreib("index.html", _seite(sprache.t(sp, "rangliste"), "\n".join(koerper), 0, build_zeit, titel,
                                 fuss_links, sp))
    schreib("feed.xml", feed.feed_xml(f"{titel} · {sprache.t(sp, 'feed_titel')}",
                                     feed.eintraege_aus(bewertet["wetten"], sp=sp), build_zeit, url))

    for inst, ws in nach_inst.items():
        koerper = [f"<h1>{_e(inst)}</h1>", _wettenliste_html(ws, 1, sp)]
        schreib(f"institution/{slug(inst)}.html",
                _seite(inst, "\n".join(koerper), 1, build_zeit, titel, fuss_links, sp))

    for w in bewertet["wetten"]:
        schreib(f"wette/{w['id']}.html",
                _seite(w["frage"], _wette_html(w, sp), 1, build_zeit, titel, fuss_links, sp))

    daten = {"format": "v1", "titel": titel, "halter": meta.get("halter"), "gebaut": build_zeit,
             "seit": _json_faehig(meta.get("seit")), "kontakt": meta.get("kontakt"),
             "lizenz": meta.get("lizenz"),
             "tabelle": bewertet["tabelle"], "wetten": _json_faehig(bewertet["wetten"])}
    schreib("wettbuch.json", json.dumps(daten, ensure_ascii=False, indent=2))
    return geschrieben


def _uebersicht_zeile_html(b: dict) -> str:
    institutionen = ", ".join(_e(i) for i in b.get("institutionen", []))
    return (f'<tr><td><a href="{_e(b["ordner"])}/index.html">{_e(b["titel"])}</a></td>'
            f"<td>{institutionen}</td><td class=zahl>{b['wetten']}</td>"
            f"<td class=zahl>{b['aufgeloest']}</td><td class=zahl>{b['offen']}</td>"
            f"<td class=zahl>{b.get('sonstige', 0)}</td></tr>")


def _wurzelseite(titel: str, koerper: str, tiefe: int, build_zeit: str,
                 fuss_links: FussLinks | None = None, mit_feed: bool = True) -> str:
    """Seite auf Ebene der Übersicht (kein Buch): die Übersicht selbst und Zusatzseiten wie Impressum."""
    wurzel = "../" * tiefe
    feed_link = (f'<link rel="alternate" type="application/atom+xml" href="{wurzel}feed.xml" title="neu aufgelöst">'
                 if mit_feed else "")
    zurueck = f'<p class="mute"><a href="{wurzel}index.html">festgehalten</a></p>\n' if tiefe else ""
    return ('<!doctype html>\n<html lang="de"><head><meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"<title>{_e(titel)}</title>\n"
            f'<link rel="stylesheet" href="{wurzel}stil.css">\n'
            f"{feed_link}</head>\n<body>\n"
            f"{zurueck}{koerper}\n"
            f"<footer>festgehalten-Format v1 · gebaut {_e(build_zeit)}{_fuss(wurzel, fuss_links)}</footer>\n"
            "</body></html>\n")


def uebersicht_schreiben(buecher: list[dict], ausgabe: Path, build_zeit: str,
                         feed_eintraege: list[dict] | None = None, url: str | None = None,
                         fuss_links: FussLinks | None = None) -> list[Path]:
    """Übersichtsseite über mehrere Bücher (FORMAT.md §5). Kein Verzeichnis im Sinne von §6,
    nur eine lokale Liste über das, was `alle` gerade gebaut hat."""
    sortiert = sorted(buecher, key=lambda b: b["ordner"])

    ausgabe.mkdir(parents=True, exist_ok=True)
    geschrieben: list[Path] = []

    def schreib(rel: str, inhalt: str) -> None:
        p = ausgabe / rel
        p.write_text(inhalt, encoding="utf-8")
        geschrieben.append(p)

    schreib("stil.css", STIL.read_text(encoding="utf-8"))

    tabelle = ('<div class="tabelle-wrap"><table><thead><tr>'
               "<th>Buch</th><th>Institution(en)</th><th class=zahl>Wetten gesamt</th>"
               "<th class=zahl>davon aufgelöst</th><th class=zahl>davon offen</th>"
               "<th class=zahl>davon sonstige</th></tr></thead><tbody>"
               + "".join(_uebersicht_zeile_html(b) for b in sortiert)
               + "</tbody></table></div>"
               '<p class="mute">Sonstige: ersetzte Einträge (FORMAT.md §1.3.3), verfallen oder strittig.</p>')
    koerper = ("<h1>festgehalten</h1>"
               "<p>Institutionen an ihren eigenen Prognosen messen. Jedes Buch ist ein Ordner; "
               "das Format ist offen — FORMAT.md.</p>" + tabelle + "\n"
               '<p class="mute">Abonnieren: <a href="feed.xml">Feed „neu aufgelöst“</a> über alle Bücher (Atom)</p>')
    schreib("index.html", _wurzelseite("Wettbuch", koerper, 0, build_zeit, fuss_links))
    schreib("feed.xml", feed.feed_xml("festgehalten · neu aufgelöst", feed_eintraege or [], build_zeit, url))

    daten = [{"ordner": b["ordner"], "titel": b["titel"], "wetten": b["wetten"],
              "aufgeloest": b["aufgeloest"], "offen": b["offen"], "sonstige": b.get("sonstige", 0)} for b in sortiert]
    schreib("alle.json", json.dumps(daten, ensure_ascii=False, indent=2))
    return geschrieben


def zusatzseiten_schreiben(zusatz: list[dict], ausgabe: Path, build_zeit: str,
                           fuss_links: FussLinks | None = None) -> list[Path]:
    """Freie Seiten neben der Übersicht (Impressum, Datenschutz …): je `<name>/index.html`.
    Jede braucht `name`, `titel` und `_text` (Markdown, wird wie Wettentext escaped)."""
    geschrieben: list[Path] = []
    for z in zusatz:
        ordner = ausgabe / z["name"]
        ordner.mkdir(parents=True, exist_ok=True)
        koerper = f"<h1>{_e(z['titel'])}</h1>\n" + _markdown_sicher(z.get("_text", ""))
        pfad = ordner / "index.html"
        pfad.write_text(_wurzelseite(str(z["titel"]), koerper, 1, build_zeit, fuss_links, mit_feed=False),
                        encoding="utf-8")
        geschrieben.append(pfad)
    return geschrieben


def buecher_schreiben(buecher: list[dict], ausgabe: Path) -> None:
    """Buchliste für Werkzeuge, die Einträge einreichen (Doorway, Spec Teil 3 §5.2)."""
    ausgabe.mkdir(parents=True, exist_ok=True)
    (ausgabe / "buecher.json").write_text(json.dumps(buecher, ensure_ascii=False, indent=2), encoding="utf-8")
