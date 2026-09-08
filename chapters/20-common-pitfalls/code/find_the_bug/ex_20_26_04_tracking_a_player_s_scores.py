"""Exercise 20.26.4 — Tracking a player's scores

Chapter 20 (Common Pitfalls), section 20.26: Mutable default arguments.

Problem
-------
Each call should start a brand-new scoreboard with just the given score.

Bug type: Logical
-----------------
The shared default `board=[]` keeps old scores between calls. Use `None` and create a new list inside the function.

The program below is the corrected version.
"""


def new_scoreboard(score, board=None):
    if board is None:
        board = []
    board.append(score)
    return board

print(new_scoreboard(10))  # [10]
print(new_scoreboard(20))  # [20]
