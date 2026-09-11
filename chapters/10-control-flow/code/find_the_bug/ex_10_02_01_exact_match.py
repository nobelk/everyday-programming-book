"""Exercise 10.2.1 — Exact match

Chapter 10 (Control Flow), section 10.2: Common Comparison Operators.

Problem
-------
This program should print `Correct` only when the answer equals 42.

Bug type: Syntax
----------------
A single `=` is assignment, not comparison, and is not allowed in an `if` condition. Use `==` to compare.

The program below is the corrected version.
"""


answer = 42

if answer == 42:
    print("Correct")
else:
    print("Try again")
