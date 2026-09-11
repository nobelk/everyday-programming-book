"""Exercise 15.1.2 — Circle area with pi

Chapter 15 (Modules), section 15.1: Python Standard Library.

Problem
-------
This program should compute the area of a circle with radius 5 using π r².

Bug type: Runtime
-----------------
`math.pi` is a value (a float), not a function, so calling it as `math.pi()` raises `TypeError: 'float' object is not callable`. Remove the parentheses and multiply by the value directly.

The program below is the corrected version.
"""


import math

radius = 5
area = math.pi * radius ** 2
print(area)   # about 78.54
