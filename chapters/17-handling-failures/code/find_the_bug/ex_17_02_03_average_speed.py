"""Exercise 17.2.3 — Average speed

Chapter 17 (Handling Failures), section 17.2: Handling Different Kinds of Errors.

Problem
-------
This program reads a distance and a time, divides to get average speed, and should report a typed-in non-number and a zero time with separate messages.

Bug type: Logical
-----------------
The broad `except Exception` is listed first, and because `ZeroDivisionError` is a subclass of `Exception`, the first handler swallows a zero-time error and prints the misleading ``Distance was not a number'' message; the specific `ZeroDivisionError` handler is unreachable. Put the specific handler before the general one.

The program below is the corrected version.
"""


distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except ZeroDivisionError:
    print("Time cannot be zero.")
except Exception:
    print("Distance was not a number.")
