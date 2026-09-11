"""Advanced problem 36 — Photosynthesis Light Response (functional)

Subject: Biology. Style: functional.

Problem
-------
A leaf's photosynthesis rate (µmol CO₂/m²/s) follows `P = P_max · I / (I + K)` where `P_max = 25`, `K = 200`. Compute the rate at light intensities `[50, 100, 200, 400, 800, 1600]` µmol/m²/s.

Concepts taught
---------------
Lambda, comprehension, `filter` with predicate that references an outer constant.

Expected output
---------------
I=  50 → P= 5.00
I= 100 → P= 8.33
I= 200 → P=12.50
I= 400 → P=16.67
I= 800 → P=20.00
I=1600 → P=22.22
Light-saturated points: []
"""


P_max, K = 25, 200
intensities = [50, 100, 200, 400, 800, 1600]

rate = lambda I: P_max * I / (I + K)
results = [(I, rate(I)) for I in intensities]
saturating = list(filter(lambda x: x[1] > 0.9 * P_max, results))

for I, P in results:
    print(f"I={I:>4} → P={P:5.2f}")
print("Light-saturated points:", [I for I, _ in saturating])
