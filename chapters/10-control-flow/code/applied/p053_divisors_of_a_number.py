"""Problem 53 — Divisors of a number

Domain: Mathematics. Chapter 10 (Control Flow), loops.

Problem
-------
Print every positive divisor of 36.

Expected output (single column)
-------------------------------
1 2 3 4 6 9 12 18 36
"""


n = 36
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
