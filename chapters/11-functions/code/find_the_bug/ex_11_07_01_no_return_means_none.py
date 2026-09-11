"""Exercise 11.7.1 — No return means None

Chapter 11 (Functions), section 11.7: Implicit None Return.

Problem
-------
This program prints a message, and the returned value should be `None`.

Bug type: Logical
-----------------
The function explicitly returns "done", so `result` is not `None`. Remove the `return` so the function returns `None` implicitly.

The program below is the corrected version.
"""


def announce():
    print("The meeting starts now.")

result = announce()
print(result)  # None
