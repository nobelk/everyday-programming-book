"""Exercise 20.6.4 — Combining a count with text

Chapter 20 (Common Pitfalls), section 20.6: Mixing strings and numbers without converting types.

Problem
-------
This program should report how many books are on a shelf.

Bug type: Runtime
-----------------
`books + " books..."` adds an int to a string, raising `TypeError`. Convert `books` to a string first.

The program below is the corrected version.
"""


books = 12
print(str(books) + " books on the shelf")
