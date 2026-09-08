"""Example 5 — Greatest common divisor, written recursively

Chapter 2 (Problem Solving).

Problem
-------
The same algorithm, expressed as a function that calls itself instead of looping.

Notes
-----
The `if b == 0` branch is the base case — the point at which the function stops calling itself. A recursive function without a base case never finishes. Compare it with the loop above: same algorithm, two ways of writing the repetition.
"""


def gcd_recursive(a, b):
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


print(gcd_recursive(60, 48))   # 12
