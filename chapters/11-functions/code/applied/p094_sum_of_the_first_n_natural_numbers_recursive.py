"""Problem 94 — Sum of the first N natural numbers (recursive)

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
Recursive twin of Problem 41.

Expected output
---------------
5050
"""


def triangle_sum(n):
    if n == 0:
        return 0
    return n + triangle_sum(n - 1)

print(triangle_sum(100))
