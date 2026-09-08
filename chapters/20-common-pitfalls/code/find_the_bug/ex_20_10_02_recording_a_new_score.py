"""Exercise 20.10.2 — Recording a new score

Chapter 20 (Common Pitfalls), section 20.10: Modifying a list item that does not exist.

Problem
-------
This program should store a new game score after the existing three.

Bug type: Runtime
-----------------
`scores[3]` does not exist yet, so assigning to it raises `IndexError`. Use `append` to add the new score.

The program below is the corrected version.
"""


scores = [10, 15, 20]
scores.append(25)
print(scores)
