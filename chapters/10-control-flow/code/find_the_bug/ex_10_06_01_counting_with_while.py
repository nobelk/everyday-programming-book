"""Exercise 10.6.1 — Counting with while

Chapter 10 (Control Flow), section 10.6: while Loops.

Problem
-------
This program should print the numbers 1 through 5 using a `while` loop.

Bug type: Runtime
-----------------
The loop never updates `count`, so the condition stays true forever—an infinite loop. Incrementing `count` each pass lets it terminate.

The program below is the corrected version.
"""


count = 1

while count <= 5:
    print(count)
    count += 1
