"""Exercise 10.2.3 — Not equal

Chapter 10 (Control Flow), section 10.2: Common Comparison Operators.

Problem
-------
This program should print `Sold out` only when the remaining seats is not 0. With 0 seats it should print nothing.

Bug type: Logical
-----------------
The condition should test ``not 0'' but uses `==`, so it prints `Sold out` exactly when seats is 0. Use `!=` to match the intended meaning.

The program below is the corrected version.
"""


seats_left = 0

if seats_left != 0:
    print("Sold out")
