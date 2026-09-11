"""Exercise 19.2.3 — Doubling a recipe

Chapter 19 (Bugs), section 19.2: Runtime Bugs.

Problem
-------
This program should double the cups of flour in a recipe.

Bug type: Runtime
-----------------
`cups_of_flour` is a string, and multiplying a string by a float raises `TypeError`. Storing the quantity as a number lets the multiplication work.

The program below is the corrected version.
"""


cups_of_flour = 2.0
doubled = cups_of_flour * 2.0
print(doubled)   # 4.0
