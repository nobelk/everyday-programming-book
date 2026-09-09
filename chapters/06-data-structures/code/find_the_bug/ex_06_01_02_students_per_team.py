"""Exercise 6.1.2 — Students per team

Chapter 6 (Data Structures), section 6.1: int.

Problem
-------
Thirty students are split evenly into 5 teams. The program should print the whole number 6.

Bug type: Logical
-----------------
The `/` operator always produces a float (6.0), but a whole number of students per team is wanted. Use integer division `//` to get the int 6.

The program below is the corrected version.
"""


students = 30
teams = 5

per_team = students // teams
print(per_team)   # 6
