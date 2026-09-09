"""Exercise 10.5.3 — Counting down

Chapter 10 (Control Flow), section 10.5: range.

Problem
-------
This program should count down from 5 to 1.

Bug type: Logical
-----------------
To count downward, `range` needs a negative step; `range(5, 0)` counts *up* and produces nothing because 5 is already past 0. Use `range(5, 0, -1)`.

The program below is the corrected version.
"""


for number in range(5, 0, -1):
    print(number)
