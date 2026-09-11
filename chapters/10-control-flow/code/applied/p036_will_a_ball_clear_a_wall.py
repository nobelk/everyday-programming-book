"""Problem 36 — Will a ball clear a wall?

Domain: Physics. Chapter 10 (Control Flow), conditionals.

Problem
-------
A ball is thrown and reaches a height of 4.5 m at the wall. The wall is 5.0 m tall — does it clear?

Expected output
---------------
Hits the wall
"""


ball_height_m = 4.5
wall_height_m = 5.0
if ball_height_m >= wall_height_m:
    print("Clears the wall")
else:
    print("Hits the wall")
