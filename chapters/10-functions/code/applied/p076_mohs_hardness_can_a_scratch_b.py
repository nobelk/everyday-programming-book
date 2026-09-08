"""Problem 76 — Mohs hardness — can A scratch B?

Domain: Geology. Chapter 10 (Functions), functions.

Problem
-------
Return `True` if mineral A can scratch mineral B.

Expected output
---------------
True
"""


def can_scratch(hardness_a, hardness_b):
    return hardness_a > hardness_b

print(can_scratch(7, 3))  # quartz vs calcite
