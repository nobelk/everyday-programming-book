"""Problem 10 — Ladder against a wall (Pythagoras)

Domain: Mathematics. Chapter 5 (Data Structures), variables.

Problem
-------
A 5 m ladder leans against a wall with its base 3 m from the wall. Compute the height it reaches.

Expected output
---------------
Height reached: 4.0 m
"""


ladder_m = 5
base_m = 3
height_m = (ladder_m ** 2 - base_m ** 2) ** 0.5
print(f"Height reached: {height_m} m")
