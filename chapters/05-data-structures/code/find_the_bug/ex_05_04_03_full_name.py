"""Exercise 5.4.3 — Full name

Chapter 5 (Data Structures), section 5.4: Strings.

Problem
-------
The program should join a first and last name with a space: "Maya Singh".

Bug type: Logical
-----------------
Concatenation does not insert a space, so the result is "MayaSingh". Add a space string between the names.

The program below is the corrected version.
"""


first = "Maya"
last = "Singh"

full = first + " " + last
print(full)   # Maya Singh
