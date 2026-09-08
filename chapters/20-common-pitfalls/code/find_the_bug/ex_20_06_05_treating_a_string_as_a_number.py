"""Exercise 20.6.5 — Treating a string as a number

Chapter 20 (Common Pitfalls), section 20.6: Mixing strings and numbers without converting types.

Problem
-------
This program should add a bonus of 10 points to a stored score.

Bug type: Runtime/Logical
-------------------------
`score` holds the text `"75"`, so `score + 10` mixes a string and an int and raises `TypeError`. Convert `score` to an integer (or store it as one) before adding.

The program below is the corrected version.
"""


score = int("75")
print(score + 10)
