"""Exercise 10.8.1 — Skip the empty entries

Chapter 10 (Control Flow), section 10.8: continue.

Problem
-------
This program should print every non-empty word in the list.

Bug type: Logical
-----------------
`break` stops the loop at the first empty string, so "dog" is never printed. To skip just the empty entries and continue, use `continue`.

The program below is the corrected version.
"""


words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        continue
    print(word)
