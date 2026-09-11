"""Exercise 15.2.2 — Calling with the module prefix

Chapter 15 (Modules), section 15.2: Writing Your Own Module.

Problem
-------
This two-file program should print the area of a 4-by-6 rectangle (24).

Bug type: Runtime
-----------------
With `import geometry`, the function must be called through its module as `geometry.rectangle_area(...)`; the bare name `rectangle_area` is undefined and raises `NameError`. Add the module prefix.

The program below is the corrected version.
"""


# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(geometry.rectangle_area(4, 6))   # 24
