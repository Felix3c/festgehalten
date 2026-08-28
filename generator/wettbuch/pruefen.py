"""Regeln aus FORMAT.md §1–2 prüfen. Wirft nicht, sammelt Fehler."""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from numbers import Real

ID_MUSTER = re.compile(r"^[a-z0-9][a-z0-9-]*$")
PFLICHT = [
    "id", "institution", "gesagt_von", "gesagt_am", "quelle", "zitat", "frage",
    "typ", "pruefung_am", "prognosen", "ausgang", "aufgeloest_am",
    "beleg_ausgang", "vermerke",
]
TYPEN = {"ja_nein", "punkt"}
ARTEN = {"angekuendigt", "voraussichtlich", "geschaetzt"}
FESTE_WERTE = {"angekuendigt": 1.0, "voraussichtlich": 0.8}
META_PFLICHT = ["titel", "halter", "seit", "format"]
NICHT_AUFGELOEST = {"verfallen", "strittig"}


@dataclass(frozen=True)
class Fehler:
    datei: str
    feld: str
    text: str


def _ist_datum(x) -> bool:
    return isinstance(x, date)


def _ist_zahl(x) -> bool:
    return isinstance(x, Real) and not isinstance(x, bool)


def _ist_url(x) -> bool:
    return isinstance(x, str) and (x.startswith("http://") or x.startswith("https://"))


def _prognosen_pruefen(d: str, typ: str, prognosen) -> list[Fehler]:
    f: list[Fehler] = []
    if not isinstance(prognosen, list) or not prognosen:
        return [Fehler(d, "prognosen", "muss eine Liste mit mindestens einem Eintrag sein")]
    for i, p in enumerate(prognosen):
        pf = f"prognosen[{i}]"
        if not isinstance(p, dict):
            f.append(Fehler(d, pf, "muss ein Mapping sein"))
            continue
        fehlend = [k for k in ("von", "wert", "hinterlegt_am", "art") if k not in p]
        for k in fehlend:
            f.append(Fehler(d, f"{pf}.{k}", "fehlt"))
        if fehlend:
            continue
        if not isinstance(p["von"], str):
            f.append(Fehler(d, f"{pf}.von", "muss Text sein"))
        if not isinstance(p["art"], str) or p["art"] not in ARTEN:
            f.append(Fehler(d, f"{pf}.art", f"muss angekuendigt, voraussichtlich oder geschaetzt sein, ist {p['art']!r}"))
        if not _ist_datum(p["hinterlegt_am"]):
            f.append(Fehler(d, f"{pf}.hinterlegt_am", "muss ein Datum sein"))
        if not _ist_zahl(p["wert"]):
            f.append(Fehler(d, f"{pf}.wert", "muss eine Zahl sein"))
            continue
        if typ == "ja_nein":
            if not 0 <= p["wert"] <= 1:
                f.append(Fehler(d, f"{pf}.wert", "muss bei ja_nein zwischen 0 und 1 liegen"))
            elif p["art"] in FESTE_WERTE and abs(p["wert"] - FESTE_WERTE[p["art"]]) > 1e-9:
                f.append(Fehler(d, f"{pf}.wert", f"bei art {p['art']} muss wert {FESTE_WERTE[p['art']]} sein"))

    von_gesehen: set[str] = set()
    for i, p in enumerate(prognosen):
        if isinstance(p, dict) and isinstance(p.get("von"), str):
            if p["von"] in von_gesehen:
                f.append(Fehler(d, f"prognosen[{i}].von", "von doppelt in dieser Wette"))
            else:
                von_gesehen.add(p["von"])
    return f


def _ausgang_pruefen(d: str, w: dict) -> list[Fehler]:
    f: list[Fehler] = []
    a = w["ausgang"]
    if a is None or (isinstance(a, str) and a in NICHT_AUFGELOEST):
        return f
    if not _ist_zahl(a):
        return [Fehler(d, "ausgang", "muss null, 0, 1, Zahl, 'verfallen' oder 'strittig' sein")]
    if w["typ"] == "ja_nein" and a not in (0, 1):
        f.append(Fehler(d, "ausgang", "bei ja_nein nur 0 oder 1"))
    if w["beleg_ausgang"] is None:
        f.append(Fehler(d, "beleg_ausgang", "Beleg-Pflicht: ausgang gesetzt, aber kein beleg_ausgang (FORMAT.md §2.1)"))
    if w["aufgeloest_am"] is None:
        f.append(Fehler(d, "aufgeloest_am", "ausgang gesetzt, aber kein aufgeloest_am"))
    return f


def _vermerke_pruefen(d: str, vermerke) -> list[Fehler]:
    f: list[Fehler] = []
    if not isinstance(vermerke, list):
        return [Fehler(d, "vermerke", "muss eine Liste sein")]
    for i, v in enumerate(vermerke):
        vf = f"vermerke[{i}]"
        if not isinstance(v, dict):
            f.append(Fehler(d, vf, "muss ein Mapping mit am und text sein"))
            continue
        if not _ist_datum(v.get("am")):
            f.append(Fehler(d, f"{vf}.am", "muss ein Datum sein"))
        if not isinstance(v.get("text"), str):
            f.append(Fehler(d, f"{vf}.text", "muss Text sein"))
    return f


def _wette_pruefen(w: dict) -> list[Fehler]:
    d = w.get("_datei", "?")
    fehlend = [feld for feld in PFLICHT if feld not in w]
    if fehlend:
        return [Fehler(d, feld, "Pflichtfeld fehlt") for feld in fehlend]

    f: list[Fehler] = []
    typ = w["typ"]
    if not isinstance(typ, str) or typ not in TYPEN:
        f.append(Fehler(d, "typ", f"muss ja_nein oder punkt sein, ist {typ!r}"))
    if not isinstance(w["id"], str) or not ID_MUSTER.match(w["id"]):
        f.append(Fehler(d, "id", "nur Kleinbuchstaben, Ziffern und Bindestrich, z. B. koeln-2025-001"))
    for feld in ("institution", "gesagt_von", "zitat", "frage"):
        if not isinstance(w[feld], str):
            f.append(Fehler(d, feld, "muss Text sein"))
    for feld in ("gesagt_am", "pruefung_am"):
        if not _ist_datum(w[feld]):
            f.append(Fehler(d, feld, "muss ein Datum YYYY-MM-DD sein"))
    if w["aufgeloest_am"] is not None and not _ist_datum(w["aufgeloest_am"]):
        f.append(Fehler(d, "aufgeloest_am", "muss ein Datum YYYY-MM-DD oder null sein"))
    if not _ist_url(w["quelle"]):
        f.append(Fehler(d, "quelle", "muss eine http(s)-URL sein"))
    if w["beleg_ausgang"] is not None and not _ist_url(w["beleg_ausgang"]):
        f.append(Fehler(d, "beleg_ausgang", "muss eine http(s)-URL oder null sein"))
    f.extend(_prognosen_pruefen(d, typ, w["prognosen"]))
    if typ == "punkt" and not w.get("einheit"):
        f.append(Fehler(d, "einheit", "bei typ punkt Pflicht (z. B. 'Mio EUR')"))
    f.extend(_ausgang_pruefen(d, w))
    if (_ist_datum(w["aufgeloest_am"]) and _ist_datum(w["pruefung_am"])
            and w["aufgeloest_am"] < w["pruefung_am"]):
        f.append(Fehler(d, "aufgeloest_am", "liegt vor pruefung_am (FORMAT.md §2.5)"))
    f.extend(_vermerke_pruefen(d, w["vermerke"]))
    return f


def _meta_pruefen(meta: dict) -> list[Fehler]:
    f = [Fehler("BUCH.md", k, "Pflichtfeld fehlt") for k in META_PFLICHT if k not in meta]
    for feld in ("titel", "halter"):
        if feld in meta and not isinstance(meta[feld], str):
            f.append(Fehler("BUCH.md", feld, "muss Text sein"))
    if "seit" in meta and not _ist_datum(meta["seit"]):
        f.append(Fehler("BUCH.md", "seit", "muss ein Datum YYYY-MM-DD sein, nicht in Anführungszeichen"))
    if "format" in meta and meta["format"] != "v1":
        f.append(Fehler("BUCH.md", "format", f"dieser Generator kennt nur v1, Buch sagt {meta['format']!r}"))
    return f


def buch_pruefen(buch: dict) -> list[Fehler]:
    fehler = _meta_pruefen(buch["meta"])
    gesehen: dict[str, str] = {}
    for w in buch["wetten"]:
        fehler.extend(_wette_pruefen(w))
        wid = str(w.get("id"))
        if wid in gesehen:
            fehler.append(Fehler(w.get("_datei", "?"), "id", f"doppelt, auch in {gesehen[wid]}"))
        else:
            gesehen[wid] = w.get("_datei", "?")
    return fehler
