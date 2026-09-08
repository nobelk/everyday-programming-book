"""Exercise 16.3.1 — Confirming a conversion

Chapter 16 (Handling Failures), section 16.3: Using else.

Problem
-------
This program converts a string to a number and, only when that succeeds, prints a success line.

Bug type: Logical
-----------------
The success line is printed twice — once inside `try` and again in `else`. Code that should run only on success belongs in `else`, not in `try`; remove the duplicate from the `try` block.

The program below is the corrected version.
"""


text = "42"
try:
    number = int(text)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
