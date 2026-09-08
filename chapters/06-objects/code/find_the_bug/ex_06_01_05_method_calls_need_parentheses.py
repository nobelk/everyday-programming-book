"""Exercise 6.1.5 — Method calls need parentheses

Chapter 6 (Objects), section 6.1: Classes.

Problem
-------
This class stores a circle's radius and returns its circumference.

Bug type: Logical
-----------------
`wheel.circumference` refers to the method object instead of calling it, so the printout is a function reference, not the number. Adding parentheses — `wheel.circumference()` — calls the method and prints `62.8318`.

The program below is the corrected version.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference())   # 62.8318
