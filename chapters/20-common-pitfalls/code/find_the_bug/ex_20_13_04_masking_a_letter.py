"""Exercise 20.13.4 — Masking a letter

Chapter 20 (Common Pitfalls), section 20.13: Forgetting that strings are immutable.

Problem
-------
This program should hide the last letter of a word with an asterisk.

Bug type: Runtime
-----------------
Assigning to `secret[3]` fails because strings cannot be changed in place, raising `TypeError`. Rebuild the string from its slices.

The program below is the corrected version.
"""


secret = "open"
secret = secret[:3] + "*"
print(secret)
