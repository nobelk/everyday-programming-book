"""Exercise 11.4.2 — global then assign

Chapter 11 (Scoping), section 11.4: Using global.

Problem
-------
This program should use `global` to set the module-level `score` to 100 from inside the function, and print 100.

Bug type: Logical
-----------------
`score == 100` is a comparison, not an assignment, so the global is never changed and stays 0. Use `=` to assign.

The program below is the corrected version.
"""


score = 0

def set_perfect():
    global score
    score = 100

set_perfect()
print("Score:", score)
