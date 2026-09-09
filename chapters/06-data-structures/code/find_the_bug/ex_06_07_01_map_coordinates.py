"""Exercise 6.7.1 — Map coordinates

Chapter 6 (Data Structures), section 6.7: Tuples.

Problem
-------
A location is stored as a (latitude, longitude) tuple. The program should print the latitude, 41.8781.

Bug type: Logical
-----------------
Index 0 is the latitude; `location[1]` returns the longitude. Use index `0`.

The program below is the corrected version.
"""


location = (41.8781, -87.6298)
print(location[0])   # 41.8781
