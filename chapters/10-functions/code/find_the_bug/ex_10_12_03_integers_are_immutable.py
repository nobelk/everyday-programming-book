"""Exercise 10.12.3 — Integers are immutable

Chapter 10 (Functions), section 10.12: Pass by Reference vs Pass by Sharing.

Problem
-------
Changing the parameter inside the function should not affect the caller's number, which stays 5.

Bug type: Logical
-----------------
The `global` line makes the function overwrite the caller's `score`, so it prints 15. An integer is passed by sharing: reassigning the local `value` never affects the caller. Drop the `global` line and work with the parameter.

The program below is the corrected version.
"""


def add_ten(value):
    value = value + 10

score = 5
add_ten(score)
print(score)   # 5
