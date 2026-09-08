"""Exercise 9.11.2 — Describe a number

Chapter 9 (Control Flow), section 9.11: Functions and return.

Problem
-------
This function should return "positive", "negative", or "zero". `describe(-3)` should print `negative`.

Bug type: Logical
-----------------
The negative branch builds the string `"negative"` but never returns it, so `describe(-3)` falls off that branch and returns `None`. Adding `return` fixes it.

The program below is the corrected version.
"""


def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(describe(-3))
