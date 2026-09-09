"""Problem 64 — Body-surface area (Mosteller)

Domain: Biology. Chapter 11 (Functions), functions.

Problem
-------
`BSA = √(height × mass / 3600)` (height in cm, mass in kg).

Expected output
---------------
1.752
"""


import math

def bsa(height_cm, mass_kg):
    return math.sqrt(height_cm * mass_kg / 3600)

print(round(bsa(170, 65), 3))
