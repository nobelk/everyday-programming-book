"""Exercise 11.9.1 — Collecting positionals

Chapter 11 (Functions), section 11.9: *args and **kwargs.

Problem
-------
This program should sum any number of grades passed in; here the total should be 270.

Bug type: Runtime
-----------------
Without a `*`, `args` is a single parameter, so passing three numbers raises a `TypeError`. Add the star to collect them into a tuple.

The program below is the corrected version.
"""


def total(*args):
    return sum(args)

print(total(90, 85, 95))  # 270
