"""Exercise 16.2.2 — Adding a measurement

Chapter 16 (Handling Failures), section 16.2: Handling Different Kinds of Errors.

Problem
-------
This program adds a typed measurement to a running total and warns if the text is not a number.

Bug type: Runtime
-----------------
Adding an integer to a string raises `TypeError`, but the code catches `ZeroDivisionError`, so the error is not caught and the program crashes. Catch `TypeError`.

The program below is the corrected version.
"""


total = 100
new_value = "twelve"
try:
    total = total + new_value
except TypeError:
    print("That measurement was not a number.")
print("Total is", total)
