"""Exercise 6.7.4 — A single value

Chapter 6 (Data Structures), section 6.7: Tuples.

Problem
-------
The program should make a one-element tuple holding the number 42 and print its length, 1.

Bug type: Runtime
-----------------
`(42)` is just the number 42 in parentheses, not a tuple, so `len(single)` raises a `TypeError` on an int. A one-element tuple needs a trailing comma: `(42,)`.

The program below is the corrected version.
"""


single = (42,)
print(len(single))   # 1
