"""Exercise 7.5.3 — Missing value check

Chapter 7 (Operators), section 7.5: Other Operators.

Problem
-------
This program should report that a measurement is missing (its value is `None`) and print `True`.

Bug type: Logical
-----------------
`measurement is not None` is `False` when the value really is `None`, the opposite of what we want. Use the identity operator `is` to test that the value is exactly `None`.

The program below is the corrected version.
"""


measurement = None
is_missing = measurement is None
print(is_missing)   # True
