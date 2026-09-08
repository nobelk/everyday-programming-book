"""Exercise 20.9.4 — Volume of a cube

Chapter 20 (Common Pitfalls), section 20.9: Using ^ for powers instead of **.

Problem
-------
This program should print the volume of a cube with edge 3 (edge cubed).

Bug type: Logical
-----------------
`3 ^ 3` is XOR (`0`), not `3` cubed. Use `**` to raise to a power.

The program below is the corrected version.
"""


edge = 3
volume = edge ** 3
print(volume)  # 27
