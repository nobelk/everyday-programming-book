"""Exercise 5.4.2 — Shouting

Chapter 5 (Data Structures), section 5.4: Strings.

Problem
-------
The program should print a greeting in all capitals: HELLO.

Bug type: Logical
-----------------
`word.upper` refers to the method without calling it, so it prints a method object, not the text. Add parentheses to call it: `word.upper()`.

The program below is the corrected version.
"""


word = "hello"
loud = word.upper()
print(loud)   # HELLO
