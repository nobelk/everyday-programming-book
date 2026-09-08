"""Problem 88 — Age of a rock stack layer by layer

Domain: Geology. Chapter 10 (Functions), recursion.

Problem
-------
Each sedimentary layer is `years_per_layer` older than the one above. Age of layer `n`.

Expected output
---------------
6000
"""


def layer_age(n, years_per_layer):
    if n == 0:
        return 0
    return years_per_layer + layer_age(n - 1, years_per_layer)

print(layer_age(5, 1200))
