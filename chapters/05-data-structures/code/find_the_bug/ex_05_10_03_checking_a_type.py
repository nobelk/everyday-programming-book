"""Exercise 5.10.3 — Checking a type

Chapter 5 (Data Structures), section 5.10: Variables and Types.

Problem
-------
The program should report the type of a price as `float`.

Bug type: Logical
-----------------
The price is a float, but the check compares against `int`, so it reports False. Compare against `float`.

The program below is the corrected version.
"""


price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == float)   # True
