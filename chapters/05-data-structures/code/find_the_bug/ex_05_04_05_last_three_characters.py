"""Exercise 5.4.5 — Last three characters

Chapter 5 (Data Structures), section 5.4: Strings.

Problem
-------
The program should print the last three characters of a code: "789".

Bug type: Logical
-----------------
`code[-3]` is a single character ("7"), not the last three. Slice with `code[-3:]` to get "789".

The program below is the corrected version.
"""


code = "ABC789"
last_three = code[-3:]
print(last_three)   # 789
