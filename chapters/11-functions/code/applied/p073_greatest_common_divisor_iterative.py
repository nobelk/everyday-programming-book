"""Problem 73 — Greatest common divisor (iterative)

Domain: Mathematics. Chapter 11 (Functions), functions.

Problem
-------
Use Euclid's algorithm in a loop.

Expected output
---------------
12
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 180))
