"""Exercise 8.5.5 — Day in the schedule

Chapter 8 (Operators), section 8.5: Other Operators.

Problem
-------
This program should report whether "Wednesday" is in the schedule and print `True`.

Bug type: Logical
-----------------
`not in` returns `False` when the day is present, the reverse of what we want. Use the `in` operator to confirm membership.

The program below is the corrected version.
"""


schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" in schedule
print(has_wednesday)   # True
