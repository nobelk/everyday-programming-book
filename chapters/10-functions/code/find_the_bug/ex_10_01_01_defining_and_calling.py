"""Exercise 10.1.1 — Defining and calling

Chapter 10 (Functions), section 10.1: Your First Function.

Problem
-------
This program should define a function that prints a welcome message and then call it once.

Bug type: Logical
-----------------
Writing `welcome` only refers to the function object; it does not run it. You must add parentheses to call it, `welcome()`, so the body executes.

The program below is the corrected version.
"""


def welcome():
    print("Welcome to the science club!")

welcome()
