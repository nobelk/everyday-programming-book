"""Exercise 20.8.1 — Splitting students into teams

Chapter 20 (Common Pitfalls), section 20.8: Using / when you want a whole-number result.

Problem
-------
This program should print how many full teams of 4 can be made from 30 students.

Bug type: Logical
-----------------
`/` gives `7.5`, but full teams need integer division. Use `//` to get `7`.

The program below is the corrected version.
"""


students = 30
team_size = 4
print(students // team_size)  # 7
