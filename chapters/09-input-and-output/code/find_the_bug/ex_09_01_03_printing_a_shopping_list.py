"""Exercise 9.1.3 — Printing a shopping list

Chapter 9 (Input and Output), section 9.1: Reading Input and Printing Output.

Problem
-------
This program should print three fruits on one line, separated by commas, like `apple, banana, cherry`.

Bug type: Logical
-----------------
The `sep` argument controls what goes between the printed items; a single space produces `apple banana cherry`, not the comma-separated list that was wanted. Set `sep=", "`.

The program below is the corrected version.
"""


fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=", ")
