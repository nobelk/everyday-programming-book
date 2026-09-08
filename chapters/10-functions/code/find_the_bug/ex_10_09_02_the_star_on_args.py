"""Exercise 10.9.2 — The star on args

Chapter 10 (Functions), section 10.9: *args and **kwargs.

Problem
-------
This program should print all the extra numbers it receives as a tuple.

Bug type: Runtime
-----------------
`args` without a star accepts only one argument, so passing three raises a `TypeError`. Use `*args` to gather them.

The program below is the corrected version.
"""


def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
