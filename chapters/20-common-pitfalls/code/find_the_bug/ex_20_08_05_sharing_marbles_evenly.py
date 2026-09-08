"""Exercise 20.8.5 — Sharing marbles evenly

Chapter 20 (Common Pitfalls), section 20.8: Using / when you want a whole-number result.

Problem
-------
This program should print how many marbles each of 3 children gets from 25 marbles.

Bug type: Logical
-----------------
`25 / 3` is `8.33...`; each child gets a whole number of marbles. `//` yields `8`.

The program below is the corrected version.
"""


marbles = 25
children = 3
print(marbles // children)  # 8
