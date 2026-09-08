"""Exercise 11.3.5 — assignment creates a fresh local

Chapter 11 (Scoping), section 11.3: Assignment Inside a Function Usually Creates a Local Variable.

Problem
-------
This program should leave the global `balance` unchanged after `spend()` runs, since the assignment inside makes a new local. The program should print 50.

Bug type: Runtime
-----------------
The final `print` reads `balanace`, a misspelling, so Python raises `NameError`. Use the correct global name `balance`.

The program below is the corrected version.
"""


balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balance)
