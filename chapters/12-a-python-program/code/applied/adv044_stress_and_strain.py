"""Advanced problem 44 — Stress and Strain (functional)

Subject: Engineering. Style: functional.

Problem
-------
A steel rod (cross-section 1×10⁻⁴ m², E = 200 GPa) is subjected to forces 5, 10, 20, 50, 100 kN. Compute stress (Pa) and strain (dimensionless) for each.

Concepts taught
---------------
Composing two pure functions, lambda calling another lambda, scientific-notation formatting.

Expected output
---------------
F=  5 kN  σ=5.00e+07 Pa  ε=2.5000e-04
F= 10 kN  σ=1.00e+08 Pa  ε=5.0000e-04
F= 20 kN  σ=2.00e+08 Pa  ε=1.0000e-03
F= 50 kN  σ=5.00e+08 Pa  ε=2.5000e-03
F=100 kN  σ=1.00e+09 Pa  ε=5.0000e-03
"""


A = 1e-4         # m^2
E = 200e9        # Pa
forces_kN = [5, 10, 20, 50, 100]

stress = lambda F: F * 1000 / A
strain = lambda F: stress(F) / E
table = list(map(lambda F: (F, stress(F), strain(F)), forces_kN))

for F, s, e in table:
    print(f"F={F:>3} kN  σ={s:.2e} Pa  ε={e:.4e}")
