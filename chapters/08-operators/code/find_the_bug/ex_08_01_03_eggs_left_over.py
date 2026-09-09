"""Exercise 8.1.3 — Eggs left over

Chapter 8 (Operators), section 8.1: Arithmetic Operators.

Problem
-------
A baker has 17 eggs and packs them into cartons of 6. This program should print how many eggs are left over after filling whole cartons, which is `5`.

Bug type: Logical
-----------------
Floor division `//` gives the number of full cartons (2), not the leftover eggs. The remainder operator `%` gives what is left over.

The program below is the corrected version.
"""


total_eggs = 17
carton_size = 6
leftover = total_eggs % carton_size
print(leftover)   # 5
