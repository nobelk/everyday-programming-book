"""Exercise 5.8.4 — Shared subjects

Chapter 5 (Data Structures), section 5.8: Sets.

Problem
-------
Two students list their subjects. The program should print the subjects they share: {"math"}.

Bug type: Logical
-----------------
`|` is union (all subjects from both); shared items need intersection `&`. Use `maya & leo` to get just `{"math"}`.

The program below is the corrected version.
"""


maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya & leo
print(shared)   # {'math'}
