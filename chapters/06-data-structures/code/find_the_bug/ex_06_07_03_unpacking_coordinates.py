"""Exercise 6.7.3 — Unpacking coordinates

Chapter 6 (Data Structures), section 6.7: Tuples.

Problem
-------
The program should unpack a tuple into two variables and print "lat 35.7, lon 139.7".

Bug type: Logical
-----------------
Assigning the whole tuple to each name does not unpack it. Unpack both values at once with `lat, lon = coords`.

The program below is the corrected version.
"""


coords = (35.7, 139.7)
lat, lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
