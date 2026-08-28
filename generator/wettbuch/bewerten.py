"""Mathematik aus FORMAT.md §3. Reine Funktionen über Dicts."""
from __future__ import annotations

RANG_AB = 10
NICHT_AUFGELOEST = {"verfallen", "strittig"}


def brier(wert: float, ausgang: int) -> float:
    return (wert - ausgang) ** 2


def abstand(wert: float, ausgang: float) -> float:
    return abs(wert - ausgang)


def _status(w: dict) -> str:
    a = w.get("ausgang")
    if a is None:
        return "offen"
    if a in NICHT_AUFGELOEST:
        return a
    return "aufgeloest"


def wette_bewerten(w: dict) -> dict:
    status = _status(w)
    scores: dict[str, float | None] = {p["von"]: None for p in w["prognosen"]}
    naeher: str | None = None
    if status == "aufgeloest":
        if w["typ"] == "ja_nein":
            for p in w["prognosen"]:
                scores[p["von"]] = brier(float(p["wert"]), int(w["ausgang"]))
        else:
            for p in w["prognosen"]:
                scores[p["von"]] = abstand(float(p["wert"]), float(w["ausgang"]))
            if len(w["prognosen"]) >= 2:
                naeher = min(sorted(scores), key=lambda k: scores[k])
    return {"status": status, "scores": scores, "naeher_dran": naeher}


def _neue_zeile(von: str) -> dict:
    return {
        "von": von, "ist_institution": False, "ja_nein_n": 0, "_ja_nein_summe": 0.0,
        "ja_nein_schnitt": None, "rang": None, "punkt_gewonnen": 0, "punkt_n": 0,
        "rechenschaft_verfallen": 0, "wetten_gesamt": 0,
    }


def buch_bewerten(buch: dict) -> dict:
    wetten: list[dict] = []
    zeilen: dict[str, dict] = {}

    for roh in buch["wetten"]:
        b = wette_bewerten(roh)
        w = {**roh, "_bewertung": b}
        wetten.append(w)

        inst = zeilen.setdefault(w["institution"], _neue_zeile(w["institution"]))
        inst["ist_institution"] = True
        inst["wetten_gesamt"] += 1
        if b["status"] in NICHT_AUFGELOEST:
            inst["rechenschaft_verfallen"] += 1

        for p in w["prognosen"]:
            z = zeilen.setdefault(p["von"], _neue_zeile(p["von"]))
            s = b["scores"][p["von"]]
            if b["status"] != "aufgeloest" or s is None:
                continue
            if w["typ"] == "ja_nein":
                z["ja_nein_n"] += 1
                z["_ja_nein_summe"] += s
            elif b["naeher_dran"] is not None:
                z["punkt_n"] += 1
                if b["naeher_dran"] == p["von"]:
                    z["punkt_gewonnen"] += 1

    for z in zeilen.values():
        if z["ja_nein_n"]:
            z["ja_nein_schnitt"] = z["_ja_nein_summe"] / z["ja_nein_n"]
        del z["_ja_nein_summe"]

    mit_rang = sorted(
        (z for z in zeilen.values() if z["ja_nein_n"] >= RANG_AB),
        key=lambda z: (z["ja_nein_schnitt"], z["von"]),
    )
    for i, z in enumerate(mit_rang, start=1):
        z["rang"] = i
    ohne_rang = sorted(
        (z for z in zeilen.values() if z["ja_nein_n"] < RANG_AB),
        key=lambda z: (-z["ja_nein_n"], z["von"]),
    )
    return {"wetten": wetten, "tabelle": mit_rang + ohne_rang, "rang_ab": RANG_AB}
