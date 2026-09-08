"""Exercise 20.7.2 — Doubling a typed quantity

Chapter 20 (Common Pitfalls), section 20.7: Forgetting to convert input() to a number.

Problem
-------
This program should double the number of cookies the user enters.

Bug type: Logical
-----------------
`cookies` is text, so `cookies * 2` repeats the string (e.g. `"1212"`) instead of doubling the number. Convert the input to `int` first.

The program below is the corrected version.
"""


cookies = int(input("How many cookies? "))
print(cookies * 2 == 24)  # for input 12
