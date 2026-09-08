"""Exercise 20.13.1 — Capitalizing a name

Chapter 20 (Common Pitfalls), section 20.13: Forgetting that strings are immutable.

Problem
-------
This program should change the first letter of a name to a capital `"S"`.

Bug type: Runtime
-----------------
Strings are immutable, so `name[0] = "S"` raises `TypeError`. Build a new string instead.

The program below is the corrected version.
"""


name = "sam"
name = "S" + name[1:]
print(name)
