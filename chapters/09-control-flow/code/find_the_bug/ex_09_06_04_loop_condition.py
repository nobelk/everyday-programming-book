"""Exercise 9.6.4 — Loop condition

Chapter 9 (Control Flow), section 9.6: while Loops.

Problem
-------
This program should print the numbers 1 through 5.

Bug type: Logical
-----------------
`while count < 5` stops after printing 4, so 5 is never reached. Use `<=` to include 5.

The program below is the corrected version.
"""


count = 1

while count <= 5:
    print(count)
    count += 1
