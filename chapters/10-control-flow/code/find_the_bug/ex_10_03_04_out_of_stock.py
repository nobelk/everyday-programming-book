"""Exercise 10.3.4 — Out of stock

Chapter 10 (Control Flow), section 10.3: Logical Operators.

Problem
-------
This program should print `Reorder` when an item is not in stock. With stock False it should print `Reorder`.

Bug type: Syntax
----------------
`not in_stock = True` mixes `not` with an assignment, which is invalid. The intent is simply to test the negation, so write `if not in_stock:`.

The program below is the corrected version.
"""


in_stock = False

if not in_stock:
    print("Reorder")
