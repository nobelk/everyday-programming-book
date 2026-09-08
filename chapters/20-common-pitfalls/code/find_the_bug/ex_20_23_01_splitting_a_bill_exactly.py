"""Exercise 20.23.1 — Splitting a bill exactly

Chapter 20 (Common Pitfalls), section 20.23: Expecting floating-point math to be exact.

Problem
-------
This program should confirm that three shares of $0.10 add up to $0.30.

Bug type: Logical
-----------------
`0.10 + 0.10 + 0.10` is not exactly `0.30` in binary floating-point, so the equality fails. Compare with a small tolerance using `round` or `math.isclose`.

The program below is the corrected version.
"""


import math

share = 0.10
total = share + share + share
if math.isclose(total, 0.30):
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
