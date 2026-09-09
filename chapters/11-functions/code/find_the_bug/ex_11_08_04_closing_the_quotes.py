"""Exercise 11.8.4 — Closing the quotes

Chapter 11 (Functions), section 11.8: Docstrings.

Problem
-------
This function should have a one-line docstring and return a perimeter.

Bug type: Syntax
----------------
The triple-quoted docstring is never closed, so Python reads the rest of the file as part of the string and raises a `SyntaxError`. Close the docstring.

The program below is the corrected version.
"""


def square_perimeter(side):
    """Return the perimeter of a square."""
    return side * 4

print(square_perimeter(3))  # 12
