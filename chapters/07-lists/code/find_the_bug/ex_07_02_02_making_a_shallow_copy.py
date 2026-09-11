"""Exercise 7.2.2 — Making a shallow copy

Chapter 7 (Lists), section 7.2: Copying a List.

Problem
-------
This should make an independent copy of a flat list of prices.

Bug type: Runtime
-----------------
`prices.copy` refers to the method without calling it, so `copy_of_prices` becomes a method object and `.append` raises an `AttributeError`. Calling `prices.copy()` makes the independent copy.

The program below is the corrected version.
"""


prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy()
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
