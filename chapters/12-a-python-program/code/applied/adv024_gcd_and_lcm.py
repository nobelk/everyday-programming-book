"""Advanced problem 24 — GCD and LCM (imperative)

Subject: Mathematics. Style: imperative.

Problem
-------
Find the greatest common divisor and least common multiple of two numbers using Euclid's algorithm.

Concepts taught
---------------
`while` loop, multiple assignment (tuple swap), function composition.

Expected output
---------------
gcd(12,18) = 6, lcm(12,18) = 36
gcd(100,75) = 25, lcm(100,75) = 300
gcd(17,31) = 1, lcm(17,31) = 527
"""


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

for a, b in [(12, 18), (100, 75), (17, 31)]:
    print(f"gcd({a},{b}) = {gcd(a, b)}, lcm({a},{b}) = {lcm(a, b)}")
