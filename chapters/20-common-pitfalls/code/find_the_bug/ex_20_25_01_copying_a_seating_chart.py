"""Exercise 20.25.1 — Copying a seating chart

Chapter 20 (Common Pitfalls), section 20.25: Shallow vs deep copy.

Problem
-------
This program should copy a seating chart so editing the copy leaves the original unchanged.

Bug type: Logical
-----------------
`original.copy()` is a shallow copy: the inner row lists are still shared, so appending through `backup` also changes `original`. Use `copy.deepcopy`.

The program below is the corrected version.
"""


import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = copy.deepcopy(original)
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
