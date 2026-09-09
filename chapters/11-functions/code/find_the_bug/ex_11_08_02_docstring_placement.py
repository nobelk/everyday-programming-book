"""Exercise 11.8.2 — Docstring placement

Chapter 11 (Functions), section 11.8: Docstrings.

Problem
-------
The docstring should sit directly under the `def` line so it becomes the function's documentation.

Bug type: Logical
-----------------
A string becomes the docstring only when it is the first statement in the body; here it sits after an assignment, so `__doc__` is `None`. Move the docstring to the top.

The program below is the corrected version.
"""


def to_meters(feet):
    """Convert feet to meters."""
    result = feet * 0.3048
    return result

print(to_meters.__doc__)  # Convert feet to meters.
