"""Exercise 16.3.3 — Doubling a recipe

Chapter 16 (Handling Failures), section 16.3: Using else.

Problem
-------
This program reads a cup amount and, when valid, prints the doubled amount using `else`.

Bug type: Logical
-----------------
The doubling work that should run only after a successful conversion is placed in the `try` block; if `cups * 2` or the print logic ever failed it would be wrongly treated as an input error. The success-only computation belongs in `else`, leaving only the risky conversion in `try`.

The program below is the corrected version.
"""


try:
    cups = float(input("How many cups? "))
except ValueError:
    print("That was not a number.")
else:
    doubled = cups * 2
    print("You need", doubled, "cups.")
