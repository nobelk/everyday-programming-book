"""Exercise 9.5.4 — Sum of first ten numbers

Chapter 9 (Control Flow), section 9.5: range.

Problem
-------
This program should add the numbers 1 through 10 and print 55.

Bug type: Logical
-----------------
`range(1, 10)` stops at 9, so 10 is left out and the total is 45. Use `range(1, 11)` to include 10.

The program below is the corrected version.
"""


total = 0

for number in range(1, 11):
    total += number

print(total)
