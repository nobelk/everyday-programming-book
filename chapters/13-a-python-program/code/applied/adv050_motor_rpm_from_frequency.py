"""Advanced problem 50 — Motor RPM from Frequency (functional)

Subject: Engineering. Style: functional.

Problem
-------
An AC induction motor's synchronous speed is `RPM = 120 · f / poles`. For a 60 Hz supply, compute the synchronous speed for motors with 2, 4, 6, 8, and 12 poles.

Concepts taught
---------------
Lambda capturing a constant via closure, `map` over a list, formatted output.

Expected output
---------------
 2 poles →  3600 RPM
 4 poles →  1800 RPM
 6 poles →  1200 RPM
 8 poles →   900 RPM
12 poles →   600 RPM
"""


freq = 60
pole_counts = [2, 4, 6, 8, 12]

rpm = lambda poles: 120 * freq / poles
results = list(map(lambda p: (p, rpm(p)), pole_counts))

for p, n in results:
    print(f"{p:>2} poles → {n:>5.0f} RPM")
