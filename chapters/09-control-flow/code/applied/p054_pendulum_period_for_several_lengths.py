"""Problem 54 — Pendulum period for several lengths

Domain: Physics. Chapter 9 (Control Flow), loops.

Problem
-------
`T = 2π √(L / g)`. Print the period for L = 0.5, 1.0, 1.5, 2.0 m.

Expected output
---------------
L = 0.5 m → T = 1.419 s
L = 1.0 m → T = 2.007 s
L = 1.5 m → T = 2.458 s
L = 2.0 m → T = 2.838 s
"""


import math
g = 9.8
for length_m in [0.5, 1.0, 1.5, 2.0]:
    period_s = 2 * math.pi * math.sqrt(length_m / g)
    print(f"L = {length_m} m → T = {period_s:.3f} s")
