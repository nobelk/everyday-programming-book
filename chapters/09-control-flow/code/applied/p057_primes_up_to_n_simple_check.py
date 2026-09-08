"""Problem 57 — Primes up to N (simple check)

Domain: Mathematics. Chapter 9 (Control Flow), loops.

Problem
-------
Print every prime from 2 to 30.

Expected output
---------------
2 3 5 7 11 13 17 19 23 29
"""


for n in range(2, 31):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
