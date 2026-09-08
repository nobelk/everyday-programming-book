"""Problem 78 — Oxygen consumption (METs)

Domain: Biology. Chapter 10 (Functions), functions.

Problem
-------
VO2 ≈ METs × 3.5 mL/kg/min. Convert to litres/min for a person of given mass.

Expected output
---------------
1.96
"""


def vo2_lpm(mets, mass_kg):
    return mets * 3.5 * mass_kg / 1000

print(round(vo2_lpm(8, 70), 3))
