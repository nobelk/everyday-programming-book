"""Exercise 20.24.1 — Average speed of a trip

Chapter 20 (Common Pitfalls), section 20.24: Writing long code without testing small pieces.

Problem
-------
This program should compute average speed (distance over time) for a 150 km trip in 3 hours and print 50.0.

Bug type: Logical
-----------------
The formula is reversed: speed is distance divided by time, not time divided by distance. Swap the operands.

The program below is the corrected version.
"""


def average_speed(distance, time):
    return distance / time

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
