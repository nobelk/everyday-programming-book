"""Exercise 6.3.1 — Is it freezing?

Chapter 6 (Data Structures), section 6.3: bool.

Problem
-------
Water freezes at 0 degrees Celsius. The program should report `True` when the temperature is below freezing. With temp = -5 it should print True.

Bug type: Logical
-----------------
"Below freezing" means less than 0, but the test used `>`, which is False for -5. Use `<` so the comparison returns True.

The program below is the corrected version.
"""


temp = -5
is_freezing = temp < 0
print(is_freezing)   # True
