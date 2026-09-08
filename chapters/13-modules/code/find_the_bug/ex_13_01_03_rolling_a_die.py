"""Exercise 13.1.3 — Rolling a die

Chapter 13 (Modules), section 13.1: Python Standard Library.

Problem
-------
This program should print a random whole number from 1 to 6, like rolling a single die.

Bug type: Logical
-----------------
`random.randint(a, b)` includes *both* endpoints, so `randint(1, 7)` can return 7, which is impossible on a six-sided die. Use `random.randint(1, 6)`.

The program below is the corrected version.
"""


import random

roll = random.randint(1, 6)
print(roll)   # a number from 1 to 6
