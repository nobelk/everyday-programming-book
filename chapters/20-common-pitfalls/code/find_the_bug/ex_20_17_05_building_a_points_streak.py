"""Exercise 20.17.5 — Building a points streak

Chapter 20 (Common Pitfalls), section 20.17: Changing a global variable inside a function by accident.

Problem
-------
The program should multiply the current streak by 2 each round.

Bug type: Runtime
-----------------
`streak` is assigned inside the function, so Python treats it as local and raises `UnboundLocalError`. Declare it `global`.

The program below is the corrected version.
"""


streak = 1

def double_streak():
    global streak
    streak = streak * 2

double_streak()
print("Streak:", streak)
