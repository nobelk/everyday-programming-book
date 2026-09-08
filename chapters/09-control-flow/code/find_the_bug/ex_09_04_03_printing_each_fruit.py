"""Exercise 9.4.3 — Printing each fruit

Chapter 9 (Control Flow), section 9.4: for Loops.

Problem
-------
This program should print each fruit in the list on its own line.

Bug type: Syntax
----------------
The `for` statement is missing its colon. Adding it fixes the parse error.

The program below is the corrected version.
"""


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
