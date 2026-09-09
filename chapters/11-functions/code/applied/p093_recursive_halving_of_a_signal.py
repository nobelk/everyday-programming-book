"""Problem 93 — Recursive halving of a signal

Domain: Engineering. Chapter 11 (Functions), recursion.

Problem
-------
A signal's amplitude halves at every filter stage. Amplitude after `k` stages.

Expected output
---------------
4.0
"""


def amplitude_after(initial, k):
    if k == 0:
        return initial
    return amplitude_after(initial, k - 1) / 2

print(amplitude_after(1024, 8))
