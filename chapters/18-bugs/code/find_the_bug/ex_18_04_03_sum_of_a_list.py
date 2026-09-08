"""Exercise 18.4.3 — Sum of a list

Chapter 18 (Bugs), section 18.4: Basic Debugging: Find and Fix Bugs.

Problem
-------
This program should print the sum of the daily rainfall totals, but the answer is wrong. Trace it with `print` and find the single wrong line.

Bug type: Logical
-----------------
Printing `total` inside the loop shows it only ever holds the latest value: the line replaces the running sum instead of adding to it. Using `+=` accumulates the total.

The program below is the corrected version.
"""


rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total += amount
print(total)   # 5.5
