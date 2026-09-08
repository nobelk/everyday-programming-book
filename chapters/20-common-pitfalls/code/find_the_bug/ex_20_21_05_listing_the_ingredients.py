"""Exercise 20.21.5 — Listing the ingredients

Chapter 20 (Common Pitfalls), section 20.21: Using range(len(...)) when iterating over items directly is simpler.

Problem
-------
This program should print each ingredient.

Bug type: Logical
-----------------
`item` becomes the index 0, 1, 2 instead of the ingredient name. Iterate over the list itself.

The program below is the corrected version.
"""


ingredients = ["flour", "sugar", "butter"]
for item in ingredients:
    print(item)
