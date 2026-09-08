"""Exercise 10.12.2 — Rebinding stays local

Chapter 10 (Functions), section 10.12: Pass by Reference vs Pass by Sharing.

Problem
-------
Reassigning the parameter should not change the caller's list, so this prints the original.

Bug type: Logical
-----------------
`clear` and `extend` mutate the shared list in place, so the caller sees `[99, 100]`, not the original. To leave the caller unchanged, rebind the local name instead.

The program below is the corrected version.
"""


def replace(numbers):
    numbers = [99, 100]

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
