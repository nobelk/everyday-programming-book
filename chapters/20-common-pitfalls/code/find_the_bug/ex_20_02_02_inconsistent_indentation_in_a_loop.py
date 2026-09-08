"""Exercise 20.2.2 — Inconsistent indentation in a loop

Chapter 20 (Common Pitfalls), section 20.2: Using the wrong indentation.

Problem
-------
This program should add up the rainfall for three days.

Bug type: Syntax
----------------
The final `print` is indented more deeply than the loop body, which Python reads as an unexpected indent. Aligning it at the outer level (after the loop) fixes it.

The program below is the corrected version.
"""


rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
print(total)  # 35
