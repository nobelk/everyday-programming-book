"""Advanced problem 60 — Geothermal Gradient (functional)

Subject: Geology. Style: functional.

Problem
-------
The temperature inside the Earth rises about 25 °C per km on average. Given a surface temperature of 15 °C, compute the temperature at depths 0, 1, 2, 5, 10, 20 km.

Concepts taught
---------------
Lambda with closure, `map`, immutable inputs.

Expected output
---------------
depth= 0 km → T=  15 °C
depth= 1 km → T=  40 °C
depth= 2 km → T=  65 °C
depth= 5 km → T= 140 °C
depth=10 km → T= 265 °C
depth=20 km → T= 515 °C
"""


surface_T, gradient = 15, 25
depths_km = [0, 1, 2, 5, 10, 20]

temp_at = lambda d: surface_T + gradient * d
table = list(map(lambda d: (d, temp_at(d)), depths_km))

for d, T in table:
    print(f"depth={d:>2} km → T={T:>4} °C")
