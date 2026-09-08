"""Exercise 20.21.3 — Greeting each guest

Chapter 20 (Common Pitfalls), section 20.21: Using range(len(...)) when iterating over items directly is simpler.

Problem
-------
This program should print a greeting for every guest.

Bug type: Logical
-----------------
`range(len(guests))` yields the numbers 0, 1, 2, so the greeting prints numbers, not names. Iterate over the guests directly.

The program below is the corrected version.
"""


guests = ["Ana", "Ben", "Cara"]
for guest in guests:
    print("Welcome,", guest)
