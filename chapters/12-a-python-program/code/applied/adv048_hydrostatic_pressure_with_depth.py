"""Advanced problem 48 — Hydrostatic Pressure with Depth (functional)

Subject: Engineering. Style: functional.

Problem
-------
Compute hydrostatic pressure `P = ρ g h` (gauge, Pa) at depths 0, 5, 10, 25, 50, 100 m in seawater (ρ = 1025 kg/m³). Convert each to atmospheres (1 atm ≈ 101325 Pa).

Concepts taught
---------------
Function composition (one lambda calling another), comprehension, thousands-separator formatting.

Expected output
---------------
depth=   0 m →         0 Pa  ( 0.00 atm)
depth=   5 m →    50,276 Pa  ( 0.50 atm)
depth=  10 m →   100,552 Pa  ( 0.99 atm)
depth=  25 m →   251,381 Pa  ( 2.48 atm)
depth=  50 m →   502,762 Pa  ( 4.96 atm)
depth= 100 m → 1,005,525 Pa  ( 9.92 atm)
"""


rho, g = 1025, 9.81
depths = [0, 5, 10, 25, 50, 100]

pressure = lambda h: rho * g * h
to_atm = lambda Pa: Pa / 101325
table = [(h, pressure(h), to_atm(pressure(h))) for h in depths]

for h, Pa, atm in table:
    print(f"depth={h:>4} m → {Pa:>9,.0f} Pa  ({atm:5.2f} atm)")
