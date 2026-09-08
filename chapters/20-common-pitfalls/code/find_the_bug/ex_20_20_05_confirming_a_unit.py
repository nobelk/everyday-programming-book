"""Exercise 20.20.5 — Confirming a unit

Chapter 20 (Common Pitfalls), section 20.20: Comparing text without thinking about case.

Problem
-------
This program should accept the unit "kg" whether typed as "KG", "Kg", or "kg".

Bug type: Logical
-----------------
`unit.upper()` produces `"KG"`, which never equals lowercase `"kg"`. Compare against the same case you converted to, for example `.lower() == "kg"`.

The program below is the corrected version.
"""


unit = "KG"
if unit.lower() == "kg":
    print("Kilograms")
