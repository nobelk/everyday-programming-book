"""Exercise 11.1.3 — The function body

Chapter 11 (Functions), section 11.1: Your First Function.

Problem
-------
This program should print the number of days in a week when called.

Bug type: Syntax
----------------
The body must be indented under the `def` line. An unindented `print` makes Python expect an indented block and raises an `IndentationError`.

The program below is the corrected version.
"""


def days_in_week():
    print("A week has 7 days.")

days_in_week()
