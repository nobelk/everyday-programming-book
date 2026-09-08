"""Exercise 10.12.4 — Mutate in place

Chapter 10 (Functions), section 10.12: Pass by Reference vs Pass by Sharing.

Problem
-------
This should add a grade to the shared list in place, so the caller sees three items.

Bug type: Logical
-----------------
`grades = grades + [grade]` rebinds the local name to a new list, so the caller's list is unchanged. Use `append` to mutate the shared list in place.

The program below is the corrected version.
"""


def record_grade(grades, grade):
    grades.append(grade)

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
