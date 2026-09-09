"""Exercise 18.1.1 — Rectangle area check

Chapter 18 (Testing), section 18.1: Why Test Python Functions.

Problem
-------
The function should return the area of a rectangle, and the assert should pass for a 4 × 3 rectangle.

Bug type: Logical
-----------------
The function adds length and width instead of multiplying them, so it returns 7 and the assert fails. Area of a rectangle is length times width.

The program below is the corrected version.
"""


def rectangle_area(length, width):
    return length * width

assert rectangle_area(4, 3) == 12
print("passed")
