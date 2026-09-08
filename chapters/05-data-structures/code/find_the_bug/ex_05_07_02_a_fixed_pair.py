"""Exercise 5.7.2 — A fixed pair

Chapter 5 (Data Structures), section 5.7: Tuples.

Problem
-------
This program should change the width to 1280 and print `(1280, 1080)`.

Bug type: Runtime
-----------------
Tuples are immutable, so `size[0] = 1280` raises a `TypeError`. You cannot change one element in place; build a new tuple instead.

The program below is the corrected version.
"""


size = (1920, 1080)
size = (1280, size[1])
print(size)   # (1280, 1080)
