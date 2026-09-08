"""Exercise 20.1.3 — Missing colon after `while`

Chapter 20 (Common Pitfalls), section 20.1: Forgetting the : after if, for, while, or def.

Problem
-------
This program should count down from 3 to 1 for a rocket launch.

Bug type: Syntax
----------------
The `while` header needs a colon before its block. Adding `:` lets the countdown loop parse and run.

The program below is the corrected version.
"""


seconds = 3
while seconds > 0:
    print(seconds)
    seconds = seconds - 1
