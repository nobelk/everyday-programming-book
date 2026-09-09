"""Exercise 17.3.2 — Area of a rectangle

Chapter 17 (Handling Failures), section 17.3: Using else.

Problem
-------
This program reads two side lengths and, if both parse, prints the area in the `else` block.

Bug type: Logical
-----------------
The `else` block computes `area` but never prints it, so the program produces no visible result on success. Print the area in the `else` block.

The program below is the corrected version.
"""


try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
    print("Area:", area)
