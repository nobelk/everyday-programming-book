"""Advanced problem 41 — Cantilever Beam Tip Deflection (imperative)

Subject: Engineering. Style: imperative.

Problem
-------
A cantilever beam of length L, with point load P at the free end, deflects by `δ = P L³ / (3 E I)`. For a steel beam (E = 200 GPa, I = 1.0×10⁻⁶ m⁴) and L = 2 m, print deflection for loads from 1 to 10 kN.

Concepts taught
---------------
Loop with unit conversion, table-style formatting.

Expected output
---------------
Load (kN) | Deflection (mm)
------------------------------
        1 |        13.3333
        2 |        26.6667
        3 |        40.0000
        4 |        53.3333
        5 |        66.6667
        6 |        80.0000
        7 |        93.3333
        8 |       106.6667
        9 |       120.0000
       10 |       133.3333
"""


E = 200e9        # Pa
I = 1.0e-6       # m^4
L = 2.0          # m

print("Load (kN) | Deflection (mm)")
print("-" * 30)
for P_kN in range(1, 11):
    P = P_kN * 1000.0
    delta = P * L ** 3 / (3 * E * I)
    print(f"{P_kN:>9} | {delta * 1000:>14.4f}")
