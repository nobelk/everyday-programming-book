"""Exercise 20.8.4 — Whole minutes from seconds

Chapter 20 (Common Pitfalls), section 20.8: Using / when you want a whole-number result.

Problem
-------
This program should print the number of whole minutes in 200 seconds.

Bug type: Logical
-----------------
`200 / 60` is `3.33...`; whole minutes need `//`, giving `3`.

The program below is the corrected version.
"""


seconds = 200
minutes = seconds // 60
print(minutes)  # 3
