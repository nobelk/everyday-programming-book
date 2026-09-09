"""Advanced problem 70 — Wind Chill Calculator (functional)

Subject: Geography. Style: functional.

Problem
-------
The wind-chill index (Environment Canada formula, Celsius) is `WC = 13.12 + 0.6215·T − 11.37·V^0.16 + 0.3965·T·V^0.16`, valid for T ≤ 10 °C and V ≥ 4.8 km/h. Compute WC for combinations of T = [0, -5, -10, -20] °C and V = [10, 20, 40] km/h.

Concepts taught
---------------
`itertools.product` for Cartesian-product combinations, lambda with two parameters, `filter` with multi-field predicate.

Expected output
---------------
T=  0°C V= 10 km/h → WC= -3.31 °C
T=  0°C V= 20 km/h → WC= -5.24 °C
T=  0°C V= 40 km/h → WC= -7.40 °C
T= -5°C V= 10 km/h → WC= -9.29 °C
T= -5°C V= 20 km/h → WC=-11.55 °C
T= -5°C V= 40 km/h → WC=-14.08 °C
T=-10°C V= 10 km/h → WC=-15.26 °C
T=-10°C V= 20 km/h → WC=-17.86 °C
T=-10°C V= 40 km/h → WC=-20.77 °C
T=-20°C V= 10 km/h → WC=-27.21 °C
T=-20°C V= 20 km/h → WC=-30.48 °C
T=-20°C V= 40 km/h → WC=-34.13 °C

Dangerous (WC < -25 °C): [(-20, 10), (-20, 20), (-20, 40)]
"""


from itertools import product

temps = [0, -5, -10, -20]
winds = [10, 20, 40]

wind_chill = lambda T, V: (13.12 + 0.6215 * T - 11.37 * V ** 0.16
                           + 0.3965 * T * V ** 0.16)

table = [(T, V, wind_chill(T, V)) for T, V in product(temps, winds)]
dangerous = list(filter(lambda r: r[2] < -25, table))

for T, V, WC in table:
    print(f"T={T:>3}°C V={V:>3} km/h → WC={WC:6.2f} °C")
print("\nDangerous (WC < -25 °C):",
      [(T, V) for T, V, _ in dangerous])
