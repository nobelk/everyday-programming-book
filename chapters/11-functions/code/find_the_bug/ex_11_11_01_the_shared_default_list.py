"""Exercise 11.11.1 — The shared default list

Chapter 11 (Functions), section 11.11: Mutable Default Argument Trap.

Problem
-------
Each call should start with a fresh list, so both lines print a single-item list.

Bug type: Logical
-----------------
The default list is created once and shared across calls, so it keeps growing. Use `None` as the default and build a fresh list inside.

The program below is the corrected version.
"""


def collect(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
