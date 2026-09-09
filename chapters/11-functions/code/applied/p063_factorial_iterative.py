"""Problem 63 — Factorial (iterative)

Domain: Mathematics. Chapter 11 (Functions), functions.

Problem
-------
Write `factorial(n)` using a loop.

Expected output
---------------
720
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(6))
