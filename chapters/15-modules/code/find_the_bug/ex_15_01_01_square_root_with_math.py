"""Exercise 15.1.1 — Square root with math

Chapter 15 (Modules), section 15.1: Python Standard Library.

Problem
-------
This program should print the length of the hypotenuse of a right triangle with legs 3 and 4 (it should be 5.0).

Bug type: Runtime
-----------------
The Pythagorean theorem adds the squares of the legs, but this code subtracts them, so `math.sqrt` receives 9-16=-7 and raises a `ValueError` (math domain error). Change the `-` to `+`.

The program below is the corrected version.
"""


import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
print(hypotenuse)   # 5.0
