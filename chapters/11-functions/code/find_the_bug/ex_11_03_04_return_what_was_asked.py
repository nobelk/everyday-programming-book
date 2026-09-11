"""Exercise 11.3.4 — Return what was asked

Chapter 11 (Functions), section 11.3: Returning a Result.

Problem
-------
This function should return the larger of two numbers; here it should return 9.

Bug type: Logical
-----------------
The `else` branch returns `a` instead of `b`, so the larger value is never returned when `b` is bigger. Return `b` in the `else` branch.

The program below is the corrected version.
"""


def larger(a, b):
    if a > b:
        return a
    else:
        return b

print(larger(4, 9))  # 9
