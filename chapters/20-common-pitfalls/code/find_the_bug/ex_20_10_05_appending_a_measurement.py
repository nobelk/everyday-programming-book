"""Exercise 20.10.5 — Appending a measurement

Chapter 20 (Common Pitfalls), section 20.10: Modifying a list item that does not exist.

Problem
-------
This program should add one more pH reading to the list.

Bug type: Runtime
-----------------
Assigning to `ph_values[3]` on a three-item list raises `IndexError`. Use `append` to add a new reading.

The program below is the corrected version.
"""


ph_values = [7.0, 6.8, 7.2]
ph_values.append(6.9)
print(ph_values)
