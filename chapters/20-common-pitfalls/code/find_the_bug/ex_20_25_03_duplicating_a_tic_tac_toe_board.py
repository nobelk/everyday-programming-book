"""Exercise 20.25.3 — Duplicating a tic-tac-toe board

Chapter 20 (Common Pitfalls), section 20.25: Shallow vs deep copy.

Problem
-------
This program should duplicate a game board so the duplicate can be edited safely.

Bug type: Logical
-----------------
`list(board)` makes a shallow copy whose inner rows are shared, so editing `trial` changes `board`. Use `copy.deepcopy`.

The program below is the corrected version.
"""


import copy

board = [["X", "O"], ["O", "X"]]
trial = copy.deepcopy(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
