"""Exercise 20.25.2 — Backing up monthly budgets

Chapter 20 (Common Pitfalls), section 20.25: Shallow vs deep copy.

Problem
-------
The program should make an independent copy of a nested budget so changes do not leak back.

Bug type: Logical
-----------------
Slicing with `[:]` copies only the outer list; the nested lists stay shared, so editing `saved` edits `budgets`. Use `copy.deepcopy`.

The program below is the corrected version.
"""


import copy

budgets = [[100, 200], [300, 400]]
saved = copy.deepcopy(budgets)
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
