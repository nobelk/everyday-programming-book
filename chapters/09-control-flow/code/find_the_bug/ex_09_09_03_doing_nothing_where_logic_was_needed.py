"""Exercise 9.9.3 — Doing nothing where logic was needed

Chapter 9 (Control Flow), section 9.9: pass.

Problem
-------
This program should add up the prices and print the total, 60, but the loop body was left as a placeholder.

Bug type: Logical
-----------------
The loop body is left as `pass`, so nothing is added and the total stays 0. The real work—accumulating the prices—must replace the placeholder.

The program below is the corrected version.
"""


prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(total)
