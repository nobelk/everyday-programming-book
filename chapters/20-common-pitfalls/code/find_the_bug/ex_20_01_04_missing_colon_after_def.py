"""Exercise 20.1.4 — Missing colon after `def`

Chapter 20 (Common Pitfalls), section 20.1: Forgetting the : after if, for, while, or def.

Problem
-------
This program should define a function that returns the area of a rectangle and print it.

Bug type: Syntax
----------------
A function definition must end with `:` after the parameter list. Adding the colon makes the definition valid.

The program below is the corrected version.
"""


def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 5))  # 20
