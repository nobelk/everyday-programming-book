"""Exercise 6.5.4 — Deep copy for nested lists

Chapter 6 (Objects), section 6.5: Copying a List.

Problem
-------
The grid holds rows of numbers. We want an independent copy whose rows can change without touching the original.

Bug type: Logical
-----------------
`copy.copy` makes a shallow copy, so the inner lists are still shared and appending to `independent[0]` also changes `grid`. `copy.deepcopy` copies the nested lists recursively, keeping the original intact.

The program below is the corrected version.
"""


import copy

grid = [[1, 2], [3, 4]]
independent = copy.deepcopy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
