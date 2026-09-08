"""Problem 87 — Shrinking cell population

Domain: Biology. Chapter 10 (Functions), recursion.

Problem
-------
A dying culture loses 10% of cells each hour. Count after `h` hours.

Expected output
---------------
531.4
"""


def cells_after(initial, h):
    if h == 0:
        return initial
    return 0.9 * cells_after(initial, h - 1)

print(round(cells_after(1000, 6), 1))
