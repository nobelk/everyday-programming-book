"""Exercise 5.2.4 — Half of a measurement

Chapter 5 (Data Structures), section 5.2: float.

Problem
-------
A board is 9.0 meters long. The program should print half its length, 4.5.

Bug type: Syntax
----------------
The closing parenthesis of `print(...)` is missing, so the program will not parse. Add the `)` after `half`.

The program below is the corrected version.
"""


length = 9.0
half = length / 2
print(half)   # 4.5
