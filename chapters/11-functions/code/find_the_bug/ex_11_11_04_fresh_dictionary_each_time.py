"""Exercise 11.11.4 — Fresh dictionary each time

Chapter 11 (Functions), section 11.11: Mutable Default Argument Trap.

Problem
-------
Each call should return a dictionary with just one entry.

Bug type: Logical
-----------------
The default dictionary is created once and shared, so entries accumulate across calls. Use `None` and create a fresh dictionary inside.

The program below is the corrected version.
"""


def tally(name, counts=None):
    if counts is None:
        counts = {}
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
