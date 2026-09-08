"""Exercise 10.3.5 — Use the returned value

Chapter 10 (Functions), section 10.3: Returning a Result.

Problem
-------
This program should print the square of 6, which is 36.

Bug type: Runtime
-----------------
The returned value is discarded and `area` is never defined, so printing it raises a `NameError`. Store the result, then print it.

The program below is the corrected version.
"""


def square(side):
    return side * side

area = square(6)
print(area)  # 36
