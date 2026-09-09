"""Exercise 6.1.4 — Counting by tens

Chapter 6 (Data Structures), section 6.1: int.

Problem
-------
The program should add 10 to a starting count and print 110.

Bug type: Runtime
-----------------
`"10"` is a string, so `count + "10"` raises a `TypeError` (you cannot add an int and a str). Use the int literal `10`.

The program below is the corrected version.
"""


count = 100
count = count + 10
print(count)   # 110
