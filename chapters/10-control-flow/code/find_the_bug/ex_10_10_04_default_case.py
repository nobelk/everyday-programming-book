"""Exercise 10.10.4 — Default case

Chapter 10 (Control Flow), section 10.10: match / case.

Problem
-------
This program should print `Unknown command` for anything it does not recognize. For "fly" it should print `Unknown command`.

Bug type: Logical
-----------------
`case "_"` matches the literal string `"_"`, not ``anything else''. The wildcard default is the bare `_` with no quotes.

The program below is the corrected version.
"""


command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
