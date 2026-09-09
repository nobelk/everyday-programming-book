"""Exercise 17.1.1 — Reading an age

Chapter 17 (Handling Failures), section 17.1: Handling Bad User Input.

Problem
-------
This program should keep asking until the user types a whole number for their age, then print it.

Bug type: Runtime
-----------------
The `int(raw)` call happens *outside* the `try`, so a non-numeric entry raises `ValueError` before the `except` can catch it and the program crashes. Move the conversion inside the `try` so the failing line is actually protected.

The program below is the corrected version.
"""


while True:
    raw = input("Enter your age in years: ")
    try:
        age = int(raw)
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
