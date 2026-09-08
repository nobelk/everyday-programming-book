"""Exercise 20.4.2 — Using a sum before it exists

Chapter 20 (Common Pitfalls), section 20.4: Using a variable before it is created.

Problem
-------
This program should add the first two test marks together.

Bug type: Runtime
-----------------
`total` is printed before it is computed, causing `NameError`. Move the assignment above the `print`.

The program below is the corrected version.
"""


first = 70
second = 85
total = first + second
print(total)
