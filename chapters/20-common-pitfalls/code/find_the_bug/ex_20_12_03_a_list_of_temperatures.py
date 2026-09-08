"""Exercise 20.12.3 — A list of temperatures

Chapter 20 (Common Pitfalls), section 20.12: Using parentheses instead of brackets for lists.

Problem
-------
This program should change the first temperature reading to 19.

Bug type: Runtime
-----------------
Parentheses make a tuple, which is immutable, so `temperatures[0] = 19` raises `TypeError`. Use brackets to make an editable list.

The program below is the corrected version.
"""


temperatures = [21, 22, 20]
temperatures[0] = 19
print(temperatures)
