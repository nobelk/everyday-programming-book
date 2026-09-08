"""Exercise 20.20.3 — Checking a chemical symbol

Chapter 20 (Common Pitfalls), section 20.20: Comparing text without thinking about case.

Problem
-------
This program should recognize the element symbol "Na" however the user types it.

Bug type: Logical
-----------------
`"NA" == "Na"` is `False` because the cases differ. Normalize the typed symbol, for example with `.capitalize()`.

The program below is the corrected version.
"""


symbol = "NA"
if symbol.capitalize() == "Na":
    print("That is sodium")
