"""Exercise 10.6.2 — Unpacking the result

Chapter 10 (Functions), section 10.6: Multiple Return Values.

Problem
-------
This program should print the quotient and remainder of 17 divided by 5.

Bug type: Runtime
-----------------
The pair is stored in one name `quotient`, and `remainder` is never defined, so printing it raises a `NameError`. Unpack into two names.

The program below is the corrected version.
"""


def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(quotient, remainder)  # 3 2
