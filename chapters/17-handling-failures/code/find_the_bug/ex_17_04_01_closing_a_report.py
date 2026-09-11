"""Exercise 17.4.1 — Closing a report

Chapter 17 (Handling Failures), section 17.4: Using finally.

Problem
-------
This program divides two numbers and should always print a closing line, whether or not the division fails.

Bug type: Logical
-----------------
The closing line sits inside the `except` block, so it prints only when the division fails; on the normal path it never runs. Move the always-run line into a `finally` block.

The program below is the corrected version.
"""


try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done with the calculation.")
