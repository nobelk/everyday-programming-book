"""Problem 96 — Number of ancestors `g` generations back

Domain: Biology. Chapter 11 (Functions), recursion.

Problem
-------
You have 2 parents, 4 grandparents, 8 great-grandparents… How many ancestors at generation `g`?

Expected output
---------------
1024
"""


def ancestors(g):
    if g == 0:
        return 1   # you
    return 2 * ancestors(g - 1)

print(ancestors(10))
