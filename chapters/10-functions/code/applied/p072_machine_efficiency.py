"""Problem 72 — Machine efficiency

Domain: Engineering. Chapter 10 (Functions), functions.

Problem
-------
`η = useful / input × 100%`.

Expected output
---------------
40.0%
"""


def efficiency(useful_j, input_j):
    return useful_j / input_j * 100

print(f"{efficiency(400, 1000):.1f}%")
