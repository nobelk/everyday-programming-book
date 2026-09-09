"""Exercise 6.5.5 — Comparing to None

Chapter 6 (Data Structures), section 6.5: None.

Problem
-------
The program should check whether a username has been set, printing `True` when it is still `None`.

Bug type: Runtime
-----------------
`Not_set` (capital N) is undefined, so printing it raises a `NameError`. Print the variable `not_set`.

The program below is the corrected version.
"""


username = None
not_set = username is None
print(not_set)   # True
