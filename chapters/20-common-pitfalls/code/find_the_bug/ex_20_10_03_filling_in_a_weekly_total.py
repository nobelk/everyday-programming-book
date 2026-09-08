"""Exercise 20.10.3 — Filling in a weekly total

Chapter 20 (Common Pitfalls), section 20.10: Modifying a list item that does not exist.

Problem
-------
This program should set the fourth week's sales figure.

Bug type: Runtime
-----------------
Index 3 is past the end of a three-item list, so the assignment raises `IndexError`. Use `append` to extend the list.

The program below is the corrected version.
"""


weekly_sales = [100, 120, 90]
weekly_sales.append(110)
print(weekly_sales)
