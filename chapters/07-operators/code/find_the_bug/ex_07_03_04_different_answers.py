"""Exercise 7.3.4 — Different answers

Chapter 7 (Operators), section 7.3: Comparison Operators.

Problem
-------
This program should check whether a student's answer differs from the correct answer and print `True`.

Bug type: Syntax
----------------
The "not equal" operator is written `!=`, not `= !`, so the expression will not parse. Use `!=`.

The program below is the corrected version.
"""


correct_answer = 42
student_answer = 38
print(student_answer != correct_answer)   # True
