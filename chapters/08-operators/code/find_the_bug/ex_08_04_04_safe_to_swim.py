"""Exercise 8.4.4 — Safe to swim

Chapter 8 (Operators), section 8.4: Boolean Operators.

Problem
-------
It is safe to swim if a lifeguard is on duty and the water is calm. This program should print `True`.

Bug type: Syntax
----------------
A boolean expression assigned to a variable must not end with a colon; the trailing `:` makes the line invalid. Remove it.

The program below is the corrected version.
"""


lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm
print(safe_to_swim)   # True
