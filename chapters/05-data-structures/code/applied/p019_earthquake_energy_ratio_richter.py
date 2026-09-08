"""Problem 19 — Earthquake energy ratio (Richter)

Domain: Geology. Chapter 5 (Data Structures), variables.

Problem
-------
Two earthquakes differ by 2 magnitudes. Compute the energy ratio ≈ `10^(1.5 × 2)`.

Expected output
---------------
Energy ratio: 1000.0
"""


magnitude_difference = 2
energy_ratio = 10 ** (1.5 * magnitude_difference)
print(f"Energy ratio: {energy_ratio}")
