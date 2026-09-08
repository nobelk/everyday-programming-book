"""Exercise 18.4.4 — Sale price

Chapter 18 (Bugs), section 18.4: Basic Debugging: Find and Fix Bugs.

Problem
-------
This program should print the savings on a $120 item at 30% off, but the answer is wrong. Trace it with `print` and find the single wrong line.

Bug type: Logical
-----------------
Printing `sale_price` shows it equals the discount amount, not the discounted price, so the subtraction yields the wrong savings. The savings are simply `price * discount_rate`.

The program below is the corrected version.
"""


def savings(price, discount_rate):
    return price * discount_rate

print(savings(120, 0.30))   # 36.0
