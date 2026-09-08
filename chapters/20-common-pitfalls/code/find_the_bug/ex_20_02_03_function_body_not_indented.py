"""Exercise 20.2.3 — Function body not indented

Chapter 20 (Common Pitfalls), section 20.2: Using the wrong indentation.

Problem
-------
This program should return the perimeter of a square and print it.

Bug type: Syntax
----------------
The `return` statement must be indented inside the function. Indenting it four spaces makes the definition valid.

The program below is the corrected version.
"""


def square_perimeter(side):
    return 4 * side

print(square_perimeter(6))  # 24
