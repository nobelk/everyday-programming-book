"""Exercise 18.3.3 — Counting to ten

Chapter 18 (Bugs), section 18.3: Logical Bugs.

Problem
-------
This program should print the numbers 1 through 10.

Bug type: Logical
-----------------
`range(1, 10)` stops at 9 because the upper bound is excluded, so 10 is never printed (an off-by-one error). Using `range(1, 11)` includes 10.

The program below is the corrected version.
"""


for number in range(1, 11):
    print(number)
