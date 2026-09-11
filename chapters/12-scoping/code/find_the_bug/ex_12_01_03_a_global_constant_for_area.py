"""Exercise 12.1.3 — a global constant for area

Chapter 12 (Scoping), section 12.1: Local and Global Scope.

Problem
-------
Using a global value of `pi`, this program should compute the area of a circle with radius 3 and print about 28.27.

Bug type: Runtime
-----------------
The global `pi` is visible inside the function, but `area` is created *inside* `circle_area`, so it does not exist at the top level and the final `print` raises `NameError`. Return the value and capture it in a variable.

The program below is the corrected version.
"""


pi = 3.14159

def circle_area():
    return pi * 3 * 3

area = circle_area()
print("Area:", area)   # Area: 28.27431
