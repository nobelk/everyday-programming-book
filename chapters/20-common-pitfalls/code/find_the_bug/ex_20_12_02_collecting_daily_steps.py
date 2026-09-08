"""Exercise 20.12.2 — Collecting daily steps

Chapter 20 (Common Pitfalls), section 20.12: Using parentheses instead of brackets for lists.

Problem
-------
This program should create a list of step counts and add today's count.

Bug type: Runtime
-----------------
`steps` is a tuple, so `append` raises `AttributeError`. Use brackets to create a list.

The program below is the corrected version.
"""


steps = [8000, 9500, 7000]
steps.append(10000)
print(steps)
