"""Exercise 20.22.1 — Counting items in a basket

Chapter 20 (Common Pitfalls), section 20.22: Shadowing built-in names like list, str, or sum.

Problem
-------
This program should count the letters in a fruit name after storing some numbers.

Bug type: Runtime
-----------------
Assigning `len = [4, 8, 15]` shadows the built-in `len`, so `len(fruit)` tries to call a list and raises `TypeError`. Rename the variable.

The program below is the corrected version.
"""


basket = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
