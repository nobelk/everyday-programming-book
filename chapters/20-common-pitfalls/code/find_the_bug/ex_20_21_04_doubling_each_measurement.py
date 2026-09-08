"""Exercise 20.21.4 — Doubling each measurement

Chapter 20 (Common Pitfalls), section 20.21: Using range(len(...)) when iterating over items directly is simpler.

Problem
-------
The program should print double each measurement in the list.

Bug type: Logical
-----------------
`range(len(...))` makes `m` the index 0, 1, 2, so it doubles indexes, not values. Iterate over the measurements directly.

The program below is the corrected version.
"""


measurements = [3, 5, 8]
for m in measurements:
    print(m * 2)
