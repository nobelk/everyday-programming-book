"""Problem 67 — Great-circle distance (simplified flat-earth)

Domain: Geography. Chapter 10 (Functions), functions.

Problem
-------
For small distances, `d ≈ √(Δx² + Δy²)`, treating 1° ≈ 111 km.

Expected output
---------------
1157.5
"""


import math

def approx_distance_km(lat1, lon1, lat2, lon2):
    dx_km = (lon2 - lon1) * 111
    dy_km = (lat2 - lat1) * 111
    return math.sqrt(dx_km ** 2 + dy_km ** 2)

print(round(approx_distance_km(28.6, 77.2, 19.1, 72.9), 1))  # Delhi → Mumbai rough
