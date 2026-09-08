"""Advanced problem 69 — Decimal Degrees ↔ DMS Conversion (imperative)

Subject: Geography. Style: imperative.

Problem
-------
Convert decimal-degree coordinates to degrees-minutes-seconds (DMS) and back.

Concepts taught
---------------
Two cooperating functions, sign handling with conditional expression, returning multiple values via tuple.

Expected output
---------------
  40.7128° → 40° 42' 46.08"  (round-trip: 40.7128°)
 -74.0060° → -74° 0' 21.60"  (round-trip: -74.0060°)
  51.5074° → 51° 30' 26.64"  (round-trip: 51.5074°)
 -33.8688° → -33° 52'  7.68"  (round-trip: -33.8688°)
"""


def dd_to_dms(dd: float):
    sign = -1 if dd < 0 else 1
    dd = abs(dd)
    degrees = int(dd)
    minutes_full = (dd - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    return sign * degrees, minutes, seconds

def dms_to_dd(d: int, m: int, s: float) -> float:
    sign = -1 if d < 0 else 1
    return sign * (abs(d) + m / 60 + s / 3600)

for dd in [40.7128, -74.0060, 51.5074, -33.8688]:
    d, m, s = dd_to_dms(dd)
    dd_back = dms_to_dd(d, m, s)
    print(f"{dd:>9.4f}° → {d}° {m}' {s:5.2f}\"  (round-trip: {dd_back:.4f}°)")
