"""Exercise 9.7.5 — Stop at zero

Chapter 9 (Control Flow), section 9.7: break.

Problem
-------
This program should print readings until it hits a 0, then stop. It should print 5 and 8.

Bug type: Logical
-----------------
`continue` merely skips the 0 and keeps going (printing 3 afterward), but the loop should stop at 0. Use `break`.

The program below is the corrected version.
"""


readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        break
    print(reading)
