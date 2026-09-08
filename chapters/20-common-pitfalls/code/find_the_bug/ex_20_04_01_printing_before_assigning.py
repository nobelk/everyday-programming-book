"""Exercise 20.4.1 — Printing before assigning

Chapter 20 (Common Pitfalls), section 20.4: Using a variable before it is created.

Problem
-------
This program should report the number of students in a class.

Bug type: Runtime
-----------------
`students` is used on the first line but assigned on the second, raising `NameError`. Assign before using.

The program below is the corrected version.
"""


students = 30
print(students)
