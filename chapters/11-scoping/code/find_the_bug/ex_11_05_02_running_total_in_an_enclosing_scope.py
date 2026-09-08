"""Exercise 11.5.2 — running total in an enclosing scope

Chapter 11 (Scoping), section 11.5: Using nonlocal in Nested Functions.

Problem
-------
This program adds amounts into an enclosing `total` using `nonlocal`, and should print 30 after two deposits.

Bug type: Logical
-----------------
A deposit should add to the total, but the code subtracts, so the balance goes negative. Use addition.

The program below is the corrected version.
"""


def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total + amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
