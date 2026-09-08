"""Exercise 20.6.1 — Joining text and a number

Chapter 20 (Common Pitfalls), section 20.6: Mixing strings and numbers without converting types.

Problem
-------
This program should print a label with the day's step count.

Bug type: Runtime
-----------------
You cannot add a string to an integer; `"Steps today: " + steps` raises `TypeError`. Convert the number with `str()`.

The program below is the corrected version.
"""


steps = 8000
print("Steps today: " + str(steps))
