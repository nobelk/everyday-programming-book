"""Exercise 9.9.4 — Placeholder branch

Chapter 9 (Control Flow), section 9.9: pass.

Problem
-------
For now, negative readings should be ignored (handled later) while others are printed. With this data it should print 5 and 8.

Bug type: Logical
-----------------
After `pass` (which does nothing), the indented `print(reading)` still runs, so negative readings are printed too. Removing that stray `print` leaves the branch as a true placeholder.

The program below is the corrected version.
"""


readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
    else:
        print(reading)
