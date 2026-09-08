"""Exercise 20.11.1 — Reading the last color

Chapter 20 (Common Pitfalls), section 20.11: Going past the end of a list.

Problem
-------
This program should print the last color in the list.

Bug type: Runtime
-----------------
Indexes run 0–2, so `colors[3]` is out of range and raises `IndexError`. The last item is at index `2`.

The program below is the corrected version.
"""


colors = ["red", "green", "blue"]
print(colors[2])
