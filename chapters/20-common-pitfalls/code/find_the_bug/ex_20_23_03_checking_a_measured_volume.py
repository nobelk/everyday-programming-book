"""Exercise 20.23.3 — Checking a measured volume

Chapter 20 (Common Pitfalls), section 20.23: Expecting floating-point math to be exact.

Problem
-------
This program should confirm that three 0.1 L pours fill a 0.3 L cup.

Bug type: Logical
-----------------
`0.1 * 3` does not equal `0.3` exactly in floating-point. Compare with a tolerance, for example `math.isclose`.

The program below is the corrected version.
"""


import math

pour = 0.1
filled = pour * 3
if math.isclose(filled, 0.3):
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
