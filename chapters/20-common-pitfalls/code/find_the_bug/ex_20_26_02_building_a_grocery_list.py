"""Exercise 20.26.2 — Building a grocery list

Chapter 20 (Common Pitfalls), section 20.26: Mutable default arguments.

Problem
-------
Each call should begin with a fresh, empty cart and add one item.

Bug type: Logical
-----------------
The mutable default `cart=[]` is shared between calls, so items pile up. Use `None` and create a new list inside the function.

The program below is the corrected version.
"""


def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
