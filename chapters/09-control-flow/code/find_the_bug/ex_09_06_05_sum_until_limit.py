"""Exercise 9.6.5 — Sum until limit

Chapter 9 (Control Flow), section 9.6: while Loops.

Problem
-------
This program should add 1, 2, 3, ... until the total reaches at least 10, then print the total, 10.

Bug type: Logical
-----------------
`number` is incremented *before* being added, so the loop adds 2+3+4+5 = 14 and skips 1. Adding first, then incrementing, sums 1+2+3+4 = 10.

The program below is the corrected version.
"""


total = 0
number = 1

while total < 10:
    total += number
    number += 1

print(total)
