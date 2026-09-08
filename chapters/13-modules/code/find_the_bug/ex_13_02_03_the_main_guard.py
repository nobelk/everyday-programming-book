"""Exercise 13.2.3 — The main guard

Chapter 13 (Modules), section 13.2: Writing Your Own Module.

Problem
-------
This module should print a sample conversion only when run directly, but it should still work when imported.

Bug type: Syntax
----------------
The guard uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error inside an `if` condition. Use `==` to compare `__name__` with `"__main__"`.

The program below is the corrected version.
"""


# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(c_to_f(100))   # 212.0
