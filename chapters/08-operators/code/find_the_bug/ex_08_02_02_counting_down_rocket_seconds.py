"""Exercise 8.2.2 — Counting down rocket seconds

Chapter 8 (Operators), section 8.2: Assignment Operator.

Problem
-------
This program should subtract 3 from a 10-second countdown and print the time remaining, which is `7`.

Bug type: Logical
-----------------
The line `seconds_left =- 3` is parsed as assigning the value `-3`, not as subtracting 3. The intended augmented-assignment operator is `-=`.

The program below is the corrected version.
"""


seconds_left = 10
seconds_left -= 3
print(seconds_left)   # 7
