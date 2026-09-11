"""Exercise 10.11.4 — Total with tax

Chapter 10 (Control Flow), section 10.11: Functions and return.

Problem
-------
This function should return the price plus 10% tax. `with_tax(100)` should print `110.0`.

Bug type: Logical
-----------------
The function returns `price` before computing the total, so the line after `return` never runs. Returning `price + tax` gives the taxed total.

The program below is the corrected version.
"""


def with_tax(price):
    tax = price * 0.10
    total = price + tax
    return total

print(with_tax(100))
