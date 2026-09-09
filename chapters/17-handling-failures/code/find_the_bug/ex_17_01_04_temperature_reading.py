"""Exercise 17.1.4 — Temperature reading

Chapter 17 (Handling Failures), section 17.1: Handling Bad User Input.

Problem
-------
This program reads a Celsius temperature and converts it to Fahrenheit, handling bad input.

Bug type: Syntax
----------------
The `except ValueError` line is missing its colon, so the file will not parse. Add the colon.

The program below is the corrected version.
"""


try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError:
    print("That was not a valid number.")
