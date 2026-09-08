"""Exercise 20.16.2 — Averaging three test grades

Chapter 20 (Common Pitfalls), section 20.16: Not returning a value from a function.

Problem
-------
The program should print the average of three grades.

Bug type: Logical
-----------------
The average is computed into `average_value` but never returned, so `None` is printed. Return the value.

The program below is the corrected version.
"""


def average(a, b, c):
    total = a + b + c
    average_value = total / 3
    return average_value

print("Average:", average(80, 90, 100))
