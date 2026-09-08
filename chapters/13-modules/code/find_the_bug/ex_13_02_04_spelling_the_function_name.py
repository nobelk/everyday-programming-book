"""Exercise 13.2.4 — Spelling the function name

Chapter 13 (Modules), section 13.2: Writing Your Own Module.

Problem
-------
This two-file program should print the perimeter of a square with side 5 (20).

Bug type: Runtime
-----------------
The call misspells the function as `square_permieter`; the module `shapes` has no such attribute, so it raises `AttributeError`. Spell it `square_perimeter` to match the definition.

The program below is the corrected version.
"""


# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_perimeter(5))   # 20
