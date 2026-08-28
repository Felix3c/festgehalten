"""Dateien lesen. Kennt YAML und Markdown, sonst nichts."""
from __future__ import annotations

from pathlib import Path

import yaml


class LeseFehler(Exception):
    def __init__(self, datei: str, text: str):
        super().__init__(f"{datei}: {text}")
        self.datei = datei
        self.text = text


def _kopf_und_text(pfad: Path) -> tuple[dict, str]:
    roh = pfad.read_text(encoding="utf-8")
    if not roh.startswith("---"):
        raise LeseFehler(pfad.name, "kein YAML-Kopf (Datei beginnt nicht mit ---)")
    teile = roh.split("\n---", 1)
    if len(teile) < 2:
        raise LeseFehler(pfad.name, "YAML-Kopf nicht geschlossen (zweites --- fehlt)")
    kopf_roh = teile[0][3:]
    text = teile[1].lstrip("\n")
    try:
        kopf = yaml.safe_load(kopf_roh) or {}
    except yaml.YAMLError as e:
        raise LeseFehler(pfad.name, f"YAML ungültig: {e}") from e
    if not isinstance(kopf, dict):
        raise LeseFehler(pfad.name, "YAML-Kopf ist kein Mapping")
    return kopf, text


def wette_lesen(pfad: Path) -> dict:
    kopf, text = _kopf_und_text(pfad)
    kopf["_datei"] = pfad.name
    kopf["_text"] = text
    return kopf


AUSGESCHLOSSEN = {"BUCH.md", "README.md", "FORMAT.md"}


def buch_lesen(ordner: Path) -> dict:
    buch_md = ordner / "BUCH.md"
    if not buch_md.exists():
        raise LeseFehler("BUCH.md", f"nicht gefunden in {ordner}")
    meta, meta_text = _kopf_und_text(buch_md)
    meta["_text"] = meta_text

    wetten: list[dict] = []
    for pfad in sorted(ordner.rglob("*.md")):
        if pfad.name in AUSGESCHLOSSEN:
            continue
        if "docs" in pfad.relative_to(ordner).parts:
            continue
        wetten.append(wette_lesen(pfad))
    wetten.sort(key=lambda w: str(w.get("id", "")))
    return {"meta": meta, "wetten": wetten, "ordner": ordner}
