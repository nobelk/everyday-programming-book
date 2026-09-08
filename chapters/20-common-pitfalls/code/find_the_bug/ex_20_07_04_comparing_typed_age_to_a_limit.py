"""Exercise 20.7.4 — Comparing typed age to a limit

Chapter 20 (Common Pitfalls), section 20.7: Forgetting to convert input() to a number.

Problem
-------
This program should print `"Adult"` when the typed age is at least 18.

Bug type: Runtime
-----------------
`age` is a string, so `age >= 18` compares a string with an int and raises `TypeError`. Convert the input to `int` before comparing.

The program below is the corrected version.
"""


age = int(input("Your age: "))
if age >= 18:
    print("Adult")
