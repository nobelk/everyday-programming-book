"""Exercise 20.7.1 — Adding to raw input

Chapter 20 (Common Pitfalls), section 20.7: Forgetting to convert input() to a number.

Problem
-------
This program should ask for a year and print the next year.

Bug type: Runtime
-----------------
`input()` returns text, so `year + 1` adds a string and an int, raising `TypeError`. Wrap the input in `int()`.

The program below is the corrected version.
"""


year = int(input("Enter the year: "))
print(year + 1)
