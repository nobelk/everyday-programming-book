"""Advanced problem 21 — Quadratic Equation Solver (imperative)

Subject: Mathematics. Style: imperative.

Problem
-------
Solve `ax² + bx + c = 0` for any user-supplied coefficients, correctly handling all three discriminant cases.

Concepts taught
---------------
Function returning a tuple, `if/elif/else`, argument unpacking with `*`, raising exceptions.

Expected output
---------------
(1, -3, 2) → ('two real roots', 2.0, 1.0)
(1, 2, 1) → ('one real root', -1.0)
(1, 0, 1) → ('two complex roots', 1j, -1j)
"""


from math import sqrt

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Not a quadratic (a = 0).")
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        r1 = (-b + sqrt(discriminant)) / (2 * a)
        r2 = (-b - sqrt(discriminant)) / (2 * a)
        return ("two real roots", r1, r2)
    elif discriminant == 0:
        return ("one real root", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imag = sqrt(-discriminant) / (2 * a)
        return ("two complex roots", complex(real, imag), complex(real, -imag))

for coeffs in [(1, -3, 2), (1, 2, 1), (1, 0, 1)]:
    print(coeffs, "→", solve_quadratic(*coeffs))
