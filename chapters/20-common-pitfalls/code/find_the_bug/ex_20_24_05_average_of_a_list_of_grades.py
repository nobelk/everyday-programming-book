"""Exercise 20.24.5 — Average of a list of grades

Chapter 20 (Common Pitfalls), section 20.24: Writing long code without testing small pieces.

Problem
-------
This program should print the average of four grades and print 85.0.

Bug type: Logical
-----------------
The stray `- 1` skews the average. Testing the bare `sum / len` step alone would expose it; remove the `- 1`.

The program below is the corrected version.
"""


def average(grades):
    return sum(grades) / len(grades)

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
