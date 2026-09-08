"""Exercise 18.3.2 — Average of three grades

Chapter 18 (Bugs), section 18.3: Logical Bugs.

Problem
-------
This program should print the average of three test grades.

Bug type: Logical
-----------------
Operator precedence divides only `c` by 3 before adding, so the result is wrong. Parenthesizing the sum before dividing computes the true average.

The program below is the corrected version.
"""


def average(a, b, c):
    return (a + b + c) / 3

print(average(80, 90, 100))   # 90.0
