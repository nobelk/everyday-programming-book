"""Exercise 18.4.5 — Speed from distance and time

Chapter 18 (Bugs), section 18.4: Basic Debugging: Find and Fix Bugs.

Problem
-------
This program should print speed in kilometres per hour, but the answer is wrong. Trace it with `print` and find the single wrong line.

Bug type: Logical
-----------------
Printing `result` reveals the division is inverted: speed is distance divided by time, not time divided by distance. Swapping the operands gives the correct speed.

The program below is the corrected version.
"""


def speed(distance_km, time_hours):
    result = distance_km / time_hours
    return result

print(speed(150, 3))   # 50.0
