"""Exercise 20.16.5 — Tax on a purchase

Chapter 20 (Common Pitfalls), section 20.16: Not returning a value from a function.

Problem
-------
This program should return the tax owed on a $200 purchase at 8 percent.

Bug type: Logical
-----------------
The tax is computed into `tax` but never returned, so the result is `None`. Add a `return`.

The program below is the corrected version.
"""


def tax_owed(price, rate):
    tax = price * rate / 100
    return tax

print("Tax:", tax_owed(200, 8))
