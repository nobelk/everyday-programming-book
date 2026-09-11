"""Problem 77 — Least common multiple

Domain: Mathematics. Chapter 11 (Functions), functions.

Problem
-------
Build `lcm` on top of `gcd`.

Expected output
---------------
36
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(12, 18))
