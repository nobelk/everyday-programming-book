"""Exercise 19.1.1 — Rectangle perimeter

Chapter 19 (Bugs), section 19.1: Syntax Bugs.

Problem
-------
This program should print the perimeter of a rectangle that is 8 metres by 5 metres.

Bug type: Syntax
----------------
The `def` header is missing the colon that must end every function definition line, so Python cannot parse the file. Adding the colon lets the function be defined and called.

The program below is the corrected version.
"""


def perimeter(length, width):
    return 2 * (length + width)

print(perimeter(8, 5))   # 26
