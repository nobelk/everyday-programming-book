"""Exercise 20.22.2 — Totaling a receipt

Chapter 20 (Common Pitfalls), section 20.22: Shadowing built-in names like list, str, or sum.

Problem
-------
The program should add up the prices on a receipt.

Bug type: Runtime
-----------------
`sum = 0` shadows the built-in `sum`, so `sum(prices)` tries to call an integer and raises `TypeError`. Use a different variable name.

The program below is the corrected version.
"""


running_total = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
