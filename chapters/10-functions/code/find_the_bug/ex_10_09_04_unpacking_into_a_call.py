"""Exercise 10.9.4 — Unpacking into a call

Chapter 10 (Functions), section 10.9: *args and **kwargs.

Problem
-------
This program should pass the list as separate positional arguments and print 6.

Bug type: Runtime
-----------------
Passing the list as one argument fills only `a`, leaving `b` and `c` missing, which raises a `TypeError`. Unpack with a star: `add_three(*numbers)`.

The program below is the corrected version.
"""


def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(*numbers))  # 6
