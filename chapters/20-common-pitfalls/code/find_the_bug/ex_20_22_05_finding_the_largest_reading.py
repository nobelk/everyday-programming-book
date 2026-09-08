"""Exercise 20.22.5 — Finding the largest reading

Chapter 20 (Common Pitfalls), section 20.22: Shadowing built-in names like list, str, or sum.

Problem
-------
This program should print the largest of three sensor readings.

Bug type: Runtime
-----------------
`max = 9999` shadows the built-in `max`, so `max(readings)` tries to call an integer and raises `TypeError`. Use a different name.

The program below is the corrected version.
"""


ceiling = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
