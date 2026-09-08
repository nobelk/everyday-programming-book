"""Exercise 20.20.2 — Matching a chosen color

Chapter 20 (Common Pitfalls), section 20.20: Comparing text without thinking about case.

Problem
-------
The program should detect the favorite color "blue" regardless of case.

Bug type: Logical
-----------------
`favorite.upper()` gives `"BLUE"`, which never equals the lowercase `"blue"`. Normalize both sides to the same case, for example `.lower() == "blue"`.

The program below is the corrected version.
"""


favorite = "Blue"
if favorite.lower() == "blue":
    print("You picked blue")
