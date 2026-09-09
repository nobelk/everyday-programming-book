"""Exercise 10.7.2 — First over budget

Chapter 10 (Control Flow), section 10.7: break.

Problem
-------
This program should print the first expense that is over 100 and then stop.

Bug type: Logical
-----------------
`break` is not indented inside the `if`, so it runs on the very first item and the loop stops before finding 150. Indenting `break` under the `if` makes it exit only after a match.

The program below is the corrected version.
"""


expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
        break
