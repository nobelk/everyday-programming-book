"""Exercise 10.8.4 — Skip the indentation

Chapter 10 (Control Flow), section 10.8: continue.

Problem
-------
This program should print every odd number from 1 to 6, skipping the even ones.

Bug type: Syntax
----------------
The `continue` under the `if` is not indented, so Python raises an `IndentationError`. Indenting it inside the `if` fixes the parse.

The program below is the corrected version.
"""


for number in range(1, 7):
    if number % 2 == 0:
        continue
    print(number)
