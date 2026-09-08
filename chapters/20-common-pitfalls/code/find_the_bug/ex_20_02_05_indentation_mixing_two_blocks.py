"""Exercise 20.2.5 — Indentation mixing two blocks

Chapter 20 (Common Pitfalls), section 20.2: Using the wrong indentation.

Problem
-------
This program should print each grade and then announce the report is finished.

Bug type: Syntax
----------------
The closing `print` is indented two spaces, matching neither the loop body nor the top level, so Python raises an `IndentationError`. Dedenting it to the top level fixes it.

The program below is the corrected version.
"""


grades = [88, 91, 79]
for grade in grades:
    print(grade)
print("Report complete")
