"""Exercise 9.3.2 — Weekend check

Chapter 9 (Control Flow), section 9.3: Logical Operators.

Problem
-------
This program should print `Relax` on Saturday or Sunday. For "Saturday" it should print `Relax`.

Bug type: Logical
-----------------
A day cannot equal both `Saturday` and `Sunday`, so the `and` condition is never true and nothing prints. The cases are alternatives, so use `or`.

The program below is the corrected version.
"""


day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Relax")
# expected: Relax
