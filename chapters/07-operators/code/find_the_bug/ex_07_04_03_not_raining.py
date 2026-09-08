"""Exercise 7.4.3 — Not raining

Chapter 7 (Operators), section 7.4: Boolean Operators.

Problem
-------
This program should report that it is not raining and print `True`.

Bug type: Syntax
----------------
`not` is a prefix operator and must come before its value; writing `is_raining not` will not parse. Move `not` in front to get `not is_raining`.

The program below is the corrected version.
"""


is_raining = False
stay_dry = not is_raining
print(stay_dry)   # True
