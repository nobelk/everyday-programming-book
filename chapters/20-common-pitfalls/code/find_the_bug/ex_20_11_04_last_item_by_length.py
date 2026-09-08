"""Exercise 20.11.4 — Last item by length

Chapter 20 (Common Pitfalls), section 20.11: Going past the end of a list.

Problem
-------
This program should print the last student's name in the list.

Bug type: Runtime
-----------------
`len(students)` is `3`, one past the last index, so `students[3]` raises `IndexError`. The last index is `len(students) - 1`.

The program below is the corrected version.
"""


students = ["Mia", "Noah", "Liam"]
print(students[len(students) - 1])
