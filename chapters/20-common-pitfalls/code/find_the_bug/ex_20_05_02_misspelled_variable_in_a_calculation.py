"""Exercise 20.5.2 — Misspelled variable in a calculation

Chapter 20 (Common Pitfalls), section 20.5: Misspelling variable names.

Problem
-------
This program should print the distance traveled at 60 km/h for 2 hours.

Bug type: Runtime
-----------------
`sped` was never defined; only `speed` exists, so the line raises `NameError`. Fix the spelling.

The program below is the corrected version.
"""


speed = 60
hours = 2
distance = speed * hours
print(distance)  # 120
