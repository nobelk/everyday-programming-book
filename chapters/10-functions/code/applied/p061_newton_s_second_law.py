"""Problem 61 — Newton's second law

Domain: Physics. Chapter 10 (Functions), functions.

Problem
-------
Write `force(mass, acceleration)` returning `m × a`.

Expected output
---------------
98.0
"""


def force(mass_kg, acceleration_mps2):
    return mass_kg * acceleration_mps2

print(force(10, 9.8))
