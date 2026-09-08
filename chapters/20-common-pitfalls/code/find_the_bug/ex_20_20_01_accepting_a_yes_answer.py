"""Exercise 20.20.1 — Accepting a yes answer

Chapter 20 (Common Pitfalls), section 20.20: Comparing text without thinking about case.

Problem
-------
This program should accept the answer "yes" no matter how it is capitalized.

Bug type: Logical
-----------------
`"YES" == "yes"` is `False` because case differs. Normalize the case first with `.lower()`.

The program below is the corrected version.
"""


answer = "YES"
if answer.lower() == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
