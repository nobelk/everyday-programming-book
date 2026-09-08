"""Exercise 20.1.5 — Missing colon after `elif`

Chapter 20 (Common Pitfalls), section 20.1: Forgetting the : after if, for, while, or def.

Problem
-------
This program should label a test score as a pass, a borderline, or a fail.

Bug type: Syntax
----------------
Like `if`, an `elif` header requires a trailing `:`. Adding it lets the three-way branch parse.

The program below is the corrected version.
"""


score = 55
if score >= 60:
    print("Pass")
elif score >= 50:
    print("Borderline")
else:
    print("Fail")
