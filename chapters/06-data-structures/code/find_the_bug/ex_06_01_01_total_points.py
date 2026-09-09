"""Exercise 6.1.1 — Total points

Chapter 6 (Data Structures), section 6.1: int.

Problem
-------
A quiz has 3 sections worth 20, 30, and 25 points. The program should print the total, 75.

Bug type: Logical
-----------------
The third section was subtracted instead of added, giving 25 instead of 75. Change the `-` to `+` so all three sections are summed.

The program below is the corrected version.
"""


section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 + section3
print(total)   # 75
