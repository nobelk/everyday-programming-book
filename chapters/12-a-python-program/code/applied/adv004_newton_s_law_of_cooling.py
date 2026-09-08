"""Advanced problem 4 — Newton's Law of Cooling (functional)

Subject: Physics. Style: functional.

Problem
-------
A cup of tea at 90 °C is left in a 22 °C room. Newton's law says the temperature after time `t` (minutes) is `T(t) = T_room + (T_initial - T_room) · e^(-k·t)` with `k = 0.05`. Produce the temperature for the first 30 minutes (every 5 minutes).

Concepts taught
---------------
Lambda capturing constants by closure, list comprehension, immutable inputs (no variable reassignment), pure function.

Expected output
---------------
t= 0 min  T=90.00 °C
t= 5 min  T=74.96 °C
t=10 min  T=63.24 °C
t=15 min  T=54.12 °C
t=20 min  T=47.02 °C
t=25 min  T=41.48 °C
t=30 min  T=37.17 °C
"""


from math import exp

room, initial, k = 22.0, 90.0, 0.05

temperature = lambda t: room + (initial - room) * exp(-k * t)
times = range(0, 31, 5)
readings = [(t, temperature(t)) for t in times]

for t, T in readings:
    print(f"t={t:2d} min  T={T:5.2f} °C")
