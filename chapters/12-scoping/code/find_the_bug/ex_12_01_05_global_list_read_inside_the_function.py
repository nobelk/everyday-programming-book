"""Exercise 12.1.5 — global list, read inside the function

Chapter 12 (Scoping), section 12.1: Local and Global Scope.

Problem
-------
This program should print the average of a global list of test scores.

Bug type: Syntax
----------------
The `def` line is missing its colon, so the file will not parse. Add the colon after the parentheses.

The program below is the corrected version.
"""


scores = [80, 90, 100]

def average():
    return sum(scores) / len(scores)

print("Average:", average())
