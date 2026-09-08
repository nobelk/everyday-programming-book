"""Advanced problem 54 — Sediment Transport Rate (Stokes) (functional)

Subject: Geology. Style: functional.

Problem
-------
Stokes' settling velocity for a small particle in water is `v = (2/9) · (ρ_p − ρ_f) · g · r² / μ`. Compute v for grain radii [1e-5, 5e-5, 1e-4, 5e-4, 1e-3] m, with quartz density 2650, water 1000, viscosity 1e-3 Pa·s.

Concepts taught
---------------
`filter` with predicate, comprehension, lambda.

Expected output
---------------
r=1e-05 m → v=3.5970e-04 m/s
r=5e-05 m → v=8.9925e-03 m/s
r=1e-04 m → v=3.5970e-02 m/s
r=5e-04 m → v=8.9925e-01 m/s
r=1e-03 m → v=3.5970e+00 m/s
Fast settlers (>1 cm/s): ['1e-04', '5e-04', '1e-03']
"""


rho_p, rho_f, g, mu = 2650, 1000, 9.81, 1e-3
radii = [1e-5, 5e-5, 1e-4, 5e-4, 1e-3]

velocity = lambda r: (2 / 9) * (rho_p - rho_f) * g * r ** 2 / mu
table = [(r, velocity(r)) for r in radii]
fast = list(filter(lambda x: x[1] > 0.01, table))

for r, v in table:
    print(f"r={r:.0e} m → v={v:.4e} m/s")
print("Fast settlers (>1 cm/s):", [f"{r:.0e}" for r, _ in fast])
