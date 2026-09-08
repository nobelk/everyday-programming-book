"""Exercise 5.6.4 — Changing a value

Chapter 5 (Data Structures), section 5.6: Lists.

Problem
-------
The program should change the second price to 5.0 and print the list.

Bug type: Syntax
----------------
Item assignment uses square brackets, not parentheses; `prices(1) = 5.0` is not valid Python. Use `prices[1] = 5.0`.

The program below is the corrected version.
"""


prices = [2.0, 3.0, 4.0]
prices[1] = 5.0
print(prices)   # [2.0, 5.0, 4.0]
