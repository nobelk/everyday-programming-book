"""Problem 80 — Molarity of a solution

Domain: Chemistry. Chapter 10 (Functions), functions.

Problem
-------
`M = moles / litres`.

Expected output
---------------
0.25
"""


def molarity(moles, volume_l):
    return moles / volume_l

print(molarity(0.5, 2.0))
