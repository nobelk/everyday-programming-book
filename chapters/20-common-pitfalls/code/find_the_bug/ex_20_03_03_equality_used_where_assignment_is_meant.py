"""Exercise 20.3.3 — Equality used where assignment is meant

Chapter 20 (Common Pitfalls), section 20.3: Confusing assignment with equality.

Problem
-------
This program should set a starting balance and print it.

Bug type: Runtime
-----------------
`balance == 100` compares instead of assigning, so `balance` is never created and the `print` raises `NameError`. Use a single `=` to assign.

The program below is the corrected version.
"""


balance = 100
print(balance)  # 100
