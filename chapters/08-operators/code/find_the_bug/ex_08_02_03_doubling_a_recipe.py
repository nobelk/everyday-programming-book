"""Exercise 8.2.3 — Doubling a recipe

Chapter 8 (Operators), section 8.2: Assignment Operator.

Problem
-------
A recipe needs 2 cups of flour, and this program should double it for a bigger batch, printing `4`.

Bug type: Runtime
-----------------
The variable is `cups_flour`, but `print` refers to `Cups_flour` with a capital C, raising a `NameError`. Match the name exactly.

The program below is the corrected version.
"""


cups_flour = 2
cups_flour *= 2
print(cups_flour)   # 4
