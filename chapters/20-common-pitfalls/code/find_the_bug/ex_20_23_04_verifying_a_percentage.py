"""Exercise 20.23.4 — Verifying a percentage

Chapter 20 (Common Pitfalls), section 20.23: Expecting floating-point math to be exact.

Problem
-------
The program should check that 0.7 plus 0.1 equals 0.8.

Bug type: Logical
-----------------
`0.7 + 0.1` is not exactly `0.8` in binary floating-point, so the strict equality fails. Use `math.isclose` to allow for rounding error.

The program below is the corrected version.
"""


import math

part_one = 0.7
part_two = 0.1
if math.isclose(part_one + part_two, 0.8):
    print("Percentages add correctly")
else:
    print("Percentages do not add correctly")
