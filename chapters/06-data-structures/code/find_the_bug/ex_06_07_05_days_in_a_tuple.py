"""Exercise 6.7.5 — Days in a tuple

Chapter 6 (Data Structures), section 6.7: Tuples.

Problem
-------
A tuple holds three weekday names. The program should print the second one, "Tue".

Bug type: Logical
-----------------
Index 1 is the second item ("Tue"); `days[2]` returns "Wed". Use index `1`.

The program below is the corrected version.
"""


days = ("Mon", "Tue", "Wed")
print(days[1])   # Tue
