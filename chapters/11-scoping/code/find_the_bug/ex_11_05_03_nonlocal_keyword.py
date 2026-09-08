"""Exercise 11.5.3 — nonlocal keyword

Chapter 11 (Scoping), section 11.5: Using nonlocal in Nested Functions.

Problem
-------
This program tracks the highest reading seen so far using `nonlocal`, and should print 9 after two readings.

Bug type: Syntax
----------------
The final `print` call is missing its closing parenthesis, so the file will not parse. Add the closing parenthesis.

The program below is the corrected version.
"""


def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9))
