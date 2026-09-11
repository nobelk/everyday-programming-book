"""Exercise 10.4.1 — Sum of a list

Chapter 10 (Control Flow), section 10.4: for Loops.

Problem
-------
This program should add up the prices in a cart and print the total, 60.

Bug type: Logical
-----------------
`total = price` overwrites the running sum each pass instead of adding to it, leaving only the last price. Use `total += price` to accumulate.

The program below is the corrected version.
"""


prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print("Total:", total)
