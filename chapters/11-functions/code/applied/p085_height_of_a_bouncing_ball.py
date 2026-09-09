"""Problem 85 — Height of a bouncing ball

Domain: Physics. Chapter 11 (Functions), recursion.

Problem
-------
Each bounce keeps 70% of the previous height. Peak height after `n` bounces?

Expected output
---------------
1.681
"""


def bounce_height(initial_m, n):
    if n == 0:
        return initial_m
    return 0.7 * bounce_height(initial_m, n - 1)

print(round(bounce_height(10, 5), 3))
