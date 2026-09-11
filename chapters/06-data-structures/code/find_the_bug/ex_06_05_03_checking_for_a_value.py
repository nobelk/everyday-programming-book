"""Exercise 6.5.3 — Checking for a value

Chapter 6 (Data Structures), section 6.5: None.

Problem
-------
When a value is `None`, the program should print "missing".

Bug type: Logical
-----------------
The test `is not None` is False when the value is `None`, so the program runs the wrong branch and prints "has value". Use `is None` so a `None` value prints "missing".

The program below is the corrected version.
"""


favorite = None

if favorite is None:
    print("missing")
else:
    print("has value")
# expected: missing
