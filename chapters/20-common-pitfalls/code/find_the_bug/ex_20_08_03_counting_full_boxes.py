"""Exercise 20.8.3 — Counting full boxes

Chapter 20 (Common Pitfalls), section 20.8: Using / when you want a whole-number result.

Problem
-------
This program should print how many full boxes of 6 eggs come from 40 eggs.

Bug type: Logical
-----------------
`40 / 6` is `6.66...`, but you can only fill whole boxes. `//` gives the correct `6`.

The program below is the corrected version.
"""


eggs = 40
per_box = 6
full_boxes = eggs // per_box
print(full_boxes)  # 6
