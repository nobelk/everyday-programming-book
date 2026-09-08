"""Exercise 20.26.1 — Collecting quiz answers

Chapter 20 (Common Pitfalls), section 20.26: Mutable default arguments.

Problem
-------
Each call should start with an empty answer sheet and add one answer.

Bug type: Logical
-----------------
The default `sheet=[]` is created once and reused, so answers accumulate across calls. Default to `None` and make a fresh list inside.

The program below is the corrected version.
"""


def record_answer(answer, sheet=None):
    if sheet is None:
        sheet = []
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
