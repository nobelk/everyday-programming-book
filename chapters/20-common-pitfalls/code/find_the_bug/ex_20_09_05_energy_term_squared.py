"""Exercise 20.9.5 — Energy term squared

Chapter 20 (Common Pitfalls), section 20.9: Using ^ for powers instead of **.

Problem
-------
This program should print the speed squared for a kinetic-energy calculation.

Bug type: Logical
-----------------
`6 ^ 2` is XOR (`4`), not `6` squared. Use `**`.

The program below is the corrected version.
"""


speed = 6
print(speed ** 2)  # 36
