"""Exercise 20.16.3 — Doubling a recipe

Chapter 20 (Common Pitfalls), section 20.16: Not returning a value from a function.

Problem
-------
This program should return the doubled amount of flour.

Bug type: Logical
-----------------
`doubled` is computed but not returned, so `flour` becomes `None`. Add `return doubled`.

The program below is the corrected version.
"""


def double_amount(cups):
    doubled = cups * 2
    return doubled

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
