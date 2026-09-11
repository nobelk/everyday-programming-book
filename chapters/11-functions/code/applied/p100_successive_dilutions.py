"""Problem 100 — Successive dilutions

Domain: Chemistry. Chapter 11 (Functions), recursion.

Problem
-------
Each dilution multiplies the concentration by 0.1 (a "1-in-10" dilution). Concentration after `n` dilutions?

Expected output
---------------
1.0000000000000004e-05
"""


def diluted(initial_molar, n):
    if n == 0:
        return initial_molar
    return 0.1 * diluted(initial_molar, n - 1)

print(diluted(1.0, 5))
