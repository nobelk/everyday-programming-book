"""Exercise 9.8.3 — Sum positive numbers

Chapter 9 (Control Flow), section 9.8: continue.

Problem
-------
This program should add only the positive numbers and print 9.

Bug type: Logical
-----------------
The `continue` after `total += number` is harmless, but `print(total + 1)` adds an extra 1, giving 10 instead of 9. Printing `total` gives the correct sum.

The program below is the corrected version.
"""


numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number

print(total)
