"""Exercise 11.3.1 — assigning makes it local

Chapter 11 (Scoping), section 11.3: Assignment Inside a Function Usually Creates a Local Variable.

Problem
-------
This program should start with a global `total` of 0 and print it unchanged after `add()` runs, because the assignment inside should create a separate local.

Bug type: Runtime
-----------------
Because `total` is assigned inside `add()`, Python treats it as local everywhere in the function; reading `total` on the right-hand side before it has a local value raises `UnboundLocalError`. Start the local from a literal instead of the global.

The program below is the corrected version.
"""


total = 0

def add():
    total = 10
    print("Inside:", total)

add()
print("Outside:", total)
