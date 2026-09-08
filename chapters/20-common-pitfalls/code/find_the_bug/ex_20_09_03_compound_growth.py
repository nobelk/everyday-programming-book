"""Exercise 20.9.3 — Compound growth

Chapter 20 (Common Pitfalls), section 20.9: Using ^ for powers instead of **.

Problem
-------
This program should print 2 raised to the tenth power.

Bug type: Logical
-----------------
`2 ^ 10` is XOR (`8`), not `2` to the tenth. Use `**` for exponentiation.

The program below is the corrected version.
"""


print(2 ** 10)  # 1024
