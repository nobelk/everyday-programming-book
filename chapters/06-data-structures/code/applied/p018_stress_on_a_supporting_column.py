"""Problem 18 — Stress on a supporting column

Domain: Engineering. Chapter 6 (Data Structures), variables.

Problem
-------
A pillar supports 50 000 N over a cross-section of 0.25 m². Compute stress `σ = F / A`.

Expected output
---------------
Stress: 200000.0 Pa
"""


force_n = 50000
area_m2 = 0.25
stress_pa = force_n / area_m2
print(f"Stress: {stress_pa} Pa")
