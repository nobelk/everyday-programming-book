"""Exercise 12.1.4 — the helper's result must come back out

Chapter 12 (Scoping), section 12.1: Local and Global Scope.

Problem
-------
This program should compute the perimeter of a rectangle and print it at the top level.

Bug type: Logical
-----------------
`edges` is a local variable; without a `return`, the function hands back `None`, so `result` is `None`. Return the value so it leaves the local scope.

The program below is the corrected version.
"""


def perimeter(length, width):
    edges = 2 * (length + width)
    return edges

result = perimeter(5, 3)
print("Perimeter:", result)
