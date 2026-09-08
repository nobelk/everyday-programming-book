"""Exercise 20.10.4 — Adding a fourth runner's time

Chapter 20 (Common Pitfalls), section 20.10: Modifying a list item that does not exist.

Problem
-------
This program should store a fourth lap time at the next position.

Bug type: Runtime
-----------------
`len(lap_times)` is `3`, which is one past the last valid index, so the assignment raises `IndexError`. Use `append`.

The program below is the corrected version.
"""


lap_times = [45, 47, 44]
lap_times.append(46)
print(lap_times)
