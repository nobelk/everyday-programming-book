"""Exercise 8.1.5 — Greeting by name

Chapter 8 (Input and Output), section 8.1: Reading Input and Printing Output.

Problem
-------
This program asks for a name and prints a greeting.

Bug type: Syntax
----------------
The f-string is missing its closing double quote, so Python never finds the end of the string and reports a syntax error. Add the closing `"` before the parenthesis.

The program below is the corrected version.
"""


# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.")
