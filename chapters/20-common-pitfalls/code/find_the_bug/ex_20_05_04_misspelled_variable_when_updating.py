"""Exercise 20.5.4 — Misspelled variable when updating

Chapter 20 (Common Pitfalls), section 20.5: Misspelling variable names.

Problem
-------
This program should add a tip to a restaurant bill and print the total.

Bug type: Runtime
-----------------
`bil` is a misspelling of `bill`, so the calculation raises `NameError`. Use the correct name.

The program below is the corrected version.
"""


bill = 40
tip = 6
total = bill + tip
print(total)  # 46
