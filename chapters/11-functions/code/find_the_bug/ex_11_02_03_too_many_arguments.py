"""Exercise 11.2.3 — Too many arguments

Chapter 11 (Functions), section 11.2: Parameters.

Problem
-------
This program should print the area of a rectangle that is 4 by 6.

Bug type: Runtime
-----------------
The function takes two parameters but the call passes three, raising a `TypeError`. Pass exactly width and height.

The program below is the corrected version.
"""


def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6))
