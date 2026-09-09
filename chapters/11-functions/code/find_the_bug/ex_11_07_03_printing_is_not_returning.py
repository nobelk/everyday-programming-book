"""Exercise 11.7.3 — Printing is not returning

Chapter 11 (Functions), section 11.7: Implicit None Return.

Problem
-------
This should store the area of a circle approximation and print about 78.5, then use it again.

Bug type: Runtime
-----------------
The function prints but returns `None`, so `area` is `None` and `area * 2` raises a `TypeError`. Return the value instead of printing it.

The program below is the corrected version.
"""


def circle_area(radius):
    return 3.14 * radius * radius

area = circle_area(5)
print(area * 2)  # uses the area twice
