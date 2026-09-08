"""Exercise 20.24.4 — Celsius to Fahrenheit

Chapter 20 (Common Pitfalls), section 20.24: Writing long code without testing small pieces.

Problem
-------
The program should convert 100 degrees Celsius to Fahrenheit and print 212.0.

Bug type: Logical
-----------------
The formula adds 32, but the code subtracts it. Change `- 32` to `+ 32`.

The program below is the corrected version.
"""


def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
