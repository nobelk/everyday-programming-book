"""Exercise 12.6.4 — a local inside a method

Chapter 12 (Scoping), section 12.6: Scope with Objects and Classes.

Problem
-------
This program computes a rectangle's area inside a method from stored sides and should print 12.

Bug type: Runtime
-----------------
`area()` uses bare `width`, which is not defined in the method's local scope, so Python raises `NameError`. Read the stored side through `self.width`.

The program below is the corrected version.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = self.width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
