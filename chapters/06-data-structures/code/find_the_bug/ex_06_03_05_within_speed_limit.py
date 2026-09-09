"""Exercise 6.3.5 — Within speed limit

Chapter 6 (Data Structures), section 6.3: bool.

Problem
-------
The limit is 65. A car going 60 is within the limit, so the program should print `True`.

Bug type: Logical
-----------------
Being within the limit means the speed is at or below it, but `>` tests the opposite. Use `<=` so 60 within 65 gives True.

The program below is the corrected version.
"""


speed = 60
limit = 65

within_limit = speed <= limit
print(within_limit)   # True
