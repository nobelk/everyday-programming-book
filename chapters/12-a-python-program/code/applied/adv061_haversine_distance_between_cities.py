"""Advanced problem 61 — Haversine Distance Between Cities (imperative)

Subject: Geography. Style: imperative.

Problem
-------
Compute the great-circle distance between cities given their latitude/longitude (degrees), using the Haversine formula. Earth radius 6371 km.

Concepts taught
---------------
Function with multiple parameters, nested loops with indices, argument unpacking.

Expected output
---------------
 New York ↔ London   :   5570.2 km
 New York ↔ Tokyo    :  10848.8 km
 New York ↔ Sydney   :  15988.8 km
   London ↔ Tokyo    :   9558.7 km
   London ↔ Sydney   :  16993.9 km
    Tokyo ↔ Sydney   :   7826.6 km
"""


from math import radians, sin, cos, asin, sqrt

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlam = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlam / 2) ** 2
    return 2 * R * asin(sqrt(a))

cities = {
    "New York":  (40.7128,  -74.0060),
    "London":    (51.5074,   -0.1278),
    "Tokyo":     (35.6895,  139.6917),
    "Sydney":    (-33.8688, 151.2093),
}

names = list(cities)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a, b = names[i], names[j]
        d = haversine_km(*cities[a], *cities[b])
        print(f"{a:>9} ↔ {b:<9}: {d:>8.1f} km")
