"""Exercise 9.11.3 — First match returns

Chapter 9 (Control Flow), section 9.11: Functions and return.

Problem
-------
This function should return the first number greater than 10, or `None`. For this list it should print 15.

Bug type: Logical
-----------------
The function `print`s the match instead of returning it, so `first_big` returns `None`. Replacing `print` with `return` sends the value back to the caller.

The program below is the corrected version.
"""


def first_big(numbers):
    for number in numbers:
        if number > 10:
            return number

print(first_big([4, 15, 22]))
