"""Exercise 7.3.5 — Within speed limit

Chapter 7 (Operators), section 7.3: Comparison Operators.

Problem
-------
The speed limit is 65. For a speed of 65 this program should report that the driver is within the limit and print `True`.

Bug type: Logical
-----------------
A speed of exactly 65 is within the limit, but `<` excludes it and gives `False`. Use `<=` to include the limit itself.

The program below is the corrected version.
"""


speed = 65
limit = 65
within_limit = speed <= limit
print(within_limit)   # True
