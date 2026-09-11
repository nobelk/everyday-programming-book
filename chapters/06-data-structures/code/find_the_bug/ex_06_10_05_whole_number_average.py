"""Exercise 6.10.5 — Whole-number average

Chapter 6 (Data Structures), section 6.10: Variables and Types.

Problem
-------
Two test scores are 80 and 91. The program should print their average as a whole number, 85.

Bug type: Runtime
-----------------
`average` is wrapped in `str()`, so `int("85.5")` raises a `ValueError`. Keep the average numeric and apply `int()` directly.

The program below is the corrected version.
"""


score1 = 80
score2 = 91

average = (score1 + score2) / 2
print(int(average))   # 85
