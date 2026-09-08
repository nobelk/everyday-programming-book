"""Exercise 20.15.1 — Reading the current temperature

Chapter 20 (Common Pitfalls), section 20.15: Forgetting to call a function with parentheses.

Problem
-------
This program should print the temperature returned by the function.

Bug type: Logical
-----------------
Writing `current_temperature` without parentheses prints the function object instead of calling it. Add `()` to invoke it.

The program below is the corrected version.
"""


def current_temperature():
    return 21.5

print("Temperature:", current_temperature())
