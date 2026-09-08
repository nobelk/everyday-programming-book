"""Exercise 11.3.2 — read before assign

Chapter 11 (Scoping), section 11.3: Assignment Inside a Function Usually Creates a Local Variable.

Problem
-------
This program should print the current step number, then set a new local step. Because `step` is assigned later in the function, the read at the top should fail unless it is read from somewhere valid.

Bug type: Runtime
-----------------
Assigning `step` later in the function makes `step` local throughout, so the `print` reads a local that has no value yet — `UnboundLocalError`. Read the value through a parameter (or remove the local assignment) so the read is valid.

The program below is the corrected version.
"""


step = 1

def advance(step):
    print("Current:", step)
    step = step + 1

advance(step)
