"""Exercise 20.8.2 — Pages per chapter

Chapter 20 (Common Pitfalls), section 20.8: Using / when you want a whole-number result.

Problem
-------
This program should print how many whole pages each of 5 chapters gets from 52 pages.

Bug type: Logical
-----------------
`52 / 5` is `10.4`; the program wants whole pages. Use `//` for the integer quotient `10`.

The program below is the corrected version.
"""


pages = 52
chapters = 5
print(pages // chapters)  # 10
