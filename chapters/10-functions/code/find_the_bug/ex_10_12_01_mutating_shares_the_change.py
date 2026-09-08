"""Exercise 10.12.1 — Mutating shares the change

Chapter 10 (Functions), section 10.12: Pass by Reference vs Pass by Sharing.

Problem
-------
Appending inside the function should change the caller's list too.

Bug type: Logical
-----------------
`numbers = numbers + [1]` builds a new list and rebinds the local name, leaving the caller's list unchanged. Use `append`, which mutates the shared list.

The program below is the corrected version.
"""


def add_one(numbers):
    numbers.append(1)

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
