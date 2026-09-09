"""Exercise 8.1.5 — Total cost with tax

Chapter 8 (Operators), section 8.1: Arithmetic Operators.

Problem
-------
An item costs $20 and tax is 10%. This program should print the total cost including tax, which is `22.0`.

Bug type: Syntax
----------------
The call to `print` is missing its closing parenthesis, so the program will not parse. Add the `)`.

The program below is the corrected version.
"""


price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total)   # 22.0
