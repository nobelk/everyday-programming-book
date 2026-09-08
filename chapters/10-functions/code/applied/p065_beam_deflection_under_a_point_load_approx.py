"""Problem 65 — Beam deflection under a point load (approx.)

Domain: Engineering. Chapter 10 (Functions), functions.

Problem
-------
For a simply-supported beam with centre load: `δ = F L³ / (48 E I)`.

Expected output
---------------
0.000104 m
"""


def deflection(force_n, length_m, e_pa, inertia_m4):
    return force_n * length_m ** 3 / (48 * e_pa * inertia_m4)

print(f"{deflection(1000, 2, 2e11, 8e-6):.6f} m")
