"""Exercise 6.2.3 — Rounding a price

Chapter 6 (Data Structures), section 6.2: float.

Problem
-------
A price of 3.14159 dollars should be rounded to 2 decimal places, printing 3.14.

Bug type: Logical
-----------------
`round(price)` with no second argument rounds to a whole number (3). Pass `2` to round to two decimal places.

The program below is the corrected version.
"""


price = 3.14159
rounded = round(price, 2)
print(rounded)   # 3.14
