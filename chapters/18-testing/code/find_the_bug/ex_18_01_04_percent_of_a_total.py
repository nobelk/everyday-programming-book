"""Exercise 18.1.4 — Percent of a total

Chapter 18 (Testing), section 18.1: Why Test Python Functions.

Problem
-------
The function should return what percent `part` is of `whole`, and the assert should pass for 25 out of 50.

Bug type: Syntax
----------------
The function header is missing the colon at the end of the `def` line, so the file will not parse. Adding the colon fixes it.

The program below is the corrected version.
"""


def percent(part, whole):
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
