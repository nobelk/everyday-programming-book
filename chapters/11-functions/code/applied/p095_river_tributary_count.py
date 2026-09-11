"""Problem 95 — River-tributary count

Domain: Geography. Chapter 11 (Functions), recursion.

Problem
-------
A river system branches: each branch splits into 2 new branches for `n` levels. Total tributaries?

Expected output
---------------
64
"""


def tributaries(n):
    if n == 0:
        return 1
    return 2 * tributaries(n - 1)

print(tributaries(6))
