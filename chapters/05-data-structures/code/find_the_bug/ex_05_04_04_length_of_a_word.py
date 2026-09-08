"""Exercise 5.4.4 — Length of a word

Chapter 5 (Data Structures), section 5.4: Strings.

Problem
-------
The program should print the number of letters in "science": 7.

Bug type: Runtime
-----------------
`word()` tries to call the string as if it were a function, raising a `TypeError`. Pass the string itself to `len`.

The program below is the corrected version.
"""


word = "science"
count = len(word)
print(count)   # 7
