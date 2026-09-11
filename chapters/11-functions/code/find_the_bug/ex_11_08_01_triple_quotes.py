"""Exercise 11.8.1 — Triple quotes

Chapter 11 (Functions), section 11.8: Docstrings.

Problem
-------
This function has a docstring describing what it does.

Bug type: Syntax
----------------
The string opens with a single double-quote but closes with triple single-quotes, so the quotes do not match and Python raises a `SyntaxError`. Use matching triple quotes.

The program below is the corrected version.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(2, 3))  # 5
