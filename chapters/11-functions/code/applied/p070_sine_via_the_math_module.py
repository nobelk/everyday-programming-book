"""Problem 70 — Sine via the math module

Domain: Mathematics. Chapter 11 (Functions), functions.

Problem
-------
Return the sine of an angle given in degrees.

Expected output
---------------
0.5
"""


import math

def sin_deg(angle_deg):
    return math.sin(math.radians(angle_deg))

print(round(sin_deg(30), 4))
