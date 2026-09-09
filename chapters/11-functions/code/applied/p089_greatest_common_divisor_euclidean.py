"""Problem 89 — Greatest common divisor (Euclidean)

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
Recursive version of Problem 73.

Expected output
---------------
12
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 180))
