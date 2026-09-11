"""Exercise 19.3.4 — Discounted price

Chapter 19 (Bugs), section 19.3: Logical Bugs.

Problem
-------
This program should print the price of a $80 jacket after a 25% discount.

Bug type: Logical
-----------------
Multiplying by the discount rate gives the amount taken off, not the price paid, so the result is 20 instead of 60. The customer pays the remaining fraction, `1 - discount_rate`.

The program below is the corrected version.
"""


price = 80.0
discount_rate = 0.25
final_price = price * (1 - discount_rate)
print(final_price)   # 60.0
