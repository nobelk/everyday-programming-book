"""Problem 92 — Decimal → binary as a string

Domain: Mathematics / Engineering. Chapter 11 (Functions), recursion.

Problem
-------
Convert a non-negative integer to its binary representation.

Expected output
---------------
1101
"""


def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

print(to_binary(13))
