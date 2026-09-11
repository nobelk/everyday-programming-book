"""Exercise 8.5.2 — Odd number not in list

Chapter 8 (Operators), section 8.5: Other Operators.

Problem
-------
This program should check that 7 is not among the listed even numbers and print `True`.

Bug type: Syntax
----------------
The membership operator is the two-word phrase `not in`, written in that order; `in not` will not parse. Use `not in` so a value absent from the list yields `True`.

The program below is the corrected version.
"""


even_numbers = [2, 4, 6, 8]
number = 7
result = number not in even_numbers
print(result)   # True
