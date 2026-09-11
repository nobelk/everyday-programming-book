"""Exercise 11.8.3 — Reading the docstring

Chapter 11 (Functions), section 11.8: Docstrings.

Problem
-------
This program should print the docstring of the function.

Bug type: Runtime
-----------------
The attribute is `__doc__`, not `__docs__`, so accessing it raises an `AttributeError`. Use the correct name.

The program below is the corrected version.
"""


def half(number):
    """Return half of a number."""
    return number / 2

print(half.__doc__)
