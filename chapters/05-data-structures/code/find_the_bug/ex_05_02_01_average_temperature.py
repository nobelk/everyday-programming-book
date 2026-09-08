"""Exercise 5.2.1 — Average temperature

Chapter 5 (Data Structures), section 5.2: float.

Problem
-------
Three readings are 20.0, 22.0, and 24.0 degrees. The program should print the average, 22.0.

Bug type: Logical
-----------------
Without parentheses, only `reading3 / 3` is divided (operator precedence), so the sum is wrong. Wrap the addition in parentheses before dividing.

The program below is the corrected version.
"""


reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = (reading1 + reading2 + reading3) / 3
print(average)   # 22.0
