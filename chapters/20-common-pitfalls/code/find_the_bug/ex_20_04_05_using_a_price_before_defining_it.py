"""Exercise 20.4.5 — Using a price before defining it

Chapter 20 (Common Pitfalls), section 20.4: Using a variable before it is created.

Problem
-------
This program should print the total cost of 3 notebooks.

Bug type: Runtime
-----------------
`price` is multiplied before it is assigned, raising `NameError`. Define `price` before the calculation.

The program below is the corrected version.
"""


quantity = 3
price = 2
print(quantity * price)
