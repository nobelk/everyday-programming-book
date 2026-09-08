"""Exercise 20.1.2 — Missing colon after `for`

Chapter 20 (Common Pitfalls), section 20.1: Forgetting the : after if, for, while, or def.

Problem
-------
This program should print each planet's distance from the Sun in millions of kilometers.

Bug type: Syntax
----------------
A `for` loop header must end with `:`. Without it the program will not run; adding the colon resolves it.

The program below is the corrected version.
"""


distances = [58, 108, 150]
for distance in distances:
    print(distance)
