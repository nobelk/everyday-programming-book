"""Exercise 7.1.3 — Appending to a list

Chapter 7 (Lists), section 7.1: Lists.

Problem
-------
This program builds a list of square numbers from 1 to 5.

Bug type: Logical
-----------------
`n + n` doubles each number instead of squaring it, so the list comes out `[2, 4, 6, 8, 10]`. Squaring with `n * n` (or `n ** 2`) produces the intended `[1, 4, 9, 16, 25]`.

The program below is the corrected version.
"""


squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]
