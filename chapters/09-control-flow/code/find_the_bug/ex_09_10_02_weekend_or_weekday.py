"""Exercise 9.10.2 — Weekend or weekday

Chapter 9 (Control Flow), section 9.10: match / case.

Problem
-------
This program should print `Weekend` for Saturday or Sunday and `Weekday` otherwise. For "Monday" it should print `Weekday`.

Bug type: Syntax
----------------
In a `case` pattern, alternatives are joined with `|`, not the keyword `or`. Using `|` fixes the pattern.

The program below is the corrected version.
"""


day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
