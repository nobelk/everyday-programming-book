"""Advanced problem 30 — 2×2 Matrix Multiplication (imperative)

Subject: Mathematics. Style: imperative.

Problem
-------
Multiply two 2×2 matrices.

Concepts taught
---------------
Triple-nested loops, list-of-lists indexing, accumulator pattern inside the innermost loop.

Expected output
---------------
[19, 22]
[43, 50]
"""


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        total = 0
        for k in range(2):
            total += A[i][k] * B[k][j]
        C[i][j] = total

for row in C:
    print(row)
