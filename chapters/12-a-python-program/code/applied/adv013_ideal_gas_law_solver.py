"""Advanced problem 13 — Ideal Gas Law Solver (imperative)

Subject: Chemistry. Style: imperative.

Problem
-------
Three gas cylinders sit in a chemistry lab. Given their pressure (atm), volume (L), and temperature (K), compute the moles of gas in each using `PV = nRT` (R = 0.0821 L·atm/(mol·K)). Warn if the cylinder contains more than 5 mol (over-filled).

Concepts taught
---------------
List of dictionaries, formula evaluation, `if/else` with side-effect prints.

Expected output
---------------
Cylinder A: n=0.812 mol
Cylinder B: n=5.577 mol  ⚠ OVER-FILLED
Cylinder C: n=1.740 mol
"""


R = 0.0821
cylinders = [
    {"name": "A", "P": 2.0, "V": 10.0, "T": 300},
    {"name": "B", "P": 5.0, "V": 25.0, "T": 273},
    {"name": "C", "P": 1.0, "V": 50.0, "T": 350},
]

for c in cylinders:
    n = (c["P"] * c["V"]) / (R * c["T"])
    print(f"Cylinder {c['name']}: n={n:.3f} mol", end="")
    if n > 5:
        print("  ⚠ OVER-FILLED")
    else:
        print()
