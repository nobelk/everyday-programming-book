"""Exercise 15.1.5 — Rounding a price up

Chapter 15 (Modules), section 15.1: Python Standard Library.

Problem
-------
This program should round a price of $4.20 up to the next whole dollar using a from-import.

Bug type: Runtime
-----------------
With `from math import ceil`, the name brought into scope is `ceil`, not `math`, so `math.ceil(price)` raises `NameError`. Call `ceil(price)` directly.

The program below is the corrected version.
"""


from math import ceil

price = 4.20
rounded_up = ceil(price)
print(rounded_up)   # 5
