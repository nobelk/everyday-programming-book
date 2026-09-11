"""Exercise 11.3.3 — Returning early

Chapter 11 (Functions), section 11.3: Returning a Result.

Problem
-------
This program should convert Celsius to Fahrenheit and print 212.0 for 100 degrees.

Bug type: Logical
-----------------
A bare `return` exits immediately and yields `None`; the formula on the next line never runs. Put the expression on the `return` line.

The program below is the corrected version.
"""


def c_to_f(celsius):
    return celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
