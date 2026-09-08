"""Problem 66 — Earthquake energy from magnitude

Domain: Geology. Chapter 10 (Functions), functions.

Problem
-------
`log10(E) = 1.5 M + 4.8` (energy in joules).

Expected output
---------------
6.31e+13 J
"""


def earthquake_energy(magnitude):
    return 10 ** (1.5 * magnitude + 4.8)

print(f"{earthquake_energy(6):.2e} J")
