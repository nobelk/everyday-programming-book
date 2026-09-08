"""Exercise 11.6.2 — reading an instance attribute

Chapter 11 (Scoping), section 11.6: Scope with Objects and Classes.

Problem
-------
This program stores a student's score and should print it back as 95.

Bug type: Runtime
-----------------
`get_score` returns plain `score`, which is not a local or global name, so Python raises `NameError`. Read the attribute through `self.score`.

The program below is the corrected version.
"""


class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

learner = Student(95)
print("Score:", learner.get_score())
