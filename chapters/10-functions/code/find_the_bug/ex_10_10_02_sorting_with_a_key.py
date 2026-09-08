"""Exercise 10.10.2 — Sorting with a key

Chapter 10 (Functions), section 10.10: Lambdas.

Problem
-------
This should sort the words from shortest to longest.

Bug type: Logical
-----------------
The key `-len(w)` sorts longest first; for shortest first the key should be `len(w)`.

The program below is the corrected version.
"""


words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'pear', 'banana']
