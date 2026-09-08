"""Exercise 20.25.4 — Snapshotting weekly readings

Chapter 20 (Common Pitfalls), section 20.25: Shallow vs deep copy.

Problem
-------
The program should take a snapshot of nested sensor readings that stays fixed.

Bug type: Logical
-----------------
`readings.copy()` is shallow, so the nested lists remain shared and editing `snapshot` also edits `readings`. Use `copy.deepcopy`.

The program below is the corrected version.
"""


import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = copy.deepcopy(readings)
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
