"""Exercise 20.14.4 — Comparing two shopping lists

Chapter 20 (Common Pitfalls), section 20.14: Using is instead of == for value comparison.

Problem
-------
The program should report that two grocery lists hold the same items.

Bug type: Logical
-----------------
Two lists with identical contents are still distinct objects, so `is` is always `False` here. Use `==` to compare contents.

The program below is the corrected version.
"""


cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one == cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
