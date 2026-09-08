"""Exercise 20.15.4 — Area of a circle

Chapter 20 (Common Pitfalls), section 20.15: Forgetting to call a function with parentheses.

Problem
-------
This program should compute and print the area of a circle with radius 4.

Bug type: Runtime
-----------------
`circle_area / 2` tries to divide the function object by 2, raising `TypeError`. Call the function first, then divide its result.

The program below is the corrected version.
"""


import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area(4) / 2)
