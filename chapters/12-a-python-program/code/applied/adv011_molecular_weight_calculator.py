"""Advanced problem 11 — Molecular Weight Calculator (imperative)

Subject: Chemistry. Style: imperative.

Problem
-------
Compute the molar mass of water (H₂O), carbon dioxide (CO₂), and glucose (C₆H₁₂O₆) given the atomic masses H=1.008, C=12.011, O=15.999.

Concepts taught
---------------
Dictionaries, nested iteration, accumulator pattern.

Expected output
---------------
H2O        → 18.015 g/mol
CO2        → 44.009 g/mol
C6H12O6    → 180.156 g/mol
"""


atomic_mass = {"H": 1.008, "C": 12.011, "O": 15.999}

def molar_mass(formula: dict) -> float:
    total = 0.0
    for element, count in formula.items():
        total += atomic_mass[element] * count
    return total

molecules = {
    "H2O":      {"H": 2, "O": 1},
    "CO2":      {"C": 1, "O": 2},
    "C6H12O6":  {"C": 6, "H": 12, "O": 6},
}

for name, formula in molecules.items():
    print(f"{name:10s} → {molar_mass(formula):.3f} g/mol")
