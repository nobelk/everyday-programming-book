"""Exercise 20.22.3 — Turning a word into letters

Chapter 20 (Common Pitfalls), section 20.22: Shadowing built-in names like list, str, or sum.

Problem
-------
This program should turn the word into a list of its letters.

Bug type: Runtime
-----------------
`list = "abc"` shadows the built-in `list`, so `list("hello")` tries to call a string and raises `TypeError`. Rename the variable.

The program below is the corrected version.
"""


word = "abc"
letters = list("hello")
print(letters)
