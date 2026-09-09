"""Exercise 6.2.2 — Splitting a bill

Chapter 6 (Data Structures), section 6.2: float.

Problem
-------
A 50-dollar bill is split between 4 people. The program should print 12.5.

Bug type: Logical
-----------------
`//` discards the fractional part, giving 12 instead of 12.5. Use true division `/` so the result is a float.

The program below is the corrected version.
"""


bill = 50
people = 4

each = bill / people
print(each)   # 12.5
