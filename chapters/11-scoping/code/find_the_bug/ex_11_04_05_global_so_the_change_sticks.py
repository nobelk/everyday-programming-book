"""Exercise 11.4.5 — global so the change sticks

Chapter 11 (Scoping), section 11.4: Using global.

Problem
-------
This program should use `global` to flip the module-level `is_open` flag to True, and print True.

Bug type: Runtime
-----------------
Python's boolean is `True` with a capital T; `false` is not defined, so the assignment raises `NameError`. Use `True`.

The program below is the corrected version.
"""


is_open = False

def open_shop():
    global is_open
    is_open = True

open_shop()
print("Open:", is_open)
