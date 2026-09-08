"""Problem 82 — Fibonacci number

Domain: Mathematics. Chapter 10 (Functions), recursion.

Problem
-------
Rabbit-population classic: `F(n) = F(n−1) + F(n−2)`.

Expected output
---------------
55
"""


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
