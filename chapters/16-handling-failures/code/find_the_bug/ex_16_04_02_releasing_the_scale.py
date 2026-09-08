"""Exercise 16.4.2 — Releasing the scale

Chapter 16 (Handling Failures), section 16.4: Using finally.

Problem
-------
This program weighs an item and must always print that the scale is released, even when input is bad.

Bug type: Logical
-----------------
``Scale released'' must always print, but it is in the `else` block, which runs only when no exception occurs; on bad input it is skipped. Use `finally` so it runs whether or not an error happened.

The program below is the corrected version.
"""


try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
finally:
    print("Scale released.")
