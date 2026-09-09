"""Exercise 11.5.3 — Spelling the keyword

Chapter 11 (Functions), section 11.5: Keyword Arguments.

Problem
-------
This program should print a labeled temperature using a keyword argument.

Bug type: Runtime
-----------------
The keyword `temp` does not match the parameter `temperature`, raising a `TypeError`. Use the exact parameter name.

The program below is the corrected version.
"""


def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temperature=30)
