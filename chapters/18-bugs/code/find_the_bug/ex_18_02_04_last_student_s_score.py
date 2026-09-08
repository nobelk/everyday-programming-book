"""Exercise 18.2.4 — Last student's score

Chapter 18 (Bugs), section 18.2: Runtime Bugs.

Problem
-------
This program should print the score of the last student in the list.

Bug type: Runtime
-----------------
`len(scores)` is 4, but valid indices run 0 to 3, so `scores[4]` raises `IndexError`. The last element is at index `len(scores) - 1` (or simply `-1`).

The program below is the corrected version.
"""


scores = [88, 91, 79, 95]
last_index = len(scores) - 1
print(scores[last_index])   # 95
