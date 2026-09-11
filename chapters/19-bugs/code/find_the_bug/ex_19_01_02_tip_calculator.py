"""Exercise 19.1.2 — Tip calculator

Chapter 19 (Bugs), section 19.1: Syntax Bugs.

Problem
-------
This program should add a 15% tip to a $40 restaurant bill.

Bug type: Syntax
----------------
The opening parenthesis after `bill *` is never closed, leaving an unbalanced bracket that the parser rejects. Closing the parenthesis fixes the expression.

The program below is the corrected version.
"""


bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate)
print(total)   # 46.0
