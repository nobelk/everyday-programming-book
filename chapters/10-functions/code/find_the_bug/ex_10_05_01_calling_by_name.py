"""Exercise 10.5.1 — Calling by name

Chapter 10 (Functions), section 10.5: Keyword Arguments.

Problem
-------
This program should print `"Lina is 12 years old"` using keyword arguments.

Bug type: Runtime
-----------------
`grade=7` is an unexpected keyword argument the function does not accept, raising a `TypeError`. Pass only `name` and `age`.

The program below is the corrected version.
"""


def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12)
