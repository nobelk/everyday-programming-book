"""Advanced problem 2 — Projectile Range Table (functional)

Subject: Physics. Style: functional.

Problem
-------
A water-rocket launches at 25 m/s. Compute the horizontal range for launch angles 10°, 20°, … 80°. Range is `R = v² sin(2θ) / g`.

Concepts taught
---------------
Pure functions (no side effects in the math), `lambda`, `map` over a numeric range, tuple packing, list comprehension alternative expressed via `map`.

Expected output
---------------
 10° →  21.79 m
 20° →  40.95 m
 30° →  55.17 m
 40° →  62.74 m
 50° →  62.74 m
 60° →  55.17 m
 70° →  40.95 m
 80° →  21.79 m
"""


from math import sin, radians

velocity = 25.0
gravity = 9.81

ranges = list(map(
    lambda angle_deg: (angle_deg,
                       velocity ** 2 * sin(radians(2 * angle_deg)) / gravity),
    range(10, 81, 10),
))

for angle, r in ranges:
    print(f"{angle:>3}° → {r:6.2f} m")
