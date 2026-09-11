"""Exercise 12.2.4 — which value gets printed

Chapter 12 (Scoping), section 12.2: A Local Variable Can Hide a Global Variable.

Problem
-------
The global `tax_rate` is 0.05. Inside `quote()` a local `tax_rate` of 0.08 should be used to compute the price with tax. The program should print 108.0.

Bug type: Logical
-----------------
The local `tax_rate` is set to 0.08, but the formula hard-codes 0.05, so the local shadow is never used and the answer is 105.0. Use the local `tax_rate` in the calculation.

The program below is the corrected version.
"""


tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * tax_rate

print("With tax:", quote(100))
