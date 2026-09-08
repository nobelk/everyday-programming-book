"""Exercise 20.12.4 — Listing class names

Chapter 20 (Common Pitfalls), section 20.12: Using parentheses instead of brackets for lists.

Problem
-------
This program should build a list of subjects and add one more.

Bug type: Runtime
-----------------
`subjects` is a tuple, so `append` raises `AttributeError`. Use square brackets for a list.

The program below is the corrected version.
"""


subjects = ["Math", "Science"]
subjects.append("History")
print(subjects)
