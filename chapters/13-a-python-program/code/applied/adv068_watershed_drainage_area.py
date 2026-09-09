"""Advanced problem 68 — Watershed Drainage Area (functional)

Subject: Geography. Style: functional.

Problem
-------
A watershed is divided into sub-basins with given areas (km²) and runoff coefficients. Compute the *effective* drainage area for each and the total.

Concepts taught
---------------
`map` with index access in a lambda, `reduce` for a projected sum.

Expected output
---------------
  Upper: effective area =  78.00 km²
 Middle: effective area =  49.50 km²
  Lower: effective area =  24.00 km²
  Marsh: effective area =   6.00 km²
  TOTAL:                  157.50 km²
"""


from functools import reduce

basins = [("Upper",  120, 0.65), ("Middle",  90, 0.55),
          ("Lower",   60, 0.40), ("Marsh",   30, 0.20)]

effective = list(map(lambda b: (b[0], b[1] * b[2]), basins))
total_eff = reduce(lambda acc, x: acc + x[1], effective, 0.0)

for name, ea in effective:
    print(f"{name:>7}: effective area = {ea:6.2f} km²")
print(f"{'TOTAL':>7}:                  {total_eff:6.2f} km²")
