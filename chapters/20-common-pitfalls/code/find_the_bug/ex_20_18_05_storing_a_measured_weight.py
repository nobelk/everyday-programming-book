"""Exercise 20.18.5 — Storing a measured weight

Chapter 20 (Common Pitfalls), section 20.18: Forgetting to close a file.

Problem
-------
This program should save a measured weight in kilograms to a file safely.

Bug type: Logical
-----------------
`weight_file` is never closed, risking unflushed data. Use a `with` block to close it safely.

The program below is the corrected version.
"""


weight_kg = 72.4
with open("weight.txt", "w") as weight_file:
    weight_file.write(f"{weight_kg}\n")
