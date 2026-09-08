"""Exercise 20.26.5 — Noting one ingredient

Chapter 20 (Common Pitfalls), section 20.26: Mutable default arguments.

Problem
-------
Each call should produce a fresh list containing only the ingredient given.

Bug type: Logical
-----------------
The mutable default `items=[]` is reused on every call, so ingredients accumulate. Default to `None` and make a fresh list.

The program below is the corrected version.
"""


def note_ingredient(name, items=None):
    if items is None:
        items = []
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
