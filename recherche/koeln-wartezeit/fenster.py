#!/usr/bin/env python3
"""Messfenster des Köln-Falls: die terminfreien Zeiten der Kundenzentren.

Laut Stadt Köln (und Wettentext koeln-2026-077 bis -082): Montag 7:30–15:00,
Mittwoch 7:30–12:00 Ortszeit. Nur Abrufe in diesen Fenstern sind
Vergleichswerte. Ein Lauf außerhalb (etwa GitHubs Zeitplan mit fünf Stunden
Verspätung, wie am Mi 16.09.2026 um 15:27) darf keine Zeile erzeugen.

Ein „Slot" ist ein Messplatz je Tag: „vormittag" (vor 12:00) und
„nachmittag" (ab 12:00, nur Montag). Je Slot höchstens ein Abruf, damit
mehrere Startversuche des Zeitplans keine doppelten Zeilen ergeben.

Nur Standardbibliothek.
"""
from __future__ import annotations

from datetime import datetime, time
from zoneinfo import ZoneInfo

ZEITZONE = ZoneInfo("Europe/Berlin")
MONTAG, MITTWOCH = 0, 2
FENSTER = {
    MONTAG: (time(7, 30), time(15, 0)),
    MITTWOCH: (time(7, 30), time(12, 0)),
}
MITTAG = time(12, 0)


def ortszeit(zeitpunkt: datetime) -> datetime:
    """Rechnet einen zeitzonenbewussten Zeitpunkt nach Europe/Berlin um."""
    if zeitpunkt.tzinfo is None:
        raise ValueError("Zeitpunkt braucht eine Zeitzone (aware datetime).")
    return zeitpunkt.astimezone(ZEITZONE)


def im_messfenster(zeitpunkt: datetime) -> bool:
    """True, wenn der Zeitpunkt in eine terminfreie Zeit der Stadt fällt."""
    lokal = ortszeit(zeitpunkt)
    grenzen = FENSTER.get(lokal.weekday())
    if grenzen is None:
        return False
    beginn, ende = grenzen
    return beginn <= lokal.time() < ende


def slot(zeitpunkt: datetime) -> str | None:
    """'vormittag', 'nachmittag' oder None (außerhalb des Messfensters)."""
    if not im_messfenster(zeitpunkt):
        return None
    return "vormittag" if ortszeit(zeitpunkt).time() < MITTAG else "nachmittag"


def slot_aus_cron(cron: str) -> str | None:
    """Slot aus dem Cron-Ausdruck, der den Lauf GEPLANT hat (github.event.schedule).

    Ein Vormittagslauf, den GitHub erst nach 12:00 startet, bleibt so ein
    Vormittagslauf und belegt nicht den Nachmittags-Slot. UTC-Stunde < 11
    heißt Vormittag (Cron-Einträge 06:37–09:27 UTC), sonst Nachmittag
    (11:17–12:13 UTC). Leer oder unlesbar: None, dann zählt die Uhrzeit.
    """
    teile = (cron or "").split()
    if len(teile) != 5 or not teile[1].isdigit():
        return None
    return "vormittag" if int(teile[1]) < 11 else "nachmittag"


def parse_abgerufen_am(text: str) -> datetime:
    """Liest die Spalte abgerufen_am (ISO 8601 mit Offset, wie messen.py sie schreibt)."""
    return datetime.fromisoformat(text)
