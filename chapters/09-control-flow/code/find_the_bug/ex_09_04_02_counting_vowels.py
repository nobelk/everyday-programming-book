"""Exercise 9.4.2 — Counting vowels

Chapter 9 (Control Flow), section 9.4: for Loops.

Problem
-------
This program should count the vowels in a word. For "education" it should print 5.

Bug type: Logical
-----------------
The count is correct, but `print(count + 1)` adds one extra at the end. Print `count` itself.

The program below is the corrected version.
"""


word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count)
