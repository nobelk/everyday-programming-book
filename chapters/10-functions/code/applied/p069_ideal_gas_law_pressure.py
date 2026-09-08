"""Problem 69 — Ideal-gas law — pressure

Domain: Chemistry. Chapter 10 (Functions), functions.

Problem
-------
`P = n R T / V`.

Expected output
---------------
1.092
"""


def pressure(n_moles, temp_k, volume_l):
    R = 0.0821  # L·atm/(mol·K)
    return n_moles * R * temp_k / volume_l

print(round(pressure(1, 298, 22.4), 3))
