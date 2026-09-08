"""Exercise 10.1.2 — The colon

Chapter 10 (Functions), section 10.1: Your First Function.

Problem
-------
This program defines a function that prints the boiling point of water and calls it.

Bug type: Syntax
----------------
The `def` header must end with a colon. Without it Python cannot tell where the body begins and raises a `SyntaxError`.

The program below is the corrected version.
"""


def boiling_point():
    print("Water boils at 100 degrees Celsius.")

boiling_point()
