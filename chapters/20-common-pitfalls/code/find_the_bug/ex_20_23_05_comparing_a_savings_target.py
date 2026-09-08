"""Exercise 20.23.5 — Comparing a savings target

Chapter 20 (Common Pitfalls), section 20.23: Expecting floating-point math to be exact.

Problem
-------
This program should confirm that saving $1.10 three times reaches $3.30.

Bug type: Logical
-----------------
`1.10 * 3` does not land exactly on `3.30` in floating-point. Compare with a tolerance using `math.isclose`.

The program below is the corrected version.
"""


import math

weekly = 1.10
saved = weekly * 3
if math.isclose(saved, 3.30):
    print("You reached the target")
else:
    print("You did not reach the target")
