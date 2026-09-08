"""Exercise 10.10.3 — Lambda with map

Chapter 10 (Functions), section 10.10: Lambdas.

Problem
-------
This should double every number in the list, giving `[2, 4, 6]`.

Bug type: Logical
-----------------
The lambda adds 2 instead of doubling, so `1` becomes 3, not 2. Multiply by 2 to double each number.

The program below is the corrected version.
"""


numbers = [1, 2, 3]
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6]
