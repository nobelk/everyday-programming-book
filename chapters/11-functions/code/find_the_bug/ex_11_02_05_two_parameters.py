"""Exercise 11.2.5 — Two parameters

Chapter 11 (Functions), section 11.2: Parameters.

Problem
-------
This program should compute the perimeter of a rectangle (2 times width plus 2 times height) for a 3 by 5 rectangle, giving 16.

Bug type: Logical
-----------------
The formula uses `width` twice, ignoring the second parameter. It should be `2 * width + 2 * height` to use both arguments.

The program below is the corrected version.
"""


def perimeter(width, height):
    return 2 * width + 2 * height

print(perimeter(3, 5))  # 16
