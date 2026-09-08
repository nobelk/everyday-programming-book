"""Exercise 10.4.4 — Order of defaults

Chapter 10 (Functions), section 10.4: Default Arguments.

Problem
-------
This function gives the area of a rectangle, using a default height of 1.

Bug type: Syntax
----------------
A parameter with a default cannot come before one without a default, so `def area(height=1, width)` is a `SyntaxError`. Put the non-default parameter first.

The program below is the corrected version.
"""


def area(width, height=1):
    return width * height

print(area(width=5))  # 5
