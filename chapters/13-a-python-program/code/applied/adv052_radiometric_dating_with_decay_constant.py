"""Advanced problem 52 — Radiometric Dating with Decay Constant (functional)

Subject: Geology. Style: functional.

Problem
-------
Given parent isotope counts `[1000, 800, 600, 400, 200, 100]` in different rock samples, all starting from 1000 atoms, compute each sample's age using `t = -ln(N/N₀) / λ` with λ = 1.21×10⁻⁴ /yr (C-14).

Concepts taught
---------------
Lambda with conditional expression for the trivial case, `map`, immutable inputs.

Expected output
---------------
N= 1000 → age ≈          0 years
N=  800 → age ≈      1,844 years
N=  600 → age ≈      4,222 years
N=  400 → age ≈      7,573 years
N=  200 → age ≈     13,301 years
N=  100 → age ≈     19,030 years
"""


from math import log

N0 = 1000
decay_const = 1.21e-4
samples = [1000, 800, 600, 400, 200, 100]

age = lambda N: 0.0 if N == N0 else -log(N / N0) / decay_const
ages = list(map(lambda N: (N, age(N)), samples))

for N, t in ages:
    print(f"N={N:>5} → age ≈ {t:>10,.0f} years")
