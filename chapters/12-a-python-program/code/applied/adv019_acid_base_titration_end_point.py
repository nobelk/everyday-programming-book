"""Advanced problem 19 — Acid-Base Titration End-Point (imperative)

Subject: Chemistry. Style: imperative.

Problem
-------
You add 0.10 M NaOH dropwise (0.5 mL per drop) to 25 mL of 0.10 M HCl. Find how many drops are needed to reach the equivalence point (equal moles).

Concepts taught
---------------
`while` loop with stopping condition derived from calculation, mutating accumulators.

Expected output
---------------
Equivalence reached after 50 drops (25.0 mL of base added)
"""


acid_volume = 25.0       # mL
acid_M = 0.10
base_M = 0.10
drop_size = 0.5          # mL per drop

acid_moles = acid_volume * acid_M / 1000.0
drops = 0
base_volume = 0.0
base_moles = 0.0

while base_moles < acid_moles:
    base_volume += drop_size
    base_moles = base_volume * base_M / 1000.0
    drops += 1

print(f"Equivalence reached after {drops} drops "
      f"({base_volume} mL of base added)")
