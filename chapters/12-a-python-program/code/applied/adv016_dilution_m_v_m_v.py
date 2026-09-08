"""Advanced problem 16 — Dilution (M₁V₁ = M₂V₂) (functional)

Subject: Chemistry. Style: functional.

Problem
-------
A lab has 2.0 M HCl stock. They want 100 mL each at 0.1, 0.5, and 1.0 M. Compute the volume of stock needed for each target and the water to add.

Concepts taught
---------------
Lambda with closure over constants, comprehension that yields a 3-tuple per element.

Expected output
---------------
0.1 M: take  5.00 mL stock + 95.00 mL water
0.5 M: take 25.00 mL stock + 75.00 mL water
1.0 M: take 50.00 mL stock + 50.00 mL water
"""


stock_molarity = 2.0
target_volume = 100.0
target_molarities = [0.1, 0.5, 1.0]

stock_needed = lambda M2: (M2 * target_volume) / stock_molarity
plan = [(M2, stock_needed(M2), target_volume - stock_needed(M2))
        for M2 in target_molarities]

for M2, stock, water in plan:
    print(f"{M2} M: take {stock:5.2f} mL stock + {water:5.2f} mL water")
