"""Exercise 16.2.5 — Percent off

Chapter 16 (Handling Failures), section 16.2: Handling Different Kinds of Errors.

Problem
-------
This program reads a typed divisor, builds a fraction from it, and should report a non-number and a zero divisor with separate messages.

Bug type: Logical
-----------------
The broad `except Exception` comes first, and since `ZeroDivisionError` is a subclass of `Exception`, a zero divisor is caught by the first handler and reported as ``not a valid number''; the specific `ZeroDivisionError` handler can never run. List the specific handler before the general one.

The program below is the corrected version.
"""


price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except ZeroDivisionError:
    print("The divisor cannot be zero.")
except Exception:
    print("That was not a valid number.")
