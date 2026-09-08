"""Exercise 20.9.1 — Area of a square

Chapter 20 (Common Pitfalls), section 20.9: Using ^ for powers instead of **.

Problem
-------
This program should print the area of a square with side 5 (side squared).

Bug type: Logical
-----------------
`^` is bitwise XOR, not exponent, so `5 ^ 2` is `7`, not `25`. Use `**` for powers.

The program below is the corrected version.
"""


side = 5
print(side ** 2)  # 25
