"""Exercise 6.5.1 — Assignment is not a copy

Chapter 6 (Objects), section 6.5: Copying a List.

Problem
-------
The backup should stay unchanged after we add a new reading to the original.

Bug type: Logical
-----------------
`backup = temps` makes both names point at the same list, so appending to `temps` also changes `backup`. Taking a real copy with `temps.copy()` (or `temps[:]`) keeps the backup unchanged.

The program below is the corrected version.
"""


temps = [33.0, 36.5, 31.0]
backup = temps.copy()
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
