"""Exercise 6.5.1 — No reading yet

Chapter 6 (Data Structures), section 6.5: None.

Problem
-------
A sensor has no reading. The program should print `True` because the reading is `None`.

Bug type: Logical
-----------------
`None` is not the same as the string `"None"`, so the comparison is always False. Compare to the real `None` value with `is None`.

The program below is the corrected version.
"""


reading = None
no_data = reading is None
print(no_data)   # True
