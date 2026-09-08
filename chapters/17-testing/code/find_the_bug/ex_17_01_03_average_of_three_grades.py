"""Exercise 17.1.3 — Average of three grades

Chapter 17 (Testing), section 17.1: Why Test Python Functions.

Problem
-------
The function should return the average of three test grades, and the assert should pass for grades 80, 90, and 100.

Bug type: Logical
-----------------
Operator precedence divides only `c` by 3 before adding, instead of dividing the whole sum. Parentheses around the sum fix the formula so the average is computed correctly.

The program below is the corrected version.
"""


def average(a, b, c):
    return (a + b + c) / 3

assert average(80, 90, 100) == 90
print("passed")
