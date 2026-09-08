"""Problem 84 — Power function

Domain: Mathematics. Chapter 10 (Functions), recursion.

Problem
-------
Compute `x^n` for a non-negative integer `n`.

Expected output
---------------
1024
"""


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 10))
