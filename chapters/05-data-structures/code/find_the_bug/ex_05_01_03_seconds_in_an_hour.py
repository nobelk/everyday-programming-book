"""Exercise 5.1.3 — Seconds in an hour

Chapter 5 (Data Structures), section 5.1: int.

Problem
-------
There are 60 seconds in a minute and 60 minutes in an hour. The program should print 3600.

Bug type: Logical
-----------------
The two counts must be multiplied, not added; `60 + 60` gives 120, not 3600. Use `*`.

The program below is the corrected version.
"""


seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)   # 3600
