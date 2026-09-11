"""Problem 81 — Factorial (recursive)

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
Same as Problem 63, but recursive.

Expected output
---------------
120
"""


def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))
