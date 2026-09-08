"""Exercise 5.3.4 — Empty cart

Chapter 5 (Data Structures), section 5.3: bool.

Problem
-------
A cart is empty when it has 0 items. The program should print `True`.

Bug type: Logical
-----------------
`is_empty = items = 0` is a chained assignment that sets `is_empty` to `0`, not the comparison you intended; it runs but prints `0`. Comparing values needs `==`, so write `is_empty = items == 0`.

The program below is the corrected version.
"""


items = 0
is_empty = items == 0
print(is_empty)   # True
