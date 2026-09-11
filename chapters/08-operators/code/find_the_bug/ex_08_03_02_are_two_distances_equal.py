"""Exercise 8.3.2 — Are two distances equal?

Chapter 8 (Operators), section 8.3: Comparison Operators.

Problem
-------
This program should check whether two measured distances are equal and print `True`.

Bug type: Runtime
-----------------
Inside a function call, `distance_a = distance_b` is read as a keyword argument, so `print` raises a `TypeError` about an invalid keyword argument. Comparison needs the equality operator `==`.

The program below is the corrected version.
"""


distance_a = 100
distance_b = 100
print(distance_a == distance_b)   # True
