"""Exercise 7.2.1 — Saving up for a bike

Chapter 7 (Operators), section 7.2: Assignment Operator.

Problem
-------
A bike costs $240 and you start with $60, then add $45 each of two weeks. This program should print your savings, which is `150`.

Bug type: Logical
-----------------
The second line uses plain assignment `=` and overwrites the starting $60 with $45, so the final total is wrong. It should be augmented assignment `+=` to add the deposit.

The program below is the corrected version.
"""


savings = 60
savings += 45
savings += 45
print(savings)   # 150
