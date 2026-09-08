"""Exercise 20.4.3 — Using a result before computing it

Chapter 20 (Common Pitfalls), section 20.4: Using a variable before it is created.

Problem
-------
This program should compute and print the area of a circle with radius 3.

Bug type: Runtime
-----------------
`area` is referenced before it is assigned, raising `NameError`. Compute `area` first, then print it.

The program below is the corrected version.
"""


radius = 3
area = 3.14159 * radius * radius
print(area)
