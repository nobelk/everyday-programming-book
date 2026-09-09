"""Exercise 11.6.5 — Returning both values

Chapter 11 (Functions), section 11.6: Multiple Return Values.

Problem
-------
This program should return and print both the sum and the product of 4 and 5.

Bug type: Runtime
-----------------
The first `return` exits the function, so it returns a single integer and tuple unpacking raises a `TypeError`. Return both values in one tuple.

The program below is the corrected version.
"""


def sum_and_product(a, b):
    return a + b, a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
