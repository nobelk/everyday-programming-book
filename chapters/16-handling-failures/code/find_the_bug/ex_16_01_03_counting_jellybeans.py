"""Exercise 16.1.3 — Counting jellybeans

Chapter 16 (Handling Failures), section 16.1: Handling Bad User Input.

Problem
-------
This program reads how many jellybeans are in a jar and prints the count, retrying on bad input.

Bug type: Logical
-----------------
There is no `break` after a successful read, so even on valid input the `while True` loop never ends — it keeps re-asking forever. Add `break` once a valid count is printed.

The program below is the corrected version.
"""


while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
        break
    except ValueError:
        print("Please type a whole number.")
