"""Exercise 9.11.1 — Even check

Chapter 9 (Control Flow), section 9.11: Functions and return.

Problem
-------
This function should return `True` when a number is even. `is_even(4)` should print `True`.

Bug type: Logical
-----------------
The function computes `number % 2 == 0` but never returns it, so it returns `None`. Adding `return` sends the result back.

The program below is the corrected version.
"""


def is_even(number):
    return number % 2 == 0

print(is_even(4))
