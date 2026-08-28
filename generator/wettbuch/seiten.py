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

STIL = Path(__file__).with_name("stil.css")
UMLAUTE = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"})


def slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", text.translate(UMLAUTE)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "x"


def datum(d) -> str:
    return d.strftime("%d.%m.%Y") if isinstance(d, date) else "–"


def zahl(x, stellen: int = 2) -> str:
    return "–" if x is None else f"{x:.{stellen}f}".replace(".", ",")


def _e(x) -> str:
    return html.escape(str(x), quote=True)


def _seite(titel: str, koerper: str, tiefe: int, build_zeit: str, buch_titel: str) -> str:
    wurzel = "../" * tiefe
    return (
        '<!doctype html>\n<html lang="de"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{_e(titel)} · {_e(buch_titel)}</title>\n"
        f'<link rel="stylesheet" href="{wurzel}stil.css"></head>\n<body>\n'
        f'<p class="mute"><a href="{wurzel}index.html">{_e(buch_titel)}</a></p>\n'
        f"{koerper}\n"
        f'<footer>Wettbuch-Format v1 · gebaut {_e(build_zeit)} · <a href="{wurzel}wettbuch.json">wettbuch.json</a></footer>\n'
        "</body></html>\n"
    )


def _status_text(w: dict) -> str:
    s = w["_bewertung"]["status"]
    if s != "aufgeloest":
        return f'<span class="status">{_e(s)}</span>'
    if w["typ"] == "ja_nein":
        return '<span class="status ja">ja</span>' if w["ausgang"] == 1 else '<span class="status nein">nein</span>'
    return f'<span class="status">{zahl(w["ausgang"])} {_e(w.get("einheit", ""))}</span>'


def _tabelle_html(tabelle: list[dict], rang_ab: int) -> str:
    z = ['<div class="tabelle-wrap"><table><thead><tr>',
         "<th>Rang</th><th>Wer</th><th class=zahl>Trefferquote (Brier)</th><th class=zahl>Ja/Nein aufgelöst</th>",
         "<th class=zahl>Näher dran</th><th class=zahl>Rechenschaft (verfallen/strittig)</th><th class=zahl>Wetten</th>",
         "</tr></thead><tbody>"]
    for r in tabelle:
        rang = str(r["rang"]) if r["rang"] else f'<span class="mute">noch kein Rang (ab {rang_ab})</span>'
        wer = _e(r["von"])
        if r["ist_institution"]:
            wer = f'<a href="institution/{slug(r["von"])}.html">{wer}</a>'
        z.append(f"<tr><td>{rang}</td><td>{wer}</td><td class=zahl>{zahl(r['ja_nein_schnitt'])}</td>"
                 f"<td class=zahl>{r['ja_nein_n']}</td><td class=zahl>{r['punkt_gewonnen']} von {r['punkt_n']}</td>"
                 f"<td class=zahl>{r['rechenschaft_verfallen']}</td><td class=zahl>{r['wetten_gesamt']}</td></tr>")
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wettenliste_html(wetten: list[dict], tiefe: int) -> str:
    p = "../" * tiefe
    z = ['<div class="tabelle-wrap"><table><thead><tr><th>Wette</th><th>Institution</th>'
         '<th>gesagt am</th><th>Prüfung ab</th><th>Ausgang</th></tr></thead><tbody>']
    for w in wetten:
        z.append(f'<tr><td><a href="{p}wette/{_e(w["id"])}.html">{_e(w["frage"])}</a></td>'
                 f'<td><a href="{p}institution/{slug(w["institution"])}.html">{_e(w["institution"])}</a></td>'
                 f'<td>{datum(w["gesagt_am"])}</td><td>{datum(w["pruefung_am"])}</td><td>{_status_text(w)}</td></tr>')
    z.append("</tbody></table></div>")
    return "\n".join(z)


def _wette_html(w: dict) -> str:
    b = w["_bewertung"]
    z = [f"<h1>{_e(w['frage'])}</h1>",
         f'<p><strong>{_e(w["institution"])}</strong> · {_e(w["gesagt_von"])} · gesagt am {datum(w["gesagt_am"])} · '
         f'<a href="{_e(w["quelle"])}">Quelle</a></p>',
         f"<blockquote>{_e(w['zitat'])}</blockquote>",
         f"<p>Typ: {_e(w['typ'])} · Prüfung ab {datum(w['pruefung_am'])} · Status: {_status_text(w)}</p>",
         "<table><thead><tr><th>Wer</th><th class=zahl>Prognose</th><th>Art</th><th>hinterlegt am</th>"
         "<th class=zahl>Score</th></tr></thead><tbody>"]
    for p in w["prognosen"]:
        s = b["scores"].get(p["von"])
        z.append(f"<tr><td>{_e(p['von'])}</td><td class=zahl>{zahl(p['wert'])}</td><td>{_e(p['art'])}</td>"
                 f"<td>{datum(p['hinterlegt_am'])}</td><td class=zahl>{zahl(s)}</td></tr>")
    z.append("</tbody></table>")
    if b["status"] == "aufgeloest":
        naeher = f' · näher dran: <strong>{_e(b["naeher_dran"])}</strong>' if b["naeher_dran"] else ""
        z.append(f'<p>Aufgelöst am {datum(w["aufgeloest_am"])} · <a href="{_e(w["beleg_ausgang"])}">Beleg</a>{naeher}</p>')
    if w.get("vermerke"):
        z.append("<h2>Vermerke</h2><ul>")
        for v in w["vermerke"]:
            z.append(f"<li>{datum(v.get('am'))}: {_e(v.get('text', ''))}</li>")
        z.append("</ul>")
    z.append(markdown.markdown(w.get("_text", "")))
    return "\n".join(z)


def _json_faehig(x):
    if isinstance(x, date):
        return x.isoformat()
    if isinstance(x, dict):
        return {k: _json_faehig(v) for k, v in x.items() if not k.startswith("_") or k == "_bewertung"}
    if isinstance(x, list):
        return [_json_faehig(v) for v in x]
    return x


def seiten_schreiben(meta: dict, bewertet: dict, ausgabe: Path, build_zeit: str) -> list[Path]:
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

    koerper = [f"<h1>{_e(titel)}</h1>",
               f'<p class="mute">Halter: {_e(meta.get("halter", ""))} · seit {datum(meta.get("seit"))} · Format {_e(meta.get("format", ""))}</p>',
               markdown.markdown(meta.get("_text", "")),
               "<h2>Rangliste</h2>", _tabelle_html(bewertet["tabelle"], bewertet["rang_ab"]),
               "<h2>Alle Wetten</h2>", _wettenliste_html(bewertet["wetten"], 0)]
    schreib("index.html", _seite("Rangliste", "\n".join(koerper), 0, build_zeit, titel))

    nach_inst: dict[str, list[dict]] = {}
    for w in bewertet["wetten"]:
        nach_inst.setdefault(w["institution"], []).append(w)

    slugs: dict[str, str] = {}
    for inst in nach_inst:
        s = slug(inst)
        if s in slugs and slugs[s] != inst:
            raise ValueError(f"Slug-Kollision: {inst!r} und {slugs[s]!r} ergeben beide {s!r}")
        slugs[s] = inst

    for inst, ws in nach_inst.items():
        koerper = [f"<h1>{_e(inst)}</h1>", _wettenliste_html(ws, 1)]
        schreib(f"institution/{slug(inst)}.html", _seite(inst, "\n".join(koerper), 1, build_zeit, titel))

    for w in bewertet["wetten"]:
        schreib(f"wette/{w['id']}.html", _seite(w["frage"], _wette_html(w), 1, build_zeit, titel))

    daten = {"format": "v1", "titel": titel, "halter": meta.get("halter"), "gebaut": build_zeit,
             "tabelle": bewertet["tabelle"], "wetten": _json_faehig(bewertet["wetten"])}
    schreib("wettbuch.json", json.dumps(daten, ensure_ascii=False, indent=2))
    return geschrieben
