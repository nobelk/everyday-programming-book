"""Exercise 11.7.4 — None in arithmetic

Chapter 11 (Functions), section 11.7: Implicit None Return.

Problem
-------
This program should add 5 to the result of a function that returns a number.

Bug type: Runtime
-----------------
The function never returns `total`, so it returns `None`, and `None + 5` raises a `TypeError`. Return the value.

The program below is the corrected version.
"""


def base_value():
    total = 10
    return total

print(base_value() + 5)  # 15
