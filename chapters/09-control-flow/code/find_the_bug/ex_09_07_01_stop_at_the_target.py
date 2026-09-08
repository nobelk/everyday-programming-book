"""Exercise 9.7.1 — Stop at the target

Chapter 9 (Control Flow), section 9.7: break.

Problem
-------
This program should print numbers from 1 and stop *before* printing 3, so it prints 1 and 2.

Bug type: Logical
-----------------
`continue` only skips 3 and keeps going (printing 4, 5), but the program should stop entirely before 3. Use `break` to exit the loop.

The program below is the corrected version.
"""


for number in range(1, 6):
    if number == 3:
        break
    print(number)
