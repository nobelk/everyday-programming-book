"""Exercise 10.7.5 — Expecting a value

Chapter 10 (Functions), section 10.7: Implicit None Return.

Problem
-------
This should check whether the helper returned a usable number and print it; it should print 42.

Bug type: Logical
-----------------
The function assigns `chosen` but never returns it, so `number` is `None`. Return `chosen`.

The program below is the corrected version.
"""


def lucky_number():
    chosen = 42
    return chosen

number = lucky_number()
print(number)  # 42
