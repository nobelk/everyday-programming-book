"""Exercise 19.3.1 — Rectangle area

Chapter 19 (Bugs), section 19.3: Logical Bugs.

Problem
-------
This program should print the area of a 6 by 4 rectangle.

Bug type: Logical
-----------------
The program runs but uses `+` where area requires multiplication, so it returns 10 instead of 24. Multiplying length by width gives the correct area.

The program below is the corrected version.
"""


def area(length, width):
    return length * width

print(area(6, 4))   # 24
