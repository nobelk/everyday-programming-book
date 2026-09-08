"""Exercise 9.4.4 — Average of readings

Chapter 9 (Control Flow), section 9.4: for Loops.

Problem
-------
This program should print the average of three temperature readings, 30.0.

Bug type: Runtime
-----------------
`len(reading)` uses the loop variable (the last item, an integer) instead of the list, raising a `TypeError`. Use `len(readings)`.

The program below is the corrected version.
"""


readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(readings)
print(average)
