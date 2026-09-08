"""Exercise 20.17.3 — Counting visitors

Chapter 20 (Common Pitfalls), section 20.17: Changing a global variable inside a function by accident.

Problem
-------
The program should increase the visitor count by one each time someone enters.

Bug type: Runtime
-----------------
Because `visitors` is assigned inside `enter`, Python marks it local and raises `UnboundLocalError`. Declare it `global`.

The program below is the corrected version.
"""


visitors = 0

def enter():
    global visitors
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
