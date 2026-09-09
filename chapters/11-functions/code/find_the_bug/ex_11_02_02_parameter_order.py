"""Exercise 11.2.2 — Parameter order

Chapter 11 (Functions), section 11.2: Parameters.

Problem
-------
This program should print `"Maya is 15 years old"`.

Bug type: Logical
-----------------
The arguments are passed in the wrong order, so `name` becomes 15 and `age` becomes "Maya". Pass the name first, then the age.

The program below is the corrected version.
"""


def describe(name, age):
    print(name, "is", age, "years old")

describe("Maya", 15)
