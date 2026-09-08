"""Exercise 20.4.4 — Reading a counter that is set later

Chapter 20 (Common Pitfalls), section 20.4: Using a variable before it is created.

Problem
-------
This program should print how many laps a runner completed.

Bug type: Runtime
-----------------
`laps` is used before it is created, so the `print` raises `NameError`. Assign `laps` before printing it.

The program below is the corrected version.
"""


laps = 4
print("Laps:", laps)
