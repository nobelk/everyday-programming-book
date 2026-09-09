"""Exercise 10.7.4 — First even number

Chapter 10 (Control Flow), section 10.7: break.

Problem
-------
This program should print the first even number in the list and stop. For these numbers it should print 4.

Bug type: Logical
-----------------
`break` runs before the `print`, so nothing is ever shown. Print the number first, then break.

The program below is the corrected version.
"""


numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
