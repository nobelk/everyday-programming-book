"""Exercise 6.8.1 — Unique colors

Chapter 6 (Data Structures), section 6.8: Sets.

Problem
-------
A set removes duplicates. The program should print how many unique colors there are: 3.

Bug type: Logical
-----------------
Square brackets create a list, which keeps the duplicate "red", so `len` is 4. Use curly braces to make a set, which drops duplicates and gives 3.

The program below is the corrected version.
"""


colors = {"red", "blue", "red", "green"}
print(len(colors))   # 3
