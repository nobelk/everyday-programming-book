"""Problem 86 — Remaining radioactive atoms

Domain: Chemistry. Chapter 11 (Functions), recursion.

Problem
-------
Amount left after `n` half-lives.

Expected output
---------------
62.5
"""


def remaining(initial, n):
    if n == 0:
        return initial
    return remaining(initial, n - 1) / 2

print(remaining(1000, 4))
