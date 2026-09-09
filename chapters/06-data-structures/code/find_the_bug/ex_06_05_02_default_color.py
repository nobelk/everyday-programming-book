"""Exercise 6.5.2 — Default color

Chapter 6 (Data Structures), section 6.5: None.

Problem
-------
The function should return a default color when none is given. Calling it with nothing should print "blue".

Bug type: Logical
-----------------
The function changes `color` but never returns it, so it returns `None`. Add a `return color` statement.

The program below is the corrected version.
"""


def choose_color(color):
    if color is None:
        color = "blue"
    return color

print(choose_color(None))   # blue
