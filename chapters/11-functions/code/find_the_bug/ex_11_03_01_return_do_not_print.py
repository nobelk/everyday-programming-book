"""Exercise 11.3.1 — Return, do not print

Chapter 11 (Functions), section 11.3: Returning a Result.

Problem
-------
This program should store the sum of two numbers and then print 12.

Bug type: Logical
-----------------
The function prints instead of returning, so `total` becomes `None`. Use `return` so the caller receives the value.

The program below is the corrected version.
"""


def add(a, b):
    return a + b

total = add(5, 7)
print(total)  # 12
