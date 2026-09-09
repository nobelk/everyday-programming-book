"""Exercise 17.4.3 — Logging an attempt

Chapter 17 (Handling Failures), section 17.4: Using finally.

Problem
-------
This program parses a count and must always log that an attempt was made, regardless of success.

Bug type: Syntax
----------------
The `finally` keyword is missing its colon, so the file will not parse. Add the colon after `finally`.

The program below is the corrected version.
"""


try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally:
    print("Attempt logged.")
