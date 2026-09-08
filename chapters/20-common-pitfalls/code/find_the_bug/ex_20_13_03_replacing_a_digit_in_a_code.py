"""Exercise 20.13.3 — Replacing a digit in a code

Chapter 20 (Common Pitfalls), section 20.13: Forgetting that strings are immutable.

Problem
-------
This program should change the first character of a code to `"9"`.

Bug type: Runtime
-----------------
Strings are immutable, so `code[0] = "9"` raises `TypeError`. Construct a new string.

The program below is the corrected version.
"""


code = "12345"
code = "9" + code[1:]
print(code)
