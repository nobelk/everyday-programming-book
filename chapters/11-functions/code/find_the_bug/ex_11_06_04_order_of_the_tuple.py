"""Exercise 11.6.4 — Order of the tuple

Chapter 11 (Functions), section 11.6: Multiple Return Values.

Problem
-------
This should report width then height of a 8 by 3 rectangle, printing `"width 8 height 3"`.

Bug type: Logical
-----------------
The tuple is returned as `(3, 8)` but the caller expects width first, so width prints as 3. Return width then height: `return 8, 3`.

The program below is the corrected version.
"""


def dimensions():
    return 8, 3

width, height = dimensions()
print("width", width, "height", height)
