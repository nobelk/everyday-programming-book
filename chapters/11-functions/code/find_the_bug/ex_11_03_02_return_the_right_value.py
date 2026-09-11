"""Exercise 11.3.2 — Return the right value

Chapter 11 (Functions), section 11.3: Returning a Result.

Problem
-------
This function should return the average of three test scores.

Bug type: Logical
-----------------
Division binds tighter than addition, so only `c` is divided by 3. Wrap the sum in parentheses before dividing.

The program below is the corrected version.
"""


def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(80, 90, 100))  # 90.0
