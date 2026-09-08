"""Exercise 20.11.3 — Showing the third prize

Chapter 20 (Common Pitfalls), section 20.11: Going past the end of a list.

Problem
-------
This program should print the third prize from the list.

Bug type: Runtime
-----------------
The list has only two items (indexes 0 and 1), so `prizes[2]` raises `IndexError`. To print a third prize, the list must contain one.

The program below is the corrected version.
"""


prizes = ["gold", "silver", "bronze"]
print(prizes[2])
