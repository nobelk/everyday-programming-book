"""Exercise 18.1.3 — Passing grade

Chapter 18 (Bugs), section 18.1: Syntax Bugs.

Problem
-------
This program should report whether a test score of 72 is a passing grade.

Bug type: Syntax
----------------
The condition uses `=` (assignment) where a comparison `==` is required, which is a syntax error inside an `if`. Using `>=` expresses the intended ``score is at least 60'' test.

The program below is the corrected version.
"""


score = 72
if score >= 60:
    print("Pass")
else:
    print("Fail")
