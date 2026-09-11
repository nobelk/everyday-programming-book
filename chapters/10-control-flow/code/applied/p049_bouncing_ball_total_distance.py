"""Problem 49 — Bouncing-ball total distance

Domain: Physics. Chapter 10 (Control Flow), loops.

Problem
-------
A ball dropped from 10 m loses 20% of its height each bounce. Total distance after 5 bounces (up and down).

Expected output
---------------
Total distance: 63.79 m
"""


height_m = 10
total_distance = height_m
for bounce in range(5):
    height_m = height_m * 0.8
    total_distance = total_distance + 2 * height_m
print(f"Total distance: {total_distance:.2f} m")
