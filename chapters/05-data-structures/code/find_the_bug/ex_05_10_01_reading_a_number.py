"""Exercise 5.10.1 — Reading a number

Chapter 5 (Data Structures), section 5.10: Variables and Types.

Problem
-------
Input arrives as text. The program should turn "25" into a number and print 30 after adding 5.

Bug type: Runtime
-----------------
`age_text` is a string, so `age_text + 5` mixes str and int and raises a `TypeError`. Convert the text with `int()` before adding.

The program below is the corrected version.
"""


age_text = "25"
age = int(age_text) + 5
print(age)   # 30
