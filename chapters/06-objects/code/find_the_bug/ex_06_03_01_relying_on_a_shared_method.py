"""Exercise 6.3.1 — Relying on a shared method

Chapter 6 (Objects), section 6.3: Duck Typing.

Problem
-------
Different shapes each provide an `area()` method, so one function can total them all.

Bug type: Runtime
-----------------
`shape.area` refers to the method without calling it, so adding it to a number raises a `TypeError`. Calling `shape.area()` invokes each shape's method and totals the areas to `25.0`.

The program below is the corrected version.
"""


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total = total + shape.area()
    return total

print(total_area([Square(4), Triangle(6, 3)]))   # 25.0
