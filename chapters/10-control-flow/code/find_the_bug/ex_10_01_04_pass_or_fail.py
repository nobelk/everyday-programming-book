"""Exercise 10.1.4 — Pass or fail

Chapter 10 (Control Flow), section 10.1: if, elif, else.

Problem
-------
This program should print `Pass` when a score is at least 60, otherwise `Fail`. With 75 it should print `Pass`.

Bug type: Syntax
----------------
The `else` is indented as if it were inside the `if` body, which is illegal. Aligning `else` with `if` fixes it.

The program below is the corrected version.
"""


score = 75

if score >= 60:
    print("Pass")
else:
    print("Fail")
