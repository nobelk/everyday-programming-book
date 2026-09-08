"""Exercise 20.21.2 — Summing daily sales

Chapter 20 (Common Pitfalls), section 20.21: Using range(len(...)) when iterating over items directly is simpler.

Problem
-------
The program should add up every day's sales and print the total.

Bug type: Runtime
-----------------
`total + sales` adds an integer to the whole list, raising `TypeError`. Iterate over the items and add each value.

The program below is the corrected version.
"""


sales = [120, 85, 200, 95]
total = 0
for amount in sales:
    total = total + amount
print("Total sales:", total)
