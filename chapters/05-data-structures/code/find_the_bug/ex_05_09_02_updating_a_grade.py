"""Exercise 5.9.2 — Updating a grade

Chapter 5 (Data Structures), section 5.9: Dictionaries.

Problem
-------
The program should change the grade to 11 and print 11.

Bug type: Syntax
----------------
Dictionary assignment uses square brackets, not parentheses; `student("grade") = 11` is invalid. Use `student["grade"] = 11`.

The program below is the corrected version.
"""


student = {"name": "Maya", "grade": 10}
student["grade"] = 11
print(student["grade"])   # 11
