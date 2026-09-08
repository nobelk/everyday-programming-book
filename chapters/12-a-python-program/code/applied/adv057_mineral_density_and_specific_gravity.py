"""Advanced problem 57 — Mineral Density and Specific Gravity (imperative)

Subject: Geology. Style: imperative.

Problem
-------
Given mass (g) and volume (cm³) of mineral specimens, compute density and specific gravity (relative to water = 1.00 g/cm³). Flag specimens denser than 5 g/cm³ as "metallic mineral candidate".

Concepts taught
---------------
Loop with conditional inline string, tuple unpacking.

Expected output
---------------
A: ρ= 2.75 g/cm³  SG=2.75
B: ρ= 7.00 g/cm³  SG=7.00  ← metallic candidate
C: ρ= 2.62 g/cm³  SG=2.62
D: ρ=11.00 g/cm³  SG=11.00  ← metallic candidate
"""


specimens = [("A", 27.5, 10.0), ("B", 84.0, 12.0),
             ("C", 17.0, 6.5),  ("D", 99.0, 9.0)]

for name, mass, vol in specimens:
    density = mass / vol
    sg = density / 1.0
    note = "  ← metallic candidate" if density > 5 else ""
    print(f"{name}: ρ={density:5.2f} g/cm³  SG={sg:.2f}{note}")
