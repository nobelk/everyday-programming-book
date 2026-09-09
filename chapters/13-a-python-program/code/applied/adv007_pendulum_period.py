"""Advanced problem 7 — Pendulum Period (imperative)

Subject: Physics. Style: imperative.

Problem
-------
A grandfather-clock pendulum has lengths from 0.5 m to 2.0 m in 0.25 m steps. Print the period `T = 2π √(L/g)` and identify which length gives a period closest to 2 seconds (the classic "seconds pendulum").

Concepts taught
---------------
`while` loop with floating-point step, accumulator pattern (track best so far), `abs`, sentinel value (`float('inf')`).

Expected output
---------------
L=0.50 m → T=1.419 s
L=0.75 m → T=1.737 s
L=1.00 m → T=2.006 s
L=1.25 m → T=2.243 s
L=1.50 m → T=2.457 s
L=1.75 m → T=2.654 s
L=2.00 m → T=2.837 s

Closest to 2s: L=1.00 m
"""


from math import pi, sqrt

g = 9.81
best_length = None
best_diff = float("inf")

length = 0.5
while length <= 2.0001:
    T = 2 * pi * sqrt(length / g)
    print(f"L={length:.2f} m → T={T:.3f} s")
    diff = abs(T - 2.0)
    if diff < best_diff:
        best_diff = diff
        best_length = length
    length += 0.25

print(f"\nClosest to 2s: L={best_length:.2f} m")
