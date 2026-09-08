"""Advanced problem 8 — Energy Conservation Down a Slide (functional)

Subject: Physics. Style: functional.

Problem
-------
A child slides down a 3 m tall slide. Assuming no friction, compute the speed at heights 3, 2.5, 2, 1.5, 1, 0.5, 0 m using `v = √(2 g (h_top - h))`.

Concepts taught
---------------
`reduce` for an aggregate (max), pure transformation via `map`, immutable data (`heights` never mutated).

Expected output
---------------
h=3.0 m → v=0.00 m/s
h=2.5 m → v=3.13 m/s
h=2.0 m → v=4.43 m/s
h=1.5 m → v=5.42 m/s
h=1.0 m → v=6.26 m/s
h=0.5 m → v=7.00 m/s
h=0.0 m → v=7.67 m/s
Max speed reached: 7.67 m/s
"""


from math import sqrt
from functools import reduce

g = 9.81
h_top = 3.0
heights = [3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]

speed_at = lambda h: sqrt(2 * g * (h_top - h))
table = list(map(lambda h: (h, speed_at(h)), heights))

max_speed = reduce(lambda acc, row: max(acc, row[1]), table, 0.0)

for h, v in table:
    print(f"h={h:.1f} m → v={v:.2f} m/s")
print(f"Max speed reached: {max_speed:.2f} m/s")
