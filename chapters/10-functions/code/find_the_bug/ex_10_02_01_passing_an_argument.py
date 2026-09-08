"""Exercise 10.2.1 — Passing an argument

Chapter 10 (Functions), section 10.2: Parameters.

Problem
-------
This program should greet a student by name.

Bug type: Runtime
-----------------
The function needs one argument but the call passes none, raising a `TypeError`. Supply the name in the call.

The program below is the corrected version.
"""


def greet_student(name):
    print("Hello,", name)

greet_student("Maya")
