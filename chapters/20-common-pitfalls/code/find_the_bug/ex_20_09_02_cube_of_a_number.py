"""Exercise 20.9.2 — Cube of a number

Chapter 20 (Common Pitfalls), section 20.9: Using ^ for powers instead of **.

Problem
-------
This program should print 4 raised to the third power.

Bug type: Logical
-----------------
`4 ^ 3` computes XOR (`7`), not `4` cubed. Use `**`.

The program below is the corrected version.
"""


base = 4
print(base ** 3)  # 64
