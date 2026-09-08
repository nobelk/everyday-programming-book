"""Problem 91 — Reverse a number

Domain: Mathematics. Chapter 10 (Functions), recursion.

Problem
-------
Turn 1234 into 4321.

Expected output
---------------
4321
"""


def reverse_number(n, acc=0):
    if n == 0:
        return acc
    return reverse_number(n // 10, acc * 10 + n % 10)

print(reverse_number(1234))
