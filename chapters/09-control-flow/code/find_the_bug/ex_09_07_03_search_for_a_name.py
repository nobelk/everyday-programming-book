"""Exercise 9.7.3 — Search for a name

Chapter 9 (Control Flow), section 9.7: break.

Problem
-------
This program should stop as soon as it finds "Ana" and print `Found`.

Bug type: Runtime
-----------------
`brake` is a misspelling of `break`, so Python raises a `NameError`. Correcting the keyword fixes it.

The program below is the corrected version.
"""


names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        break
