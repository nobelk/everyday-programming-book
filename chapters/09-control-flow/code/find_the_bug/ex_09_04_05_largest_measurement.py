"""Exercise 9.4.5 — Largest measurement

Chapter 9 (Control Flow), section 9.4: for Loops.

Problem
-------
This program should find the largest of several distances and print it, 45.

Bug type: Logical
-----------------
The comparison `<` keeps the smallest value, not the largest. To track the maximum, replace it when the current value is *greater*, using `>`.

The program below is the corrected version.
"""


distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance > largest:
        largest = distance

print(largest)
