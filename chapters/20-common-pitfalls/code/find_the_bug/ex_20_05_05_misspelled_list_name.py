"""Exercise 20.5.5 — Misspelled list name

Chapter 20 (Common Pitfalls), section 20.5: Misspelling variable names.

Problem
-------
This program should print the average of three exam scores.

Bug type: Runtime
-----------------
`score` (singular) was never defined; the list is named `scores`, so `sum(score)` raises `NameError`. Pass the correct list name.

The program below is the corrected version.
"""


scores = [80, 90, 100]
average = sum(scores) / len(scores)
print(average)  # 90.0
