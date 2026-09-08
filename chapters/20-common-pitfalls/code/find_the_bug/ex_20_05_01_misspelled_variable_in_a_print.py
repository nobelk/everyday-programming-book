"""Exercise 20.5.1 — Misspelled variable in a print

Chapter 20 (Common Pitfalls), section 20.5: Misspelling variable names.

Problem
-------
This program should print a welcome message.

Bug type: Runtime
-----------------
`greting` is a different name from `greeting`, so Python raises `NameError`. Use the correct spelling.

The program below is the corrected version.
"""


greeting = "Good morning"
print(greeting)
