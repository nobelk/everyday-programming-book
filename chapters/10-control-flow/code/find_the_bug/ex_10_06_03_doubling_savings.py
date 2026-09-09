"""Exercise 10.6.3 — Doubling savings

Chapter 10 (Control Flow), section 10.6: while Loops.

Problem
-------
Starting at $1, this should double the balance until it reaches at least $8, printing each balance.

Bug type: Logical
-----------------
`balance + 2` adds a fixed 2 each pass instead of *doubling*, so the balance grows 1, 3, 5, 7, ... and the values are wrong. Multiplying by 2 doubles it as intended.

The program below is the corrected version.
"""


balance = 1

while balance < 8:
    print(balance)
    balance = balance * 2
