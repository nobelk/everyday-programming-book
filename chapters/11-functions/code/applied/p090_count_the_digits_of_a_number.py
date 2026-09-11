"""Problem 90 — Count the digits of a number

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
How many digits does 987 654 have?

Expected output
---------------
6
"""


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(987654))
