"""Advanced problem 64 — Map-Scale Conversion (functional)

Subject: Geography. Style: functional.

Problem
-------
A map is at scale 1 : 50,000. For real distances of 100, 500, 1,000, 2,500, 10,000 m, compute the corresponding map distance in cm.

Concepts taught
---------------
Lambda capturing a constant, `map`, formatted output.

Expected output
---------------
   100 m on ground →  0.200 cm on map
   500 m on ground →  1.000 cm on map
  1000 m on ground →  2.000 cm on map
  2500 m on ground →  5.000 cm on map
 10000 m on ground → 20.000 cm on map
"""


scale = 50_000
real_distances_m = [100, 500, 1_000, 2_500, 10_000]

map_cm = lambda real_m: real_m * 100 / scale
table = list(map(lambda d: (d, map_cm(d)), real_distances_m))

for d_real, d_map in table:
    print(f"{d_real:>6} m on ground → {d_map:>6.3f} cm on map")
