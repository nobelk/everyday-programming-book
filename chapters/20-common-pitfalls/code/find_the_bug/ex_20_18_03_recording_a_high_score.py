"""Exercise 20.18.3 — Recording a high score

Chapter 20 (Common Pitfalls), section 20.18: Forgetting to close a file.

Problem
-------
This program should save the player's high score to disk safely.

Bug type: Logical
-----------------
`score_file` is opened but never closed. Use `with open(...)` so the file closes automatically after writing.

The program below is the corrected version.
"""


high_score = 4200
with open("highscore.txt", "w") as score_file:
    score_file.write(str(high_score))
print("High score recorded")
