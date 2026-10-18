"""Anzeigetexte je Sprache (FORMAT.md §4, optionales Feld `sprache` in BUCH.md).

Nur die Anzeige wechselt. Feldnamen und feste Werte in den Dateien (`angekuendigt`, `ja_nein` …)
bleiben deutsch, weil sie Teil von Format v1 sind. Monatsnamen stehen hier von Hand statt über
`locale`, damit der Bau auf jedem Rechner dasselbe Ergebnis gibt."""
from __future__ import annotations

from datetime import date

STANDARD = "de"
SPRACHEN = ("de", "en")

MONATE_EN = ("January", "February", "March", "April", "May", "June", "July", "August",
             "September", "October", "November", "December")

TEXTE: dict[str, dict[str, str]] = {
    "de": {
        "feed_titel": "neu aufgelöst",
        "fuss_format": "festgehalten-Format v1 · gebaut {zeit}",
        "ersetzt_durch": "ersetzt durch",
        "offen": "offen",
        "beleg_gesucht": "Beleg gesucht, zuletzt {datum}",
        "ja": "ja",
        "nein": "nein",
        "rang": "Rang",
        "wer": "Wer",
        "trefferquote": "Trefferquote (Brier)",
        "ja_nein_aufgeloest": "Ja/Nein aufgelöst",
        "naeher_dran_spalte": "Näher dran",
        "rechenschaft": "Rechenschaft (verfallen/strittig)",
        "wetten_als_institution": "Wetten als Institution",
        "kein_rang": "noch kein Rang (ab {n})",
        "von_n": "{a} von {b}",
        "wette": "Wette",
        "institution": "Institution",
        "gesagt_am": "gesagt am",
        "pruefung_ab": "Prüfung ab",
        "herkunft": "Herkunft",
        "ausgang": "Ausgang",
        "quelle": "Quelle",
        "typ": "Typ",
        "status": "Status",
        "prognose": "Prognose",
        "art": "Art",
        "hinterlegt_am": "hinterlegt am",
        "score": "Score",
        "ersetzt_satz": "Dieser Eintrag wurde ersetzt durch {link} und wird nicht mehr aufgelöst (FORMAT.md §1.3.3).",
        "naeher_dran": "näher dran",
        "aufgeloest_am": "Aufgelöst am",
        "beleg": "Beleg",
        "vermerke": "Vermerke",
        "halter": "Halter",
        "seit": "seit",
        "format": "Format",
        "lizenz": "Lizenz",
        "rangliste": "Rangliste",
        "alle_wetten": "Alle Wetten",
        "abonnieren": "Abonnieren: <a href=\"feed.xml\">Feed „neu aufgelöst“</a> (Atom)",
        "feed_ausgang": "Ausgang",
        "feed_beleg": "Beleg",
        "feed_ja": "Ja",
        "feed_nein": "Nein",
        "zitat_auf": "„",
        "zitat_zu": "“",
    },
    "en": {
        "feed_titel": "newly resolved",
        "fuss_format": "festgehalten format v1 · built {zeit}",
        "ersetzt_durch": "replaced by",
        "offen": "open",
        "beleg_gesucht": "evidence searched, last on {datum}",
        "ja": "yes",
        "nein": "no",
        "rang": "Rank",
        "wer": "Who",
        "trefferquote": "Accuracy (Brier)",
        "ja_nein_aufgeloest": "Yes/no resolved",
        "naeher_dran_spalte": "Closer",
        "rechenschaft": "Accountability (lapsed/disputed)",
        "wetten_als_institution": "Bets as institution",
        "kein_rang": "no rank yet (from {n})",
        "von_n": "{a} of {b}",
        "wette": "Bet",
        "institution": "Institution",
        "gesagt_am": "said on",
        "pruefung_ab": "Check from",
        "herkunft": "Origin",
        "ausgang": "Outcome",
        "quelle": "Source",
        "typ": "Type",
        "status": "Status",
        "prognose": "Forecast",
        "art": "Kind",
        "hinterlegt_am": "filed on",
        "score": "Score",
        "ersetzt_satz": "This entry was replaced by {link} and will no longer be resolved (FORMAT.md §1.3.3).",
        "naeher_dran": "closer",
        "aufgeloest_am": "Resolved on",
        "beleg": "Evidence",
        "vermerke": "Notes",
        "halter": "Keeper",
        "seit": "since",
        "format": "Format",
        "lizenz": "Licence",
        "rangliste": "Ranking",
        "alle_wetten": "All bets",
        "abonnieren": "Subscribe: <a href=\"feed.xml\">feed “newly resolved”</a> (Atom)",
        "feed_ausgang": "Outcome",
        "feed_beleg": "Evidence",
        "feed_ja": "Yes",
        "feed_nein": "No",
        "zitat_auf": "“",
        "zitat_zu": "”",
    },
}

# Feste Werte aus Format v1, nur für die Anzeige. Deutsch zeigt sie wie bisher roh.
WERTE: dict[str, dict[str, str]] = {
    "de": {k: k for k in ("ja_nein", "punkt", "angekuendigt", "voraussichtlich", "geschaetzt",
                          "zitiert", "hinterlegt", "verfallen", "strittig", "ersetzt", "offen", "aufgeloest")},
    "en": {"ja_nein": "yes/no", "punkt": "number", "angekuendigt": "announced",
           "voraussichtlich": "expected", "geschaetzt": "estimated", "zitiert": "quoted",
           "hinterlegt": "filed", "verfallen": "lapsed", "strittig": "disputed",
           "ersetzt": "replaced", "offen": "open", "aufgeloest": "resolved"},
}


def von_meta(meta: dict) -> str:
    """Sprache eines Buchs; fehlt das Feld, Deutsch. Ungültige Werte fängt `pruefen` ab."""
    s = meta.get("sprache", STANDARD)
    return s if s in SPRACHEN else STANDARD


def t(sprache: str, schluessel: str, **werte) -> str:
    text = TEXTE[sprache][schluessel]
    return text.format(**werte) if werte else text


def wert(x, sprache: str) -> str:
    return WERTE[sprache].get(str(x), str(x))


def datum(d, sprache: str = STANDARD) -> str:
    if not isinstance(d, date):
        return "–"
    if sprache == "en":
        return f"{d.day} {MONATE_EN[d.month - 1]} {d.year}"
    return d.strftime("%d.%m.%Y")


def zahl(x, stellen: int = 2, sprache: str = STANDARD) -> str:
    if x is None:
        return "–"
    text = f"{x:.{stellen}f}"
    return text if sprache == "en" else text.replace(".", ",")
