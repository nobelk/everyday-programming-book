"""Exercise 10.5.4 — Keyword after positional

Chapter 10 (Functions), section 10.5: Keyword Arguments.

Problem
-------
This program should print `"Sam scored 95"` using one positional and one keyword argument.

Bug type: Syntax
----------------
A positional argument cannot follow a keyword argument, so `score_line(name="Sam", 95)` is a `SyntaxError`. Either make both keywords or both positional.

The program below is the corrected version.
"""


def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", points=95)
