"""Problem 97 — Tower of Hanoi — move count

Domain: Mathematics. Chapter 11 (Functions), recursion.

Problem
-------
Minimum moves to transfer `n` disks is `2^n − 1`, expressible recursively.

Expected output
---------------
255
"""


def hanoi_moves(n):
    if n == 0:
        return 0
    return 2 * hanoi_moves(n - 1) + 1

print(hanoi_moves(8))
