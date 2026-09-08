"""Exercise 16.4.4 — Final tally

Chapter 16 (Handling Failures), section 16.4: Using finally.

Problem
-------
Whatever happens above, this program must always print `Final tally complete.` at the end. With `rounds` set to 0 it currently does not.

Bug type: Logical
-----------------
The tally line sits inside the `try` right after the division, so a `ZeroDivisionError` skips it. A line that must always run belongs in a `finally` block, which executes whether or not an exception occurs.

The program below is the corrected version.
"""


points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
except ZeroDivisionError:
    print("No rounds played.")
finally:
    print("Final tally complete.")
