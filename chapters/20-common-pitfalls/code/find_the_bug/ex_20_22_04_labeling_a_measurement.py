"""Exercise 20.22.4 — Labeling a measurement

Chapter 20 (Common Pitfalls), section 20.22: Shadowing built-in names like list, str, or sum.

Problem
-------
The program should print a number alongside its unit as text.

Bug type: Runtime
-----------------
`str = "kilograms"` shadows the built-in `str`, so `str(weight)` tries to call a string and raises `TypeError`. Rename the variable.

The program below is the corrected version.
"""


unit = "kilograms"
weight = 70
print(str(weight) + " " + unit)
