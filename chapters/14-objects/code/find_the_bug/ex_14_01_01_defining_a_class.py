"""Exercise 14.1.1 — Defining a class

Chapter 14 (Objects), section 14.1: Classes.

Problem
-------
This class should store a rectangle's width and height and report its area.

Bug type: Syntax
----------------
The `def __init__(self, width, height)` header is missing the colon at the end, so Python cannot parse the method definition. Adding the colon fixes it.

The program below is the corrected version.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
