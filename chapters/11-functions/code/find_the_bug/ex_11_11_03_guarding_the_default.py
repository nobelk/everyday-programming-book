"""Exercise 11.11.3 — Guarding the default

Chapter 11 (Functions), section 11.11: Mutable Default Argument Trap.

Problem
-------
The guard should replace the shared default with a new list when none is given.

Bug type: Runtime
-----------------
The guard assigns `scores = scores`, leaving it `None`, so `append` raises an `AttributeError`. Assign a new empty list instead.

The program below is the corrected version.
"""


def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(90))  # [90]
