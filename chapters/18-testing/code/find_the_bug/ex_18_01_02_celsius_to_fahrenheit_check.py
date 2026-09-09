"""Exercise 18.1.2 — Celsius to Fahrenheit check

Chapter 18 (Testing), section 18.1: Why Test Python Functions.

Problem
-------
The function converts Celsius to Fahrenheit, and the assert should confirm that 100 °C is 212 °F.

Bug type: Logical
-----------------
The function is correct, but the expected value in the test is wrong: 100 °C is 212 °F, not 211. The fix corrects the expected value.

The program below is the corrected version.
"""


def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 212
print("passed")
