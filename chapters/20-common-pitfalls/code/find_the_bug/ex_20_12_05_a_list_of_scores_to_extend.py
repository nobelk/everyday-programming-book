"""Exercise 20.12.5 — A list of scores to extend

Chapter 20 (Common Pitfalls), section 20.12: Using parentheses instead of brackets for lists.

Problem
-------
This program should start a list of scores and append a new one.

Bug type: Runtime
-----------------
Parentheses create a tuple, which has no `append`, raising `AttributeError`. Use brackets to make a list.

The program below is the corrected version.
"""


scores = [88, 92]
scores.append(75)
print(scores)
