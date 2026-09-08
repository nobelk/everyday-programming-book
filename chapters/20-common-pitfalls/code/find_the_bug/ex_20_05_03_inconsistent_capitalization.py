"""Exercise 20.5.3 — Inconsistent capitalization

Chapter 20 (Common Pitfalls), section 20.5: Misspelling variable names.

Problem
-------
This program should print a city's recorded high temperature.

Bug type: Runtime
-----------------
Python is case-sensitive: `Temperature` and `temperature` are different names, so the `print` raises `NameError`. Match the case used at assignment.

The program below is the corrected version.
"""


Temperature = 31
print(Temperature)
