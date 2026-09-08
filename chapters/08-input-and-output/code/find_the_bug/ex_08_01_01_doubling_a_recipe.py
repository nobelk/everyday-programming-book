"""Exercise 8.1.1 — Doubling a recipe

Chapter 8 (Input and Output), section 8.1: Reading Input and Printing Output.

Problem
-------
This program asks how many cookies a recipe makes, then prints double that amount.

Bug type: Logical
-----------------
`input()` always returns a string, so `cookies * 2` repeats the text (`"1212"`) instead of computing `24`. Convert the input to an `int` before doing arithmetic.

The program below is the corrected version.
"""


# Assume the user types: 12
cookies = int(input("How many cookies does the recipe make? "))
print(f"Doubled, that is {cookies * 2} cookies.")
