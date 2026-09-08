"""Exercise 18.2.2 — Final price with tax

Chapter 18 (Bugs), section 18.2: Runtime Bugs.

Problem
-------
This program should print a $50 item's price after 8% sales tax.

Bug type: Runtime
-----------------
The expression references `tax`, but the variable defined above is `tax_rate`, so Python raises a `NameError`. Using the correct name computes the taxed price.

The program below is the corrected version.
"""


price = 50.0
tax_rate = 0.08
final_price = price + (price * tax_rate)
print(final_price)   # 54.0
