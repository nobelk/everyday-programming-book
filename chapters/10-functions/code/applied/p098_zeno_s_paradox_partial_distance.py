"""Problem 98 — Zeno's paradox — partial distance

Domain: Physics. Chapter 10 (Functions), recursion.

Problem
-------
Sum of 1/2 + 1/4 + 1/8 + … up to `n` terms (approaches 1).

Expected output
---------------
0.999023
"""


def zeno(n):
    if n == 0:
        return 0
    return 0.5 ** n + zeno(n - 1)

print(round(zeno(10), 6))
