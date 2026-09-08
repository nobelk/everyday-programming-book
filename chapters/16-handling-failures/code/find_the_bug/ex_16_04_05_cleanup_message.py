"""Exercise 16.4.5 — Cleanup message

Chapter 16 (Handling Failures), section 16.4: Using finally.

Problem
-------
This program reads a distance and must always print a cleanup line at the very end, no matter what happens.

Bug type: Syntax
----------------
The clauses are out of order: `finally` appears before `except`, which is not allowed — `except` (and `else`) must come before `finally`. Reorder so `except` precedes `finally`.

The program below is the corrected version.
"""


try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
except ValueError:
    print("That was not a number.")
finally:
    print("Sensor reset.")
