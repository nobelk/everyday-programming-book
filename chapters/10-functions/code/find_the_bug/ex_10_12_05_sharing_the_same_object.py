"""Exercise 10.12.5 — Sharing the same object

Chapter 10 (Functions), section 10.12: Pass by Reference vs Pass by Sharing.

Problem
-------
Both names point to the same list, so the append should be visible outside; this prints a 4-item list.

Bug type: Logical
-----------------
`items = list(items)` makes a separate copy, so the append affects only the copy and the caller's list is unchanged. Append directly to the passed-in list.

The program below is the corrected version.
"""


def append_value(items, value):
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
