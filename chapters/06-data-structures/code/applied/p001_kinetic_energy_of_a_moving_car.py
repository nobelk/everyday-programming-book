"""Problem 1 — Kinetic energy of a moving car

Domain: Physics. Chapter 6 (Data Structures), variables.

Problem
-------
A car of mass 1200 kg travels at 25 m/s. Compute its kinetic energy using `KE = 0.5 × m × v²`.

Expected output
---------------
Kinetic energy: 375000.0 J
"""


mass_kg = 1200
velocity_mps = 25
kinetic_energy_j = 0.5 * mass_kg * velocity_mps ** 2
print(f"Kinetic energy: {kinetic_energy_j} J")
