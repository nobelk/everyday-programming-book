"""Exercise 20.13.5 — Correcting a unit label

Chapter 20 (Common Pitfalls), section 20.13: Forgetting that strings are immutable.

Problem
-------
This program should change the first letter of `"km"` to make `"Km"`.

Bug type: Runtime
-----------------
`unit[0] = "K"` tries to mutate an immutable string, raising `TypeError`. Make a new string instead.

The program below is the corrected version.
"""


unit = "km"
unit = "K" + unit[1:]
print(unit)
