"""Exercise 7.2.3 — Copying with a slice

Chapter 7 (Lists), section 7.2: Copying a List.

Problem
-------
A slice copy of a flat list should leave the original alone.

Bug type: Logical
-----------------
The slice `grades[0:2]` copies only the first two items, so `working` starts as `[85, 90]` and the result is wrong. A full-list slice `grades[:]` copies every element.

The program below is the corrected version.
"""


grades = [85, 90, 78]
working = grades[:]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
