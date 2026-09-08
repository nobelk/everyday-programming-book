"""Exercise 11.1.2 — a local name stays local

Chapter 11 (Scoping), section 11.1: Local and Global Scope.

Problem
-------
A scientist measures a temperature inside a helper function. The program should print the reading from inside the function only.

Bug type: Runtime
-----------------
`temperature_c` is local to `take_reading()`, so it does not exist at the top level; the final `print` raises `NameError`. Remove that line (a local name is not visible outside its function).

The program below is the corrected version.
"""


def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
