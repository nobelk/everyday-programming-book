"""Exercise 12.2.3 — shadowing a built-in name

Chapter 12 (Scoping), section 12.2: A Local Variable Can Hide a Global Variable.

Problem
-------
This program should add up a list of grocery prices and print the total.

Bug type: Runtime
-----------------
The global `sum = 0` shadows the built-in `sum` function, so `sum(prices)` tries to call an integer and raises `TypeError`. Remove the shadowing variable so the built-in is used.

The program below is the corrected version.
"""


prices = [2.50, 1.25, 3.00]

def total():
    return sum(prices)

print("Total:", total())
