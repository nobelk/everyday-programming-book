"""Exercise 19.3.5 — Fahrenheit to Celsius

Chapter 19 (Bugs), section 19.3: Logical Bugs.

Problem
-------
This program should convert 212 degrees Fahrenheit to Celsius.

Bug type: Logical
-----------------
The conversion factor is inverted: Fahrenheit to Celsius multiplies by `5 / 9`, not `9 / 5`. Swapping the fraction gives the right temperature.

The program below is the corrected version.
"""


def f_to_c(f):
    return (f - 32) * 5 / 9

print(f_to_c(212))   # 100.0
