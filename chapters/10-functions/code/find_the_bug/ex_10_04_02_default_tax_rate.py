"""Exercise 10.4.2 — Default tax rate

Chapter 10 (Functions), section 10.4: Default Arguments.

Problem
-------
This function should add an 8 percent tax by default, so a 50 dollar bill becomes 54.0.

Bug type: Logical
-----------------
The body multiplies by the literal 0.8 instead of the `rate` parameter, charging 80 percent. Use `rate` so the default 0.08 applies.

The program below is the corrected version.
"""


def with_tax(price, rate=0.08):
    return price + price * rate

print(with_tax(50))  # 54.0
