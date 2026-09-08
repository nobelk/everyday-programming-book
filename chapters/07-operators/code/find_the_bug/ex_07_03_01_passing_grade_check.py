"""Exercise 7.3.1 — Passing grade check

Chapter 7 (Operators), section 7.3: Comparison Operators.

Problem
-------
A grade of 60 or above passes. For a score of 60 this program should print `True`.

Bug type: Logical
-----------------
A score of exactly 60 should pass, but `>` excludes 60 and gives `False`. Use `>=` to include the boundary.

The program below is the corrected version.
"""


score = 60
passing = score >= 60
print(passing)   # True
