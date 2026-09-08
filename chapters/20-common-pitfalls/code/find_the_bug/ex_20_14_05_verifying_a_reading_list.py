"""Exercise 20.14.5 — Verifying a reading list

Chapter 20 (Common Pitfalls), section 20.14: Using is instead of == for value comparison.

Problem
-------
The program checks whether the books read so far match the planned reading list.

Bug type: Logical
-----------------
Two lists with identical contents are still different objects, so `is` is always `False` here. Use `==` to compare contents.

The program below is the corrected version.
"""


planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far == planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
