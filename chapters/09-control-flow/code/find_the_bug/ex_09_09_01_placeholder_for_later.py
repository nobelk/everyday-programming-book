"""Exercise 9.9.1 — Placeholder for later

Chapter 9 (Control Flow), section 9.9: pass.

Problem
-------
The `if` branch is a planned feature not yet written, so it should do nothing for now; the program should still print every item.

Bug type: Syntax
----------------
The `if` body is empty, so Python raises an `IndentationError`. A placeholder body needs `pass`.

The program below is the corrected version.
"""


for item in [1, 2, 3]:
    if item == 2:
        pass
    print(item)
