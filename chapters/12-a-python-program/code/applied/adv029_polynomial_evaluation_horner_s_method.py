"""Advanced problem 29 — Polynomial Evaluation (Horner's Method) (functional)

Subject: Mathematics. Style: functional.

Problem
-------
Evaluate `P(x) = 2x³ - 4x² + 3x - 5` at `x = -2, -1, 0, 1, 2` using Horner's method, expressed via `reduce`.

Concepts taught
---------------
Horner's method as a fold, `reduce` with non-trivial combining function, lambda capturing `x`.

Expected output
---------------
P(-2) = -43
P(-1) = -14
P( 0) = -5
P( 1) = -4
P( 2) = 1
"""


from functools import reduce

coeffs = [2, -4, 3, -5]      # highest power first
horner = lambda x: reduce(lambda acc, c: acc * x + c, coeffs, 0)

for x in [-2, -1, 0, 1, 2]:
    print(f"P({x:>2}) = {horner(x)}")
