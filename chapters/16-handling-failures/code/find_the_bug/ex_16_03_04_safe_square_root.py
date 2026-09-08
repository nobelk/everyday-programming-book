"""Exercise 16.3.4 — Safe square root

Chapter 16 (Handling Failures), section 16.3: Using else.

Problem
-------
This program reads a number and, only if it parses, prints its square root in the `else` block.

Bug type: Syntax
----------------
The `try` keyword is missing its colon, so the file will not parse. Add the colon after `try`.

The program below is the corrected version.
"""


import math

try:
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
