"""Exercise 18.1.5 — Total cost with tax

Chapter 18 (Testing), section 18.1: Why Test Python Functions.

Problem
-------
The function should add 10% tax to a price, and the assert should pass for a $20 item costing $22.

Bug type: Logical
-----------------
The function is correct (20 + 2 = 22), but the expected value in the assert is 20 instead of 22, so the check fails. The fix corrects the expected value.

The program below is the corrected version.
"""


def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 22
print("passed")
