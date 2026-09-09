"""Problem 68 — Terminal velocity (simplified)

Domain: Physics. Chapter 11 (Functions), functions.

Problem
-------
`v_t = √(2 m g / (ρ A C))`.

Expected output
---------------
40.41
"""


import math

def terminal_velocity(mass_kg, air_density, area_m2, drag_coeff):
    return math.sqrt(2 * mass_kg * 9.8 / (air_density * area_m2 * drag_coeff))

print(round(terminal_velocity(70, 1.2, 0.7, 1.0), 2))
