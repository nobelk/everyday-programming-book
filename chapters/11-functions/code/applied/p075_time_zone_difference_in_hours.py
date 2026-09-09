"""Problem 75 — Time-zone difference in hours

Domain: Geography. Chapter 11 (Functions), functions.

Problem
-------
Given two UTC offsets, return the difference.

Expected output
---------------
-10.5
"""


def tz_difference(offset_a, offset_b):
    return offset_b - offset_a

print(tz_difference(5.5, -5))  # India → New York
