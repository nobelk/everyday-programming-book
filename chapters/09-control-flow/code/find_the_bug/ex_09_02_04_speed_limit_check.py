"""Exercise 9.2.4 — Speed limit check

Chapter 9 (Control Flow), section 9.2: Common Comparison Operators.

Problem
-------
A car at exactly the speed limit is allowed. This program should print `OK` when speed is at most 60. At 60 it should print `OK`.

Bug type: Logical
-----------------
``At most 60'' includes 60, but `<` excludes it, so a car at the limit is wrongly flagged. Use `<=`.

The program below is the corrected version.
"""


speed = 60
limit = 60

if speed <= limit:
    print("OK")
else:
    print("Too fast")
