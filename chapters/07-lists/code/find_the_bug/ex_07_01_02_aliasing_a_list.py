"""Exercise 7.1.2 — Aliasing a list

Chapter 7 (Lists), section 7.1: Lists.

Problem
-------
The two names are meant to refer to the same list, so a change through one is seen through the other. This should print the list with the new reading.

Bug type: Logical
-----------------
`list(readings)` builds a brand-new list, so `same_readings` is a separate object and appending to it does not change `readings`. To make both names refer to the same list, assign directly with `same_readings = readings`.

The program below is the corrected version.
"""


readings = [12, 15, 9]
same_readings = readings
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
