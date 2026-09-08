"""Exercise 20.16.1 — Converting miles to kilometers

Chapter 20 (Common Pitfalls), section 20.16: Not returning a value from a function.

Problem
-------
This program should print the distance in kilometers for 5 miles.

Bug type: Logical
-----------------
The function computes `km` but never returns it, so the call yields `None`. Add a `return`.

The program below is the corrected version.
"""


def miles_to_km(miles):
    km = miles * 1.60934
    return km

print("Kilometers:", miles_to_km(5))
