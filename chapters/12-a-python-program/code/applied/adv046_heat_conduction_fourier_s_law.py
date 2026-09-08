"""Advanced problem 46 — Heat Conduction (Fourier's Law) (functional)

Subject: Engineering. Style: functional.

Problem
-------
Compute heat flow `Q = k · A · ΔT / L` through walls of several materials: brick (k=0.7), wood (0.13), glass (1.0), insulation (0.04). Wall area 10 m², thickness 0.1 m, ΔT = 25 °C.

Concepts taught
---------------
`map` + `sorted` with `key=lambda`, pure function.

Expected output
---------------
 insulation: Q =  100.00 W
       wood: Q =  325.00 W
      brick: Q = 1750.00 W
      glass: Q = 2500.00 W
"""


A, L, dT = 10, 0.1, 25
materials = [("brick", 0.7), ("wood", 0.13),
             ("glass", 1.0), ("insulation", 0.04)]

heat_flow = lambda k: k * A * dT / L
results = list(map(lambda m: (m[0], heat_flow(m[1])), materials))

for name, Q in sorted(results, key=lambda x: x[1]):
    print(f"{name:>11}: Q = {Q:7.2f} W")
