"""Exercise 19.4.1 — Total grocery cost

Chapter 19 (Bugs), section 19.4: Basic Debugging: Find and Fix Bugs.

Problem
-------
This program should print the total cost of three grocery items, but the answer is wrong. Trace it with `print` and find the single wrong line.

Bug type: Logical
-----------------
Printing the subtotal reveals it is too low: the milk price is subtracted instead of added. Changing the `-` to `+` totals all three items.

The program below is the corrected version.
"""


def total_cost(apples, bread, milk):
    subtotal = apples + bread + milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # 7.5
