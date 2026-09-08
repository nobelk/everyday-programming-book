"""Exercise 20.3.1 — Assignment inside an `if`

Chapter 20 (Common Pitfalls), section 20.3: Confusing assignment with equality.

Problem
-------
This program should check whether a thermostat is set to 20 degrees.

Bug type: Syntax
----------------
`=` assigns and cannot appear as a condition; comparing requires `==`. Using `==` makes the test valid.

The program below is the corrected version.
"""


thermostat = 20
if thermostat == 20:
    print("Comfortable")
