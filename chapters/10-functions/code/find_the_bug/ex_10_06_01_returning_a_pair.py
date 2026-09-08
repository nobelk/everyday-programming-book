"""Exercise 10.6.1 — Returning a pair

Chapter 10 (Functions), section 10.6: Multiple Return Values.

Problem
-------
This program should print the smallest and largest of three temperatures.

Bug type: Runtime
-----------------
The function returns a single value, so unpacking into two names raises a `ValueError`. Return both `min` and `max` as a pair.

The program below is the corrected version.
"""


def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
