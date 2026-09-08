"""Exercise 5.3.2 — Passing grade

Chapter 5 (Data Structures), section 5.3: bool.

Problem
-------
A grade of 60 or more passes. With a grade of 72, the program should print `True`.

Bug type: Runtime
-----------------
`Passed` (capital P) is a different, undefined name, so printing it raises a `NameError`. Print the variable `passed`.

The program below is the corrected version.
"""


grade = 72
passed = grade >= 60
print(passed)   # True
