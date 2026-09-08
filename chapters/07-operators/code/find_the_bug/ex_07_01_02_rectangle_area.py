"""Exercise 7.1.2 — Rectangle area

Chapter 7 (Operators), section 7.1: Arithmetic Operators.

Problem
-------
This program should compute the area of a rectangle (length times width) and print `15`.

Bug type: Logical
-----------------
Area is length times width, but the program adds them, giving 8 instead of 15. Use `*` instead of `+`.

The program below is the corrected version.
"""


length = 5
width = 3
area = length * width
print(area)   # 15
