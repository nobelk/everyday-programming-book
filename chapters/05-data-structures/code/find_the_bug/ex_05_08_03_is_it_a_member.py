"""Exercise 5.8.3 — Is it a member?

Chapter 5 (Data Structures), section 5.8: Sets.

Problem
-------
The program should check whether "blue" is in the set and print `True`.

Bug type: Logical
-----------------
The program tests "yellow", which is not in the set, so it prints False. Test for "blue" to get True.

The program below is the corrected version.
"""


colors = {"red", "blue", "green"}
print("blue" in colors)   # True
