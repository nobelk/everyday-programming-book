"""Exercise 10.11.2 — A safe default

Chapter 10 (Functions), section 10.11: Mutable Default Argument Trap.

Problem
-------
This should add a reading to a fresh list each call, printing a one-item list each time.

Bug type: Logical
-----------------
The guard checks for `None`, but the default is a shared list, not `None`, so the guard never runs and the list grows. Make the default `None`.

The program below is the corrected version.
"""


def add_reading(value, readings=None):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
