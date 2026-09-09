"""Exercise 8.5.1 — Vowel check

Chapter 8 (Operators), section 8.5: Other Operators.

Problem
-------
This program should report whether the letter is a vowel and print `True`.

Bug type: Logical
-----------------
The code used `not in`, which would report `False` for a real vowel. To confirm membership, use the `in` operator.

The program below is the corrected version.
"""


letter = "e"
vowels = "aeiou"
is_vowel = letter in vowels
print(is_vowel)   # True
