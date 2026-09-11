"""Exercise 17.3.5 — Tax on a purchase

Chapter 17 (Handling Failures), section 17.3: Using else.

Problem
-------
This program parses a purchase amount and, when it succeeds, computes 8 percent tax in the `else` block.

Bug type: Logical
-----------------
The tax formula uses addition (`amount + 0.08`) instead of multiplication, so it adds eight cents rather than computing 8 percent of the amount. Use `amount * 0.08`.

The program below is the corrected version.
"""


try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount * 0.08
    print("Tax is", tax)
