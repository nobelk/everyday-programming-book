"""Exercise 5.1.5 — Apples per box

Chapter 5 (Data Structures), section 5.1: int.

Problem
-------
You have 17 apples and want 5 per box. The program should print how many full boxes (3) you can fill.

Bug type: Logical
-----------------
`%` gives the remainder (2 leftover apples), not the number of full boxes. Use integer division `//` to get 3.

The program below is the corrected version.
"""


apples = 17
per_box = 5

full_boxes = apples // per_box
print(full_boxes)   # 3
