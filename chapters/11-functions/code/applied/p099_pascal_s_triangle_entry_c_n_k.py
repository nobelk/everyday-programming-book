"""Problem 99 — Pascal's triangle entry C(n, k)

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
`C(n, k) = C(n−1, k−1) + C(n−1, k)`, with base cases at the triangle's edges.

Expected output
---------------
15
"""


def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

print(pascal(6, 2))
