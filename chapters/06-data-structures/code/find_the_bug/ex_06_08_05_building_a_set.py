"""Exercise 6.8.5 — Building a set

Chapter 6 (Data Structures), section 6.8: Sets.

Problem
-------
The program should start with an empty set, add one item, and print the set with that item.

Bug type: Runtime
-----------------
`{}` creates an empty dictionary, not a set, so `seen.add` raises an `AttributeError`. Use `set()` to create an empty set.

The program below is the corrected version.
"""


seen = set()
seen.add("apple")
print(seen)   # {'apple'}
