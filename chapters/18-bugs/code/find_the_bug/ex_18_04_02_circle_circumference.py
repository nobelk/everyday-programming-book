"""Exercise 18.4.2 — Circle circumference

Chapter 18 (Bugs), section 18.4: Basic Debugging: Find and Fix Bugs.

Problem
-------
This program should print the circumference of a circle with radius 5, but the answer is wrong. Trace it with `print` and find the single wrong line.

Bug type: Logical
-----------------
Printing the returned value shows it is half the expected size: the formula omits the factor of 2 (circumference is `2 * pi * radius`). Adding the 2 corrects it.

The program below is the corrected version.
"""


def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

print(circumference(5))   # about 31.4
