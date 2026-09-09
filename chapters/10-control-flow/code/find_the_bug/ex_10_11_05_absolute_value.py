"""Exercise 10.11.5 — Absolute value

Chapter 10 (Control Flow), section 10.11: Functions and return.

Problem
-------
This function should return the absolute value of a number. `absolute(7)` should print `7`.

Bug type: Logical
-----------------
When the number is not negative there is no `return`, so the function falls off the end and returns `None`. Adding an `else` (or a final `return number`) handles the non-negative case.

The program below is the corrected version.
"""


def absolute(number):
    if number < 0:
        return -number
    else:
        return number

print(absolute(7))
