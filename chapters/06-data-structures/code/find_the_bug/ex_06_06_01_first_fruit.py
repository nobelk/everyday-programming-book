"""Exercise 6.6.1 — First fruit

Chapter 6 (Data Structures), section 6.6: Lists.

Problem
-------
The program should print the first fruit in the list: "apple".

Bug type: Logical
-----------------
List indexing starts at 0, so `fruits[1]` is "banana". Use index `0` for the first fruit.

The program below is the corrected version.
"""


fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
