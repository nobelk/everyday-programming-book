"""Exercise 20.16.4 — Perimeter of a rectangle

Chapter 20 (Common Pitfalls), section 20.16: Not returning a value from a function.

Problem
-------
The program should print the perimeter of a 6 by 4 rectangle.

Bug type: Logical
-----------------
The perimeter `p` is calculated but never returned, so the program prints `None`. Return `p`.

The program below is the corrected version.
"""


def perimeter(length, width):
    p = 2 * (length + width)
    return p

print("Perimeter:", perimeter(6, 4))
