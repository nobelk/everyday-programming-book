"""Exercise 10.2.2 — Freezing point

Chapter 10 (Control Flow), section 10.2: Common Comparison Operators.

Problem
-------
Water freezes at 0 degrees Celsius or below. This program should print `Frozen` for a temperature of 0.

Bug type: Logical
-----------------
`<` excludes 0 itself, but water freezes *at* 0 too. Using `<=` includes the freezing point.

The program below is the corrected version.
"""


temp_c = 0

if temp_c <= 0:
    print("Frozen")
else:
    print("Liquid")
