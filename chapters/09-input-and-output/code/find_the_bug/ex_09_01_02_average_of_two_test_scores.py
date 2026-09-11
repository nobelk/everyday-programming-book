"""Exercise 9.1.2 — Average of two test scores

Chapter 9 (Input and Output), section 9.1: Reading Input and Printing Output.

Problem
-------
Assuming the user types 80 then 90, this program should print `Your average is 85.0.`.

Bug type: Logical
-----------------
Without parentheses, `score1 + score2 / 2` divides only the second score first (operator precedence), giving 125.0 instead of 85.0. Parenthesize the sum before dividing.

The program below is the corrected version.
"""


# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = (score1 + score2) / 2
print(f"Your average is {average}.")
