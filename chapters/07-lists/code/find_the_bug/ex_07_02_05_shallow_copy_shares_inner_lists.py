"""Exercise 7.2.5 — Shallow copy shares inner lists

Chapter 7 (Lists), section 7.2: Copying a List.

Problem
-------
The seating chart is a list of rows. We copy it, then add a seat to one row of the copy; the original chart should be unchanged.

Bug type: Logical
-----------------
`seats.copy()` is a shallow copy: the outer list is new, but the row lists are shared, so `new_seats[0].append` also changes `seats`. Using `copy.deepcopy` copies each row, leaving the original chart unchanged.

The program below is the corrected version.
"""


import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = copy.deepcopy(seats)
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
