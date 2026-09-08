"""Problem 38 — Quadratic — real or complex roots?

Domain: Mathematics. Chapter 9 (Control Flow), conditionals.

Problem
-------
Compute the discriminant `b² − 4ac` and say whether roots are real or complex.

Expected output
---------------
Complex roots
"""


a, b, c = 1, 3, 5
discriminant = b * b - 4 * a * c
if discriminant >= 0:
    print("Real roots")
else:
    print("Complex roots")
