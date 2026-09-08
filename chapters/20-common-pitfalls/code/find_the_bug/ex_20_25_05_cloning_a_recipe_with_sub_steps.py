"""Exercise 20.25.5 — Cloning a recipe with sub-steps

Chapter 20 (Common Pitfalls), section 20.25: Shallow vs deep copy.

Problem
-------
This program should clone a recipe (with nested steps) so editing the clone is safe.

Bug type: Logical
-----------------
Slicing with `[:]` copies only the outer list; the nested step lists are shared, so appending through `clone` changes `recipe`. Use `copy.deepcopy`.

The program below is the corrected version.
"""


import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = copy.deepcopy(recipe)
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
