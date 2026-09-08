"""Exercise 7.4.2 — Weekend or holiday

Chapter 7 (Operators), section 7.4: Boolean Operators.

Problem
-------
You can sleep in if it is a weekend or a holiday. This program should print `True`.

Bug type: Logical
-----------------
Either condition should let you sleep in, but `and` requires both to be true, giving `False`. Use `or`.

The program below is the corrected version.
"""


is_weekend = False
is_holiday = True
sleep_in = is_weekend or is_holiday
print(sleep_in)   # True
