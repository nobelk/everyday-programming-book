"""Exercise 10.2.5 — Adult check

Chapter 10 (Control Flow), section 10.2: Common Comparison Operators.

Problem
-------
This program should print `Adult` for anyone 18 or older. An 18-year-old should print `Adult`.

Bug type: Logical
-----------------
``18 or older'' includes 18, but `>` excludes it. Use `>=`.

The program below is the corrected version.
"""


age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
