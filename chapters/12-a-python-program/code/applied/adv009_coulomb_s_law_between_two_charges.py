"""Advanced problem 9 — Coulomb's Law Between Two Charges (imperative)

Subject: Physics. Style: imperative.

Problem
-------
Two small charged balls are placed at distances 0.05 m, 0.10 m, 0.20 m, and 0.50 m apart. Each carries 2 µC. Print the electrostatic force between them and label whether the force is *strong* (> 1 N) or *weak*.

Concepts taught
---------------
Scientific notation literals, looping with conditional labelling.

Expected output
---------------
d=0.05 m → F=14.3840 N (strong)
d=0.10 m → F=3.5960 N (strong)
d=0.20 m → F=0.8990 N (weak)
d=0.50 m → F=0.1438 N (weak)
"""


k = 8.99e9
q1 = 2e-6
q2 = 2e-6
distances = [0.05, 0.10, 0.20, 0.50]

for d in distances:
    F = k * q1 * q2 / d ** 2
    if F > 1.0:
        label = "strong"
    else:
        label = "weak"
    print(f"d={d:.2f} m → F={F:.4f} N ({label})")
