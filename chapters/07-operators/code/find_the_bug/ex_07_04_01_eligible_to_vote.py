"""Exercise 7.4.1 — Eligible to vote

Chapter 7 (Operators), section 7.4: Boolean Operators.

Problem
-------
A person may vote only if they are at least 18 *and* a citizen. This adult is not a citizen, so the program should print `False`.

Bug type: Logical
-----------------
Voting requires both conditions, but `or` returns `True` when only one holds, so a non-citizen adult is wrongly allowed. Use `and` so both age and citizenship must be satisfied.

The program below is the corrected version.
"""


age = 20
is_citizen = False
can_vote = age >= 18 and is_citizen
print(can_vote)   # False
