"""Exercise 9.9.2 — Empty function

Chapter 9 (Control Flow), section 9.9: pass.

Problem
-------
This empty helper is a placeholder, and the program should print `Done`.

Bug type: Syntax
----------------
A function with an empty body is illegal; Python raises an `IndentationError`. Adding `pass` as the placeholder body fixes it.

The program below is the corrected version.
"""


def future_feature():
    pass

future_feature()
print("Done")
