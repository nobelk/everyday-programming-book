"""Exercise 10.1.2 — Temperature category

Chapter 10 (Control Flow), section 10.1: if, elif, else.

Problem
-------
This program should classify a temperature in Celsius. With 36.5 it should print only `Heat warning`.

Bug type: Syntax
----------------
The body of the first `if` is not indented, so Python raises an `IndentationError`. Indenting the `print` four spaces fixes it.

The program below is the corrected version.
"""


temp_c = 36.5

if temp_c > 35:
    print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
