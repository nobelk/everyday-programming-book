"""Exercise 20.6.2 — Adding a number to a string label

Chapter 20 (Common Pitfalls), section 20.6: Mixing strings and numbers without converting types.

Problem
-------
This program should print how many liters of water to drink.

Bug type: Runtime
-----------------
Mixing `str` and `int` with `+` raises `TypeError`. Convert `liters` to a string before concatenating.

The program below is the corrected version.
"""


liters = 2
print("Drink " + str(liters) + " liters")
