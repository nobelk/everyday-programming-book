"""Exercise 6.4.4 — Indexing the last item

Chapter 6 (Objects), section 6.4: Lists.

Problem
-------
This program prints the most recent score in the list.

Bug type: Runtime
-----------------
`len(scores)` is 4, but valid indexes are 0 through 3, so `scores[len(scores)]` raises an `IndexError`. The last item is at `scores[len(scores) - 1]`, or more simply `scores[-1]`.

The program below is the corrected version.
"""


scores = [91, 87, 95, 78]
latest = scores[-1]
print(latest)   # 78
