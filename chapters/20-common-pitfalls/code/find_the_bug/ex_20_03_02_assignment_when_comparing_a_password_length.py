"""Exercise 20.3.2 — Assignment when comparing a password length

Chapter 20 (Common Pitfalls), section 20.3: Confusing assignment with equality.

Problem
-------
This program should confirm a password has exactly 8 characters.

Bug type: Syntax
----------------
A condition must compare with `==`, not assign with `=`. Switching to `==` fixes the error.

The program below is the corrected version.
"""


length = 8
if length == 8:
    print("Valid length")
