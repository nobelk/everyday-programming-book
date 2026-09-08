"""Exercise 9.10.3 — Locating a point

Chapter 9 (Control Flow), section 9.10: match / case.

Problem
-------
This program should describe a point. For (0, 5) it should print `On the y-axis at 5`.

Bug type: Logical
-----------------
The catch-all `(x, y)` pattern matches *any* pair, so it is reached before the specific y-axis case and (0, 5) is wrongly labelled ``Somewhere else''. The general pattern must come last, after the specific ones.

The program below is the corrected version.
"""


point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On the y-axis at", y)
    case (x, y):
        print("Somewhere else:", x, y)
