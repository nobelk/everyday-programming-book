"""Exercise 20.13.2 — Fixing a typo in a word

Chapter 20 (Common Pitfalls), section 20.13: Forgetting that strings are immutable.

Problem
-------
This program should change `"hpllo"` into `"hello"` by replacing one letter.

Bug type: Runtime
-----------------
You cannot assign to a single character of a string; `word[1] = "e"` raises `TypeError`. Rebuild the word from slices.

The program below is the corrected version.
"""


word = "hpllo"
word = word[0] + "e" + word[2:]
print(word)
