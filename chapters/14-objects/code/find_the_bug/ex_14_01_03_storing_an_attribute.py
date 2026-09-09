"""Exercise 14.1.3 — Storing an attribute

Chapter 14 (Objects), section 14.1: Classes.

Problem
-------
This class records a student's name and quiz score, then prints a summary.

Bug type: Runtime
-----------------
The attribute stored in `__init__` is named `score`, but `summary` reads `self.grade`, which was never set. Referring to `self.score` fixes the `AttributeError`.

The program below is the corrected version.
"""


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.score}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
