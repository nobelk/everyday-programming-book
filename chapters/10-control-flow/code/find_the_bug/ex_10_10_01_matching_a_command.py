"""Exercise 10.10.1 — Matching a command

Chapter 10 (Control Flow), section 10.10: match / case.

Problem
-------
This program should respond to a command. For "start" it should print `Starting...`.

Bug type: Syntax
----------------
The first `case` line is missing its colon. Adding it fixes the parse.

The program below is the corrected version.
"""


command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
