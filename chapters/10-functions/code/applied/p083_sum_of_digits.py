"""Problem 83 — Sum of digits

Domain: Mathematics. Chapter 10 (Functions), recursion.

Problem
-------
Add the digits of 12 345 by peeling off the last one.

Expected output
---------------
15
"""


def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))
