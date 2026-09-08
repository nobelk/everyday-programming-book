"""Exercise 18.1.4 — Weekly distance

Chapter 18 (Bugs), section 18.1: Syntax Bugs.

Problem
-------
This program should print the total distance walked over three days.

Bug type: Syntax
----------------
There is a missing operator (or comma) between `tuesday` and `wednesday`; two names sitting side by side cannot be parsed. Adding the `+` sums all three days.

The program below is the corrected version.
"""


monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday + wednesday
print(total)   # 10.0
