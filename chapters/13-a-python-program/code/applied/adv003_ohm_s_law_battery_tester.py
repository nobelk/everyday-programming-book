"""Advanced problem 3 — Ohm's Law Battery Tester (imperative)

Subject: Physics. Style: imperative.

Problem
-------
A flashlight has a 4.5 V battery and a bulb whose resistance you measured at several brightness settings: 6 Ω, 9 Ω, 12 Ω, 18 Ω. Print the current through the bulb at each setting, and warn if the current exceeds 0.5 A (the bulb's safe limit).

Concepts taught
---------------
Variables, looping over a list, `if` conditional with descriptive flag variable, formatted output.

Expected output
---------------
R=6Ω  I=0.750A  DANGER — bulb may burn out
R=9Ω  I=0.500A  OK
R=12Ω  I=0.375A  OK
R=18Ω  I=0.250A  OK
"""


voltage = 4.5
resistances = [6, 9, 12, 18]
safe_limit = 0.5

for r in resistances:
    current = voltage / r
    status = "OK"
    if current > safe_limit:
        status = "DANGER — bulb may burn out"
    print(f"R={r}Ω  I={current:.3f}A  {status}")
