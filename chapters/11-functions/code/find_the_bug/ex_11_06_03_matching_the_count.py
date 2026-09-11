"""Exercise 11.6.3 — Matching the count

Chapter 11 (Functions), section 11.6: Multiple Return Values.

Problem
-------
This program should unpack a name and an age into two variables.

Bug type: Runtime
-----------------
The function returns three values but only two names receive them, raising a `ValueError`. Return just the two values you unpack.

The program below is the corrected version.
"""


def person():
    return "Luis", 14

name, age = person()
print(name, age)  # Luis 14
