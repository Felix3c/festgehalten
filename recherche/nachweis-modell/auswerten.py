"""Wertet ein Protokoll aus lauf.py aus: Wie nah liegt das lokale Modell am Claude-Wert?"""
import json, sys, pathlib, statistics, collections
pfad = pathlib.Path(sys.argv[1])
zeilen = [json.loads(z) for z in pfad.read_text(encoding="utf-8").splitlines() if z.strip()]
def zahl(x):
    try: return float(str(x).replace(",", "."))
    except Exception: return None
gesamt = len(zeilen); fehler = [z for z in zeilen if "fehler" in z or zahl(z.get("wert")) is None]
jn = [z for z in zeilen if z["typ"] == "ja_nein" and z not in fehler]
pk = [z for z in zeilen if z["typ"] == "punkt" and z not in fehler]
print(f"Protokoll {pfad.name}: {gesamt} Wetten, {len(fehler)} ohne verwertbare Antwort")
print(f"Dauer gesamt {sum(z['sekunden'] for z in zeilen)/3600:.1f} h, Median {statistics.median(z['sekunden'] for z in zeilen):.0f} s je Wette")
if jn:
    diffs = [abs(zahl(z["wert"]) - zahl(z["computer_claude"])) for z in jn if zahl(z["computer_claude"]) is not None]
    ausserhalb = sum(1 for z in jn if not 0 <= zahl(z["wert"]) <= 1)
    print(f"\nJa/Nein ({len(jn)}): mittlere Abweichung zu Claude {statistics.mean(diffs):.2f}, Median {statistics.median(diffs):.2f}, "
          f"max {max(diffs):.2f}; {sum(1 for d in diffs if d <= 0.10)} von {len(diffs)} binnen 0,10; {ausserhalb} Werte ausserhalb [0,1]")
if pk:
    rel = [abs(zahl(z["wert"]) - zahl(z["computer_claude"])) / abs(zahl(z["computer_claude"])) for z in pk if zahl(z["computer_claude"]) not in (None, 0)]
    print(f"\nPunkt ({len(pk)}): relative Abweichung zu Claude Median {statistics.median(rel):.0%}, {sum(1 for r in rel if r <= 0.15)} von {len(rel)} binnen 15 %")
print("\nKlassen (lokal):")
for k, n in collections.Counter(z.get("klasse", "?")[:60] for z in zeilen).most_common(15): print(f"  {n:3d}  {k}")
if fehler:
    print("\nOhne verwertbare Antwort:"); [print("  ", z["id"], str(z.get("fehler", z.get("wert")))[:80]) for z in fehler]
