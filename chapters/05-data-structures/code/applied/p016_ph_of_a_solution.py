"""Problem 16 — pH of a solution

Domain: Chemistry. Chapter 5 (Data Structures), variables.

Problem
-------
The hydrogen-ion concentration of lemon juice is 1e-2 mol/L. Compute `pH = −log10([H⁺])`.

Expected output
---------------
pH: 2.0
"""


import math
h_concentration = 1e-2
ph = -math.log10(h_concentration)
print(f"pH: {ph}")
