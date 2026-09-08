"""Exercise 20.10.1 — Setting a fourth temperature

Chapter 20 (Common Pitfalls), section 20.10: Modifying a list item that does not exist.

Problem
-------
This program should replace a placeholder list with three real readings, then store a fourth.

Bug type: Runtime
-----------------
`readings` has indexes 0–2, so assigning to `readings[3]` raises `IndexError`; assignment cannot grow a list. Use `append` to add a fourth value.

The program below is the corrected version.
"""


readings = [20, 22, 21]
readings.append(23)
print(readings)
