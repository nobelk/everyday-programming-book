"""Exercise 20.3.5 — Equality used for assignment

Chapter 20 (Common Pitfalls), section 20.3: Confusing assignment with equality.

Problem
-------
This program should record a measured speed and print it in km/h.

Bug type: Runtime
-----------------
`speed == 60` does not create `speed`; the later `print` raises `NameError`. A single `=` assigns the value.

The program below is the corrected version.
"""


speed = 60
print("Speed:", speed)  # Speed: 60
