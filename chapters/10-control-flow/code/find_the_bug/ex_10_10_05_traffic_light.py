"""Exercise 10.10.5 — Traffic light

Chapter 10 (Control Flow), section 10.10: match / case.

Problem
-------
This program should print the action for a traffic light colour. For an unknown colour like "blue" it should print `Unknown`.

Bug type: Logical
-----------------
The default case builds the string `"Unknown"` but never prints it, so an unrecognized colour produces no output. Adding `print` produces the expected output.

The program below is the corrected version.
"""


color = "blue"

match color:
    case "green":
        print("Go")
    case "yellow":
        print("Slow down")
    case "red":
        print("Stop")
    case _:
        print("Unknown")
