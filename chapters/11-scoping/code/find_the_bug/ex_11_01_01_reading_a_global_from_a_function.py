"""Exercise 11.1.1 — reading a global from a function

Chapter 11 (Scoping), section 11.1: Local and Global Scope.

Problem
-------
This program should print the speed limit twice: once from inside `report()` and once from the top level.

Bug type: Runtime
-----------------
The top-level `print` reads `speed_limit`, but the global is named `speed_limit_kmh`, so Python raises `NameError`. Use the correct global name.

The program below is the corrected version.
"""


speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit_kmh)
