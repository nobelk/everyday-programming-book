"""Exercise 5.5.4 — Length of nothing

Chapter 5 (Data Structures), section 5.5: None.

Problem
-------
A list of temperatures has not been filled in yet, so it is `None`. The program tries to count it and should instead detect the missing list and print 0.

Bug type: Runtime
-----------------
`len(None)` raises a `TypeError` because `None` has no length. Check for `None` first and use 0 in that case.

The program below is the corrected version.
"""


temps = None
count = len(temps) if temps is not None else 0
print(count)   # 0
